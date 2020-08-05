---
title : "Exclude Unused Styles during Excel to HTML conversion" 
description : "" 
weight : 12031 
toc : false
type: docs
url: /pythonjava/developerguide/html/exclude+unused+styles+during+excel+to+html+conversion/
---

# Aspose.Cells for Python via Java : Exclude Unused Styles during Excel to HTML conversion


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Exclude Unused Styles during Excel to HTML conversion](#exclude-unused-styles-during-excel-to-html-conversion)
{{< /panel >}}
 

 

## Exclude Unused Styles during Excel to HTML conversion

Microsoft Excel files may contain many unused styles. When these files are exported to HTML format, the unused styles are also exported. This results in the increased size of the output HTML. Aspose.Cells for Python via Java supports excluding these styles during the conversion of Excel file to HTML. For this, the API provides the [HtmlSaveOptions.ExcludeUnusedStyles](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) property. Setting the value of [HtmlSaveOptions.ExcludeUnusedStyles](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) property to **True** will exclude all unused styles from the output HTML.

The following screenshot shows unused styles in the HTML file which will be removed by setting the value of [HtmlSaveOptions.ExcludeUnusedStyles](https://apireference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) property to **True**.

![image](https://docs.aspose.com/download/attachments/61540998/HtmlSaveOptions-Exclude-Unused-Styles.png?version=1&modificationDate=1517307631543&api=v2)

The following sample code demonstrates removing unused styles during Excel to HTML conversion.

