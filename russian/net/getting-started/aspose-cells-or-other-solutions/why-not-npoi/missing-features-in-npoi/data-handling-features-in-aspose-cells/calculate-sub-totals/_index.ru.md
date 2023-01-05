---
title: Рассчитать промежуточные итоги
type: docs
weight: 10
url: /ru/net/calculate-sub-totals/
---
## **Aspose.Cells - Расчет промежуточных итогов**
Вы можете автоматически создавать промежуточные итоги для любых повторяющихся значений в электронной таблице. Aspose.Cells предоставляет функции API, которые помогают программно добавлять промежуточные итоги в электронные таблицы.

**C#**

{{< highlight "cs" >}}

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

cells.Subtotal(ca, 0, ConsolidationFunction.Sum, new int[]{ 1 });

//Save the excel file

workbook.Save("AsposeTotal.xls"); 

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Рассчитать промежуточные итоги** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Calculate.Sub.Totals.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Создание промежуточных итогов](/cells/ru/net/creating-subtotals/).

{{% /alert %}}
