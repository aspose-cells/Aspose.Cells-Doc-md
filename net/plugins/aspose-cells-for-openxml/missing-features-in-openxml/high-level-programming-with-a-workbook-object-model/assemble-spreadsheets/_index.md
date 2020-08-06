---
title: Assemble Spreadsheets
type: docs
weight: 10
url: /net/assemble-spreadsheets/
---

This section describes how to:

Create a new Excel file from scratch and add worksheet to it.

- Add worksheets to designer spreadsheets.
- Access worksheets using the sheet name.
- Remove a worksheet from an Excel file using its sheet name.
- Remove a worksheet from an Excel file using its sheet index.
- Aspose.Cells provides a class, Workbook that represents an Excel file. The Workbook class contains a Worksheets collection that allows to access to each worksheet in the Excel file.

A worksheet is represented by the Worksheet class. The Worksheet class provides a wide range of properties and methods for managing worksheets.
## **Adding Worksheets to a New Excel File**
To create a new Excel file programmatically:

- Create an object of the Workbook class.
- Call the Add method of the Worksheets collection. An empty worksheet is added to the Excel file * automatically. It can be referenced by passing the sheet index of the new worksheet to the Worksheets collection.
- Obtain a worksheet reference.
- Perform work on the worksheets.
- Save the new Excel file with new worksheets by calling the Workbook class' Save method.

{{< highlight csharp >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Adding Worksheet.xls");

{{< /highlight >}}
## **Adding Worksheets to a Designer Spreadsheet**
The process of adding worksheets to a designer spreadsheet is the same as that of adding a new worksheet, except that the Excel file already exists so should be opened before worksheets are added. A designer spreadsheet can be opened by the Workbook class.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Adding a new worksheet to the Workbook object

int i = workbook.Worksheets.Add();

//Obtaining the reference of the newly added worksheet by passing its sheet index

Worksheet worksheet = workbook.Worksheets[i];

//Setting the name of the newly added worksheet

worksheet.Name = "My Worksheet";

//Saving the Excel file

workbook.Save("Designer Spreadsheet.xls");

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}
## **Accessing Worksheets using Sheet Name**
Access or get any worksheet by specifying its name or index.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Accessing a worksheet using its sheet name

Worksheet worksheet = workbook.Worksheets["Sheet1"];

{{< /highlight >}}
## **Removing Worksheets using Sheet Name**
To remove worksheets from a file, call the Worksheets collection' RemoveAt method. Pass the sheet name to the RemoveAt method to remove a specific worksheet.

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet name

workbook.Worksheets.RemoveAt("Sheet3");

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Removing Worksheets using Sheet Index**
Removing worksheets by name works well when the name of the worksheet is known. If you don't know the worksheet's name, use an overloaded version of the RemoveAt method that takes the sheet index of the worksheet instead of its sheet name.

{{< highlight csharp >}}

 //creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("WorksHeet Operations.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook workbook = new Workbook(fstream);

//Removing a worksheet using its sheet index

workbook.Worksheets.RemoveAt(1);

workbook.Save("WorksHeet Operations.xls");

{{< /highlight >}}
## **Download Sample Code**
- [Codeplex](https://asposecellsopenxml.codeplex.com/releases/view/619160)
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Code.MSDN](https://code.msdn.microsoft.com/AsposeCells-Features-8fba7c3c)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Assemble%20Worksheet%20%28Aspose.Cells%29.zip)
