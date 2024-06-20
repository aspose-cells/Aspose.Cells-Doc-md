---
title: تجميد الخانات في أباتشي بوي وأسبوز.سيلز
type: docs
weight: 80
url: /ar/java/freeze-panes-in-apache-poi-and-aspose-cells/
---

## **Aspose.Cells - تجميد الألواح**
توفر Aspose.Cells فئة [Workbook](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook) التي تمثل ملف Microsoft Excel. تحتوي فئة Workbook على مجموعة WorksheetCollection التي تسمح بالوصول إلى كل ورق عمل في ملف Excel.

ورقة عمل ممثلة بفئة [Worksheet](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet). توفر فئة Worksheet مجموعة واسعة من الخصائص والأساليب لإدارة الأوراق العمل. لتكوين التجميد، استدعي FreezePanesmethod من فئة Worksheet. تأخذ FreezePanes طريقة المعلمات التالية:

- **الصف**، فهرس الصف للخلية التي سيبدأ منها التجميد.
- **العمود**، فهرس العمود للخلية التي سيبدأ منها التجميد.
- **الصفوف المجمدة**، عدد الصفوف المرئية في اللوحة العلوية.
- **الأعمدة المجمدة**، عدد الأعمدة المرئية في اللوحة اليسرى.

**Java**

{{< highlight java >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - تجميد اللوحات**
sheet.createFreezePane متاحة لتحقيق وظيفة FreezePane أثناء استخدام Apache POI SS - HSSF و XSSF.

**Java**

{{< highlight java >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **تحميل رمز التشغيل**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تحميل رمز عينة**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/freezepanes)

{{% alert color="primary" %}} 

لمزيد من التفاصيل، قم بزيارة [تجميد اللوحات](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
