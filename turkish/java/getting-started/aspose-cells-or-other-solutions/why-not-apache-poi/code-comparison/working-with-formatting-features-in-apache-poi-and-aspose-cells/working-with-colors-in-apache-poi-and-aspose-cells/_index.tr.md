---
title: Apache POI ve Aspose.Cells ile Renklerle Çalışma
type: docs
weight: 20
url: /tr/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - Renklerle Çalışma**
Aspose.Cells, Microsoft Excel dosyasını temsil eden [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) adlı bir sınıf sağlar. Workbook sınıfı, Excel dosyasındaki her çalışma sayfasına erişim sağlayan bir WorksheetCollection içerir. Bir çalışma sayfası, [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet) sınıfı tarafından temsil edilir. Worksheet sınıfı, bir Cells koleksiyonunu sağlar. Cells koleksiyonundaki her öğe, [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) sınıfının bir nesnesini temsil eder.

Aspose.Cells, Cell sınıfındaki setStyle metodunu sağlar, bu metot hücrenin biçimlendirmesini ayarlamak için kullanılır. Ayrıca, Style sınıfının Style nesnesi yazı tipi ayarlarını yapılandırmak için kullanılabilir.

**Java**

{{< highlight java >}}

 //Accessing cell from the worksheet

Cell cell = cells.get("B2");

Style style = cell.getStyle();

//Setting the foreground color to yellow

style.setBackgroundColor(Color.getYellow());

//Setting the background pattern to vertical stripe

style.setPattern(BackgroundType.VERTICAL_STRIPE);

//Saving the modified style to the "A1" cell.

cell.setStyle(style);

// === Setting Foreground ===

//Adding custom color to the palette at 55th index

Color color = Color.fromArgb(212,213,0);

workbook.changePalette(color,55);

//Accessing cell from the worksheet

cell = cells.get("B3");

//Adding some value to the cell

cell.setValue("Hello Aspose!");

//Setting the custom color to the font

style = cell.getStyle();

Font font = style.getFont();

font.setColor(color);

cell.setStyle(style);


{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - Renklerle Çalışma**
CellStyle sınıfı arka plan ve doldurma deseni ayarlamak için kullanılabilir.

**Java**

{{< highlight java >}}

 // Aqua background

CellStyle style = wb.createCellStyle();

style.setFillBackgroundColor(IndexedColors.AQUA.getIndex());

style.setFillPattern(CellStyle.BIG_SPOTS);

Cell cell = row.createCell((short) 1);

cell.setCellValue("X");

cell.setCellStyle(style);

// Orange "foreground", foreground being the fill foreground not the font color.

style = wb.createCellStyle();

style.setFillForegroundColor(IndexedColors.ORANGE.getIndex());

style.setFillPattern(CellStyle.SOLID_FOREGROUND);

cell = row.createCell((short) 2);

cell.setCellValue("X");

cell.setCellStyle(style);

{{< /highlight >}}
## **Çalışan Kodu İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Örnek Kod İndir**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

Daha fazla bilgi için [Renkler ve Arka Plan Desenleri](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns) ziyaret edin.

{{% /alert %}}
