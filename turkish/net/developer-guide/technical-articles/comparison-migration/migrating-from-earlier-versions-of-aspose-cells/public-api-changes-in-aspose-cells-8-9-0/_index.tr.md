---
title: Aspose.Cells 8.9.0 da Halka Açık API Değişiklikleri
type: docs
weight: 300
url: /tr/net/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.8.3'ten 8.9.0'a versiyonunda açıklar. Yeni ve güncellenmiş halka açık yöntemlerin yanı sıra eklenen ve kaldırılan sınıflar vb. sadece değişikliklerin sunumunu değil, aynı zamanda Aspose.Cells'in arka planda olan davranışında herhangi bir değişikliği de açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **Added HtmlSaveOptions.DefaultFontName Property**
Aspose.Cells for .NET 8.9.0, HtmlSaveOptions sınıfı için varsayılan yazı tipi adını belirlemeye izin veren DefaultFontName özelliğini ortaya çıkardı. Varsayılan yazı tipi, yalnızca stilin yazı tipi mevcut olmadığında kullanılır. HtmlSaveOptions.DefaultFontName özelliğinin varsayılan değeri, orijinal yazı tipiyle aynı aileye sahip evrensel yazı tipini kullanacaktır.

{{% alert color="primary" %}} 

Bu özelliğin ayrıntıları için lütfen [HTML Formatına Rendere Etmek İçin Varsayılan Yazı Tipi Ayarlama](/cells/tr/net/set-default-font-while-rendering-spreadsheet-to/) makalesini inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **Added ImageOrPrintOptions.DefaultFont Property**
Aspose.Cells for .NET 8.9.0, ImageOrPrintOptions sınıfı için Varsayılan Yazı Tipi adını ayarlamayı sağlayan DefaultFont özelliğini açıklıyor. Söz konusu özellik, elektronik tablodaki Unicode karakterlerinin hücre stili içinde doğru yazı tipiyle ayarlanmadığı durumlarda kullanılabilir, bu nedenle bu tür karakterler sonuç resimlerinde bloklar olarak görünebilir.

{{% alert color="primary" %}} 

Unicode karakterlerini göstermek için DefaultFont özelliğini MingLiu veya MS Gothic olarak ayarlayın. Söz konusu özellik ayarlanmamışsa, Aspose.Cells, Unicode karakterlerini göstermek için sistem varsayılan yazı tipini kullanacaktır.

{{% /alert %}} {{% alert color="primary" %}} 

Bu özelliğin ayrıntıları için lütfen [Görüntü Biçimlerine Rendere Etmek İçin Varsayılan Yazı Tipini Ayarlama](/cells/tr/net/set-default-font-while-rendering-spreadsheet-to-images/) makalesini inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Create an instance of ImageOrPrintOptions

var options = new ImageOrPrintOptions();

// Set default font name for image rendering

options.DefaultFont = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the worksheet to be rendered

var sheet = book.Worksheets[0];

// Create an instance of SheetRender

var render = new SheetRender(sheet, options);

// Save spreadsheet to image

render.ToImage(0, dir + "output.png");

{{< /highlight >}}


### **PivotTable.IsExcel2003Compatible Özelliği Eklendi**
Aspose.Cells for .NET API, PivotTable sınıfı için Excel 2003 uyumlu olup olmadığını belirtmeyi sağlayan Boolean türünde IsExcel2003Compatible özelliğini açıklamıştır. IsExcel2003Compatible özelliğinin varsayılan değeri true'dur; bu, bir dizenin 255 karakterden küçük veya eşit olması gerektiği anlamına gelir. Dize 255 karakterden büyükse kısaltılacaktır. false ise, söz konusu kısıtlama uygulanmayacaktır.

{{% alert color="primary" %}} 

Bu özelliğin ayrıntıları için lütfen [Pivot Tablolarını Yeniden Oluştururken Excel 2003 Uyumluluğu](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/) makalesini inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

 // Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Access the desired Pivot Table from the spreadsheet

var pivot = book.Worksheets[0].PivotTables[0];

// Set Excel 2003 compatibility to false

pivot.IsExcel2003Compatible = false;

// Refresh & recalculate Pivot Table

pivot.RefreshData();

pivot.CalculateData();

{{< /highlight >}}


### **GridWeb.GetVersion Yöntemi Eklendi**
Aspose.Cells.GridWeb for .NET 8.9.0, GridWeb bileşeninin sürümünü döndüren {GetVersion}} fabrika yöntemini açıklamıştır.
