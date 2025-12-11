---  
title: Embed Attachment to PDF  
type: docs  
weight: 370  
url: /java/embed-attachment-to-pdf/  

ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---  

In Excel, you can insert an OLE Object with source data ([embedded-attachments-example.xlsx](embedded-attachments-example.xlsx)). Double‑click the OLE Object, and the embedded file will be opened.  

Generally, while converting to PDF, the OLE Object will be rendered as an icon or a thumbnail without the OLE Object source data. With the option [PdfSaveOptions.EmbedAttachments](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setEmbedAttachments-boolean-), you can embed the OLE Object source data as an attachment in the PDF. You can double‑click the icon or the thumbnail in the PDF to open the source file of the OLE Object.  

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Docs-Pdf-EmbedAttachmentToPdf.java" >}}  

![embedded-attachment.png](embedded-attachment.png)  

{{< app/cells/assistant language="java" >}}
