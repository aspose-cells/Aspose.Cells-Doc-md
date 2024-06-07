---
title: 在Excel转HTML期间排除未使用样式
type: docs
weight: 30
url: /zh/net/exclude-unused-styles-during-excel-to-html-conversion/
---

## **可能的使用场景**

Microsoft Excel文件可能包含许多未使用的样式。当您将Excel文件导出为HTML格式时，这些未使用的样式也会被导出。这会增加HTML文件的大小。您可以在将Excel文件转换为HTML期间使用[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles)属性排除未使用的样式。当您将其设置为**true**时，所有未使用的样式将从输出的HTML中排除。以下截图显示了输出HTML中的一个样本未使用的样式。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **在Excel转换为HTML期间排除未使用的样式**

以下示例代码创建一个工作簿，并创建一个未使用的命名样式。由于[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/excludeunusedstyles)设置为**true**，因此此未使用的命名样式不会导出到[输出HTML](61767778.zip)中。但是，如果将其设置为**false**，那么此未使用的样式将存在于输出HTML中，您可以在HTML标记中查看，如上面的截图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "HTML-ExcludeUnusedStylesInExcelToHTML.cs" >}}
