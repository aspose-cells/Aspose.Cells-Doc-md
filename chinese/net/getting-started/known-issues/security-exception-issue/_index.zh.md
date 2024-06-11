---
title: 安全异常问题
type: docs
weight: 30
url: /zh/net/security-exception-issue/
---

## **安全异常问题**
一些用户在尝试使用 Aspose.Cells 时可能会遇到"安全异常"错误。这个问题通常发生在 web 应用程序中。
### **Explanation**
Aspose.Cells需要调用一些**Win32 GDI APIs**以提供一些重要功能。如果Web服务器的信任级别严格，可能会出现此安全异常。
### **Solution**
请尝试创建新的权限集，启用"允许调用不受管理的程序集"，以赋予Aspose.Cells.dll安全权限。
