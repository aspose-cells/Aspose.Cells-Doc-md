---
title: Exclude Unused Styles during Excel to HTML conversion
type: docs
weight: 30
url: /python-java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **Exclude Unused Styles during Excel to HTML conversion**
Microsoft Excel files may contain many unused styles. When these files are exported to HTML format, the unused styles are also exported. This results in the increased size of the output HTML. Aspose.Cells for Python via Java supports excluding these styles during the conversion of Excel file to HTML. For this, the API provides the [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) property. Setting the value of [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) property to **True** will exclude all unused styles from the output HTML.

The following screenshot shows unused styles in the HTML file which will be removed by setting the value of [HtmlSaveOptions.ExcludeUnusedStyles](https://reference.aspose.com/cells/python/asposecells.api/htmlsaveoptions#ExcludeUnusedStyles) property to **True**.

![todo:image_alt_text](HtmlSaveOptions-Exclude-Unused-Styles.png)

The following sample code demonstrates removing unused styles during Excel to HTML conversion.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "HTML-ExcludeUnusedStylesInExcelToHTML.py" >}}
