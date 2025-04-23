---
title: إدارة الأوراق العمل
linktitle: أوراق العمل
type: docs
weight: 60
url: /ar/java/manage-worksheets/
---

{{% alert color="primary" %}}

يمكن للمطورين إنشاء وإدارة ورق العمل في ملفات Excel الخاصة بهم برمجياً باستخدام واجهة برمجة التطبيقات المرنة لـ Aspose.Cells. في هذا الموضوع، سنناقش بعض الطرق لإضافة وإزالة صفحات العمل في ملفات Excel.

{{% /alert %}}

إدارة صفحات العمل باستخدام Aspose.Cells هي سهلة كما ABC. في هذا القسم، سنصف كيف يمكننا:

1. إنشاء ملف Excel جديد من البداية وإضافة ورقة عمل إليه
1. إضافة صفحات عمل إلى جداول التصميم
1. الوصول إلى الصفحات باستخدام اسم الصفحة
1. إزالة ورقة عمل من ملف Excel باستخدام اسم الورقة
1. إزالة ورقة عمل من ملف Excel باستخدام فهرس الورقة

توفر Aspose.Cells فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. تحتوي فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) على [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet). توفر فئة [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة ورقة العمل. لنرى كيف يمكننا الاستفادة من مجموعة الواجهة البرمجية الأساسية هذه.

## **إضافة ورقات العمل إلى ملف Excel جديد**

لإنشاء ملف Excel جديد برمجياً ، سيحتاج المطورون إلى إنشاء كائن من فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) التي تمثل ملف Excel. ثم يمكن للمطورين استدعاء الأسلوب [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--) في [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). عند استدعاء الأسلوب [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add--)، يتم إضافة ورقة عمل فارغة إلى ملف Excel تلقائيًا ، والتي يمكن الإشارة إليها عن طريق تمرير فهرس ورقة العمل الجديدة إلى [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection). بعد الحصول على مرجع على ورقة العمل ، يمكن للمطورين العمل على ورقات العمل حسب متطلباتهم. بعد الانتهاء من العمل على الورقات الجدولية ، يمكن للمطورين حفظ ملف Excel الجديد الذي تم إنشاؤه مع الورقات الجديدة عن طريق استدعاء الأسلوب [**save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save-java.io.OutputStream-com.aspose.cells.SaveOptions-) في فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **إضافة ورقات عمل إلى جدول التصميم**

عملية إضافة ورقات العمل إلى جدول بيانات المصمم هي تمامًا نفس عملية الأعلى باستثناء أن ملف Excel موجود بالفعل ونحتاج إلى فتح ذلك الملف Excel أولاً قبل إضافة ورقة عمل إليه. يمكن فتح جدول بيانات المصمم من خلال تمرير مسار الملف أو التيار أثناء تهيئة فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **الوصول إلى الأوراق العمل باستخدام اسم الورقة**

يمكن للمطورين الوصول أو الحصول على أي ورقة عمل عن طريق تحديد اسمها أو فهرسها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **إزالة الأوراق العمل باستخدام اسم الورقة**

أحيانًا يمكن أن يحتاج المطورون إلى إزالة أوراق العمل من ملفات Excel الحالية ويمكن أداء هذه المهمة عن طريق استدعاء الأسلوب [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-) في [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) مجموعة. يمكننا تمرير اسم الورقة إلى الأسلوب [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-java.lang.String-) لإزالة ورقة عمل معينة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **إزالة الأوراق العمل باستخدام فهرس الورقة**

الطريقة المذكورة أعلاه لإزالة أوراق العمل تعمل بشكل جيد إذا كان المطورون يعرفون بالفعل أسماء الورقة للأوراق التي سيتم حذفها. ولكن، ماذا لو كنت لا تعرف اسم الورقة لورقة العمل التي تريد إزالتها من ملف Excel الخاص بك؟

حسنًا ، في مثل هذه الظروف ، يمكن للمطورين استخدام الإصدار المتحمل من الأسلوب [**removeAt**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt-int-) الذي يأخذ فهرس ورقة العمل بدلاً من اسم ورقة العمل.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **مواضيع متقدمة**
- [تفعيل الأوراق وتفعيل خلية في ورقة العمل](/cells/ar/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [نسخ ونقل أوراق العمل داخل مصنف وبين مصنفين](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [نسخ ونقل أوراق العمل](/cells/ar/java/copying-and-moving-worksheets/)
- [عدد الخلايا في ورقة العمل](/cells/ar/java/count-number-of-cells-in-the-worksheet/)
- [الكشف عن ورق العمل الفارغة](/cells/ar/java/detecting-empty-worksheets/)
- [العثور على ورقة العمل هل هي ورقة حوار](/cells/ar/java/find-if-the-worksheet-is-dialog-sheet/)
- [الحصول على معرف فريد لورقة العمل](/cells/ar/java/get-worksheet-unique-id/)
- [إدراج صورة خلفية في Excel](/cells/ar/java/insert-background-image-to-excel/)
- [إنشاء أو تلاعب أو إزالة السيناريوهات من ورقات العمل](/cells/ar/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [إدارة فواصل الصفحات](/cells/ar/java/managing-page-breaks/)
- [ميزات إعداد الصفحة](/cells/ar/java/page-setup-features/)
- [تحديث المراجع في ورقات العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [الاستفادة من خاصية Sheet.SheetId في الشكل المفتوحXML باستخدام Aspose.Cells](/cells/ar/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [العمل مع الخلفية في ملفات ODS](/cells/ar/java/working-with-background-in-ods-files/)
- [عروض ورقة العمل](/cells/ar/java/worksheet-views/)
{{< app/cells/assistant language="java" >}}
