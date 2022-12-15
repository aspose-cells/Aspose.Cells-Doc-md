---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/java/managing-page-breaks/
---
{{% alert color="primary" %}}

فاصل الصفحة هو مكان في النص تنتهي فيه صفحة وتبدأ الصفحة التالية. Microsoft يمكن لبرنامج Excel إضافة فواصل صفحات في أي خلية محددة بورقة عمل.
تنتهي الصفحة في الخلية حيث تتم إضافة فاصل الصفحة ويتم طباعة جميع البيانات بعد فاصل الصفحة على الصفحة التالية. بكلمات بسيطة ، تقسم فواصل الصفحات أوراق العمل إلى صفحات متعددة. من الممكن أيضًا إضافة فواصل صفحات إلى أوراق العمل في وقت التشغيل باستخدام Aspose.Cells. يدعم Aspose.Cells نوعين من فواصل الصفحات:

- عرضي
- عمودي.

توضح هذه المقالة كيفية إضافة فواصل الصفحات الأفقية أو العمودية إلى أوراق العمل باستخدام Aspose.Cells.

{{% /alert %}}

## **Aspose.Cells وفواصل الصفحات**

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) فئة توفر مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل. لإضافة فواصل الصفحات ، استخدم ملف[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي'[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) و[**عمودي PageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)الخصائص.

 ال[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#HorizontalPageBreaks) و[**عمودي PageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#VerticalPageBreaks)الخصائص هي في الواقع مجموعات حقيقة قد تحتوي على عدة فواصل صفحات. تحتوي كل مجموعة على عدة طرق لإدارة فواصل الصفحات الأفقية والعمودية. يتم مناقشة كيفية استخدام هذه الأساليب أدناه.

## **مضيفا فواصل الصفحات**

 لإضافة فاصل صفحات في ورقة عمل ، قم بإدراج فواصل صفحات عمودية وأفقية في الخلية المحددة عن طريق استدعاء ملف[**HorizontalPageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) و[**عمودي PageBreaks**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) المجموعات**يضيف** طُرق. كل**يضيف**يأخذ الأسلوب اسم الخلية حيث سيتم إضافة فاصل الصفحة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingPageBreaks-AddingPageBreaks.java" >}}

{{% alert color="primary" %}}

في أوضاع معاينة فاصل الصفحة أو معاينة الطباعة ، يمكنك مشاهدة كيفية عمل فواصل الصفحات هذه.

{{% /alert %}}

## **مسح كافة فواصل الصفحات**

 لمسح كل فواصل الصفحات في ورقة عمل ، قم باستدعاء[**أفقي صفحة بريككولكشن**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) و[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) المجموعات**صافي**طُرق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-ClearAllPageBreaks-ClearAllPageBreaks.java" >}}

## **إزالة فاصل صفحة معين**

 لإزالة فاصل صفحات معين في ورقة العمل ، قم باستدعاء[**أفقي صفحة بريككولكشن**](https://reference.aspose.com/cells/java/com.aspose.cells/HorizontalPageBreakCollection) و[**VerticalPageBreakCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/VerticalPageBreakCollection) المجموعات**إزالة** طُرق. كل**إزالة**ستأخذ الطريقة فهرس فاصل الصفحة المراد إزالته.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemoveSpecificPageBreak-RemoveSpecificPageBreak.java" >}}

{{% alert color="primary" %}}

**من المهم أن تعرف** : عند تعيين خصائص الملاءمة للصفحة (أي[**FitToPagesTall**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesTall) و[**FitToPagesWide**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup#FitToPagesWide)) في إعدادات إعداد الصفحة ، تتأثر إعدادات فاصل الصفحة ، لذلك إذا قمت بطباعة ورقة العمل ، فلن يتم أخذ إعدادات فاصل الصفحة في الاعتبار على الرغم من أنها لا تزال موجودة في الملف.

{{% /alert %}}
