---
title: Security Exception Issue
type: docs
weight: 30
url: /net/security-exception-issue/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Security Exception Problem**
Some users may receive "Security Exception" error while trying to use Aspose.Cells. This problem is generally happened in a web application.
### **Explanation**
Aspose.Cells has to call some **Win32 GDI APIs** to provide some important features. If the web server has a strict trust level, this security exception may be thrown.
### **Solution**
Please try to create a new permission set to give Aspose.Cells.dll security permission with "Allow calls to unmanaged assemblies" enabled.
{{< app/cells/assistant language="csharp" >}}
