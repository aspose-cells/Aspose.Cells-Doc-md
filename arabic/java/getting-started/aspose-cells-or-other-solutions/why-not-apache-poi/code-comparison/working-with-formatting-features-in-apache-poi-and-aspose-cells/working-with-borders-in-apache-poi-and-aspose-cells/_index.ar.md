---
title: العمل مع الحدود في أباتشي بوي وأسبوز.سيلس
type: docs
weight: 10
url: /ar/java/working-with-borders-in-apache-poi-and-aspose-cells/
---

## **أسبوز.سيلس - العمل مع الحدود**
توفر Aspose.Cells فئة، [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) التي تمثل ملف Microsoft Excel. تحتوي الفئة Workbook على مجموعة WorksheetCollection التي تسمح بالوصول لكل ورقة عمل في ملف Excel. تُمثل ورقة العمل بواسطة فئة [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). توفر فئة الورقة العمل Cellscollection. يمثل كل عنصر في مجموعة Cells كائنًا من الفئة [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell).

توفر Aspose.Cells الطريقة setStyle في الفئة [Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell) المستخدمة لتعيين نمط تنسيق الخلية. أيضا، يتم استخدام كائن Style من الفئة [Style](http://docs.aspose.com:8082/docs/display/cellsjava/Style) ويوفر خصائص لضبط إعدادات الخط.

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
## **أباتشي بوي إس إس - إتش إس إس إف - العمل مع الحدود**
توفر فئة CellStyle ميزات لتعيين إعدادات الحدود باستخدام أباتشي بوي إس إس - إتش إس إس إف.

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
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/formatting/borders)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [إضافة حدود للخلايا](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
