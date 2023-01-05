---
title: Genel API Aspose.Cells 8.5.2'deki değişiklikler
type: docs
weight: 190
url: /tr/java/public-api-changes-in-aspose-cells-8-5-2/
---
{{% alert color="primary" %}} 

 Bu belge, Aspose.Cells API sürümünde 8.5.1'den 8.5.2'ye modül/uygulama geliştiricilerin ilgisini çekebilecek değişiklikleri açıklamaktadır. Yalnızca yeni ve güncellenmiş genel yöntemleri içermez,[eklenen sınıflar vb.](/cells/tr/java/public-api-changes-in-aspose-cells-8-5-2/), aynı zamanda Aspose.Cells'deki perde arkasındaki davranış değişikliklerinin açıklaması.

{{% /alert %}} 
## **Eklenen API'ler**
### **Çalışma Sayfasını Grafik Bağlamına Dönüştür**
Aspose.Cells for Java API'in bu sürümü, artık Graphics2D sınıfının bir örneğini kabul etmeye izin veren SheetRender.toImage yönteminin başka bir aşırı yüklemesini açığa çıkardı.[Çalışma Sayfasını Grafik bağlamında işleyin](/cells/tr/java/render-worksheet-to-graphic-context/). Yeni eklenen yöntemin imzaları aşağıdaki gibidir.

- SheetRender.toImage(int pageIndex, Graphics2D grafiği)

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
### **Yöntem PivotTable.getCellByDisplayName Eklendi**
 Aspose.Cells for Java 8.5.2, PivotTable.getCellByDisplayName yöntemini kullanıma sundu.[PivotField adına göre Cell nesnesini alın](/cells/tr/java/get-the-cell-object-by-displayname-of-pivotfield-of-pivottable/). Bu yöntem, PivotField başlığını vurgulamak veya biçimlendirmek istediğiniz senaryolarda yararlı olabilir.

Basit kullanım senaryosu aşağıdadır.

**Java**

{{< highlight "csharp" >}}

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
### **Özellik SaveOptions.MergeAreas Eklendi**
Aspose.Cells for Java 8.5.2, Boole türü değeri kabul edebilen SaveOptions.MergeAreas özelliğini kullanıma sundu. Varsayılan değer false'tur, ancak true olarak ayarlanırsa Aspose.Cells for Java API, dosyayı kaydetmeden önce ayrı CellArea'yı birleştirmeye çalışır.

{{% alert color="primary" %}} 

Bir e-tabloda doğrulama uygulanmış çok fazla bireysel hücre varsa, ortaya çıkan e-tablonun bozulma olasılığı vardır. Muhtemel bir çözüm, hücreleri aynı doğrulama kurallarına sahip birleştirmek veya artık API'i kaydetme işleminden önce CellAreas'ı otomatik olarak birleştirmeye yönlendirmek için SaveOptions.MergeAreas özelliğini kullanabilirsiniz.

{{% /alert %}} 
### **Özellik Geometry.ShapeAdjustValues Eklendi**
 v8.5.2 sürümüyle birlikte Aspose.Cells API, şu amaçlarla kullanılabilecek Geometry.getShapeAdjustValues yöntemini kullanıma sundu.[farklı şekillerin ayar noktalarına erişin ve bu noktalarda değişiklik yapın](/cells/tr/java/change-adjustment-values-of-the-shape/).

{{% alert color="primary" %}} 

Microsoft Excel arayüzünde, ayar noktaları sarı elmas düğümler olarak görüntülenir.

{{% /alert %}} 

 Örneğin,

1. Yuvarlatılmış Dikdörtgenin yayı değiştirmek için bir ayarı vardır
1. Üçgenin noktanın konumunu değiştirmek için bir ayarı vardır
1. Yamuk, üst kısmın genişliğini değiştirmek için bir ayara sahiptir
1. Baş ve kuyruğun şeklini değiştirmek için okların iki ayarı vardır

İşte en basit kullanım senaryosu.

**Java**

{{< highlight "csharp" >}}

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
### **Numaralandırma Alanı KonsolidasyonFunction.DISTINCT_COUNT Eklendi**
Aspose.Cells for Java 8.5.2, bir PivotTable'ın DataField'inde Distinct Count birleştirilmiş işlevini uygulamak için kullanılabilecek ConsolidationFunction.DISTINCT_COUNT alanını kullanıma sundu.

{{% alert color="primary" %}} 

Farklı Sayı birleştirme işlevi yalnızca Microsoft Excel 2013 tarafından desteklenir.

{{% /alert %}}
