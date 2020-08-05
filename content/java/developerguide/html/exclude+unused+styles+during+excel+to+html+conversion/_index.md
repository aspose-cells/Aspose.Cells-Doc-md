---
title : "Exclude Unused Styles during Excel to HTML conversion" 
description : "" 
weight : 12087 
toc : false
type: docs
url: /java/developerguide/html/exclude+unused+styles+during+excel+to+html+conversion/
---

# Aspose.Cells for Java : Exclude Unused Styles during Excel to HTML conversion


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Exclude Unused Styles during Excel to HTML conversion](#exclude-unused-styles-during-excel-to-html-conversion)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Microsoft Excel file may contain many unused styles. When you export the Excel file to HTML format, these unused styles are also exported. This can increase the size of HTML. You can exclude the unused styles during the conversion of Excel file to HTML using the [HtmlSaveOptions.ExcludeUnusedStyles](https://apireference.aspose.com/javascript/cells/aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) property. When you set it **true**, all unused styles are excluded from output HTML. The following screenshot displays a sample unused style inside the output HTML. 

![image](https://docs2.aspose.com/cells/java/attachments/61540998/61767780.png)

## Exclude Unused Styles during Excel to HTML conversion

The following sample code creates a workbook and also creates an unused named style. Since the [HtmlSaveOptions.ExcludeUnusedStyles](https://apireference.aspose.com/javascript/cells/aspose.cells/htmlsaveoptions#ExcludeUnusedStyles) is set to **true**, so this unused named style will not be exported to [output HTML](https://docs2.aspose.com/cells/java/attachments/61540998/61767781.zip). But if you set it **false**, then this unused style will be present inside the output HTML which you can then see in HTML markup as shown in the above screenshot.

## Sample Code

