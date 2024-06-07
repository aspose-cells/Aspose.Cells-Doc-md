---
title: 在Excel转HTML期间排除未使用样式
type: docs
weight: 30
url: /zh/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **可能的使用场景**

Microsoft Excel文件可能包含许多未使用的样式。将Excel文件导出为HTML格式时，这些未使用的样式也会被导出。这会增加HTML的大小。您可以使用[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)属性在将Excel文件转换为HTML时排除未使用的样式。当您将其设置为**true**时，所有未使用的样式都将从输出的HTML中排除。以下截图显示了输出的HTML中的一个示例未使用的样式。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **在Excel转换为HTML期间排除未使用的样式**

以下示例代码创建一个工作簿，并创建一个未使用的命名样式。由于[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)设置为**true**，因此此未使用的命名样式将不会导出到[输出的HTML](61767781.zip)。但如果你将它设置为**false**，那么这个未使用的样式将会出现在输出的HTML中，你可以在HTML标记中看到上述截图中所示的效果。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
