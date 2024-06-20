---
title: Hücrelere Bağlantılar Ekle
type: docs
weight: 60
url: /tr/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET, Microsoft Excel'de bir kullanıcının gerçekleştirebileceği neredeyse tüm görevleri uygulamanız aracılığıyla gerçekleştirmenizi sağlar. Bu makale, bir çalışma sayfasındaki bir hücreye bir bağlantı eklemenin VSTO ve Aspose.Cells for .NET kullanarak nasıl yapıldığını karşılaştırır.

{{% /alert %}}

## **Hücrelere Bağlantılar Ekleme**

Bir elektronik tabloya hücrelere bağlantı eklemek için aşağıdaki adımları izleyin:

1. Çalışma sayfasını kurun:
   1. Bir Uygulama nesnesi örnekleyin.
      (Sadece VSTO.)
   1. Bir çalışma kitabı ekleyin.
   1. İlk sayfayı alın.
   1. Hücrelere bağlantı eklenecek metni ekleyin.
1. Bağlantı ekle.
1. Belgeyi kaydedin.

Bu adımlar aşağıdaki kod örnekleriyle gösterilmiştir. İlk örnekler, [VSTO](/cells/tr/net/add-hyperlinks-to-cells/) kullanarak bir hücreye bağlantı eklemenin C# veya Visual Basic kullanarak nasıl yapılacağını gösterir. Bunu yapmanın aynı adımlarını gösteren örneklerin ardından, yine C# veya Visual Basic kullanarak [Aspose.Cells for .NET](/cells/tr/net/add-hyperlinks-to-cells/) kullanarak aynı şeyi nasıl yapacağınızı gösteren örnekler bulunmaktadır.

Kod örnekleri, birinci çalışma sayfasındaki A1 hücresinde bir bağlantıya sahip bir Excel dosyası oluşturur.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**A1 hücresine bir bağlantı eklenir.**

### **VSTO ile Hücrelere Bağlantı Ekleme**

**C#**

{{< highlight csharp >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET ile Hücrelere Bağlantı Ekleme**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
