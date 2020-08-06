---
title: Create New Worksheet
type: docs
weight: 50
url: /net/create-new-worksheet/
---

## **Aspose.Cells - Create New Worksheet**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Adding a new worksheet to the Workbook object

WorksheetCollection worksheets = workbook.Worksheets;

Worksheet worksheet = worksheets.Add("My Worksheet");

//Saving the Excel file

workbook.Save("newWorksheet.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - Create New Worksheet**
**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook();

ISheet sheet1 = wb.CreateSheet("First Sheet");

ISheet sheet2 = wb.CreateSheet("Second Sheet");


// Note that sheet name is Excel must not exceed 31 characters

// and must not contain any of the any of the following characters:

// 0x0000

// 0x0003

// colon (:)

// backslash (\)

// asterisk (*)

// question mark (?)

// forward slash (/)

// opening square bracket ([)

// closing square bracket (])

// You can use org.apache.poi.ss.util.WorkbookUtil#createSafeSheetName(String nameProposal)}

// for a safe way to create valid names, this utility replaces invalid characters with a space (' ')

String safeName = WorkbookUtil.CreateSafeSheetName("[O'Brien's sales*?]");

ISheet sheet3 = wb.CreateSheet(safeName);

FileStream sw = File.Create("newWorksheet.xls");

wb.Write(sw);

sw.Close();

{{< /highlight >}}
## **Download Running Code**
Download **Create New Worksheet** form any of the below mentioned social coding sites:

- [CodePlex](https://asposecellsnpoi.codeplex.com/downloads/get/1536886)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.2/Create.New.Worksheet.zip)

{{% alert color="primary" %}} 

For more details, visit [Working with Worksheets](http://www.aspose.com/docs/display/cellsnet/Working+with+Worksheets).

{{% /alert %}}
