---
title: العمل مع الحدود في Apache POI و Aspose.Cells
type: docs
weight: 10
url: /ar/java/working-with-borders-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - العمل مع الحدود**
Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel. يتم تمثيل ورقة العمل بواسطة[ورقة عمل](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)صف دراسي. توفر فئة ورقة العمل مجموعة الخلايا. يمثل كل عنصر في مجموعة Cells عنصرًا من عناصر[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)صف دراسي.

يوفر Aspose.Cells طريقة setStyle في ملف[Cell](http://docs.aspose.com:8082/docs/display/cellsjava/Cell)فئة تستخدم لتعيين نمط تنسيق الخلية. أيضًا ، فإن كائن Style لـ[أسلوب](http://docs.aspose.com:8082/docs/display/cellsjava/Style)يتم استخدام class وتوفر خصائص لتكوين إعدادات الخط.

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
## **Apache POI SS - HSSF XSSF - العمل مع الحدود**
توفر فئة CellStyle ميزات لضبط إعدادات الحدود باستخدام Apache POI SS - HSSF و XSSF.

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
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / cells / أمثلة / featurescomparison / formatting / border)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[إضافة الحدود إلى Cells](http://docs.aspose.com:8082/docs/display/cellsjava/Adding+Borders+to+Cells).

{{% /alert %}}
