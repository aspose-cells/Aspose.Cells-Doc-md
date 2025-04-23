---
title: Bir Çalışma Kitabında Çalışsayfaları Gizlemek ve Göstermek
type: docs
weight: 80
url: /tr/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

Müşterilere çalışma kitapları sunulurken veya sunum yaparken, çalışma kitaplarında çalışsayfaları gizlemek faydalı olabilir. Yapılandırılmış bir elektronik tablo modelleme yaklaşımı, verilerin, formüllerin ve grafikler gibi görselleştirmelerin ayrı çalışma sayfalarında tutulmasını önerir. Bu yaklaşım, düzeni temiz ve basit tutar ve çalışma kitabını gezinmeyi daha kolay hale getirir. Sonuçları sunarken, verileri veya formül sayfalarını dikkat dağıtmamak için gizlemek isteyebilirsiniz.

Microsoft Excel'de çalışan kullanıcılar, çalışsayfalarını kolayca gizleyebilir ve ardından gösterebilir (gösteremez) çalışabilirler. Aynı özellikler, Excel elektronik tablolarla programlama yapan geliştiriciler için de mevcuttur. Yazılım uygulamaları içinde elektronik tablolarla çalışmanın farklı yolları bulunmaktadır. Bir yöntem, VSTO'nun kullanılmasıdır, diğer bir yöntem de Aspose.Cells for .NET'nin kullanılmasıdır.

{{% /alert %}}

## **Çalışsayfalarını Gizleme ve Gösterme**

Bu makale, [VSTO ile](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) veya C# veya Visual Basic kullanarak çalışmayı [gizleme](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) ve [gösterme](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) işlemlerini [Aspose.Cells ile](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) yine C# veya Visual Basic kullanarak karşılaştırmaktadır. Aspose.Cells, Microsoft Excel yüklü olmadan çalışmanızı sağlar.

Bir çalışsayfayı gizlemek için izlenmesi gereken adımlar:

1. Bir dosyayı açın.
1. Bir çalışsayfayı alın.
1. Çalışsayfayı gizleyin.
1. Dosyayı kaydedin.

Bir çalışsayfayı [gizledikten](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) sonra tekrar görünür hale getirmek için sadece gizlenen çalışsayfanın görünürlüğünü açın.

Aşağıdaki kod örnekleri ilk olarak bir çalışma sayfasını gizlemeyi nasıl gösterir. İlk örnekler, [VSTO ile](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/), yine C# veya Visual Basic kullanarak, aynı görevi [Aspose.Cells ile](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) yine C# veya Visual Basic kullanarak karşılaştırır.

İkinci kod örnekleri, [VSTO'da](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) veya [Aspose.Cells'da](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) çalışma sayfasını göstermek için kullanılan satırı gösterir.

## **Çalışsayfaları Gizleme**

Aşağıda, çalışma kitabında bir çalışsayfayı gizlemek için VSTO ve Aspose.Cells için çözümlemeleri gösteren kod örnekleri bulunmaktadır.

### **VSTO ile Çalışma Sayfalarını Gizleme**

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



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Aspose.Cells for .NET ile Çalışma Sayfalarını Gizleme**

**C#**

{{< highlight csharp >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Çalışma Sayfalarını Gösterme**

Aşağıda, çalışma kitabında bir çalışsayfayı yeniden göstermek için VSTO ve Aspose.Cells için kod örnekleri bulunmaktadır.

### **VSTO ile Bir Çalışma Sayfasını Gösterme**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Aspose.Cells for .NET ile Bir Çalışma Sayfasını Gösterme**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
