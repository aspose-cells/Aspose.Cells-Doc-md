---
title: Скрытие и отображение листов в книге в VSTO и Aspose.Cells
type: docs
weight: 140
url: /ru/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

В этой статье сравнивается скрытие и отображение листов с использованием VSTO, как на C#, так и Visual Basic, с выполнением той же задачи с помощью Aspose.Cells, снова с использованием как C#, так и Visual Basic. Aspose.Cells позволяет вам работать без установленного Microsoft Excel.

Шаги по скрытию листа:

1. Открыть файл.
1. Получить лист.
1. Скрыть лист.
1. Сохраните файл.
   Чтобы снова отобразить лист, просто переключите видимость для скрытого листа.

Приведенные ниже примеры кода сначала показывают, как скрыть лист. Первые примеры показывают процесс с использованием VSTO, как на C#, по сравнению с использованием Aspose.Cells, снова с использованием как C#.

Второй набор примеров кода показывает строку, используемую для отображения скрытого листа в VSTO или Aspose.Cells.
## **Скрытие листов**
Ниже приведены примеры кода для VSTO и Aspose.Cells, которые иллюстрируют, как скрыть лист в книге.
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **Отображение листа**
Ниже приведены примеры кода для VSTO и Aspose.Cells, которые иллюстрируют, как отобразить скрытый лист в книге.
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Загрузить образец кода**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
