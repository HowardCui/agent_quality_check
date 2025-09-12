## 📌 参数说明

该配置用于调用 Dify 工作流接口，上传对话与音频数据，并可通过邮件发送质检结果。

### 🔧 参数结构

```json
{
  "upload_url": "http://localhost/v1/files/upload",
  "workflow_url": "http://localhost/v1/workflows/run",
  "upload_file_type": "Audio",
  "dialog": "...",  // 字符串形式的 JSON
  "audio_path": "***",
  "save_file_name": "abd",
  "user": "user1",
  "email_info": {
    "sender_email": "",
    "sender_password": ""
  },
  "receiver": "",
  "dialog_id": "DIALOG00001",
  "staff_id": "121313131",
  "authorization":"",
}
```
### 🧾 字段说明

| 参数名                  | 类型           | 描述                                                       | 是否必填 |
| -------------------- | ------------ |----------------------------------------------------------| ---- |
| `upload_url`         | string       | 文件上传接口地址（如：Dify 文件上传）。示例：`http://localhost/v1/files/upload` | ✅ 是  |
| `workflow_url`       | string       | 工作流执行接口地址。用于触发质检或分析流程。示例：`http://localhost/v1/workflows/run` | ✅ 是  |
| `upload_file_type`   | string       | 上传文件类型， `"Audio"` 表示音频，`"TXT"`表示对话文本。取值需与接口支持类型匹配。       | ✅ 是  |
| `dialog`             | string（JSON） | 对话数据，支持多组对话。**必须为 JSON 字符串**，结构为 `muti_dialog` 列表。       | ✅ 是  |
| `audio_path`         | string       | 本地音频路径，音频分析时使用。示例：`C:/Users/xxx/Desktop/test.mp3`        | ❌ 否  |
| `save_file_name`     | string       | 导出文件名（不含扩展名）。如填写 `abd`，则输出为 `abd.xlsx`。                  | ✅ 是  |
| `user`               | string       | 用户名或用户标识。用于记录调用者。                                        | ✅ 是  |
| `email_info`         | object       | 发件人邮箱配置。仅在需发送邮件时填写：                                      | ❌ 否  |
| ├─ `sender_email`    | string       | 发件人邮箱地址。                                                 | ❌ 否  |
| └─ `sender_password` | string       | 对应邮箱的授权码或密码。                                             | ❌ 否  |
| `receiver`           | string       | 收件人邮箱。用于发送质检结果 Excel 附件。                                 | ❌ 否  |
| `dialog_id`          | string       | 对话的编号。与 `muti_dialog` 冲突时优先使用 `muti_dialog`。             | ❌ 否  |
| `staff_id`           | string       | 对话中的客服编号。                                                | ❌ 否  |
| `authorization`           | string       |                                                 | ✅ 是   |

### 💡 备注
#### dialog 字段为字符串形式的 JSON
```json
{
  "muti_dialog": [
    {
      "dialog_id": "DIALOG001",
      "staff_id": "XX",
      "dialog": [
        {
          "role": "客户",
          "time": "09:45:00",
          "content": "我昨天申请退款，进度怎么样了？"
        },
        ...
      ]
    }
  ]
}
```
#### `"dialog"`跟`"audio_path"`是二选一 

#### `"audio_path"`支持url输入 例如 `"https://example.com/audio.mp3"`

