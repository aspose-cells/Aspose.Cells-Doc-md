---
title: Расчетный движок формул в Aspose.Cells
type: docs
weight: 30
url: /ru/net/formula-calculation-engine-in-aspose-cells/
---

## **Aspose.Cells - Расчетный Движок Формул**
Расчетный движок формул встроен в Aspose.Cells. Он может не только пересчитывать формулы, импортированные из файла дизайнера, но также поддерживает вычисление результатов формул, добавленных во время выполнения программы.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook book = new Workbook();

//Obtaining the reference of the newly added worksheet

int sheetIndex = book.Worksheets.Add();

Worksheet worksheet = book.Worksheets[sheetIndex];

Cells cells = worksheet.Cells;

Cell cell = null;

//Adding a value to "A1" cell

cell = cells["A1"];

cell.Value = 1;

//Adding a value to "A2" cell

cell = cells["A2"];

cell.Value = 2;

//Adding a value to "A3" cell

cell = cells["A3"];

cell.Value = 3;

//Adding a SUM formula to "A4" cell

cell = cells["A4"];

cell.Formula = "=SUM(A1:A3)";

//Calculating the results of formulas

book.CalculateFormula();

//Saving the Excel file

book.Save("AsposeFormulaEngine.xls");

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Расчетный Движок Формул** с любого из упомянутых выше социальных сайтов для кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Расчетный Движок Формул](/cells/ru/net/formula-calculation-engine/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
