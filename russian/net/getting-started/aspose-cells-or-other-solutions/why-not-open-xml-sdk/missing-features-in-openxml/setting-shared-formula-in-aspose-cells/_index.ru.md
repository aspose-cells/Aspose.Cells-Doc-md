---
title: Настройка общей формулы в Aspose.Cells
type: docs
weight: 110
url: /ru/net/setting-shared-formula-in-aspose-cells/
---

{{% alert color="primary" %}} 

Предположим, у вас есть лист, заполненный данными.

Вы хотите добавить функцию в B2, которая будет вычислять налог с продаж для первой строки данных. Налог составляет **9%**. Формула, вычисляющая налог с продаж, такова: **"=A2*0.09"**. В этой статье объясняется, как применить эту формулу с помощью Aspose.Cells.

{{% /alert %}} 

Aspose.Cells позволяет указать формулу с использованием свойства Cell.Formula.

Есть два варианта добавления формул в другие ячейки (B3, B4, B5 и так далее) в столбце.

Либо сделайте то же самое, что и для первой ячейки, фактически устанавливая формулу для каждой ячейки, обновляя ссылку на ячейку соответственно (A3*0.09, A4*0.09, A5*0.09 и так далее). Это требует обновления ссылок на ячейку для каждой строки. Также это требует от Aspose.Cells проанализировать каждую формулу отдельно, что может занимать много времени для больших таблиц и сложных формул. Это также добавляет дополнительные строки кода, хотя циклы могут сократить их в некоторой степени.

Другой подход - использовать **общую формулу**. С общей формулой формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы налог рассчитывался правильно. Метод Cell.SetSharedFormula более эффективен, чем первый метод.

Приведенный ниже пример демонстрирует, как его использовать.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Shared Formula.xlsx";

//Instantiate a Workbook from existing file

Workbook workbook = new Workbook(FileName);

//Get the cells collection in the first worksheet

Aspose.Cells.Cells cells = workbook.Worksheets[0].Cells;

//Apply the shared formula in the range i.e.., B2:B14

cells["B2"].SetSharedFormula("=A2*0.09", 13, 1);

//Save the excel file

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Скачать пример выполнения**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
