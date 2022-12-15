---
title: تجميد الأجزاء في Apache POI و Aspose.Cells
type: docs
weight: 80
url: /ar/java/freeze-panes-in-apache-poi-and-aspose-cells/
---
## **Aspose.Cells - تجميد الأجزاء**
Aspose.Cells يوفر فصل دراسي ،[دفتر العمل](http://docs.aspose.com:8082/docs/display/cellsjava/Workbook)يمثل ملف Excel Microsoft. تحتوي فئة المصنف على مجموعة أوراق العمل التي تتيح الوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](http://docs.aspose.com:8082/docs/display/cellsjava/Worksheet)صف دراسي. توفر فئة ورقة العمل نطاقًا واسعًا من الخصائص والأساليب لإدارة أوراق العمل. لتكوين أجزاء التجميد ، قم باستدعاء أسلوب التجميد لفئة ورقة العمل. تأخذ طريقة FreezePanes المعلمات التالية:

- **صف**، فهرس صف الخلية الذي سيبدأ التجميد منه.
- **عمودي**، فهرس العمود الخاص بالخلية التي سيبدأ التجميد منها.
- **صفوف مجمدة**، عدد الصفوف المرئية في الجزء العلوي.
- **أعمدة مجمدة**، عدد الأعمدة المرئية في الجزء الأيمن

**Java**

{{< highlight "java" >}}

 worksheet1.freezePanes(0,2,0,2); // Freezing Columns

worksheet2.freezePanes(2,0,2,0); // Freezing Rows

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - تجميد الأجزاء**
sheet.createFreezePane متاح لتحقيق وظيفة FreezePane أثناء استخدام Apache POI SS - HSSF و XSSF

**Java**

{{< highlight "java" >}}

 // Freeze just one row

sheet1.createFreezePane( 0, 2, 0, 2 );

// Freeze just one column

sheet2.createFreezePane( 2, 0, 2, 0 );

// Freeze the columns and rows (forget about scrolling position of the lower right quadrant).

sheet3.createFreezePane( 2, 2 );

{{< /highlight >}}
## **تحميل كود الجري**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **تنزيل نموذج التعليمات البرمجية**
- [جيثب](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/ src / main / java / com / aspose / خلية / أمثلة / featurescomparison / cellrowscolumns / freezepanes)

{{% alert color="primary" %}} 

 لمزيد من التفاصيل ، قم بزيارة[أجزاء التجميد](http://docs.aspose.com:8082/docs/display/cellsjava/Freeze+Panes).

{{% /alert %}}
