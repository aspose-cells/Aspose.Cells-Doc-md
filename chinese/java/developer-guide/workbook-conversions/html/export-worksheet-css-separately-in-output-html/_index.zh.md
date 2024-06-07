---
title: 在输出HTML中单独导出工作表CSS
type: docs
weight: 80
url: /zh/java/export-worksheet-css-separately-in-output-html/
---

## **可能的使用场景**

Aspose.Cells提供了将工作表CSS导出到单独文件的功能，当您将Excel文件转换为HTML时。请使用HtmlSaveOptions.ExportWorksheetCSSSeparately属性，并在保存Excel文件为HTML格式时将其设置为true。

## **在输出HTML中单独导出工作表CSS**

以下示例代码创建一个Excel文件，在单元格B5中添加一些红色文本，然后使用HtmlSaveOptions.ExportWorksheetCSSSeparately属性以HTML格式保存它。请查看代码生成的[输出HTML](60489780.zip)进行参考。您会发现其中包含一个样本代码的结果的stylesheet.css。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **将单个表格工作簿导出为HTML**

使用Aspose.Cells将包含多个工作表的工作簿转换为HTML时，它会创建一个HTML文件，同时包含CSS和多个HTML文件的文件夹。当在浏览器中打开此HTML文件时，选项卡是可见的。当将单个工作表的工作簿转换为HTML时，需要相同的行为。之前，单表工作簿不会创建单独的文件夹，只会创建HTML文件。此类HTML文件在浏览器中打开时不会显示选项卡。Excel为单表也创建了正确的文件夹和HTML，因此使用Aspose.Cells实现了相同的行为。可以从以下链接下载用于下面样本代码的样本文件:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
