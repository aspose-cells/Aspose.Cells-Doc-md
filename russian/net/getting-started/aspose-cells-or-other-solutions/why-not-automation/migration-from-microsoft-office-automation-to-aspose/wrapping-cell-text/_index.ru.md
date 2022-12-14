---
title: Упаковка Cell Текст
type: docs
weight: 130
url: /ru/net/wrapping-cell-text/
---
{{% alert color="primary" %}}

Обтекание текста облегчает чтение: ячейка с перенесенным текстом расширяется, чтобы соответствовать тексту, поэтому текст не отображается поверх других ячеек.

С помощью Aspose.Cells for .NET разработчики могут выполнять в своих приложениях большинство задач, которые пользователи могут выполнять с помощью Microsoft Excel, включая перенос текста в ячейки. В этой статье объясняется, как это сделать, и сравнивается задача с использованием VSTO и Aspose.Cells. Aspose.Cells оптимизирован для эффективного кодирования и работает без автоматизации Microsoft.

{{% /alert %}}

## **Упаковка Cell Текст**

Чтобы создать рабочий лист с двумя ячейками, одна с переносом текста и одна без:

1. Настройте рабочий лист:
 1. Создайте рабочую книгу.
 1. Откройте первый рабочий лист.
1. Добавить текст:
 1. Добавьте текст в ячейку A1.
 1. Добавьте переносимый текст в ячейку A5.
1. Сохраните таблицу.

 Примеры кода ниже показывают, как выполнить эти шаги, используя[ВСТО](/cells/ru/net/wrapping-cell-text/) либо с C#, либо с Visual Basic. Примеры кода, которые показывают, как сделать то же самое, используя[Aspose.Cells for .NET](/cells/ru/net/wrapping-cell-text/), снова используя C# или Visual Basic сразу после этого.

Выполнение кода приводит к электронной таблице с двумя ячейками, одна из которых содержит текст, который не был перенесен, а другая имеет:

|<p>**Вывод переноса текста ячейки с помощью VSTO** </p><p>![дело:изображение_альтернативный_текст](wrapping-cell-text_1.png)</p>|<p>**Текст ячейки для переноса вывода с Aspose.Cells for .NET** </p><p>![дело:изображение_альтернативный_текст](wrapping-cell-text_2.png)</p>|
|:- |:- |

### **Перенос текста Cell с помощью VSTO**

**C#**

{{< highlight "csharp" >}}

 //Note: To help you better, the code uses full namespacing

void WrappingCellText()

{

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

    workbook.SaveAs("f:\\downloads\\OutputVsto.xlsx");

    //Quit the application

    app.Quit();

}

{{< /highlight >}}

### **Обтекание Cell Использование текста Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 void WrappingCellText()

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

    workbook.Save("f:\\downloads\\OutputAspose.xlsx", SaveFormat.Xlsx);

}

{{< /highlight >}}
