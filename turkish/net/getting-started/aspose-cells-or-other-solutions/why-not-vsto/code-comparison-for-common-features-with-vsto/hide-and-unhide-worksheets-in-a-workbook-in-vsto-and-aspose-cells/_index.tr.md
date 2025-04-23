---
title: VSTO ve Aspose.Cells te Çalışma Kitabında Çalışsayfalarını Gizle ve Göster
type: docs
weight: 140
url: /tr/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

Bu makale, VSTO ile çalışsayfaları gizleme ve gösterme işlemini, C# veya Visual Basic kullanarak Aspose.Cells ile aynı görevi gerçekleştirmek için karşılaştırır. Aspose.Cells, Microsoft Excel'in yüklü olmadan çalışmanıza olanak tanır.

Bir çalışsayfayı gizlemek için izlenmesi gereken adımlar:

1. Bir dosyayı açın.
1. Bir çalışsayfayı alın.
1. Çalışsayfayı gizleyin.
1. Dosyayı kaydedin.
   Bir çalışsayfayı yeniden göstermek için, gizli sayfa için görünürlüğü basitçe açın.

Aşağıdaki kod örnekleri öncelikle bir çalışsayfayı gizlemenin nasıl olduğunu gösterir. İlk örnekler, C#, kullanarak VSTO ile süreci Aspose.Cells kullanarak yine C# kullanarak karşılaştırır.

İkinci set kod örnekleri, VSTO veya Aspose.Cells'te çalışsayfayı yeniden göstermek için kullanılan satırı gösterir.
## **Çalışsayfaları Gizleme**
Aşağıda, çalışma kitabında bir çalışsayfayı gizlemek için VSTO ve Aspose.Cells için çözümlemeleri gösteren kod örnekleri bulunmaktadır.
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
## **Çalışsayfayı Gizleme**
Aşağıda, çalışma kitabında bir çalışsayfayı yeniden göstermek için VSTO ve Aspose.Cells için kod örnekleri bulunmaktadır.
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
## **Örnek Kod İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
