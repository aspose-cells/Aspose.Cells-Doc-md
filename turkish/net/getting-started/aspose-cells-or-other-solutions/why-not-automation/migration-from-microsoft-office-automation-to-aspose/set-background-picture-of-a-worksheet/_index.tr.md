---
title: Bir Çalışma Sayfasının Arka Plan Resmini Ayarlama
type: docs
weight: 90
url: /tr/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

Arka plan resimleri, bir e-tablodaki metnin ve satırların arkasında bulunur. Bir çalışma kitabı hakkında bilgi vermek için kullanılırlar, örneğin durum filigranı olarak kullanıldıklarında, ancak şirket markasını veya dekorasyonu da ekleyebilirler. Microsoft Excel, kullanıcıların arka plan resimlerini manuel olarak eklemesine olanak tanır.

Geliştiriciler ayrıca uygulamaları aracılığıyla Aspose.Cells for .NET veya VSTO kullanarak arka plan resimleri ekleyebilirler. Bu makale iki yaklaşımı karşılaştırmaktadır.

{{% /alert %}}

## **Çalışma Sayfasında Arka Plan Resmi Ayarlama**

Bir e-tabloya arka plan resmi uygulamak için:

1. Bir çalışma kitabı oluşturun ve arka plan resmi uygulamak istediğiniz sayfaya erişin.
1. Arka plan resmini uygulayın.
1. Çalışma kitabını kaydedin.

 Aşağıdaki kod örnekleri, öncelikle bunun nasıl yapılacağını gösterir.[VSTO](/cells/tr/net/set-background-picture-of-a-worksheet/) , C# veya Visual Basic kullanarak ve ardından[Aspose.Cells for .NET](/cells/tr/net/set-background-picture-of-a-worksheet/), yine C# veya Visual Basic kullanarak.

Bu makaledeki kod örnekleri, aşağıdaki ekran görüntüsündeki gibi yinelenen bir arka plan görüntüsüne sahip bir çalışma sayfası oluşturur.

**Çalışma sayfası için bir arka plan ayarlandı.**

![yapılacaklar:resim_alternatif_metin](set-background-picture-of-a-worksheet_1.png)

### **VSTO ile Arka Plan Resimleri Ayarlama**

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

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("e:\\test\\school.jpg");

//Save the excel file.

objBook.SaveCopyAs("c:\\BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET ile Arka Plan Resimlerinin Ayarlanması**

**C#**

{{< highlight "csharp" >}}

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

byte[]imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
