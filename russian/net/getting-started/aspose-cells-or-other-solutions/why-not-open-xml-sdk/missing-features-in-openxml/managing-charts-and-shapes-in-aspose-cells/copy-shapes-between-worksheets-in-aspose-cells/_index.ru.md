---
title: Копирование форм между листами в Aspose.Cells
type: docs
weight: 30
url: /ru/net/copy-shapes-between-worksheets-in-aspose-cells/
---

{{% alert color="primary" %}} 

Иногда вам может понадобиться скопировать элементы на листе, например, изображения, диаграммы и другие объекты рисования, между листами. Aspose.Cells поддерживает эту функцию. Диаграммы, изображения и другие объекты могут быть скопированы с высокой степенью точности.

Эта статья дает вам подробное понимание того, как копировать формы между листами. Для пояснения создается консольное приложение в Visual Studio.Net, копируются изображения, диаграммы и другие объекты рисования между листами с использованием Aspose.Cells.

{{% /alert %}} 

Ниже приведен код для копирования диаграммы с одного листа на другой

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Copy Shapes between Worksheets.xlsx";

//Open the template file

Workbook workbook = new Workbook(FileName);

//Get the Chart from the "Chart" worksheet.

Aspose.Cells.Charts.Chart source = workbook.Worksheets["Chart"].Charts[0];

Aspose.Cells.Drawing.ChartShape cshape = source.ChartObject;

//Copy the Chart to the Result Worksheet

workbook.Worksheets["Result"].Shapes.AddCopy(cshape, 20, 0, 2, 0);

//Save the Worksheet

workbook.Save(FileName);



{{< /highlight >}}

**Примечание:** Для получения дополнительной информации о копировании нескольких форм посетите [здесь](/cells/ru/net/copy-shapes-between-worksheets/)
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Скачать пример выполнения**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
