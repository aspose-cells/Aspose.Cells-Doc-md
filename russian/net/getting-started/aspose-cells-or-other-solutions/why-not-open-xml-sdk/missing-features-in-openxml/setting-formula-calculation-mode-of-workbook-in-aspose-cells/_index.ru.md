---
title: Установка режима вычисления формул рабочей книги в Aspose.Cells
type: docs
weight: 100
url: /ru/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---

{{% alert color="primary" %}} 

В Microsoft Excel вы можете установить режим вычисления формул, то есть способ, которым происходит вычисление формул. Существуют три возможных значения:

- Автоматический - пересчитывать при изменении чего-либо и каждый раз при открытии книги.
- Автоматический, за исключением таблиц данных - пересчитывать при изменении чего-либо, но исключая таблицы данных.
- Ручной - пересчитывать только при явном запросе пользователя нажатием F9 или CTRL+ALT+F9, или при сохранении книги.

{{% /alert %}} 

Для установки режима вычисления формул в Microsoft Excel:

1. Выберите **Формулы**, а затем **Параметры расчета**.
1. Выберите один из вариантов.

Aspose.Cells также позволяет установить **Режим вычисления формулы** с использованием свойства режима FormulaSettings.CalculationMode. Вы можете присвоить ему перечисление CalcModeType, которое имеет одно из следующих значений:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

В следующем примере кода сначала создается книга, затем устанавливается режим расчета формул на **Ручной** и сохраняется книга как файл Excel на диске.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Скачать пример выполнения**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
