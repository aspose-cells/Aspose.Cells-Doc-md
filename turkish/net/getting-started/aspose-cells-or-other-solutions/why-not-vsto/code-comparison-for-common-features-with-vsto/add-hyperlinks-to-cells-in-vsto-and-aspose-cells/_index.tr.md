---
title: VSTO'da Cells'e ve Aspose.Cells'e Köprüler ekleyin
type: docs
weight: 20
url: /tr/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
Bir elektronik tablodaki hücrelere köprüler eklemek için aşağıdaki adımları izleyin:

1.  Çalışma sayfasını ayarlayın:
 1. Bir Uygulama nesnesinin örneğini oluşturun. (Yalnızca VSTO.)
 1. Bir Çalışma Kitabı ekleyin.
 1. İlk sayfayı alın.
 1. Köprü ekleyeceğiniz hücrelere metin ekleyin.
1. Köprü ekle.
1. Belgeyi kaydedin.

Bu adımlar aşağıdaki kod örneklerinde gösterilmektedir. İlk örnekler, bir hücreye köprü eklemek için VSTO'nun C# ile nasıl kullanılacağını gösterir. Aşağıdaki örnekler, aynı şeyi Aspose.Cells for .NET kullanarak ve yine C# kullanarak nasıl yapacağınızı göstermektedir.

Kod örnekleri, ilk çalışma sayfasındaki A1 hücresinde köprü bulunan bir Excel dosyası oluşturur.

![yapılacaklar:resim_alternatif_metin](picture1.png)

A1 hücresine bir köprü eklenir.

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

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

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

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

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Örnek Kodu İndir**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [kaynak forge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/indir)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
