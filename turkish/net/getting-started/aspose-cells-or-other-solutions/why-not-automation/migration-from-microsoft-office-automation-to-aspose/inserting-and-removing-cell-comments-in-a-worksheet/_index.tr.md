---
title: Çalışma Sayfasındaki Hücre Yorumlarını Eklemek ve Kaldırmak
type: docs
weight: 30
url: /tr/net/inserting-and-removing-cell-comments-in-a-worksheet/
---

{{% alert color="primary" %}}

Genellikle yorumlar, çalışsayfadaki hücrelere ek bilgi eklemek için kullanılır. Her zaman kullanırız ve artık ihtiyaç duymadığımızda silebiliriz. Yorumlar, belirli bir değeri belgelemek veya bir formülün ne yaptığını hatırlamak için faydalıdır. Bir yoruma sahip bir hücrenin üzerine fare işaretçisini götürdüğünüzde, yorum küçük bir kutuda ortaya çıkar.

Bu makalede, VSTO ve Aspose.Cells for .NET kullanarak hücrelere yorum eklemeyi ve kaldırmayı nasıl karşılaştırıyoruz. Aspose.Cells for .NET, Office Otomasyonundan bağımsız olarak Microsoft Excel dosyaları ile çalışır ve elektronik tablolar oluşturmak ve değiştirmek için güçlü araçlar sunar.

{{% /alert %}}

## **Hücrelere Yorum Eklemek ve Kaldırmak**

Hücrelere yorum eklemek için:

1. Mevcut bir Excel dosyasını açın.
1. Bir hücreye yorum ekleyin.
1. Dosyayı kaydedin.

Yorumları kaldırmak için, süreç benzerdir, tek fark yorumun kaldırılmasıdır.

Aşağıdaki kod örnekleri öncelikle bir hücreye [yorum eklemeyi](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) ve ardından VSTO veya Aspose.Cells for .NET ile [yorumu kaldırmayı](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) nasıl gösterir.

## **Yorum Ekleme**

Bu kod parçaları, önce bir hücreye [VSTO ile](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) ve sonra [Aspose.Cells for .NET ile](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) bir yorum eklemeyi gösterir.

### **VSTO ile Yorum Ekleme**

**C#**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

Bir hücreden yorumu kaldırmak için [VSTO ile](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) ve .NET için [Aspose.Cells](/cells/tr/net/inserting-and-removing-cell-comments-in-a-worksheet/) (C#, VB) için aşağıdaki kod satırlarını kullanın.

### **VSTO ile Yorum Kaldırma**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

rng1.Comment.Delete();    



{{< /highlight >}}

### **Aspose.Cells for .NET ile Yorum Kaldırma**

**C#**

{{< highlight csharp >}}

 //Remove the comment.

workbook.Worksheets[0].Comments.RemoveAt("A1");

{{< /highlight >}}
