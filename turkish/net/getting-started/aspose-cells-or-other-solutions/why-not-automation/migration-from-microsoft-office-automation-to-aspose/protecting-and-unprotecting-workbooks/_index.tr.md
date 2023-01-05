---
title: Çalışma Kitaplarını Koruma ve Korumayı Kaldırma
type: docs
weight: 20
url: /tr/net/protecting-and-unprotecting-workbooks/
---
{{% alert color="primary" %}} 

Birinin çalışma sayfalarını yanlışlıkla veya kasıtlı olarak değiştirmesini, taşımasını veya silmesini önlemek için, çalışma kitabı öğelerini parolayla veya parola olmadan koruyabilirsiniz. Bir çalışma kitabının yapısını korumak için çalışma kitabındaki çalışma sayfalarının taşınması, silinmesi, gizlenmesi, gösterilmesi veya yeniden adlandırılması ve yeni çalışma sayfalarının eklenmemesi için, ProtectionType'ı Yapı olarak belirtin.

 Çalışma kitabı her açıldığında aynı boyut ve konumda olacak şekilde Windows'i korumak için, ProtectionType'ı Windows olarak belirtin. Bu makalede, nasıl yapılacağını gösteriyoruz.[korumak](/cells/tr/net/protecting-and-unprotecting-workbooks/) ve[korumayı kaldırmak](/cells/tr/net/protecting-and-unprotecting-workbooks/) iki yöntemi karşılaştırmanıza izin vermek için VSTO ve Aspose.Cells for .NET kullanan çalışma kitapları.

Aspose.Cells, Microsoft Ofis Otomasyonundan bağımsız olarak çalışır ve kullanımı kolay ve düzgün kod üretecek şekilde geliştirilmiştir.

Bir çalışma kitabının korunması, kullanıcıların hücreleri düzenlemesini engellemez. Verileri korumak için çalışma sayfalarını korumanız gerekir.

{{% /alert %}} 
## **Çalışma Kitabını Koruma**
Mevcut bir Microsoft Excel dosyasını açmak için çalışma kitabını yapı ve Windows öznitelikleri ile koruyun ve dosyayı kaydedin.

Aşağıda, bir çalışma kitabının nasıl korunacağını gösteren VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) için paralel kod parçacıkları bulunmaktadır.
### **VSTO**
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

string myPath = @"d:\test\MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Protect the workbook specifying a password with Structure and Windows attributes.

excelApp.ActiveWorkbook.Protect("007", true, true);

//Save the file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......


//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

workbook.Protect(ProtectionType.All,"007");

//Save As the excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}
## **Bir Çalışma Kitabının Korumasını Kaldırmak**
Bir çalışma kitabının korumasını kaldırmak için VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) için aşağıdaki kod satırlarını kullanın.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
