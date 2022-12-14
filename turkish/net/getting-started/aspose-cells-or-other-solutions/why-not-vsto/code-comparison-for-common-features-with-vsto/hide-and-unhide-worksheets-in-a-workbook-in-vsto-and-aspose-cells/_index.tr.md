---
title: VSTO ve Aspose.Cells'de Çalışma Kitabındaki Çalışma Sayfalarını Gizle ve Göster
type: docs
weight: 140
url: /tr/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
Bu makale, C# veya Visual Basic kullanan VSTO ile çalışma sayfalarını gizleme ve gösterme ile aynı görevi Aspose.Cells ile tekrar C# veya Visual Basic kullanarak gerçekleştirmeyle karşılaştırır. Aspose.Cells, Microsoft Excel yüklü olmadan çalışmanıza izin verir.

Bir çalışma sayfasını gizleme adımları şunlardır:

1. Bir dosya aç.
1. Bir çalışma sayfası alın.
1. Çalışma sayfasını gizleyin.
1. Dosya 'yı kaydet.
 Bir çalışma sayfasını tekrar göstermek için, gizli sayfanın görünürlüğünü açmanız yeterlidir.

Aşağıdaki kod örnekleri öncelikle bir çalışma sayfasının nasıl gizleneceğini gösterir. İlk örnekler, C#'i kullanan VSTO ile işlemi, yine C#'i kullanan Aspose.Cells'i kullanmaya kıyasla gösterir.

İkinci kod örnekleri grubu, çalışma sayfasını VSTO veya Aspose.Cells'de göstermek için kullanılan satırı gösterir.
## **Çalışma Sayfalarını Gizleme**
Aşağıda, çalışma kitabında bir çalışma sayfasının nasıl gizleneceğini gösteren VSTO ve Aspose.Cells kod örnekleri bulunmaktadır.
### **VSTO**
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
## **Çalışma Sayfasını Gösterme**
Aşağıda, çalışma kitabında bir çalışma sayfasının nasıl gösterileceğini gösteren VSTO ve Aspose.Cells kod örnekleri bulunmaktadır.
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Örnek Kodu İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [kaynak forge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/indir)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
