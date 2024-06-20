---
title: إدارة أوراق العمل في ملفات Microsoft Excel.
linktitle: أوراق العمل
type: docs
weight: 90
url: /ar/net/manage-worksheets/
description: إضافة ورقة عمل، إزالة ورقة عمل وورقة نشطة باستخدام Aspose.Cells.
---


{{% alert color="primary" %}}

يمكن للمطورين إنشاء وإدارة أوراق العمل بشكل سهل في ملفات مايكروسوفت إكسل برمجيًا باستخدام واجهة برمجة التطبيقات المرنة لـ Aspose.Cells. يصف هذا الموضوع الطرق لإضافة وإزالة أوراق العمل في ملفات مايكروسوفت إكسل.

{{% /alert %}}

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)، تمثل ملف إكسل. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) على مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) تتيح الوصول إلى كل ورقة عمل في ملف إكسل.

تمثل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل.

## **إضافة ورقات العمل إلى ملف Excel جديد**

لإنشاء ملف Excel جديد برمجياً:

1. إنشاء كائن من الفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. استدعاء الطريقة [**Add**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) من الفئة [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). يتم إضافة ورقة عمل فارغة تلقائياً إلى ملف إكسل. يمكن الإشارة إليها عن طريق تمرير فهرس الورقة الجديدة إلى مجموعة [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets).
1. الحصول على مرجع ورقة العمل.
1. القيام بالعمل على أوراق العمل.
1. حفظ ملف إكسل الجديد مع أوراق جديدة بتوجيه طريقة [**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index) لفئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **إضافة ورقات عمل إلى جدول التصميم**

عملية إضافة أوراق العمل إلى جدول إكسل للمصمم هي نفس عملية إضافة ورقة عمل جديدة، باستثناء أن ملف إكسل موجود بالفعل ويجب فتحه قبل إضافة الأوراق. يمكن فتح جدول إكسل للمصمم بواسطة فئة [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **الوصول إلى الأوراق العمل باستخدام اسم الورقة**

الوصول إلى أي ورقة عمل عن طريق تحديد اسمها أو فهرسها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **إزالة الأوراق العمل باستخدام اسم الورقة**

لإزالة أوراق العمل من ملف، ادع الطريقة [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) من فئة [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection). امرر اسم الورقة إلى الطريقة [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1) لإزالة ورقة عمل معينة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **إزالة الأوراق العمل باستخدام فهرس الورقة**

يعمل إزالة الأوراق باسم عندما يكون اسم ورقة العمل معروفًا. إذا لم تكن تعرف اسم ورقة العمل، استخدم الطراز الزائد للطريقة [**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat) الذي يأخذ فهرس ورقة العمل بدلاً من اسمها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **تنشيط الأوراق وجعل خلية نشطة في ورقة العمل**

أحيانًا، تحتاج ورقة عمل معينة إلى أن تكون نشطة ومعروضة عندما يفتح المستخدم ملف إكسل في إكسل. بالمثل، قد ترغب في تنشيط خلية معينة وتعيين شريطي التمرير لعرض الخلية النشطة.
تمتلك Aspose.Cells القدرة على القيام بكل هذه المهام.

ورقة العمل النشطة هي الورقة التي تعمل عليها: اسم الورقة النشطة على علامة التبويب يكون سميك افتراضيًا.

الخلية النشطة هي الخلية المحددة، الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. تكون خلية واحدة فقط نشطة في وقت واحد. يتم تمييز الخلية النشطة بحد ثقيل.

### **تفعيل الأوراق وجعل خلية نشطة**

توفر Aspose.Cells استدعاءات API محددة لتفعيل ورقة وخلية. على سبيل المثال، تعد خاصية [**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex) مفيدة لضبط الورقة النشطة في دفتر العمل.
بالمثل، تستخدم الخاصية [**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell) لضبط والحصول على خلية نشطة في ورقة العمل.

للتأكد من أن شريطي التمرير الأفقي أو العمودي في موضع فهرس الصف والعمود الذي تريد عرض البيانات المحددة فيه، استخدم الخصائص [**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) و [**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn).

تُظهر الشفرة المثالية التالية كيفية تفعيل ورقة عمل وجعل خلية نشطة فيها. في الناتج المولد، ستتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين لديها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **مواضيع متقدمة**
- [نسخ ونقل أوراق العمل](/cells/ar/net/copying-and-moving-worksheets/)
- [عدد الخلايا في ورقة العمل](/cells/ar/net/count-number-of-cells-in-the-worksheet/)
- [الكشف عن ورق العمل الفارغة](/cells/ar/net/detecting-empty-worksheets/)
- [العثور على ورقة العمل هل هي ورقة حوار](/cells/ar/net/find-if-the-worksheet-is-dialog-sheet/)
- [الحصول على معرف فريد لورقة العمل](/cells/ar/net/get-worksheet-unique-id/)
- [إنشاء أو تلاعب أو إزالة السيناريوهات من ورقات العمل](/cells/ar/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [إدارة فواصل الصفحات](/cells/ar/net/managing-page-breaks/)
- [ميزات إعداد الصفحة](/cells/ar/net/page-setup-features/)
- [طباعة عدة نسخ من ورقة العمل](/cells/ar/net/print-multiple-copies-of-a-worksheet/)
- [الاستفادة من خاصية Sheet.SheetId في الشكل المفتوحXML باستخدام Aspose.Cells](/cells/ar/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [عروض ورقة العمل](/cells/ar/net/worksheet-views/)

