---
title: Working with Freeze Panes
type: docs
weight: 100
url: /net/working-with-freeze-panes/
---

## **Aspose.Cells - Working with Freeze Panes**
**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

worksheet.FreezePanes(2, 2, 2, 0);

workbook.Save("output-FreezeFile-Aspose.Cells.xls");


{{< /highlight >}}

{{% alert color="primary" %}} 

For more details, visit [FreezePanes Method](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/freezepanes/index).

{{% /alert %}} 
## **NPOI - HSSF XSSF - Working with Freeze Panes**
**C#**

{{< highlight cs >}}

 HSSFWorkbook hssfworkbook = new HSSFWorkbook();

ISheet sheet1 = hssfworkbook.CreateSheet("new sheet");

ISheet sheet2 = hssfworkbook.CreateSheet("second sheet");

ISheet sheet3 = hssfworkbook.CreateSheet("third sheet");

// Freeze just one row

sheet1.CreateFreezePane(0, 2, 0, 2);

// Freeze just one column

sheet2.CreateFreezePane(2, 0, 2, 0);

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.CreateFreezePane(2, 2);

FileStream file = new FileStream(@"output-FreezeFile-NPOI.xls", FileMode.Create);

hssfworkbook.Write(file);

file.Close();


{{< /highlight >}}
## **Download Running Code**
Download **Working with Freeze Panes** form any of the below mentioned social coding sites:

- [CodePlex](https://archive.codeplex.com/?p=asposecellsnpoi)
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_Vs_NPOI_HWPF_and_XWPF_v1.3/Freeze.Panes.zip)

{{% alert color="primary" %}} 

For more details, visit [Working with Worksheets](/cells/net/working-with-worksheets-in-npoi-and-aspose-cells/).

{{% /alert %}}
