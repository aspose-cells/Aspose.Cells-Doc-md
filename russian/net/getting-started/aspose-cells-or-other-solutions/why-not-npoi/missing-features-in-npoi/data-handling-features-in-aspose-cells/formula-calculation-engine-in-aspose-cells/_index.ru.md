---
title: Механизм вычисления формулы в Aspose.Cells
type: docs
weight: 30
url: /ru/net/formula-calculation-engine-in-aspose-cells/
---
## **Aspose.Cells - Механизм расчета формулы**
Механизм вычисления формул встроен в Aspose.Cells. Он может не только пересчитывать формулы, импортированные из файла электронной таблицы дизайнера, но также поддерживает вычисление результатов формул, добавленных во время выполнения.

**C#**

{{< highlight "cs" >}}

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
## **Скачать рабочий код**
 Скачать**Механизм вычисления формулы** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Formula.Calculation.Engine.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Механизм вычисления формулы](/cells/ru/net/formula-calculation-engine/).

{{% /alert %}}
