---
title: Get a List of Fonts Used in a Spreadsheet or Workbook
description: Aspose.Cells for Python via .NET is a library for working with spreadsheet files. It supports retrieving a list of fonts used in a spreadsheet or workbook, allowing users to obtain font information used in a document. This article shows how to use the Aspose.Cells for Python via .NET library to get a list of fonts.
keywords: Aspose.Cells for Python via .NET, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

It is often necessary to know the fonts being used in your workbook for rendering purposes. When you convert your workbook into PDF or an image, Aspose.Cells for Python via .NET requires that all needed fonts are installed on your system or present in your **fonts directory**. If Aspose.Cells for Python via .NET is unable to find the required font, it tries to replace it with another suitable font that is present on your system or in your fonts directory and can substitute the original font. This not only results in undesired rendering of PDFs or images but also adds processing time for finding suitable fonts.

In order to deal with such cases, you should know which fonts are being used by your workbook, then either install those fonts on your system in a Windows environment or place them in your fonts directory in a Windows or Linux environment.

Aspose.Cells for Python via .NET provides the [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts) method, which returns the list of all fonts used in your workbook or spreadsheet.

## **Get a List of Fonts Used in a Spreadsheet or Workbook**

The following sample code loads the source Excel file and retrieves the list of fonts used inside it. It contains one dummy worksheet with some dummy fonts added for illustration purposes. When the code prints all fonts inside the workbook, it also prints those dummy fonts. The following screenshot shows the [sample Excel file](25395211.xlsx) and how the dummy fonts are listed.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

## **Console Output**

Here is the console output of the above sample code when executed with the given [sample Excel file](25395211.xlsx).

{{< highlight java >}}
Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]
{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
