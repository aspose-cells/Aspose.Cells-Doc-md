---
title: 在Excel转换为HTML时排除未使用的样式
type: docs
weight: 30
url: /zh/java/exclude-unused-styles-during-excel-to-html-conversion/
---

## **可能的使用场景**

Microsoft Excel文件可能包含许多未使用的样式。当您将Excel文件导出为HTML格式时，这些未使用的样式也会被导出。这可能会增加HTML的大小。使用属性[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)，您可以在转换Excel文件为HTML时排除未使用的样式。当您设置为true时，所有未使用的样式都将被排除在输出的HTML之外。以下屏幕截图显示了输出的HTML中的一个未使用的样式示例。

![todo:image_alt_text](exclude-unused-styles-during-excel-to-html-conversion_1.png)

## **在将 Excel 转换为 HTML 时排除未使用的样式**

以下示例代码创建一个工作簿，并且创建一个未使用的命名样式。由于[**HtmlSaveOptions.ExcludeUnusedStyles**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExcludeUnusedStyles)被设置为true，因此这个未使用的命名样式将不会导出到[输出的HTML](61767781.zip)中。但如果您将其设置为false，那么这个未使用的样式将存在于输出的HTML中，您可以在HTML标记中看到，如上面的屏幕截图所示。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExcludeUnusedStylesInExcelToHTML.java" >}}
{{< app/cells/assistant language="java" >}}
