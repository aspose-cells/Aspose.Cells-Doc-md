---
title: 在输出HTML中单独导出工作表CSS
type: docs
weight: 80
url: /zh/net/export-worksheet-css-separately-in-output/
---

## **可能的使用场景**

Aspose.Cells提供了将工作表CSS单独导出到HTML的功能。请在保存Excel文件为HTML格式时使用 [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) 属性，将其设置为**true**。

## **在输出HTML中单独导出工作表CSS**

以下示例代码创建一个Excel文件，在单元格**B5**中添加一些红色文本，然后使用 [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) 属性将其保存为HTML格式。请参考代码生成的 [输出HTML](60489766.zip)，其中包含 **stylesheet.css**。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **将单个表格工作簿导出为HTML**

当使用Aspose.Cells将包含多个工作表的工作簿转换为HTML时，它会创建一个HTML文件以及包含CSS和多个HTML文件的文件夹。在浏览器中打开此HTML文件时，选项卡是可见的。同样的行为也适用于将单工作表工作簿转换为HTML。之前为单表工作簿不会创建单独的文件夹，只会创建HTML文件。这种HTML文件在浏览器中打开时没有选项卡显示。MS Excel 也会为单工作表创建合适的文件夹和HTML，因此使用Aspose.Cells API实现相同的行为。

[sampleSingleSheet.xlsx](79527937.xlsx)

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
