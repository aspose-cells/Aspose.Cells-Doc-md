---
title: إدارة الأوراق العمل
type: docs
weight: 20
url: /ar/cpp/manage-worksheets/
---

{{% alert color="primary" %}} 

يمكن للمطورين إنشاء وإدارة صفحات العمل بشكل سهل في ملفات Microsoft Excel برمجياً باستخدام واجهة برمجة التطبيقات المرنة Aspose.Cells. يصف هذا الموضوع النهج لإضافة وإزالة صفحات العمل في ملفات Microsoft Excel.

{{% /alert %}} 

يوفر Aspose.Cells صنف [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel. يحتوي صنف [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) على مجموعة [Worksheets](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) تسمح بالوصول إلى كل صفحة عمل في ملف Excel.

تمثل صفحة العمل بواسطة صنف [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/). يوفر صنف [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) مجموعة واسعة من الطرق لإدارة صفحات العمل.
## **إضافة ورقات العمل إلى ملف Excel جديد**
لإنشاء ملف Excel جديد برمجياً:

1. إنشاء كائن من فئة [Worksheet](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) .
1. استدعاء الأسلوب [Add](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) لمجموعة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) . يتم إضافة ورقة عمل فارغة إلى ملف Excel تلقائيًا. يمكن الإشارة إليها عن طريق تمرير فهرس الورقة الجديدة إلى مجموعة [WorksheetCollection](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) .
1. الحصول على مرجع ورقة العمل.
1. القيام بالعمل على أوراق العمل.
1. حفظ ملف Excel الجديد مع أوراق عمل جديدة عن طريق استدعاء فئة [Workbook](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الأسلوب [Save](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/) .



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
## **الوصول إلى الأوراق العمل باستخدام فهرس الورقة**
يوضح الكود المصدري التالي كيفية الوصول أو الحصول على أي ورقة عمل عن طريق تحديد فهرستها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
## **إزالة الأوراق العمل باستخدام فهرس الورقة**
يعمل إزالة الأوراق العمل بواسطة الاسم بشكل جيد عند معرفة اسم ورقة العمل. إذا لم تكن تعرف اسم الورقة العمل، استخدم الإصدار المكدس من الأسلوب [RemoveAt](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat) الذي يأخذ فهرس ورقة العمل بدلاً من اسمها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
