---
title: 安全异常问题
type: docs
weight: 30
url: /zh/net/security-exception-issue/
---
## **安全异常问题**
某些用户在尝试使用 Aspose.Cells 时可能会收到“安全异常”错误。此问题通常发生在 Web 应用程序中。
### **解释**
 Aspose.Cells 必须打电话给一些**Win32 GDI API**提供一些重要的功能。如果 Web 服务器具有严格的信任级别，则可能会抛出此安全异常。
### **解决方案**
请尝试创建一个新的权限集，以在启用“允许调用非托管程序集”的情况下授予 Aspose.Cells.dll 安全权限。
