---
title: VSTO ve Aspose.Cells te Hücrelere Bağlantı Ekleme
type: docs
weight: 20
url: /tr/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

Bir elektronik tabloya hücrelere bağlantı eklemek için aşağıdaki adımları izleyin:

1. Çalışma sayfasını kurun: 
   1. Bir Uygulama nesnesi örneği oluşturun.(Sadece VSTO.)
   1. Bir çalışma kitabı ekleyin.
   1. İlk sayfayı alın.
   1. Hücrelere bağlantı eklenecek metni ekleyin.
1. Bağlantı ekle.
1. Belgeyi kaydedin.

Bu adımlar aşağıdaki kod örneklerinde gösterilmiştir. İlk örnekler, VSTO'yu C# kullanarak bir hücreye bağlantı eklemek için nasıl kullanacağınızı gösterir. Bu örneklerin ardından aynı işlemi Aspose.Cells for .NET kullanarak C# ile nasıl yapacağınızı gösteren örnekler bulunmaktadır.

Kod örnekleri, birinci çalışma sayfasındaki A1 hücresinde bir bağlantıya sahip bir Excel dosyası oluşturur.

![todo:image_alt_text](picture1.png)

Hücre A1'e bir bağlantı eklenir.

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

## **Örnek Kod İndir**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
