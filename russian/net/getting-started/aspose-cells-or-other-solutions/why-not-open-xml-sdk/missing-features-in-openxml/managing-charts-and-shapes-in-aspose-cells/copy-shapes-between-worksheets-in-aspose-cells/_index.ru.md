---
title: Копировать фигуры между рабочими листами в Aspose.Cells
type: docs
weight: 30
url: /ru/net/copy-shapes-between-worksheets-in-aspose-cells/
---
{{% alert color="primary" %}} 

Иногда вам нужно копировать элементы на рабочем листе, например изображения, диаграммы и другие объекты рисования, между рабочими листами. Aspose.Cells поддерживает эту функцию. Диаграммы, изображения и другие объекты можно копировать с высочайшей степенью точности.

В этой статье вы подробно узнаете, как копировать фигуры между листами. Для иллюстрации он создает консольное приложение в Visual Studio.Net, копирует изображения, диаграммы и другие объекты рисования между рабочими листами с помощью Aspose.Cells.

{{% /alert %}} 

Ниже приведен код для копирования диаграммы с рабочего листа на другой.

**C#**

{{< highlight "csharp" >}}

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

**Примечание:** Для получения более подробной информации о копировании нескольких фигур вам необходимо посетить[здесь](/cells/ru/net/copy-shapes-between-worksheets/)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Copy%20Shapes%20between%20Worksheets)
## **Скачать пример запуска**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
