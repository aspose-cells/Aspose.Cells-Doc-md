---
title: Aspose.Cells 8.5.2 de Yapılan Genel API Değişiklikleri
type: docs
weight: 180
url: /tr/net/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Bu belge, 8.5.1'den 8.5.2 sürümüne kadar Aspose.Cells API'deki değişiklikleri modül / uygulama geliştiricileri için ilgi çekebilecek değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemleri [eklenen sınıflar vb.](/cells/tr/net/public-api-changes-in-aspose-cells-8-5-2/) sadece içermez ayrıca Aspose.Cells'in perde arkasındaki herhangi bir değişikliğin açıklamasını da içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Çalışsayısını Grafiksel Ortama Dönüştürme**
Aspose.Cells for .NET API'nin bu sürümü, artık SheetRender.ToImage yönteminin iki yeni aşırı yüklemesini ortaya çıkardı, bu da System.Drawing.Graphics sınıfının bir örneğini [Grafik bağlamında oluşturmaya izin verir](/cells/tr/net/render-worksheet-to-graphic-context/). Yeni eklenen yöntemlerin imzaları şu şekildedir.

1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)
1. SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float height)

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **PivotTable.GetCellByDisplayName Yöntemi Eklendi**
Aspose.Cells for .NET 8.5.2, PivotTable.GetCellByDisplayName yöntemini açığa çıkardı. Bu yöntem, PivotField'in adıyla [hücre nesnesini almak için kullanılabilir](/cells/tr/net/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Bu yöntem, PivotField başlığını vurgulamak veya biçimlendirmek istediğiniz senaryolarda kullanışlı olabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**C#**

{{< highlight csharp >}}

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


### **Eklenen SaveOptions.MergeAreas Özelliği**
Aspose.Cells for .NET 8.5.2, SaveOptions.MergeAreas özelliğini açığa çıkardı ve Boolean tür değer alabilir. Varsayılan değer false'dur, ancak true olarak ayarlanırsa, Aspose.Cells for .NET API dosyayı kaydetmeden önce bireysel CellArea'ları birleştirmeye çalışır.

{{% alert color="primary" %}} 

Bir elektronik tabloda uygulanan çok sayıda tekil hücre varsa, sonucun bozulma olasılıkları vardır. Tekil doğrulama kurallarına sahip hücreleri birleştirmenin bir olası çözümü veya Aspose.Cells for Java API'nın kaydetme işleminden önce hücre Alanlarını otomatik olarak birleştirmek için artık SaveOptions.MergeAreas özelliğini kullanabilirsiniz.

{{% /alert %}} 
### **Shape.Geometry.ShapeAdjustValues Özelliği Eklendi**
8.5.2 sürümüyle Aspose.Cells API, Shape.Geometry.ShapeAdjustValues özelliğini açığa çıkardı ve farklı şekillerin ayarlama noktalarına [değişiklik yapmak için kullanılabilir](/cells/tr/net/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Microsoft Excel arayüzünde, ayarlama noktaları sarı elmas düğmeleri olarak görüntülenir.

{{% /alert %}} 

Örneğin,

1. Yuvarlatılmış Dikdörtgenin yay'ı değiştirmek için bir ayarı vardır
1. Üçgen'in noktasının konumunu değiştirmek için bir ayarı vardır
1. Yaygın olmayan yukarıda bir ayarı değiştirmek için bir ayarı vardır
1. Okların kuyruk ve başının şeklini değiştirmek için iki ayarı vardır

İşte en basit kullanım senaryosu.

**C#**

{{< highlight csharp >}}

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
Aspose.Cells for .NET 8.5.2, DistinctCount alanını [PivotTable'ın DataField'ına uygulamak için](/cells/tr/net/consolidation-function/) kullanılabilen bir konsolidasyon işlevini açığa çıkardı.

{{% alert color="primary" %}} 

Farklı Sayıda konsolidasyon fonksiyonu yalnızca Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}} 
### **GridDesktop için Daha İyi Olay İşleme**
Aspose.Cells.GridDesktop'ın bu sürümü, 4 yeni olayı ortaya çıkardı. Bu olaylardan 2'si GridDesktop'ta elektronik tablo dosyalarının farklı durumlarında tetiklenir, diğer 2'si ise formüllerin hesaplanmasında tetiklenir.

Olaylar aşağıdaki gibi listelenmiştir.

1. GridDesktop.BeforeLoadFile
1. GridDesktop.FinishLoadFile
1. GridDesktop.BeforeCalculate
1. GridDesktop.FinishCalculate
{{< app/cells/assistant language="csharp" >}}
