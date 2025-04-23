---
title: Bir Çalışma Sayfasının Arka Plan Resmini Ayarla
type: docs
weight: 90
url: /tr/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Arka plan resimleri, bir elektronik tabloda metin ve çizgilerin arkasına yerleşir. Bir çalışma kitabı hakkında bilgi vermek için kullanılır, örneğin durum filigranları olarak kullanıldığında, ancak aynı zamanda şirket markasını veya süslemesini de ekleyebilir. Microsoft Excel, kullanıcıların arka plan resimleri eklemelerine izin verir. Geliştiriciler, uygulamaları üzerinden, Aspose.Cells for .NET veya VSTO kullanarak arka plan resimleri de ekleyebilirler. Bu makale, bu iki yaklaşımı karşılaştırır.

Bu makaledeki kod örnekleri, önce [VSTO](/cells/tr/net/set-background-picture-of-a-worksheet/) ile, C# veya Visual Basic kullanarak ve ardından [Aspose.Cells for .NET](/cells/tr/net/set-background-picture-of-a-worksheet/) ile, yine C# veya Visual Basic kullanarak, bunu nasıl yapacağınızı gösterir.

{{% /alert %}}

## **Bu makaledeki kod örnekleri, aşağıda ekran görüntüsündeki gibi, tekrarlanan bir arka plan görüntüsüne sahip bir çalışma sayfası oluşturur.**

Bir elektronik tabloya arka plan resmi uygulamak için:

1. Bir çalışma kitabı oluşturun ve arka plan resmi uygulamak istediğiniz sayfaya erişin.
1. Arka plan resmini uygulayın.
1. Çalışma kitabını kaydedin.

Aşağıda verilen kod örnekleri, bunu önce [VSTO](/cells/tr/net/set-background-picture-of-a-worksheet/) ile, C# veya Visual Basic kullanarak veya [Aspose.Cells for .NET](/cells/tr/net/set-background-picture-of-a-worksheet/) ile, yine C# veya Visual Basic kullanarak nasıl yapılacağını gösterir.

Bu makaledeki kod örnekleri, aşağıdaki ekran görüntüsündeki gibi tekrarlayan bir arka plan resmi olan bir çalışsayfa oluşturur.

**Çalışsayfa için bir arka plan belirlenmiştir.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### ****Bir çalışma sayfası için arka plan belirlendi.****

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

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("e:\\test\\school.jpg");

//Save the excel file.

objBook.SaveCopyAs("c:\\BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET ile Arka Plan Resimleri Belirleme**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet. 

Worksheet sheet = workbook.Worksheets[0];



//Define a string variable to store the image path.

string ImageUrl = @"e:\test\school.jpg";

//Get the picture into the streams.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[] imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
