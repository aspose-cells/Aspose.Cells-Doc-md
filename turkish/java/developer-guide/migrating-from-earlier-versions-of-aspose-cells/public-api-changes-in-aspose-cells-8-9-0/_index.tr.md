---
title: Aspose.Cells 8.9.0 da Halka Açık API Değişiklikleri
type: docs
weight: 310
url: /tr/java/public-api-changes-in-aspose-cells-8-9-0/
---

{{% alert color="primary" %}} 

Bu belge, modül/uygulama geliştiricilerinin ilgisini çekebilecek Aspose.Cells API'sindeki değişiklikleri 8.8.3'ten 8.9.0'a versiyonunda açıklar. Yeni ve güncellenmiş halka açık yöntemlerin yanı sıra eklenen ve kaldırılan sınıflar vb. sadece değişikliklerin sunumunu değil, aynı zamanda Aspose.Cells'in arka planda olan davranışında herhangi bir değişikliği de açıklar.

{{% /alert %}} 
## **Eklenen API'lar**
### **Added HtmlSaveOptions.DefaultFontName Property**
Aspose.Cells for Java 8.9.0, HtmlSaveOptions sınıfı için DefaultFontName özelliğini açığa çıkardı; bu özellik, elek tablolarını HTML biçimine dönüştürürken varsayılan yazı tipi adını belirtmeyi sağlar. Varsayılan yazı tipi, stilin yazı tipi mevcut olmadığında yalnızca kullanılır. HtmlSaveOptions.DefaultFontName özelliğinin varsayılan değeri null'dur, yani, Aspose.Cells for Java API, orijinal yazı tipiyle aynı aileye sahip evrensel yazı tipini kullanır.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [Elek Tablosunu HTML Biçimine Dönüştürürken Varsayılan Yazı Tipini Belirleme] başlıklı makaleyi inceleyin.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set default font name for Html rendering

options.setDefaultFontName("Arial");

//Load a spreadsheet in an instance of Workbook

Workbook book = new Workbook(dir + "sample.xlsx");

//Save the spreadsheet in Html format while passing instance of HtmlSaveOptions

book.save(dir + "output.html", options);

{{< /highlight >}}
### **Added ImageOrPrintOptions.DefaultFont Property**
Aspose.Cells for Java 8.9.0, ImageOrPrintOptions sınıfı için varsayılan yazı tipi adını belirlemek üzere DefaultFont özelliğini açıklar. Söz konusu özellik, elektronik tablodaki Unicode karakterlerinin hücre stili üzerinde doğru yazı tipi ile ayarlanmadığı durumlarda kullanılabilir, bu nedenle bu tür karakterler sonuçta görüntülerde blok olarak görünebilir. 

{{% alert color="primary" %}} 

Unicode karakterlerini göstermek için DefaultFont özelliğini MingLiu veya MS Gothic olarak ayarlayın. Söz konusu özellik ayarlanmamışsa, Aspose.Cells, Unicode karakterlerini göstermek için sistem varsayılan yazı tipini kullanacaktır. 

{{% /alert %}} {{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [Görüntü Formatlarında Elektronik Tabloları Rendirlerken Varsayılan Yazı Tipi Ayarlama](/cells/tr/java/set-default-font-while-rendering-spreadsheet-to-images/) makalesine göz atın.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
### **Eklenen PivotTable.Excel2003Compatible Özelliği**
Aspose.Cells for Java API'si, PivotTable sınıfı için Excel 2003 uyumlu olup olmadığını belirtmek için Boolean türü Excel2003Compatible özelliğini açıklar. Excel2003Compatible özelliğinin varsayılan değeri doğrudur, bu da bir dize 255 karakterden az olmalıdır anlamına gelir. Dize 255 karakterden büyükse, kısaltılacaktır. False ise, yukarıda bahsedilen kısıtlama uygulanmayacaktır.

{{% alert color="primary" %}} 

Bu özellikle ilgili daha fazla bilgi için [Pivot Tablosu Yenilenirken Excel 2003 için Uyumlu Olup Olmadığını Belirtme](/cells/tr/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/) makalesine göz atın.

{{% /alert %}} 

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

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
