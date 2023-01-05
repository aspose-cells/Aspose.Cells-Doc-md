---
title: إدارة أوراق العمل
linktitle: أوراق عمل
type: docs
weight: 60
url: /ar/java/manage-worksheets/
---
{{% alert color="primary" %}}

يمكن للمطورين إنشاء أوراق العمل وإدارتها بسهولة في ملفات Excel الخاصة بهم برمجيًا باستخدام API المرن من Aspose.Cells. في هذا الموضوع ، سنناقش بعض الأساليب لإضافة أوراق العمل وإزالتها في ملفات Excel.

{{% /alert %}}

إدارة أوراق العمل باستخدام Aspose.Cells سهلة مثل ABC. في هذا القسم ، سنصف كيف يمكننا:

1. قم بإنشاء ملف Excel جديد من البداية وأضف ورقة عمل إليه
1. أضف أوراق العمل إلى جداول بيانات المصمم
1. الوصول إلى أوراق العمل باستخدام اسم الورقة
1. قم بإزالة ورقة عمل من ملف Excel باستخدام اسم الورقة الخاص بها
1. قم بإزالة ورقة عمل من ملف Excel باستخدام فهرس الورقة الخاص بها

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) يمثل ملف Excel.[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تحتوي على[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)يسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet) صف دراسي.[**ورقة عمل**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet)توفر class مجموعة كبيرة من الخصائص والأساليب لإدارة ورقة العمل. دعونا نرى كيف يمكننا الاستفادة من هذه المجموعة الأساسية من واجهات برمجة التطبيقات.

## **إضافة أوراق عمل إلى ملف Excel جديد**

 لإنشاء ملف Excel جديد برمجيًا ، سيحتاج المطورون إلى إنشاء كائن[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) فئة تمثل ملف Excel. ثم يمكن للمطورين الاتصال[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) طريقة ال[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . عندما نتصل[**يضيف**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#add() ) طريقة ، تتم إضافة ورقة عمل فارغة إلى ملف Excel تلقائيًا ، والتي يمكن الرجوع إليها عن طريق تمرير فهرس الورقة الخاص بورقة العمل المضافة حديثًا إلى[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) . بعد الحصول على مرجع ورقة العمل ، يمكن للمطورين العمل على أوراق العمل الخاصة بهم وفقًا لمتطلباتهم. بعد الانتهاء من العمل على أوراق العمل ، يمكن للمطورين حفظ ملف Excel الذي تم إنشاؤه حديثًا بأوراق عمل جديدة عن طريق استدعاء ملف[**حفظ**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions) ) طريقة ال[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)صف دراسي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoNewExcelFile-AddingWorksheetstoNewExcelFile.java" >}}

## **إضافة أوراق عمل إلى جدول بيانات المصمم**

تتشابه عملية إضافة أوراق العمل إلى جدول بيانات المصمم تمامًا مع الطريقة المذكورة أعلاه باستثناء أن ملف Excel قد تم إنشاؤه بالفعل ونحن بحاجة إلى فتح ملف Excel هذا أولاً قبل إضافة ورقة عمل إليه. يمكن فتح جدول بيانات المصمم عن طريق تمرير مسار الملف أو دفقه أثناء تهيئة ملف[**دفتر العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)صف دراسي.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AddingWorksheetstoDesignerSpreadsheet-AddingWorksheetstoDesignerSpreadsheet.java" >}}

## **الوصول إلى أوراق العمل باستخدام اسم الورقة**

يمكن للمطورين الوصول إلى أي ورقة عمل أو الحصول عليها عن طريق تحديد اسمها أو فهرسها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-AccessingWorksheetsusingSheetName-AccessingWorksheetsusingSheetName.java" >}}

## **إزالة أوراق العمل باستخدام اسم الورقة**

 في بعض الأحيان ، قد يحتاج المطورون إلى إزالة أوراق العمل من ملفات Excel الحالية ويمكن تنفيذ هذه المهمة عن طريق استدعاء ملف[**إزالة**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String) ) طريقة ال[**ورقة العمل**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) مجموعة. يمكننا تمرير اسم الورقة إلى[**إزالة**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(java.lang.String)) طريقة لإزالة ورقة عمل معينة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetName-RemovingWorksheetsusingSheetName.java" >}}

## **إزالة أوراق العمل باستخدام فهرس الورقة**

تعمل الطريقة المذكورة أعلاه لإزالة أوراق العمل بشكل جيد إذا كان المطورون يعرفون بالفعل أسماء أوراق العمل المراد حذفها. ولكن ، ماذا لو كنت لا تعرف اسم ورقة العمل التي تريد إزالتها من ملف Excel الخاص بك؟

 حسنًا ، في مثل هذه الظروف ، يمكن للمطورين استخدام إصدار محمّل من[**إزالة**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#removeAt(int)طريقة تأخذ فهرس ورقة العمل بدلاً من اسم الورقة الخاص بها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-RemovingWorksheetsusingSheetIndex-RemovingWorksheetsusingSheetIndex.java" >}}

## **موضوعات مسبقة**
- [تنشيط الأوراق وتفعيل Cell في ورقة العمل](/cells/ar/java/activating-sheets-and-activating-a-cell-in-worksheet/)
- [نسخ ونقل أوراق العمل داخل وبين المصنفات](/cells/ar/java/copy-and-move-worksheets-within-and-between-workbooks/)
- [نسخ أوراق العمل ونقلها](/cells/ar/java/copying-and-moving-worksheets/)
- [عد عدد الخلايا في ورقة العمل](/cells/ar/java/count-number-of-cells-in-the-worksheet/)
- [كشف أوراق العمل الفارغة](/cells/ar/java/detecting-empty-worksheets/)
- [اكتشف ما إذا كانت ورقة العمل هي ورقة حوار](/cells/ar/java/find-if-the-worksheet-is-dialog-sheet/)
- [احصل على معرف فريد لورقة العمل](/cells/ar/java/get-worksheet-unique-id/)
- [إدراج صورة الخلفية في Excel](/cells/ar/java/insert-background-image-to-excel/)
- [إنشاء أو معالجة أو إزالة السيناريوهات من أوراق العمل](/cells/ar/java/create-manipulate-or-remove-scenarios-from-worksheets/)
- [إدارة فواصل الصفحات](/cells/ar/java/managing-page-breaks/)
- [ميزات إعداد الصفحة](/cells/ar/java/page-setup-features/)
- [قم بتحديث المراجع في أوراق العمل الأخرى أثناء حذف الأعمدة والصفوف الفارغة في ورقة العمل](/cells/ar/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)
- [استخدم خاصية Sheet.SheetId الخاصة بـ OpenXml باستخدام Aspose.Cells](/cells/ar/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [العمل مع الخلفية في ملفات ODS](/cells/ar/java/working-with-background-in-ods-files/)
- [طرق عرض ورقة العمل](/cells/ar/java/worksheet-views/)
