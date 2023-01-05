---
title: Apache POI ve Aspose.Cells'de Sınırlarla Çalışma
type: docs
weight: 10
url: /tr/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Sınırlarla Çalışmak**
Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)sınıf. Worksheet sınıfı bir Cellscollection sağlar. Cells koleksiyonundaki her öğe, bir nesneyi temsil eder.[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)sınıf.

Aspose.Cells, setStyle yöntemini sağlar.[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)hücrenin biçimlendirme stilini ayarlamak için kullanılan sınıf. Ayrıca, Stil nesnesi[stil](http://docs.aspose.com:8082/docs/display/cellsjava/Style)class kullanılır ve yazı tipi ayarlarını yapılandırmak için özellikler sağlar.

**Java**

{{< highlight "java" >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Sınırlarla Çalışmak**
CellStyle sınıfı, Apache POI SS - HSSF ve XSSF kullanarak kenarlık ayarlarını yapmak için özellikler sağlar.

**Java**

{{< highlight "java" >}}

 //Setting the line of the top border

style.setBorder(BorderType.TOP_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the bottom border

style.setBorder(BorderType.BOTTOM_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the left border

style.setBorder(BorderType.LEFT_BORDER,CellBorderType.THICK,Color.getBlack());

//Setting the line of the right border

style.setBorder(BorderType.RIGHT_BORDER,CellBorderType.THICK,Color.getBlack());

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/biçimlendirme/kenarlıklar)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Cells'e Kenarlık Ekleme](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
