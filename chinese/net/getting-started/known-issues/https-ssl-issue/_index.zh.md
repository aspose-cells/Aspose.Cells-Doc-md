---
title: HTTPS SSL问题
type: docs
weight: 20
url: /zh/net/https-ssl-issue/
---

## **HTTPS/SSL问题**
一些用户报告称，使用Aspose.Cells生成的Excel文件下载时出现问题。当保存对话框打开时，文件名包含aspx页面的名称而不是excel文件，并且文件类型为空。
### **解释**
我们更改了HTTP响应标头以解决HTTP压缩问题。这可能会在通过HTTPS/SSL向客户端浏览器发送文件时出现问题。
### **解决方案**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
