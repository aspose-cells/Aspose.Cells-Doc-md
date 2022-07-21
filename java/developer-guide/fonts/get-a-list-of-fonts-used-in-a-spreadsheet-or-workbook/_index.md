---
title: Get a List of Fonts used in a Spreadsheet or Workbook
type: docs
weight: 20
url: /java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Possible Usage Scenarios**

It is often necessary to know the fonts being used in your workbook for rendering purpose. When you convert your workbook into PDF or image, then Aspose.Cells requires that all the needed fonts are installed on your system or present in your **fonts directory**. If Aspose.Cells is unable to find the needed font, it tries to replace it with some other suitable font which is present on your system or in your font directory and can substitute your actual font. This not only results in the undesired rendering of PDF or images but also takes processing time for finding suitable fonts.

In order to deal with such cases, you should know what fonts are beings used by your workbook, then either install those fonts on your system in case of Windows environment or place it in your fonts directory in case of windows or Linux environment.

Aspose.Cells provides the [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts()) method which returns the list of all the fonts used in your workbook or spreadsheet.

## **Get a List of Fonts used in a Spreadsheet or Workbook**

The following sample code loads the source excel file and retrieves the list of fonts used inside it. It has one dummy worksheet which has some dummy fonts added for illustration purpose. When the code prints all the fonts inside the workbook, it also prints those dummy fonts. The following screenshot shows the [sample excel file](sampleGetFonts.xlsx) and how the dummy fonts are listed.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Console Output**

Here is the console output of the above sample code when executed with the given [sample excel file](sampleGetFonts.xlsx).

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
