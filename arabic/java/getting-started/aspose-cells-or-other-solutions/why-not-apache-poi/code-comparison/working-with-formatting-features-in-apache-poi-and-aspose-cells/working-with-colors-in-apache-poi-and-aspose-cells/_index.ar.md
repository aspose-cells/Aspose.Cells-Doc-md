---
title: العمل مع الألوان في Apache POI و Aspose.Cells
type: docs
weight: 20
url: /ar/java/working-with-colors-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - العمل مع الألوان**
Aspose.Cells توفر فئة تمثل ملف Excel من Microsoft تسمى [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook). الفئة Workbook تحتوي على مجموعة من الورقات تتيح الوصول إلى كل ورقة في ملف Excel. تُمثل الورقة بواسطة فئة [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). توفر فئة Worksheet مجموعة من الخلايا. يُمثل كل عنصر في مجموعة الخلايا كائنًا من فئة [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

تقدم Aspose.Cells الطريقة setStyle في فئة Cell التي تُستخدم لتحديد تنسيق الخلية. أيضًا، يمكن استخدام كائن Style من فئة Style لتكوين إعدادات الخطوط.

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
## **Apache POI SS - HSSF XSSF - العمل مع الألوان**
تتوفر فئة CellStyle لتحديد إعدادات الخلفية ونمط التعبئة.

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
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/colors)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [ألوان وأنماط الخلفية](http://docs.aspose.com:8082/docs/display/cellsjava/Colors+and+Background+Patterns).

{{% /alert %}}
