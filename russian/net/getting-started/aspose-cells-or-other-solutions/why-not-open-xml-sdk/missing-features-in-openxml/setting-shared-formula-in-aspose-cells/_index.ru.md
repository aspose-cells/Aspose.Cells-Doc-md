---
title: Установка общей формулы в Aspose.Cells
type: docs
weight: 110
url: /ru/net/setting-shared-formula-in-aspose-cells/
---
{{% alert color="primary" %}} 

Предположим, у вас есть рабочий лист, заполненный данными.

 Вы хотите добавить в B2 функцию, которая будет вычислять налог с продаж для первой строки данных. Налог**9%** . Формула, по которой рассчитывается налог с продаж, выглядит следующим образом:**"=А2*0,09"**. В этой статье объясняется, как применить эту формулу к номеру Aspose.Cells.

{{% /alert %}} 

Aspose.Cells позволяет указать формулу с помощью свойства Cell.Formula.

Есть два варианта добавления формул в другие ячейки (B3, B4, B5 и т. д.) в столбце.

Либо сделайте то, что вы сделали для первой ячейки, фактически установив формулу для каждой ячейки, соответственно обновив ссылку на ячейку (A3*0,09, А4*0,09, A5*0,09 и так далее). Это требует обновления ссылок на ячейки для каждой строки. Также требуется Aspose.Cells для анализа каждой формулы по отдельности, что может занять много времени для больших электронных таблиц и сложных формул. Он также добавляет дополнительные строки кода, хотя циклы могут несколько их сократить.

 Другой подход заключается в использовании**общая формула**. При использовании общей формулы формулы автоматически обновляются для ссылок на ячейки в каждой строке, чтобы налог был рассчитан правильно. Метод Cell.SetSharedFormula более эффективен, чем первый метод.

В следующем примере показано, как его использовать.

**C#**

{{< highlight "csharp" >}}

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
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Shared%20Formula)
## **Скачать пример запуска**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
