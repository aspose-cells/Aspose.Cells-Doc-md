---
title: Print spreadsheets
type: docs
weight: 20
url: /net/print-spreadsheets/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

Page setup settings also provide several Print Options (also referred to as Sheet Options) that allow users to control the printed pages of worksheets. These print options allow users to:

- Select a specific Print Area of the worksheet
- Print Titles
- Print Gridlines
- Print Row/Column Headings
- Achieve Draft Quality
- Print Comments
- Print Cell Errors
- Define Page Ordering  

**Setting Print/Sheet Options**

Aspose.Cells supports all of these print options and developers can easily configure them for their desired worksheets using several properties offered by the **PageSetup** class. The usage of these properties of the **PageSetup** class is discussed in more detail below.

## **Set Print Area**
By default, the print area selected encompasses the entire worksheet that contains data. However, developers can also specify a specific print area as needed.

To select a specific print area, developers can set the **PrintArea** property of the **PageSetup** class. You can provide the cell range of the print area as a string.

{{< highlight csharp >}}
 //Instantiating a Workbook object
Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet
PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area
pageSetup.PrintArea = "A1:T35";
{{< /highlight >}}

## **Set Print Titles**
Aspose.Cells allows you to designate row and column headers that you want to have repeated on all pages of your printed worksheet. To do so, developers can set **PrintTitleColumns** and **PrintTitleRows** properties of the **PageSetup** class.

The rows or columns (to be repeated on all pages of the printed worksheet) are defined by passing their row or column numbers. For example, rows are defined as `$1:$2` and columns are defined as `$A:$B`.

{{< highlight csharp >}}
 //Instantiating a Workbook object
Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet
Aspose.Cells.PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns
pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows
pageSetup.PrintTitleRows = "$1:$2";
{{< /highlight >}}

## **Set Other Print Options**
**PageSetup** class also provides several other methods to set general print options as follows:

- **setPrintGridlines** method – a boolean parameter that defines whether to print gridlines.
- **setPrintHeadings** method – a boolean parameter that defines whether to print row and column headings.
- **setBlackAndWhite** method – a boolean parameter that defines whether to print the worksheet in black‑and‑white mode.
- **setPrintComments** method – defines whether to display the print comments on the worksheet or at the end of the worksheet.
- **setPrintDraft** method – a boolean parameter that defines whether to print the worksheet in draft quality.
- **setPrintErrors** method – defines whether to print cell errors as displayed, blank, dash, or N/A.

To use the **PrintComments** and **PrintErrors** properties, Aspose.Cells provides two enumerations, **PrintCommentsType** and **PrintErrorsType**, that contain predefined values to be passed as parameters.

{{< highlight csharp >}}
 //Instantiating a Workbook object
Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet
PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Allowing to print gridlines
pageSetup.PrintGridlines = true;

//Allowing to print row/column headings
pageSetup.PrintHeadings = true;

//Allowing to print worksheet in black & white mode
pageSetup.BlackAndWhite = true;

//Allowing to print comments as displayed on worksheet
pageSetup.PrintComments = PrintCommentsType.PrintInPlace;

//Allowing to print worksheet with draft quality
pageSetup.PrintDraft = true;

//Allowing to print cell errors as N/A
pageSetup.PrintErrors = PrintErrorsType.PrintErrorsNA;
{{< /highlight >}}

## **Set Page Order**
**PageSetup** class provides the **Order** property that is used to set the order of multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows:

- **Down then over** – prints all pages down before moving to the right.
- **Over then down** – prints pages left to right before moving down.

Aspose.Cells provides an enumeration, **PrintOrderType**, that contains all predefined order types to be assigned to the **Order** property.

{{< highlight csharp >}}
 //Instantiating a Workbook object
Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet
PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down
pageSetup.Order = PrintOrderType.OverThenDown;
{{< /highlight >}}

## **Download Sample Code**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
{{< app/cells/assistant language="csharp" >}}
