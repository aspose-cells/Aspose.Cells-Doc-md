---
title: Apache POI ve Aspose.Cells'de Yazı Tipleriyle Çalışma
type: docs
weight: 30
url: /tr/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - Yazı Tipleriyle Çalışma**
Aspose.Cells bir sınıf sağlar,[Çalışma kitabı](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)bu bir Microsoft Excel dosyasını temsil eder. Workbook sınıfı, bir Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası şununla temsil edilir:[Çalışma kağıdı](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)sınıf. Worksheet sınıfı bir Cells koleksiyonu sağlar. Cells koleksiyonundaki her öğe, bir nesneyi temsil eder.[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)sınıf.

**Java**

{{< highlight "java" >}}

 //Adding some value to cell

Cell cell = cells.get("A1");

cell.setValue("This is Aspose test of fonts!");

//Setting the font name to "Courier New"

Style style = cell.getStyle();

Font font = style.getFont();

font.setName("Courier New");

font.setSize(24);

font.setBold(true);

font.setUnderline(FontUnderlineType.SINGLE);

font.setColor(Color.getBlue());

font.setStrikeout(true);

//font.setSubscript(true);

cell.setStyle(style);

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Yazı Tipleriyle Çalışma**
Apache POI SS, çeşitli Font ayarlarını yapmak için Font sınıfını sağlar.

**Java**

{{< highlight "java" >}}

 // Create a new font and alter it.

Font font = wb.createFont();

font.setFontHeightInPoints((short)24);

font.setFontName("Courier New");

font.setItalic(true);

font.setStrikeout(true);

// Fonts are set into a style so create a new one to use.

CellStyle style = wb.createCellStyle();

style.setFont(font);

// Create a cell and put a value in it.

Cell cell = row.createCell(1);

cell.setCellValue("This is a test of fonts");

cell.setCellStyle(style);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/biçimlendirme/yazı tipleri)

{{% alert color="primary" %}} 

 Daha fazla ayrıntı için, ziyaret edin[Yazı Tipi Ayarlarıyla Başa Çıkma](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
