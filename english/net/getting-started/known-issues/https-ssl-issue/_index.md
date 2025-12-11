---
title: HTTPS SSL Issue
type: docs
weight: 20
url: /net/https-ssl-issue/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **HTTPS/SSL Problem**
Some users reported that they had problems downloading Excel files generated with Aspose.Cells. When the save dialog opens, the file name contains the name of the ASPX page instead of the Excel file, and the file type is blank.

### **Explanation**
We changed HTTP response headers to solve the problem with HTTP compression. This may cause problems while sending files to the client’s browser through HTTPS/SSL.

### **Solution**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
{{< app/cells/assistant language="csharp" >}}
