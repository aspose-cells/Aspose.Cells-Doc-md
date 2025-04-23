---
title: Exportera kommentarer vid sparande av Excel fil till HTML
type: docs
weight: 40
url: /sv/python-net/export-comments-while-saving-excel-file-to/
---

## **Möjliga användningsscenario**

När du sparar din Excel-fil till HTML exporteras inte kommentarer. Dock ger Aspose.Cells för Python via .NET denna funktion med hjälp av [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments)-egenskapen. Om du ställer in den till **true**, kommer HTML att visa kommentarer som finns i din Excel-fil.

## **Exportera kommentarer vid sparande av Excel-fil till HTML**

Följande exempelkod förklarar användningen av egenskapen [**HtmlSaveOptions.is_export_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/is_export_comments). Skärmbilden visar effekten av koden på HTML när den är inställd på **true**. Var god ladda ner [exempel Excel-filen](50528260.xlsx) och [genererad HTML](5052826.txt) för referens.

![todo:image_alt_text](export-comments-while-saving-excel-file-to-html_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportCommentsWhileSavingExcelFileToHtml.py" >}}
