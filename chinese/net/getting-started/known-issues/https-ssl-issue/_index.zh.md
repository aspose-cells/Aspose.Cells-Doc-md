---
title: HTTPS SSL 问题
type: docs
weight: 20
url: /zh/net/https-ssl-issue/
---

## **HTTPS/SSL 问题**
一些用户报告说，他们在使用 Aspose.Cells 生成的 Excel 文件时遇到问题。当保存对话框打开时，文件名包含 aspx 页面名称而不是 Excel 文件名称，并且文件类型为空白。
### **解释**
我们更改了 HTTP 响应头来解决 HTTP 压缩的问题。这可能会导致通过 HTTPS/SSL 向客户端浏览器发送文件时出现问题。
### **解决方案**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
