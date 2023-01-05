---
title: Bir Çalışma Sayfasına Cell Yorum Ekleme ve Kaldırma
type: docs
weight: 30
url: /tr/net/inserting-and-removing-cell-comments-in-a-worksheet/
---
{{% alert color="primary" %}}

Genel olarak, açıklamalar bir çalışma sayfasındaki hücrelere ek bilgi eklemek için kullanılır. Onları ara sıra kullanırız ve artık onlara ihtiyacımız kalmadığında sileriz. Belirli bir değeri belgelemeniz gerekiyorsa veya bir formülün ne yaptığını hatırlamanıza yardımcı olması için yorumlar kullanışlıdır. Fare işaretçisini yorumu olan bir hücrenin üzerine getirdiğinizde, yorum küçük bir kutuda açılır.

Bu makalede, VSTO ve Aspose.Cells for .NET kullanarak hücrelere nasıl yorum ekleneceğini ve kaldırılacağını karşılaştırıyoruz. Aspose.Cells for .NET, Office Automation'dan bağımsız olarak Microsoft Excel dosyalarıyla çalışır ve size elektronik tablo oluşturmak ve değiştirmek için güçlü araçlar sunar.

{{% /alert %}}

## **Yorum Ekleme ve Kaldırma Cells**

Hücrelere yorum eklemek için:

1. Mevcut bir Excel dosyasını açın.
1. Bir hücreye yorum ekleyin.
1. Dosya 'yı kaydet.

Yorumları kaldırmak için, yorumun kaldırılması dışında süreç benzerdir.

 Aşağıdaki kod örnekleri, öncelikle nasıl yapılacağını gösterir.[yorum ekle](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) ve sonra nasıl[bir yorumu kaldır](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) VSTO veya Aspose.Cells for .NET ile.

## **Yorum ekleme**

 Bu kod parçacıkları, önce bir hücreye nasıl yorum ekleneceğini gösterir.[VSTO](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) ve ardından[Aspose.Cells for .NET](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB).

### **VSTO ile Yorum Ekleme**

**C#**

{{< highlight "csharp" >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the A1 cell.

Excel.Range rng1=excelApp.get_Range("A1", Missing.Value);

//Add the comment with text.

rng1.AddComment("This is my comment");

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

### **Aspose.Cells for .NET ile Yorum Ekleme**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Specify the template excel file path.

string myPath=@"d:\test\Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Add a Comment to A1 cell.

int commentIndex=workbook.Worksheets[0].Comments.Add("A1");

//Accessing the newly added comment

Comment comment=workbook.Worksheets[0].Comments[commentIndex];

//Setting the comment note

comment.Note="This is my comment";

//Save As the excel file.

workbook.Save(@"d:\test\Book1.xls");



{{< /highlight >}}

## **Yorumları Kaldırma**

 Bir hücreden yorumu kaldırmak için aşağıdaki kod satırlarını kullanın.[VSTO](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) ve[Aspose.Cells](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) for .NET (C#, VB).

### **VSTO ile Yorum Kaldırma**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Aspose.Cells for .NET İle Yorum Kaldırma**

**C#**

{{< highlight "csharp" >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
