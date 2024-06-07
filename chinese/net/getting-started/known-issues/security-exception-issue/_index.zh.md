---
title: 安全异常问题
type: docs
weight: 30
url: /zh/net/security-exception-issue/
---

## **安全异常问题**
一些用户在尝试使用Aspose.Cells时可能会遇到"安全异常"错误。这个问题通常发生在Web应用程序中。
### **解释**
Aspose.Cells必须调用一些**Win32 GDI API**来提供一些重要功能。如果Web服务器具有严格的信任级别，可能会抛出此安全异常。
### **解决方案**
请尝试创建一个新的权限集，启用"允许调用非托管程序集"选项以给予Aspose.Cells.dll的安全权限。
