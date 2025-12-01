---
title: Public API Changes in Aspose.Cells 8.1.2
type: docs
weight: 60
url: /net/public-api-changes-in-aspose-cells-8-1-2/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

This document describes changes to the Aspose.Cells API from version 8.1.1 to 8.1.2, that may be of interest to module/application developers. It includes not only new and updated public methods, but also a description of any changes in the behavior behind the scenes in Aspose.Cells.

{{% /alert %}} 
## **Added Support for Warning if Font Substitution Occur**
With Aspose.Cells for .NET 8.1.2, the WarningInfo, WarningType classes, IWarningCallback interface and SaveOptions.WarningCallback, ImageOrPrintOptions.WarningCallback properties have been added to facilitate the user to receive warning if font substitution occurs while converting spreadsheets to images or PDF format. 

{{% alert color="primary" %}} 

Please check the detailed article on [Getting Warnings for Font Substitution while Rendering Spreadsheets](http://aspose.com/docs/display/cellsnet/Get+Warnings+for+Font+Substitution+while+Rendering+Excel+File)

{{% /alert %}}
## **Deleted Obsolete PdfSaveOptions.ChartImageType Property**
Aspose.Cells for .NET 8.1.2 has removed the obsolete PdfSaveOptions.ChartImageType property from the public API.
{{< app/cells/assistant language="csharp" >}}
