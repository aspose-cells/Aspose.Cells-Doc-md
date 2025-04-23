---
title: Çalışma Kitaplarını Koruma ve Korumasını Kaldırma
type: docs
weight: 20
url: /tr/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

Kullanıcıların çalışma sayfalarını yanlışlıkla veya kasıtlı olarak değiştirmesini, taşımasını veya silmesini engellemek için çalışma kitabı öğelerini şifreleyebilirsiniz. Yeni çalışma sayfaları eklenmeyip, taşınamayan, silinemeyen, gizlenemeyen veya yeniden adlandırılamayan bir çalışma kitabının yapısını korumak için KorumaTürünü belirtin.

Çalışma kitaplarınızı korumak ve korumayı kaldırmak için VSTO ve Aspose.Cells for .NET kullanarak iki yöntemi karşılaştırabilmeniz için [koruma](/cells/tr/net/protecting-and-unprotecting-workbooks/) ve [korumayı kaldırma](/cells/tr/net/protecting-and-unprotecting-workbooks/) yöntemlerini nasıl göstereceğimizi gösteren paralel kod parçalarını aşağıda bulabilirsiniz.

Aspose.Cells, Microsoft Office Otomasyonundan bağımsız olarak çalışır ve kullanımı kolay olacak şekilde geliştirilmiştir ve temiz kod üretir.

Bir çalışma kitabını korumak, kullanıcıların hücreleri düzenlemesini durdurmaz. Verileri korumak için çalışma sayfalarını korumalısınız.

{{% /alert %}} 
## **Bir Çalışma Kitabını Koruma**
Var olan bir Microsoft Excel dosyasını açın, çalışma kitabını yapı ve Windows özellikleriyle koruyun ve dosyayı kaydedin.

Bir çalışma kitabını korumanın nasıl yapıldığını gösteren VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) üzerinde paralel kod parçaları aşağıda verilmiştir.
### **VSTO**
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

{{< highlight csharp >}}

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
## **Bir Çalışma Kitabını Korumasız Bırakma**
Bir çalışma kitabını korumasız bırakmak için VSTO (C#, VB) ve Aspose.Cells for .NET (C#, VB) için aşağıdaki kod satırlarını kullanın.
### **VSTO**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
