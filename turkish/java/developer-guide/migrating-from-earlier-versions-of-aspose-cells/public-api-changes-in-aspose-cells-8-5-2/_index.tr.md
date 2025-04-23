---
title: Aspose.Cells 8.5.2 de Yapılan Genel API Değişiklikleri
type: docs
weight: 190
url: /tr/java/public-api-changes-in-aspose-cells-8-5-2/
---

{{% alert color="primary" %}} 

Bu belge, Aspose.Cells API'sının 8.5.1'den 8.5.2'ye sürümünde modül/uygulama geliştiricilerinin ilgisini çekebilecek değişiklikleri açıklar. Yeni ve güncellenmiş genel yöntemler, [eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-5-2/) yanı sıra Aspose.Cells'in arka plandaki davranışındaki herhangi bir değişikliğin açıklamasını içerir.

{{% /alert %}} 
## **Eklenen API'lar**
### **Çalışsayısını Grafiksel Ortama Dönüştürme**
Bu Aspose.Cells for Java API sürümü, Artık SheetRender.toImage yönteminin bir başka aşırısını ortaya çıkardı ve şimdi [Çalışsayıyı Görsel bağlamda oluşturmaya izin veren bir Graphics2D sınıfının örneğini kabul etmek için](/cells/tr/java/render-worksheet-to-graphic-context/) kullanılabilir. Yeni eklenen yöntemin imzaları aşağıdaki gibidir.

- SheetRender.toImage(int pageIndex, Graphics2D graphic)

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Create empty image and fill it with blue color

int width = 800;

int height = 800;

BufferedImage image = new BufferedImage(width, height, BufferedImage.TYPE_INT_ARGB);

Graphics2D g = image.createGraphics();

g.setColor(java.awt.Color.blue);

g.fillRect(0, 0, width, height);

//Set one page per sheet to true in image or print options

ImageOrPrintOptions opts = new ImageOrPrintOptions();

opts.setOnePagePerSheet(true);

//Render worksheet to graphics context

SheetRender sr = new SheetRender(worksheet, opts);

sr.toImage(0, g);

//Save the graphics context image in Png format

File outputfile = new File("test.png");

ImageIO.write(image, "png", outputfile);

{{< /highlight >}}
### **Eklenen PivotTable.getCellByDisplayName Yöntemi**
Aspose.Cells for Java 8.5.2, PivotTable.getCellByDisplayName yöntemini açığa çıkardı ve bu, [PivotField'ın adına göre Hücre nesnesini almak için](/cells/tr/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/) kullanılabilir. Bu yöntem, PivotField başlığını vurgulamak veya biçimlendirmek istediğiniz senaryolarda faydalı olabilir.

Basit kullanım senaryosu aşağıda gösterilmektedir.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first pivot table inside the worksheet

PivotTable pivotTable = worksheet.getPivotTables().get(0);

//Access cell by display name of 2nd data field of the pivot table

String displayName = pivotTable.getDataFields().get(1).getDisplayName();

Cell cell = pivotTable.getCellByDisplayName(displayName);

//Access cell style and set its fill color and font color

Style style = cell.getStyle();

style.setForegroundColor(Color.getLightBlue());

style.getFont().setColor(Color.getBlack());

//Set the style of the cell

pivotTable.format(cell.getRow(), cell.getColumn(), style);

//Save workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Eklenen SaveOptions.MergeAreas Özelliği**
Aspose.Cells for Java 8.5.2, SaveOptions.MergeAreas özelliğini açığa çıkardı ve Boolean türünde değer alabilen bir özelliktir. Varsayılan değer false olmasına rağmen, true olarak ayarlanırsa, Aspose.Cells for Java API dosyayı kaydetmeden önce hücre alanlarını birleştirmeye çalışır.

{{% alert color="primary" %}} 

Bir elektronik tabloda uygulanan çok sayıda tekil hücre varsa, sonucun bozulma olasılıkları vardır. Tekil doğrulama kurallarına sahip hücreleri birleştirmenin bir olası çözümü veya Aspose.Cells for Java API'nın kaydetme işleminden önce hücre Alanlarını otomatik olarak birleştirmek için artık SaveOptions.MergeAreas özelliğini kullanabilirsiniz.

{{% /alert %}} 
### **Eklenen Geometry.ShapeAdjustValues Özelliği**
V8.5.2'nin piyasaya sürülmesiyle Aspose.Cells API, farklı şekillerin ayar noktalarına [erişmek ve değişiklik yapmak için kullanılabilecek Geometry.getShapeAdjustValues yöntemini açığa çıkardı](/cells/tr/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Microsoft Excel arayüzünde, ayar noktaları sarı elmas düğümleri olarak görüntülenir.

{{% /alert %}} 

Örneğin, 

1. Yuvarlatılmış Dikdörtgenin yay'ı değiştirmek için bir ayarı vardır
1. Üçgen'in noktasının konumunu değiştirmek için bir ayarı vardır
1. Yaygın olmayan yukarıda bir ayarı değiştirmek için bir ayarı vardır
1. Okların kuyruk ve başının şeklini değiştirmek için iki ayarı vardır

İşte en basit kullanım senaryosu.

**Java**

{{< highlight csharp >}}

 //Create workbook object from source excel file

Workbook workbook = new Workbook("source.xlsx");

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access first three shapes of the worksheet

Shape shape1 = worksheet.getShapes().get(0);

Shape shape2 = worksheet.getShapes().get(1);

Shape shape3 = worksheet.getShapes().get(2);

//Change the adjustment values of the shapes

shape1.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

shape2.getGeometry().getShapeAdjustValues().get(0).setValue(0.8d);

shape3.getGeometry().getShapeAdjustValues().get(0).setValue(0.5d);

//Save the workbook

workbook.save("output.xlsx");

{{< /highlight >}}
### **Numaralı Alan Konsolidasyon Fonksiyonu.DISTINCT_COUNT Eklendi**
Aspose.Cells for Java 8.5.2, ConsolidationFunction.DISTINCT_COUNT alanını DataField'ın üzerine Uygulanan Farklı Sayıda birleşik fonksiyonu için kullanılabilir hale getirdi.

{{% alert color="primary" %}} 

Farklı Sayıda konsolidasyon fonksiyonu yalnızca Microsoft Excel 2013 tarafından desteklenmektedir.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
