---
title: Apache POI ve Aspose.Cells ile Kenarlıklarla Çalışma
type: docs
weight: 10
url: /tr/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Kenarlıklarla Çalışma**
Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) adlı bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) sınıfı tarafından temsil edilir. Worksheet sınıfı, bir Cells koleksiyonunu sağlar. Cells koleksiyonundaki her öğe, [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) sınıfındaki setStyle yöntemini bir hücrenin biçimlendirme stili olarak ayarlamak için kullanır. Ayrıca, [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) sınıfının Style nesnesi kullanılır ve yazı tipi ayarlarını yapılandırmak için özellikler sağlar.

**Java**

{{< highlight java >}}

 // Style the cell with borders all around.

Style style = workbook.createStyle();

style.setBorder(BorderType.BOTTOM_BORDER, CellBorderType.THIN, Color.getBlack());

style.setBorder(BorderType.LEFT_BORDER, CellBorderType.THIN, Color.getGreen());

style.setBorder(BorderType.RIGHT_BORDER, CellBorderType.THIN, Color.getBlue());

style.setBorder(BorderType.TOP_BORDER, CellBorderType.MEDIUM_DASH_DOT, Color.getBlack());

// Setting style to the cell

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Kenarlıklarla Çalışma**
CellStyle sınıfı, Apache POI SS - HSSF ve XSSF kullanılarak kenarlık ayarlarını belirleme özellikleri sağlar.

**Java**

{{< highlight java >}}

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
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

Daha fazla ayrıntı için [Hücrelere Kenarlık Ekleme](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells) sayfasını ziyaret edin.

{{% /alert %}}
