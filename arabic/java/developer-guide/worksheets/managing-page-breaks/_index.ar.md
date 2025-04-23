---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/java/managing-page-breaks/
---

{{% alert color="primary" %}}

كسر الصفحة هو المكان في النص حيث تنتهي صفحة وتبدأ الصفحة التالية. يمكن لبرنامج Microsoft Excel إضافة كسر الصفحة في أي خلية محددة في ورقة العمل.
تنتهي الصفحة في الخلية التي يتم إضافة كسر الصفحة إليها ويتم طباعة جميع البيانات بعد كسر الصفحة على الصفحة التالية. ببساطة، يقوم كسر الصفحة بتقسيم ورقات العمل إلى عدة صفحات. كما هو ممكن أيضًا إضافة كسر الصفحة إلى ورقات العمل أثناء التشغيل باستخدام Aspose.Cells. Aspose.Cells تدعم نوعين من كسر الصفحة:

- أفقي
- رأسي.

يصف هذا المقال كيفية إضافة كسر صفحة أفقي أو رأسي إلى ورقات العمل باستخدام Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells وكسر الصفحات**

توفر Aspose.Cells فئةً، [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) الذي يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

تمثل ورقة العمل بواسطة الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) والتي توفر مجموعة واسعة من الخصائص والأساليب لإدارة ورقات العمل. لإضافة كسر الصفحات، استخدم الفئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) وخصائص [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) و [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks).

تحتوي الخصائص [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) و [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks) في الواقع على مجموعات قد تحتوي على عدة كسر صفحة. تحتوي كل مجموعة على عدة طرق لإدارة كسر الصفحات الأفقي والرأسي. يتم مناقشة كيفية استخدام هذه الطرق أدناه.

## **إضافة فواصل الصفحات**

لإضافة كسر صفحة في ورقة عمل، أدخل كسر صفحة أفقي ورأسي في الخلية المحددة عن طريق استدعاء **Add** لـ [**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) و [**VerticalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). يأخذ كل طريقة **Add** اسم الخلية التي يجب إضافة كسر الصفحة إليها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

في وضع معاينة كسر الصفحة أو معاينة الطباعة، يمكنك رؤية كيف تعمل هذه الكسور.

{{% /alert %}}

## **مسح كافة فواصل الصفحات**

لمسح جميع كسر الصفحات في ورقة عمل، استدعي **Clear** لـ [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) و [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **إزالة كسر صفحة محدد**

لإزالة كسر صفحة محدد في الورقة، استدعي **removeAt** لـ [**HorizontalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) و [**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection). يأخذ كل طريقة **removeAt** فهرس كسر الصفحة المراد إزالته.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**ملاحظة مهمة**: عند ضبط خصائص ملائمة الصفحة (وهي [**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) و [**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide-) في إعدادات إعداد الصفحة)، تتأثر إعدادات كسر الصفحة، لذلك، إذا قمت بطباعة ورقة العمل، فإن إعدادات كسر الصفحة لا تؤخذ بعين الاعتبار على الرغم من وجودها في الملف.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
