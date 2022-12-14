---
title: Скрытие и отображение рабочих листов в книге в VSTO и Aspose.Cells
type: docs
weight: 140
url: /ru/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
В этой статье сравнивается скрытие и отображение листов с помощью VSTO с использованием C# или Visual Basic с выполнением той же задачи с помощью Aspose.Cells, опять же с использованием C# или Visual Basic. Aspose.Cells позволяет работать без установленного Microsoft Excel.

Шаги, чтобы скрыть рабочий лист:

1. Откройте файл.
1. Получите рабочий лист.
1. Скрыть рабочий лист.
1. Сохраните файл.
 Чтобы снова отобразить рабочий лист, просто включите видимость для скрытого листа.

Примеры кода ниже сначала показывают, как скрыть рабочий лист. В первых примерах показан процесс с VSTO, используя либо C#, либо Aspose.Cells, либо C#.

Второй набор примеров кода показывает строку, используемую для отображения рабочего листа в VSTO или Aspose.Cells.
## **Скрытие рабочих листов**
Ниже приведены примеры кода для VSTO и Aspose.Cells, иллюстрирующие, как скрыть лист в книге.
### **ВСТО**
{{< highlight "csharp" >}}

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
{{< highlight "csharp" >}}

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
## **Отображение рабочего листа**
Ниже приведены примеры кода для VSTO и Aspose.Cells, иллюстрирующие, как отобразить лист в книге.
### **ВСТО**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Скачать пример кода**
- [Гитхаб](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Источникфорж](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/скачать)
- [Битбакет](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
