---
title: Print spreadsheets
type: docs
weight: 20
url: /net/print-spreadsheets/
---

Page setup settings also provide several Print Options (also referred as Sheet Options ) that allow users to control their printed pages of worksheets. These print options allow users to:

- Select a specific Print Area of the worksheet
- Print Titles
- Print Gridlines
- Print Row/Column Headings
- Achieve Draft Quality
- Print Comments
- Print Cell Errors
- Define Page Ordering
  **Setting Print/Sheet Options**

Aspose.Cells supports all of these print options and developers can easily configure these options for their desired worksheets using the several properties offered by PageSetup class. The usage of these properties of PageSetup class is discussed below in more detail.
## **Set Print Area**
By default, only that print area is selected that incorporates the entire area of the worksheet, which contains data but developers can also establish a specific print area of the worksheet according to their desire.

To select a specific print area, developers can use set **PrintArea** method of the **PageSetup** class. You can provide the cells range of the print area to this method as argument.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Specifying the cells range (from A1 cell to T35 cell) of the print area

pageSetup.PrintArea = "A1:T35";


{{< /highlight >}}
## **Set Print Titles**
Aspose.Cells allows you to designate row and column headers that you want to have repeated on all pages of your printed worksheet. To do so, developers can use set **PrintTitleColumns** and **setPrintTitleRows** methods of the **PageSetup** class.

The rows or columns (to be repeated on all pages of the printed worksheet) are defined by passing their row or column numbers. For example, rows are defined as \ $1: \ $2 and columns are defined as \ $A: \ $B.

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

- **setPrintGridline s method** , a boolean parameter is passed to this method that defines whether to print or not print gridlines
- **setPrintHeadings method** , a boolean parameter is passed to this method that defines whether to print row and column headings or not
- **setBlackAndWhite method** , a boolean parameter is passed to this method that defines whether to print worksheet in black and white mode or not
- **setPrintComments method** , defines that whether to display the print comments on the worksheet or at the end of the worksheet
- **setPrintDraft method** , a boolean parameter is passed to this method that defines whether to print worksheet in draft quality or not
- **setPrintErrors method** , defines that whether to print cell errors as displayed, blank, dash or N/A

To use set **PrintComments** and set **PrintErrors** methods, Aspose.Cells also provides two enumerations, PrintCommentsType & PrintErrorsType that contain pre-defined values to be passed a parmeters to set PrintComments and set PrintErrors methods respectively.

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
**PageSetup** class provides set Order method that is used to order multiple pages of your worksheet to be printed. There are two possibilities to order the pages as follows:

Down then over thus it will print all pages down before printing pages to the right
Over then down thus it will print pages left to right before printing pages below
Aspose.Cells provides an enumeration, PrintOrderType that contains all pre-defined order types to be assigned to setPage Order method.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Setting the printing order of the pages to over then down

pageSetup.Order = PrintOrderType.OverThenDown;

{{< /highlight >}}
## **Download Sample Code**
- [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Print%20Spreadsheet%20with%20Options%20%28Aspose.Cells%29.zip)
