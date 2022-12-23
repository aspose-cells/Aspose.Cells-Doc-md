---
title: Genel API Aspose.Cells 8.9.0'daki değişiklikler
type: docs
weight: 300
url: /tr/net/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.8.3 sürümünden 8.9.0 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **HtmlSaveOptions.DefaultFontName Özelliği eklendi**
Aspose.Cells for .NET 8.9.0, elektronik tabloları HTML biçiminde işlerken varsayılan yazı tipi adını belirtmeye izin veren HtmlSaveOptions sınıfı için DefaultFontName özelliğini kullanıma sundu. Varsayılan yazı tipi, yalnızca stil yazı tipi olmadığında kullanılacaktır. HtmlSaveOptions.DefaultFontName özelliğinin varsayılan değeri boştur, yani Aspose.Cells for .NET API orijinal yazı tipiyle aynı aileye sahip evrensel yazı tipini kullanır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Elektronik Tabloları Oluşturmak için Varsayılan Yazı Tipini HTML Biçimine Ayarlama](/cells/tr/net/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 // Create an instance of HtmlSaveOptions

var options = new HtmlSaveOptions();

// Set default font name for Html rendering

options.DefaultFontName = "Arial";

// Load a spreadsheet in an instance of Workbook

var book = new Workbook(dir + "sample.xlsx");

// Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.Save(dir + "output.html", options);

{{< /highlight >}}


### **ImageOrPrintOptions.DefaultFont Özelliği Eklendi**
Aspose.Cells for .NET 8.9.0, DefaultFont özelliğini göstererek ImageOrPrintOptions sınıfı için varsayılan yazı tipi adının ayarlanmasına izin verir. Söz konusu özellik, elektronik tablodaki Unicode karakterler hücre stilinde doğru yazı tipiyle ayarlanmadığında kullanılabilir, bu nedenle bu tür karakterler elde edilen görüntülerde bloklar olarak görünebilir.

{{% alert color="primary" %}} 

Unicode karakterleri göstermek için DefaultFont özelliğini MingLiu veya MS Gothic olarak ayarlayın. Söz konusu özellik ayarlanmazsa, Aspose.Cells, Unicode karakterleri göstermek için sistemin varsayılan yazı tipini kullanır.

{{% /alert %}} {{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Elektronik Tabloları Görüntü Formatlarında Oluşturmak için Varsayılan Yazı Tipini Ayarlama](/cells/tr/net/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells for .NET API, PivotTable sınıfı için, PivotTable'ın yenileme amacıyla Excel 2003 uyumlu olup olmadığını belirtmeye olanak tanıyan Boolean türü IsExcel2003Compatible özelliğini kullanıma sundu. IsExcel2003Compatible özelliğinin varsayılan değeri true'dur; bu, bir dizenin 255 karakterden küçük veya eşit olması gerektiği anlamına gelir. Dize 255 karakterden uzunsa kesilecektir. Yanlış ise, yukarıda belirtilen kısıtlama uygulanmaz.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Pivot Tabloları Yenilemek için Excel 2003 Uyumluluğu](https://docs.aspose.com/cells/net/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

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
Aspose.Cells.GridWeb for .NET 8.9.0, GridWeb bileşeninin yayın sürümünü döndüren {GetVersion}} fabrika yöntemini kullanıma sundu.
