---
title: إدارة أوراق عمل Microsoft ملفات Excel.
linktitle: أوراق عمل
type: docs
weight: 90
url: /ar/net/manage-worksheets/
description: إضافة ورقة عمل وإزالة ورقة العمل والورقة النشطة باستخدام Aspose.Cells.
---
{{% alert color="primary" %}}

يمكن للمطورين إنشاء أوراق عمل وإدارتها بسهولة في ملفات Excel Microsoft برمجيًا باستخدام API Aspose.Cells 'مرنًا. يصف هذا الموضوع طرق إضافة أوراق العمل وإزالتها في ملفات Excel Microsoft.

{{% /alert %}}

 Aspose.Cells يوفر فصل دراسي ،[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) يمثل ملف Excel. ال[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)فئة تحتوي على[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)صف دراسي. ال[**ورقة عمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)توفر class مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل.

## **إضافة أوراق عمل إلى ملف Excel جديد**

لإنشاء ملف Excel جديد برمجيًا:

1.  قم بإنشاء كائن من[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)صف دراسي.
1.  اتصل ب[**يضيف**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/add) طريقة[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) صف دراسي. تتم إضافة ورقة عمل فارغة إلى ملف Excel تلقائيًا. يمكن الرجوع إليه عن طريق تمرير فهرس ورقة ورقة العمل الجديدة إلى ملف[**أوراق عمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) مجموعة.
1. الحصول على مرجع ورقة العمل.
1. أداء العمل على أوراق العمل.
1.  احفظ ملف Excel الجديد بأوراق عمل جديدة عن طريق استدعاء ملف[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي'[**يحفظ**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)طريقة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToNewExcelFile-1.cs" >}}

## **إضافة أوراق عمل إلى جدول بيانات المصمم**

 عملية إضافة أوراق العمل إلى جدول بيانات المصمم مماثلة لعملية إضافة ورقة عمل جديدة ، باستثناء أن ملف Excel موجود بالفعل ، لذا يجب فتحه قبل إضافة أوراق العمل. يمكن فتح جدول بيانات المصمم بواسطة[**دفتر العمل**](https://reference.aspose.com/cells/net/aspose.cells/workbook)صف دراسي.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.cs" >}}

## **الوصول إلى أوراق العمل باستخدام اسم الورقة**

قم بالوصول إلى أي ورقة عمل بتحديد اسمها أو فهرسها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-AccessingWorksheetsusingSheetName-1.cs" >}}

## **إزالة أوراق العمل باستخدام اسم الورقة**

لإزالة أوراق العمل من أحد الملفات ، اتصل بامتداد[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat/index) طريقة[**ورقة العمل**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) صف دراسي. قم بتمرير اسم الورقة إلى[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells.worksheetcollection/removeat/methods/1)طريقة لإزالة ورقة عمل محددة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetName-1.cs" >}}

## **إزالة أوراق العمل باستخدام فهرس الورقة**

 تعمل إزالة أوراق العمل حسب الاسم بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا كنت لا تعرف اسم ورقة العمل ، فاستخدم إصدارًا محملاً بشكل زائد من ملف[**RemoveAt**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/methods/removeat)الطريقة التي تأخذ فهرس ورقة العمل بدلاً من اسم الورقة الخاص بها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.cs" >}}

## **تنشيط الأوراق وتفعيل Cell في ورقة العمل**

في بعض الأحيان ، تحتاج إلى ورقة عمل محددة لتكون نشطة ويتم عرضها عندما يفتح المستخدم ملف Excel Microsoft في Excel. وبالمثل ، قد ترغب في تنشيط خلية معينة وتعيين أشرطة التمرير لإظهار الخلية النشطة.
Aspose.Cells قادر على القيام بكل هذه المهام.

 ان**الورقة النشطة** هي ورقة تعمل عليها: اسم الورقة النشطة في علامة التبويب غامق افتراضيًا.

 ان**خلية نشطة** هي خلية محددة ، الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. فقط خلية واحدة نشطة في كل مرة. يتم تمييز الخلية النشطة بحد ثقيل.

### **تنشيط الأوراق وتنشيط Cell**

يوفر Aspose.Cells استدعاءات API محددة لتنشيط جدول وخانة. على سبيل المثال ، ملف[**Aspose.Cells.WorksheetCollection.ActiveSheetIndex**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/activesheetindex)الخاصية مفيدة لتعيين الورقة النشطة في مصنف.
بصورة مماثلة،[**Aspose.Cells.Worksheet.ActiveCell**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/activecell)تُستخدم الخاصية لتعيين خلية نشطة والحصول عليها في ورقة العمل.

للتأكد من أن أشرطة التمرير الأفقية أو الرأسية موجودة في موضع فهرس الصفوف والأعمدة الذي تريده لإظهار بيانات محددة ، استخدم[**Aspose.Cells.Worksheet.FirstVisibleRow**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblerow) و[**Aspose.Cells.Worksheet.FirstVisibleColumn**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/firstvisiblecolumn)الخصائص.

يوضح المثال التالي كيفية تنشيط ورقة عمل وإنشاء خلية نشطة فيها. في الإخراج الذي تم إنشاؤه ، سيتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني كأول صف وعمود مرئيين.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-MakeCellActive-1.cs" >}}

## **موضوعات مسبقة**
- [نسخ أوراق العمل ونقلها](/cells/ar/net/copying-and-moving-worksheets/)
- [عد عدد الخلايا في ورقة العمل](/cells/ar/net/count-number-of-cells-in-the-worksheet/)
- [كشف أوراق العمل الفارغة](/cells/ar/net/detecting-empty-worksheets/)
- [اكتشف ما إذا كانت ورقة العمل هي ورقة حوار](/cells/ar/net/find-if-the-worksheet-is-dialog-sheet/)
- [احصل على معرف فريد لورقة العمل](/cells/ar/net/get-worksheet-unique-id/)
- [إنشاء أو معالجة أو إزالة السيناريوهات من أوراق العمل](/cells/ar/net/create-manipulate-or-remove-scenarios-from-worksheets/)
- [إدارة فواصل الصفحات](/cells/ar/net/managing-page-breaks/)
- [ميزات إعداد الصفحة](/cells/ar/net/page-setup-features/)
- [اطبع عدة نسخ من ورقة العمل](/cells/ar/net/print-multiple-copies-of-a-worksheet/)
- [استخدم خاصية Sheet.SheetId الخاصة بـ OpenXml باستخدام Aspose.Cells](/cells/ar/net/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [طرق عرض ورقة العمل](/cells/ar/net/worksheet-views/)

