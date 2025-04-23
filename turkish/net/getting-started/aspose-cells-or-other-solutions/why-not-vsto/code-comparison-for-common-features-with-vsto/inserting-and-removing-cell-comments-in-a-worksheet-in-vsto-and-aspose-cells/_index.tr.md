---
title: VSTO ve Aspose.Cells te Çalışma Kitabında Hücre Yorumları Eklemek ve Kaldırmak
type: docs
weight: 150
url: /tr/net/inserting-and-removing-cell-comments-in-a-worksheet-in-vsto-and-aspose-cells/
---

Hücrelere yorum eklemek için:

1. Mevcut bir Excel dosyasını açın.
1. Bir hücreye yorum ekleyin.
1. Dosyayı kaydedin.

Yorumları kaldırmak için, süreç benzerdir, tek fark yorumun kaldırılmasıdır.

Aşağıdaki kod örnekleri önce bir yorum eklemenin nasıl yapıldığını ve ardından VSTO veya Aspose.Cells for .NET ile nasıl yorum kaldırılacağını göstermektedir.
## **Yorum Ekleme**
Bu kod parçacıkları, önce VSTO (C#) ile bir hücreye nasıl yorum ekleneceğini ve ardından Aspose.Cells for .NET (C#) ile nasıl ekleneceğini göstermektedir.
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

 Excel.Application excelApp = Application;

//Specify the template excel file path.

  string myPath = "Book1.xls";

//Open the excel file.

 excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value);

//Get the A1 cell.

 Excel.Range rng1 = excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

 rng1.AddComment("This is my comment");

//Save the file.

  excelApp.ActiveWorkbook.Save();

//Quit the Application.

  excelApp.Quit();

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Specify the template excel file path.

string myPath = "Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

 Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

 int commentIndex = workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

 Comment comment = workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

 comment.Note = "This is my comment";

//Save As the excel file.

 workbook.Save("Book1.xls");

{{< /highlight >}}
## **Yorumları Kaldırma**
Bir hücreden yorumu kaldırmak için VSTO (C#) ve Aspose.Cells for .NET (C#) için aşağıdaki kod satırlarını kullanın.
### **VSTO**
{{< highlight csharp >}}

 //Remove the comment.

  rng1.Comment.Delete();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //removing comments

 workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
## **Örnek Kod İndir**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Inserting.and.Removing.Cell.Comments.in.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Inserting%20and%20Removing%20Cell%20Comments%20in%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
