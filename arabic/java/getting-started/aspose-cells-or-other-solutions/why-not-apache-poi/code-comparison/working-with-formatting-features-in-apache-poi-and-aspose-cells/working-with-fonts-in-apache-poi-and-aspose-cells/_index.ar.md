---
title: العمل مع الخطوط في Apache POI و Aspose.Cells
type: docs
weight: 30
url: /ar/java/working-with-fonts-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - التعامل مع الخطوط**
Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)صف دراسي. توفر فئة ورقة العمل مجموعة Cells. يمثل كل عنصر في مجموعة Cells عنصرًا من عناصر[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)صف دراسي.

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
## **Apache POI SS - HSSF XSSF - العمل مع الخطوط**
يوفر Apache POI SS فئة الخط لضبط إعدادات الخط المتنوعة.

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
## **قم بتنزيل كود التشغيل**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)src / main / java / com / aspose / cells / أمثلة / featurescomparison / formatting / Fonts)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[التعامل مع إعدادات الخط](http://docs.aspose.com:8082/docs/display/cellsjava/Dealing+with+Font+Settings).

{{% /alert %}}
