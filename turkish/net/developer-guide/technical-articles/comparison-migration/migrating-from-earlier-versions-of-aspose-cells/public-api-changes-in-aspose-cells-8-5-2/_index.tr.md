---
title: Genel API Aspose.Cells 8.5.2'deki değişiklikler
type: docs
weight: 180
url: /tr/net/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.5.1'den 8.5.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-5-2/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Çalışma Sayfasını Grafik Bağlamına Dönüştür**
 Aspose.Cells for .NET API'in bu sürümü, artık System.Drawing.Graphics sınıfının bir örneğini kabul etmeye izin veren SheetRender.ToImage yönteminin iki yeni aşırı yüklemesini ortaya çıkardı.[Grafik bağlamında oluştur](/cells/tr/net/render-worksheet-to-graphic-context/). Yeni eklenen metotların imzaları aşağıdaki gibidir.

1. SheetRender.ToImage(int pageIndex, Graphics g, kayan nokta x, kayan nokta y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float genişliği, float yüksekliği)

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Create empty Bitmap

Bitmap bmp = new Bitmap(800, 800);

//Create Graphics Context

Graphics g = Graphics.FromImage(bmp);

g.Clear(Color.Blue);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.OnePagePerSheet = true;

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.ToImage(0, g, 0, 0);

//Save the graphics context image in Png format

bmp.Save("test.png", ImageFormat.Png);

{{< /highlight >}}


### **Yöntem PivotTable.GetCellByDisplayName Eklendi**
 Aspose.Cells for .NET 8.5.2, PivotTable.GetCellByDisplayName yöntemini kullanıma sundu.[PivotField adına göre Cell nesnesini alın](/cells/tr/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Bu yöntem, PivotField başlığını vurgulamak veya biçimlendirmek istediğiniz senaryolarda yararlı olabilir.

Basit kullanım senaryosu aşağıdadır.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.PivotTables[0];

//Access cell by display name of 2nd data field of the pivot table

Cell cell = pivotTable.GetCellByDisplayName(pivotTable.DataFields[1].DisplayName);

//Access cell style and set its fill color and font color

Style style = cell.GetStyle();

style.ForegroundColor = Color.LightBlue;

style.Font.Color = Color.Black;

//Set the style of the cell

pivotTable.Format(cell.Row, cell.Column, style);

//Save workbook

workbook.Save("output.xlsx");

{{< /highlight >}}


### **Özellik SaveOptions.MergeAreas Eklendi**
Aspose.Cells for .NET 8.5.2, Boole türü değeri kabul edebilen SaveOptions.MergeAreas özelliğini kullanıma sundu. Varsayılan değer false'tur, ancak true olarak ayarlanırsa Aspose.Cells for .NET API, dosyayı kaydetmeden önce ayrı CellArea'yı birleştirmeye çalışır.

{{% alert color="primary" %}} 

Bir e-tabloda doğrulama uygulanmış çok fazla bireysel hücre varsa, ortaya çıkan e-tablonun bozulma olasılığı vardır. Muhtemel bir çözüm, hücreleri aynı doğrulama kurallarına sahip birleştirmek veya artık API'i kaydetme işleminden önce CellAreas'ı otomatik olarak birleştirmeye yönlendirmek için SaveOptions.MergeAreas özelliğini kullanabilirsiniz.

{{% /alert %}} 
### **Özellik Shape.Geometry.ShapeAdjustValues Eklendi**
 v8.5.2 sürümüyle birlikte Aspose.Cells API, şu amaçlarla kullanılabilen Shape.Geometry.ShapeAdjustValues özelliğini kullanıma sunmuştur.[farklı şekillerin ayar noktalarında değişiklik yapma](/cells/tr/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Microsoft Excel arayüzünde, ayar noktaları sarı elmas düğümler olarak görüntülenir.

{{% /alert %}} 

Örneğin,

1. Yuvarlatılmış Dikdörtgenin yayı değiştirmek için bir ayarı vardır
1. Üçgenin noktanın konumunu değiştirmek için bir ayarı vardır
1. Yamuk, üst kısmın genişliğini değiştirmek için bir ayara sahiptir
1. Baş ve kuyruğun şeklini değiştirmek için okların iki ayarı vardır

İşte en basit kullanım senaryosu.

**C#**

{{< highlight "csharp" >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook(filePath);

//Access first worksheet

Worksheet worksheet = workbook.Worksheets[0];

//Access first three shapes of the worksheet

Shape shape1 = worksheet.Shapes[0];

Shape shape2 = worksheet.Shapes[1];

Shape shape3 = worksheet.Shapes[2];

//Change the adjustment values of the shapes

shape1.Geometry.ShapeAdjustValues[0].Value = 0.5d;

shape2.Geometry.ShapeAdjustValues[0].Value = 0.8d;

shape3.Geometry.ShapeAdjustValues[0].Value = 0.5d;

//Save the workbook

workbook.Save("output.xls);

{{< /highlight >}}


### **Numaralandırma Alanı ConsolidationFunction.DistinctCount Eklendi**
 Aspose.Cells for .NET 8.5.2, ConsolidationFunction.DistinctCount alanını kullanıma sundu.[Farklı Sayı birleştirme işlevini uygulama](/cells/tr/net/consolidation-function/) bir PivotTable'ın DataField'ında.

{{% alert color="primary" %}} 

Farklı Sayı birleştirme işlevi yalnızca Microsoft Excel 2013 tarafından desteklenir.

{{% /alert %}} 
### **GridDesktop için Daha İyi Olay Yönetimi**
Aspose.Cells.GridDesktop'un bu sürümü 4 yeni olay ortaya çıkardı. Bu olaylardan 2'si, GridDesktop'ta elektronik tablo dosyalarının yüklenmesinin farklı durumlarında tetiklenirken, diğer 2'si formüllerin hesaplanması sırasında tetiklenir.

Etkinlikler aşağıdaki gibi listelenmiştir.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
