---
title: Set DefaultFont property of PdfSaveOptions and ImageOrPrintOptions to have priority
type: docs
weight: 30
url: /python-net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

While setting the **DefaultFont** property of [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) and [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions), you might expect that saving to PDF or image would apply that DefaultFont to all the text in a workbook that uses a missing (not installed) font.

Generally, when saving to PDF or image, Aspose.Cells for Python via .NET will first try to set the workbook's default font (i.e., `Workbook.DefaultStyle.Font`). If the workbook's default font still cannot display/render the text properly, Aspose.Cells for Python via .NET will try to render with the font specified by the **DefaultFont** attribute in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions).

To meet your expectation, we have a Boolean property named **check_workbook_default_font** in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions). You can set it to **false** to disable checking the workbook's default font, or let the **default_font** setting in [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) have priority.

## **Set DefaultFont property of PdfSaveOptions/ImageOrPrintOptions**

The following sample code opens an Excel file. The A1 cell (in the first worksheet) contains the text “Christmas Time Font text”. The font name is “Christmas Time Personal Use”, which is not installed on the machine. We set the **default_font** attribute of [**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions) / [**ImageOrPrintOptions**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions) to “Times New Roman”. We also set the **check_workbook_default_font** Boolean property to **false**, which ensures that the text in cell A1 is rendered with the “Times New Roman” font and does not use the workbook’s default font (“Calibri” in this case). The code renders the first worksheet to PNG and TIFF image formats and finally to a PDF file.

{{% alert color="primary" %}}

The default value of **CheckWorkbookDefaultFont** attribute is **true**.

{{% /alert %}}

This is the screenshot of the [template file](49446913.xlsx) used in the example code.

![todo:image_alt_text](1.png)

This is the output PNG image after setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to “Times New Roman”.

![todo:image_alt_text](2.png)

See the output [TIFF](48496672.tiff) image after setting the [**ImageOrPrintOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/imageorprintoptions/default_font) property to “Times New Roman”.

See the output [PDF](48496673.pdf) file after setting the [**PdfSaveOptions.default_font**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/default_font/) property to “Times New Roman”.

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SetDefaultFontPropertyOfPdfSaveOptionsAndImageOrPrintOptions.py" >}}

{{< app/cells/assistant language="python-net" >}}
