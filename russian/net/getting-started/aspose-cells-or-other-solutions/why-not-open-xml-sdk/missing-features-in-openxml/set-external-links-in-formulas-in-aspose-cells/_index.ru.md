---
title: Установка внешних ссылок в формулах Aspose.Cells
type: docs
weight: 90
url: /ru/net/set-external-links-in-formulas-in-aspose-cells/
---

{{% alert color="primary" %}} 

Иногда необходимо включить ссылки на внешние файлы в формулах, например, для оценки значения ячейки или диапазона по ним. Aspose.Cells предоставляет такую ​​возможность, и в этом документе объясняется, как ею пользоваться.

{{% /alert %}} 

Ниже приведен пример кода, показывающий, как включить внешние файлы в формулы.

**C#**

{{< highlight csharp >}}

 string FilePath = @"..\..\..\Sample Files\";

string FileName = FilePath + "Set External Links in Formula.xlsx";

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get first Worksheet

Worksheet sheet = workbook.Worksheets[0];

//Get Cells collection

Aspose.Cells.Cells cells = sheet.Cells;

//Set formula with external links

cells["A1"].Formula = "=SUM('[book1.xls]Sheet1'!A2, '[book1.xls]Sheet1'!A4)";

//Set formula with external links

cells["A2"].Formula = "='[book1.xls]Sheet1'!A8";

//Save the workbook

workbook.Save(FileName);

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20OpenXML%20Spreadsheets/OpenXML%20Missing%20Features/Set%20External%20Links%20in%20Formula)
## **Скачать пример выполнения**
- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
{{< app/cells/assistant language="csharp" >}}
