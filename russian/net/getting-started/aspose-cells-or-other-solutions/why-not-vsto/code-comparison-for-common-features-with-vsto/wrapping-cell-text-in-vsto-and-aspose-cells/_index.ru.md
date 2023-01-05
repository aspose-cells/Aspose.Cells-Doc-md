---
title: Упаковка Cell Текст в VSTO и Aspose.Cells
type: docs
weight: 250
url: /ru/net/wrapping-cell-text-in-vsto-and-aspose-cells/
---
Чтобы создать рабочий лист с двумя ячейками, одна с переносом текста и одна без:

1.  Настройте рабочий лист:
 1. Создайте рабочую книгу.
 1. Откройте первый рабочий лист.
1.  Добавить текст:
 1. Добавьте текст в ячейку A1.
 1. Добавьте переносимый текст в ячейку A5.
1. Сохраните таблицу.
 В приведенных ниже примерах кода показано, как выполнить эти шаги с помощью VSTO с любым из C#. Примеры кода, которые показывают, как сделать то же самое, используя Aspose.Cells for .NET, снова используя либо C#, следуют сразу за ними.

Выполнение кода приводит к электронной таблице с двумя ячейками, одна из которых содержит текст, который не был перенесен, а другая имеет:

## **Вывод с использованием VSTO Excel**

![дело:изображение_альтернативный_текст](picture1.png)

## **Вывод с использованием Aspose.Cells for .NET**

![дело:изображение_альтернативный_текст](picture2.png)

## **ВСТО**

{{< highlight "csharp" >}}

 //Access vsto application

Microsoft.Office.Interop.Excel.Application app = Globals.ThisAddIn.Application;

//Access workbook

Microsoft.Office.Interop.Excel.Workbook workbook = app.ActiveWorkbook;

//Access worksheet

Microsoft.Office.Interop.Excel.Worksheet m_sheet = workbook.Worksheets[1];

//Access vsto worksheet

Microsoft.Office.Tools.Excel.Worksheet sheet = Globals.Factory.GetVstoObject(m_sheet);

//Place some text in cell A1 without wrapping

Microsoft.Office.Interop.Excel.Range cellA1 = sheet.Cells.get_Range("A1");

cellA1.Value = "Sample Text Unwrapped";

//Place some text in cell A5 with wrapping

Microsoft.Office.Interop.Excel.Range cellA5 = sheet.Cells.get_Range("A5");

cellA5.Value = "Sample Text Wrapped";

cellA5.WrapText = true;

//Save the workbook

workbook.SaveAs("OutputVsto.xlsx");

//Quit the application

app.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

 private static void WrappingCellText()

{

	//Create workbook

	Workbook workbook = new Workbook();

	//Access worksheet

	Worksheet worksheet = workbook.Worksheets[0];

	//Place some text in cell A1 without wrapping

	Cell cellA1 = worksheet.Cells["A1"];

	cellA1.PutValue("Some Text Unwrapped");

	//Place some text in cell A5 wrapping

	Cell cellA5 = worksheet.Cells["A5"];

	cellA5.PutValue("Some Text Wrapped");

	Style style = cellA5.GetStyle();

	style.IsTextWrapped = true;

	cellA5.SetStyle(style);

	//Autofit rows

	worksheet.AutoFitRows();

	//Save the workbook

	workbook.Save("OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}

## **Скачать пример кода**

- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Wrapping.Cell.Text.Aspose.Cells.zip)
- [Источникфорж](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip/скачать)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Wrapping%20Cell%20Text%20\(Aspose.Cells\).zip)
