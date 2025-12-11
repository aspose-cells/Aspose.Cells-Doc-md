---  
title: HTTP Compression  
type: docs  
weight: 10  
url: /net/http-compression/  
ai_search_scope: cells_net  
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

## **HTTP Compression problem**  
Some users report that if they configure HTTP Compression in IIS, they encounter errors while sending generated files to client browsers.  

### **Explanation**  
We use the **"Content-Disposition: inline; filename=test.xls"** header to force the browser to open the file, and the **"Content-Disposition: attachment; filename=test.xls"** header to display the Save As dialog and open the file with Microsoft Excel. However, there are some exceptions that do exist.  

### **Exceptions**  
You can use the following code to verify that it is not a bug in Aspose.  

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}  

### **Solutions**  
You can use one of the following workarounds to solve this problem:  

- Move those specified ASP.NET files (which contain code calling Aspose.Cells) to another folder that is not compressed.  
- Disable HTTP Compression for dynamic content.  
- Save the generated file on your server and provide a link to your users.  

If you do wish to use HTTP Compression, please always use the *OpenInExcel* option instead of the *OpenInBrowser* option when you have enabled IIS compression.  
{{< app/cells/assistant language="csharp" >}}
