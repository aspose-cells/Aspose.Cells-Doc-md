---
title: HTTPS SSL Issue
type: docs
weight: 20
url: /net/https-ssl-issue/
---

## **HTTPS/SSL Problem**
Some users reported that they had problems to download Excel files generated with Aspose.Cells. When the save dialog opens, the file name contains the name of the aspx page instead of the excel file, and the File Type is blank.
### **Explanation**
We changed HTTP response headers to solve the problem with HTTP compression. This may cause problem while sending files to client browser through HTTPS/SSL.
### **Solution**


{{< gist "aspose-cells" "18f6c28b77ee30c773fb2199168e73ed" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPSSSLIssue.aspx-SSLIssue.cs" >}}
