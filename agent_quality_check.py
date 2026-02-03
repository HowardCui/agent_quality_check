#!/usr/bin/env python 3.8
# -*- coding: utf-8 -*-
# time: 2025/08/05
# name: Haowen Cui

import requests
import json
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from urllib.parse import urljoin, urlparse
import pandas as pd
import ast
import io
import mimetypes
from io import BytesIO
import re

class Agent_quality_check:
    def __init__(self, upload_url,
                 workflow_url,
                 save_file_name,
                 user,
                 email_info,
                 receiver,
                 upload_file_type,
                 dialog,
                 authorization,
                 audio_path = None,
                 dialog_id = None,
                 staff_id = None,
                 ):

        self.upload_file_type=upload_file_type
        self.receiver=receiver
        self.email_info=email_info
        self.file_id=None
        self.upload_url=upload_url
        self.workflow_url=workflow_url
        self.audio_path=audio_path
        self.save_file_name=save_file_name
        self.user=user
        self.excel_url=None
        self.datasets=None
        self.dialog=dialog
        self.dialog_id=dialog_id
        self.staff_id=staff_id
        self.authorization=authorization

    def is_url(self):
        return re.match(r'^https?://', self.audio_path) is not None

    def upload_text_file(self):
        headers={
            "Authorization": self.authorization,
        }
        try:
            json_str=json.dumps(self.dialog, indent=2, ensure_ascii=False)
            byte_stream=io.BytesIO(json_str.encode('utf-8'))
            byte_stream.name='upload.txt'  # 模拟文件名
            files={
                'file': ('upload.txt', byte_stream, 'text/plain')
            }
            data={
                "user": self.user,
                "type": "TXT"
            }

            response=requests.post(self.upload_url, headers=headers, files=files, data=data)
            if response.status_code==201:  # 201 表示创建成功
                print("文件上传成功")
                return response.json().get("id")  # 获取上传的文件 ID
            else:
                print(f"文件上传失败，状态码: {response.status_code}")
                print("响应内容:", response.text)
                return None
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return None

    def upload_audio_file(self):
        headers={
            "Authorization": self.authorization,
        }
        try:
            # 上传本地音频文件
            print("正在读取本地音频文件...")
            filename=os.path.basename(self.audio_path)
            mime_type, _=mimetypes.guess_type(filename)
            if not mime_type:
                mime_type='application/octet-stream'
            file_stream=open(self.audio_path, 'rb')

            # 构造上传请求
            files={
                'file': (filename, file_stream, mime_type)
            }
            data={
                "user": self.user,
                "type": "AUDIO"
            }
            response=requests.post(self.upload_url, headers=headers, files=files, data=data)
            if response.status_code==201:  # 201 表示创建成功
                print("文件上传成功")
                return response.json().get("id")  # 获取上传的文件 ID
            else:
                print(f"文件上传失败，状态码: {response.status_code}")
                print("响应内容:", response.text)
                return None
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return None

    def run_workflow_muti_dialog(self):
        response_mode="blocking"
        headers={
            "Authorization": self.authorization,
            "Content-Type": "application/json"
        }
        data={
            "inputs": {
                "muti_dialog": {
                    "transfer_method": "local_file",
                    "upload_file_id": self.file_id,
                    "type": "document"
                },
                "name_file": self.save_file_name,
                "output_type": "JSON",
            },
            "response_mode": response_mode,
            "user": self.user
        }

        print("提交的请求数据:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        try:
            print("运行工作流...")
            response=requests.post(self.workflow_url, headers=headers, json=data)
            if response.status_code==200:
                print("工作流执行成功")
                return response.json()
            else:
                print(f"工作流执行失败，状态码: {response.status_code}")
                print("响应内容:", response.text)
                return {"status": "error",
                        "message": f"Failed to execute workflow, status code: {response.status_code}"}
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return {"status": "error", "message": str(e)}

    def run_workflow_audio(self):
        response_mode="blocking"
        headers={
            "Authorization": self.authorization,
            "Content-Type": "application/json"
        }
        data= {
            "inputs": {
                "audio_input": {
                    "transfer_method": "local_file",
                    "upload_file_id": self.file_id,
                    "type": "audio"
                },
                "name_file": self.save_file_name,
                "output_type": "JSON",
                "dialog_id": self.dialog_id,
                "staff_id": self.staff_id,
            },
            "response_mode": response_mode,
            "user": self.user
        }

        print("提交的请求数据:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        try:
            print("运行工作流...")
            response=requests.post(self.workflow_url, headers=headers, json=data)
            if response.status_code==200:
                print("工作流执行成功")
                return response.json()
            else:
                print(f"工作流执行失败，状态码: {response.status_code}")
                print("响应内容:", response.text)
                return {"status": "error",
                        "message": f"Failed to execute workflow, status code: {response.status_code}"}
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return {"status": "error", "message": str(e)}

    def run_workflow_audio_url(self):
        response_mode="blocking"
        headers={
            "Authorization": self.authorization,
            "Content-Type": "application/json"
        }
        data= {
            "inputs": {
                "audio_input": {
                    "transfer_method": "remote_url",
                    "url": self.audio_path,
                    "type": "audio"
                },
                "name_file": self.save_file_name,
                "output_type": "JSON",
                "dialog_id": self.dialog_id,
                "staff_id": self.staff_id,
            },
            "response_mode": response_mode,
            "user": self.user
        }

        print("提交的请求数据:")
        print(json.dumps(data, indent=2, ensure_ascii=False))

        try:
            print("运行工作流...")
            response=requests.post(self.workflow_url, headers=headers, json=data)
            if response.status_code==200:
                print("工作流执行成功")
                return response.json()
            else:
                print(f"工作流执行失败，状态码: {response.status_code}")
                print("响应内容:", response.text)
                return {"status": "error",
                        "message": f"Failed to execute workflow, status code: {response.status_code}"}
        except Exception as e:
            print(f"发生错误: {str(e)}")
            return {"status": "error", "message": str(e)}

    def JSON_to_EXCEL(self):
        df=pd.DataFrame(json.loads(self.datasets))
        self.save_file_name='dialog_analysis_output.xlsx'
        excel_stream=io.BytesIO()
        with pd.ExcelWriter(excel_stream, engine='xlsxwriter') as writer:
            df.to_excel(writer,
                        sheet_name='Data',
                        startcol=0,
                        index=False,
                        columns=[
                            'dialog_id',
                            'staff_id',
                            'passed',
                            'fatal_issues',
                            'non_fatal_issues',
                            'bonus_points',
                            'score_details',
                            'utterance_analysis'
                        ])
        excel_stream.seek(0)
        return excel_stream

    def send_email(self, excel_stream):
        message=MIMEMultipart()
        message["From"]=self.email_info['sender_email']
        message["To"]=self.receiver
        message["Subject"]="你请求的质检结果"

        html_content="""
        <html>
            <body>
                <p>您好，</p>
                <p>您请求的客服对话质检结果已生成，详情请查收附件 <b>dialog_analysis_output.xlsx</b>。</p>
                <p>如有任何问题，欢迎随时联系。</p>
                <br>
                <p>祝好，<br>自动质检系统</p>
            </body>
        </html>
        """
        message.attach(MIMEText(html_content, "html"))

        part=MIMEApplication(excel_stream.read(), Name="dialog_analysis_output.xlsx")
        part["Content-Disposition"]='attachment; filename="dialog_analysis_output.xlsx"'
        message.attach(part)

        try:
            with smtplib.SMTP("smtp.qiye.aliyun.com", 80) as server:
                server.starttls()
                server.login(self.email_info['sender_email'], self.email_info['sender_password'])
                server.sendmail(self.email_info['sender_email'], self.receiver, message.as_string())
            print("邮件发送成功！")
        except Exception as e:
            print(f"邮件发送失败: {e}")

    def run(self):
        if self.upload_file_type=='TXT':
            self.file_id=self.upload_text_file()
            self.datasets=self.run_workflow_muti_dialog()["data"]["outputs"]['result']
            excel_stream=self.excel_url=self.JSON_to_EXCEL()
            self.send_email(excel_stream)
        elif not self.is_url():
            self.file_id=self.upload_audio_file()
            self.datasets=self.run_workflow_audio()["data"]["outputs"]['result']
            excel_stream=self.excel_url=self.JSON_to_EXCEL()
            self.send_email(excel_stream)
        else:
            self.datasets=self.run_workflow_audio_url()["data"]["outputs"]['result']
            excel_stream=self.excel_url=self.JSON_to_EXCEL()
            self.send_email(excel_stream)

if __name__=="__main__":
    email_info={
        "sender_email": 'cuihw@wotransfer.com',
        "sender_password": "******",
    }

    bot=Agent_quality_check(
        email_info=email_info,
    )
    bot.run()


