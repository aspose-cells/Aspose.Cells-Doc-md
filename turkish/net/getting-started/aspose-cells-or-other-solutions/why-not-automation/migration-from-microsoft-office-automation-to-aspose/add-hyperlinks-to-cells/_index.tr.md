---
title: Cells'e Köprü Ekle
type: docs
weight: 60
url: /tr/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET, bir kullanıcının Microsoft Excel'de gerçekleştirebileceği hemen hemen tüm görevleri uygulamanız üzerinden gerçekleştirmenizi sağlar. Bu makale, VSTO ve Aspose.Cells for .NET kullanarak bir çalışma sayfasındaki bir hücreye nasıl köprü ekleneceğini karşılaştırır.

{{% /alert %}}

## **Cells'e Köprüler Ekleme**

Bir elektronik tablodaki hücrelere köprüler eklemek için aşağıdaki adımları izleyin:

1. Çalışma sayfasını ayarlayın:
 1. Bir Uygulama nesnesi oluşturun.
 (Yalnızca VSTO.)
 1. Bir Çalışma Kitabı ekleyin.
 1. İlk sayfayı alın.
 1. Köprü ekleyeceğiniz hücrelere metin ekleyin.
1. Köprü ekle.
1. Belgeyi kaydedin.

 Bu adımlar aşağıdaki kod örneklerinde gösterilmektedir. İlk örnekler nasıl kullanılacağını gösterir[VSTO](/cells/tr/net/add-hyperlinks-to-cells/) bir hücreye köprü eklemek için C# veya Visual Basic ile. Aşağıdaki örnekler, kullanarak aynı şeyi nasıl yapacağınızı gösterir.[Aspose.Cells for .NET](/cells/tr/net/add-hyperlinks-to-cells/), yine C# veya Visual Basic kullanarak.

Kod örnekleri, ilk çalışma sayfasındaki A1 hücresinde köprü bulunan bir Excel dosyası oluşturur.

![yapılacaklar:resim_alternatif_metin](add-hyperlinks-to-cells_1.png)

**A1 hücresine bir köprü eklenir.**

### **VSTO ile Cells'e Köprü Ekleme**

**C#**

{{< highlight "csharp" >}}

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

### **Aspose.Cells for .NET ile Cells'e Köprü Ekleme**

**C#**

{{< highlight "csharp" >}}

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
