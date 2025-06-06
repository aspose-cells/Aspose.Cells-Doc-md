---
title: Вычисление подытогов
type: docs
weight: 10
url: /ru/net/calculate-sub-totals/
---

## **Aspose.Cells - Вычисление подытогов**
Вы можете автоматически создавать подытоги для любых повторяющихся значений в электронной таблице. Aspose.Cells предоставляет API-функции, которые помогают вам программно добавлять подытоги в электронные таблицы.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the Cells collection in the first worksheet

Cells cells = workbook.Worksheets[0].Cells;

//Create a cellarea i.e.., B3:C19

CellArea ca = new CellArea();

ca.StartRow = 2;

ca.StartColumn = 1;

ca.EndRow = 18;

ca.EndColumn = 2;

//Apply subtotal, the consolidation function is Sum and it will applied to

//Second column (C) in the list

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[] { 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Вычислить Промежуточные Итоги** с любого из упомянутых выше социальных сайтов для кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Создание Промежуточных Итогов](/cells/ru/net/creating-subtotals/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
