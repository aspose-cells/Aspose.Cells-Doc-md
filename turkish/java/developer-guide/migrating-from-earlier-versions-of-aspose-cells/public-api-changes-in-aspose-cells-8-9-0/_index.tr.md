---
title: Genel API Aspose.Cells 8.9.0'daki değişiklikler
type: docs
weight: 310
url: /tr/java/public-api-changes-in-aspose-cells-8-9-0/
---
{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek 8.8.3 sürümünden 8.9.0 sürümüne Aspose.Cells API üzerindeki değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri, eklenen ve kaldırılan sınıfları vb. değil, aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'ler**
### **HtmlSaveOptions.DefaultFontName Özelliği eklendi**
Aspose.Cells for Java 8.9.0, HtmlSaveOptions sınıfı için elektronik tabloları HTML biçiminde işlerken varsayılan yazı tipi adını belirtmeye izin veren DefaultFontName özelliğini kullanıma sundu. Varsayılan yazı tipi, yalnızca stil yazı tipi olmadığında kullanılacaktır. HtmlSaveOptions.DefaultFontName özelliğinin varsayılan değeri boştur, yani Aspose.Cells for Java API, orijinal yazı tipiyle aynı aileye sahip evrensel yazı tipini kullanır.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[E-tabloları HTML Biçiminde İşleme İçin Varsayılan Yazı Tipini Ayarlama](/cells/tr/java/set-default-font-while-rendering-spreadsheet-to/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **ImageOrPrintOptions.DefaultFont Özelliği Eklendi**
Aspose.Cells for Java 8.9.0, DefaultFont özelliğini göstererek ImageOrPrintOptions sınıfı için varsayılan yazı tipi adının ayarlanmasına izin verir. Söz konusu özellik, elektronik tablodaki Unicode karakterler hücre stilinde doğru yazı tipiyle ayarlanmadığında kullanılabilir, bu nedenle bu tür karakterler elde edilen görüntülerde bloklar olarak görünebilir.

{{% alert color="primary" %}} 

 Unicode karakterleri göstermek için DefaultFont özelliğini MingLiu veya MS Gothic olarak ayarlayın. Söz konusu özellik ayarlanmazsa, Aspose.Cells, Unicode karakterleri göstermek için sistemin varsayılan yazı tipini kullanır.

{{% /alert %}} {{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Elektronik Tabloları Görüntü Formatlarında Oluşturmak için Varsayılan Yazı Tipini Ayarlama](/cells/tr/java/set-default-font-while-rendering-spreadsheet-to-images/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Create an instance of ImageOrPrintOptions

ImageOrPrintOptions options = new ImageOrPrintOptions();

//Set default font name for image rendering

options.setDefaultFont("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the worksheet to be rendered

Worksheet sheet = book.getWorksheets().get(0);

//Create an instance of SheetRender

SheetRender render = new SheetRender(sheet, options);

//Save spreadsheet to image

render.toImage(0, dir + "output.png");

{{< /highlight >}}
### **PivotTable.Excel2003Compatible Özelliği Eklendi**
Aspose.Cells for Java API, PivotTable sınıfı için, PivotTable'ın Excel 2003 ile uyumlu olup olmadığını yenileme amacıyla belirtmeye izin veren Boolean türü Excel2003Compatible özelliğini kullanıma sundu. Excel2003Compatible özelliğinin varsayılan değeri true'dur; bu, bir dizenin 255 karakterden küçük veya eşit olması gerektiği anlamına gelir. Dize 255 karakterden uzunsa kesilecektir. Yanlış ise, yukarıda belirtilen kısıtlama uygulanmaz.

{{% alert color="primary" %}} 

 Bu özellikle ilgili daha fazla ayrıntı için lütfen şu makaleyi inceleyin:[Pivot Tabloları Yenilemek için Excel 2003 Uyumluluğu](/cells/tr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/).

{{% /alert %}} 

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Access the desired Pivot Table from the spreadsheet

PivotTable pivot = book.getWorksheets().get(0).getPivotTables().get(0);

//Set Excel 2003 compatibility to false

pivot.setExcel2003Compatible(false);

//Refresh & recalculate Pivot Table

pivot.refreshData();

pivot.calculateData();

{{< /highlight >}}
