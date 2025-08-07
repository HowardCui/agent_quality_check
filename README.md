# 📊 Agent Quality Check System

本项目是一个用于客服对话质检的自动化系统，支持文本上传、音频分析（本地或远程URL），自动执行工作流并生成 Excel 报告，通过邮件发送给指定接收人。

---

## 🚀 功能说明

### ✅ 主要功能

| 方法名 | 功能说明 |
|--------|----------|
| `upload_text_file()` | 上传本地对话文本（`dialog` 字段）为 `.txt` 文件 |
| `upload_audio_file()` | 上传本地音频文件用于质检分析 |
| `run_workflow_muti_dialog()` | 运行多轮对话的工作流 |
| `run_workflow_audio()` | 运行本地音频的工作流 |
| `run_workflow_audio_url()` | 运行远程音频URL的工作流 |
| `JSON_to_EXCEL()` | 将 JSON 分析结果转换为 Excel 表格文件流 |
| `send_email(excel_stream)` | 将结果 Excel 通过邮件发送给收件人 |
| `run()` | 一键执行整个质检流程，根据类型自动选择上传与分析方式 |

---

### 注意API key要到dify中自己设置 包括百炼的
