---
title: إدارة أوراق العمل
type: docs
weight: 20
url: /ar/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

يمكن للمطورين إنشاء أوراق العمل وإدارتها بسهولة في ملفات Excel Microsoft برمجيًا باستخدام Aspose.Cells المرن API. يصف هذا الموضوع طرق إضافة أوراق العمل وإزالتها في ملفات Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells يوفر فئة[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) الذي يمثل ملف Excel. ال[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) يحتوي الفصل على أ[أوراق عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)المجموعة التي تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

يتم تمثيل ورقة العمل بواسطة[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) فصل. ال[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)يوفر الفصل مجموعة واسعة من الأساليب لإدارة أوراق العمل.
##  **إضافة أوراق العمل إلى ملف Excel جديد**
لإنشاء ملف Excel جديد برمجياً:

1.  إنشاء كائن من[ورقة عمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)فصل.
1.  اتصل ب[يضيف](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/add/) طريقة[مجموعة أوراق العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/) مجموعة. تتم إضافة ورقة عمل فارغة إلى ملف Excel تلقائيًا. ويمكن الرجوع إليه عن طريق تمرير فهرس الورقة لورقة العمل الجديدة إلى ملف[مجموعة أوراق العمل](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/)مجموعة.
1. الحصول على مرجع ورقة العمل.
1. تنفيذ العمل على أوراق العمل.
1. احفظ ملف Excel الجديد بأوراق عمل جديدة عن طريق الاتصال بـ[دفتر العمل](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) فصل[يحفظ](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile-new.cpp" >}}
##  **الوصول إلى أوراق العمل باستخدام فهرس الورقة**
يوضح نموذج التعليمات البرمجية التالي كيفية الوصول إلى أي ورقة عمل أو الحصول عليها عن طريق تحديد الفهرس الخاص بها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex-new.cpp" >}}
##  **إزالة أوراق العمل باستخدام فهرس الورقة**
 تعمل إزالة أوراق العمل حسب الاسم بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا كنت لا تعرف اسم ورقة العمل، فاستخدم إصدارًا محمّلاً بشكل زائد من ملف[إزالة في](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/removeat)الطريقة التي تأخذ فهرس ورقة العمل بدلاً من اسم الورقة الخاصة بها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex-new.cpp" >}}
