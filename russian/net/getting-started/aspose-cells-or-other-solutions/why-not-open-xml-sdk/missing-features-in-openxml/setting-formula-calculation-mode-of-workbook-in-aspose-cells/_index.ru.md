---
title: Настройка режима вычисления формулы рабочей книги в Aspose.Cells
type: docs
weight: 100
url: /ru/net/setting-formula-calculation-mode-of-workbook-in-aspose-cells/
---
{{% alert color="primary" %}} 

Microsoft Excel позволяет установить режим расчета формулы, то есть способ расчета формулы. Возможны три значения:

- Автоматически — пересчитывать всякий раз, когда что-то изменяется и каждый раз, когда открывается рабочая книга.
- Автоматически, за исключением таблиц данных — пересчитывать всякий раз, когда что-то изменяется, но исключая таблицы данных.
- Вручную — пересчитывать только тогда, когда пользователь явно запрашивает его, нажав F9 или CTRL+ALT+F9, или при сохранении книги.

{{% /alert %}} 

Чтобы установить режим вычисления формулы в Microsoft Excel:

1.  Выбирать**Формулы** а потом**Варианты расчета**.
1. Выберите один из вариантов.

 Aspose.Cells также позволяет установить**Режим вычисления формулы** с использованием свойства режима FormulaSettings.CalculationMode. Вы можете назначить ему перечисление CalcModeType, которое имеет одно из следующих значений:

- CalcModeType.Automatic
- CalcModeType.AutomaticExceptTable
- CalcModeType.Manual

В следующем примере кода сначала создается рабочая книга, а затем устанавливается режим расчета формулы**Руководство** и сохраняет книгу как выходной файл Excel на диске.

**C#**

{{< highlight "csharp" >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Setting Formula Calculation Mode.xlsx";

//Create a workbook

Workbook workbook = new Workbook();

//Set the Formula Calculation Mode to Manual

workbook.Settings.FormulaSettings.CalculationMode = CalcModeType.Manual;

//Save the workbook

workbook.Save(FileName, SaveFormat.Xlsx);

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Setting%20Formula%20Calculation%20Mode)
## **Скачать пример запуска**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
