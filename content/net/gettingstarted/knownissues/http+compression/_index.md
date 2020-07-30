---
title : "HTTP Compression" 
description : "" 
weight : 12023 
toc : false
type: docs
url: /net/gettingstarted/knownissues/http+compression/
---

# Aspose.Cells for .NET : HTTP Compression


{{< panel title="Contents Summary" style="primary" >}}
*   1 [HTTP Compression problem](#http-compression-problem)
    *   1.1 [Explanation](#explanation)
    *   1.2 [Exceptions](#exceptions)
    *   1.3 [Solutions](#solutions)
{{< /panel >}}
 

## HTTP Compression problem

Some users report that if they configure HTTP Compression in IIS, they find errors while sending generated files to client browsers.

### Explanation

We use **"Content-disposition", "inline; filename=test.xls"** header to force the browser to open the file and **"Content-disposition", "attachment; filename=test.xls"** header to force the browser to open the **Save As** dialog and use Microsoft Excel to open the file. However, there are some exceptions that do exist.

### Exceptions

You can use the following code to verify that it is NOT a bug of Aspose.

  

### Solutions

You can use one of the following workarounds to solve this problem:

*   Move those specified ASP.NET files (which contain code calling Aspose.Cells) to another folder, which is not compressed.
*   Disable HTTP Compression for dynamic content.
*   Save the generated file in your server and provide a link to your users.

If you do wish to use HTTP Compression, please always use *OpenInExcel* option instead of *OpenInBrowser* option when you know you've enabled IIS compression.

