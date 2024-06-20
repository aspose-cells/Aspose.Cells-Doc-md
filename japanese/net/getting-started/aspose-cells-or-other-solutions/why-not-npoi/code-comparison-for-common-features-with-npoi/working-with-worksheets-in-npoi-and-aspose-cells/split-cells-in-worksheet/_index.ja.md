---
title: ワークシート内のセルを分割
type: docs
weight: 90
url: /ja/net/split-cells-in-worksheet/
---

## **Aspose.Cells - ワークシート内のセルを分割**
**C#**

{{< highlight cs >}}



Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];          

//Set the active cell

workbook.Worksheets[0].ActiveCell = "A10";

//Split the worksheet window

workbook.Worksheets[0].Split();

workbook.Save("output-Split.xls");


{{< /highlight >}}
## **NPOI - HSSF XSSF - ワークシート内のセルを分割**
**C#**

{{< highlight cs >}}



HSSFWorkbook hssfworkbook = new HSSFWorkbook();

ISheet sheet1 = hssfworkbook.CreateSheet("new sheet");

ISheet sheet2 = hssfworkbook.CreateSheet("second sheet");

//Create a split with the lower left side being the active quadrant

sheet2.CreateSplitPane(2000, 2000, 0, 0, PanePosition.LowerLeft);

//Write the stream data of workbook to the root directory

FileStream file = new FileStream(@"output-Split.xls", FileMode.Create);

hssfworkbook.Write(file);

file.Close();


{{< /highlight >}}

{{% alert color="primary" %}} 

詳細については、[ワークシートの操作](/cells/ja/net/working-with-worksheets-in-npoi-and-aspose-cells/)ページを参照してください。

{{% /alert %}}
