---
title: Перенос текста в ячейке
type: docs
weight: 130
url: /ru/net/wrapping-cell-text/
---

{{% alert color="primary" %}}

Перенос текста упрощает чтение: ячейка с перенесенным текстом расширяется, чтобы вместить текст, чтобы текст не отображался поверх других ячеек.

С помощью Aspose.Cells for .NET разработчики могут выполнять большую часть задач в своих приложениях, которые пользователи могут выполнять с помощью Microsoft Excel, включая перенос текста в ячейках. Эта статья объясняет, как это сделать, и сравнивает задачу с использованием VSTO и Aspose.Cells. Aspose.Cells оптимизирован для эффективной разработки и работает без автоматизации Microsoft.

{{% /alert %}}

## **Перенос текста в ячейке**

Для создания листа с двумя ячейками, одна из которых содержит перенесенный текст, а другая - нет:

1. Настройте лист:
   1. Создать книгу.
   1. Получите доступ к первому листу.
1. Добавьте текст:
   1. Добавьте текст в ячейку A1.
   1. Добавьте перенесенный текст в ячейку A5.
1. Сохраните электронную таблицу.

Приведенные ниже фрагменты кода показывают, как выполнить эти шаги с помощью [VSTA](/cells/ru/net/wrapping-cell-text/) с использованием либо C#, либо Visual Basic. Фрагменты кода, показывающие, как сделать то же самое с использованием [Aspose.Cells for .NET](/cells/ru/net/wrapping-cell-text/), снова с использованием либо C#, либо Visual Basic, следуют непосредственно после него.

Запуск кода приводит к электронной таблице с двумя ячейками, одна из которых содержит текст, который не был перенесен, а другая содержит:

|<p>**Output wrapping cell text with VSTO** </p><p>![todo:image_alt_text](wrapping-cell-text_1.png)</p>|<p>**Output wrapping cell text with Aspose.Cells for .NET** </p><p>![todo:image_alt_text](wrapping-cell-text_2.png)</p>|
| :- | :- |

### **Перенос текста в ячейке с использованием VSTA**

**C#**

{{< highlight csharp >}}

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

### **Перенос текста ячейки с использованием Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
