---
title: Bir Çalışma Kitabında Çalışma Sayfalarını Gizle ve Göster
type: docs
weight: 80
url: /tr/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

Çalışma kitaplarını müşterilere sunarken veya sunum yaparken, çalışma kitaplarını çalışma kitabında gizlemek yararlı olabilir. Elektronik tablo modellemeye yönelik yapılandırılmış bir yaklaşım, grafikler gibi verilerin, formüllerin ve görselleştirmelerin ayrı sayfalarda tutulmasını önerir. Bu yaklaşım, düzeni temiz ve basit tutar ve çalışma kitabında gezinmeyi kolaylaştırır. Sonuçları sunarken dikkatin dağılmasını önlemek için verileri veya formül sayfalarını gizlemek isteyebilirsiniz.

Microsoft Excel'de çalışan kullanıcılar, çalışma sayfalarını kolayca gizleyebilir ve ardından gösterebilir (gösterebilir). Aynı özellikler, Excel elektronik tablolarıyla programlama yapan geliştiriciler tarafından kullanılabilir. Yazılım uygulamalarının içinden elektronik tablolarla çalışmanın farklı yolları vardır. Bir yöntem VSTO kullanmak, diğeri ise Aspose.Cells for .NET.

{{% /alert %}}

## **Çalışma Sayfalarını Gizleme ve Gösterme**

 Bu makale karşılaştırır[saklanmak](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) ve[gizleme](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) ile çalışma sayfaları[VSTO](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) ile aynı görevi gerçekleştirmek için C# veya Visual Basic kullanarak[Aspose.Cells](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/), yine C# veya Visual Basic kullanarak. Aspose.Cells, Microsoft Excel yüklü olmadan çalışmanıza izin verir.

Bir çalışma sayfasını gizleme adımları şunlardır:

1. Bir dosya aç.
1. Bir çalışma sayfası alın.
1. Çalışma sayfasını gizleyin.
1. Dosya 'yı kaydet.

 İle[göster](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) tekrar bir çalışma sayfası, sadece gizli sayfa için görünürlüğü açın.

 Aşağıdaki kod örnekleri öncelikle bir çalışma sayfasının nasıl gizleneceğini gösterir. İlk örnekler ile süreci gösterir[VSTO](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) C# veya Visual Basic kullanarak, kullanmaya kıyasla[Aspose.Cells](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/), yine C# veya Visual Basics kullanarak.

 İkinci kod örnekleri grubu, çalışma sayfasını göstermek için kullanılan satırı gösterir.[VSTO](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/) veya[Aspose.Cells](/cells/tr/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Çalışma Sayfalarını Gizleme**

Aşağıda, çalışma kitabında bir çalışma sayfasının nasıl gizleneceğini gösteren VSTO ve Aspose.Cells kod örnekleri bulunmaktadır.

### **Çalışma Sayfalarını VSTO ile Gizleme**

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

{{< highlight "csharp" >}}



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

Aşağıda, çalışma kitabında bir çalışma sayfasının nasıl gösterileceğini gösteren VSTO ve Aspose.Cells kod örnekleri bulunmaktadır.

### **Bir Çalışma Sayfasını VSTO ile Gösterme**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Aspose.Cells for .NET ile Çalışma Sayfasını Gösterme**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
