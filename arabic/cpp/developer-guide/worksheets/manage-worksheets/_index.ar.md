---
title: إدارة أوراق العمل
type: docs
weight: 20
url: /ar/cpp/manage-worksheets/
---
{{% alert color="primary" %}} 

يمكن للمطورين إنشاء أوراق العمل وإدارتها بسهولة في ملفات Excel Microsoft برمجيًا باستخدام Aspose.Cells مرن API. يصف هذا الموضوع طرق إضافة أوراق العمل وإزالتها في ملفات Excel Microsoft.

{{% /alert %}} 

 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) يمثل ملف Excel. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)يوفر class مجموعة واسعة من الأساليب لإدارة أوراق العمل.
## **إضافة أوراق عمل إلى ملف Excel جديد**
لإنشاء ملف Excel جديد برمجيًا:

1.  قم بإنشاء كائن من[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)صف دراسي.
1.  اتصل ب[يضيف](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#aa2bb166f57a4d8eba8e25ce1f99d0c55) طريقة[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection) مجموعة. تتم إضافة ورقة عمل فارغة إلى ملف Excel تلقائيًا. يمكن الرجوع إليه عن طريق تمرير فهرس ورقة ورقة العمل الجديدة إلى ملف[IWorksheetCollection](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة.
1. الحصول على مرجع ورقة العمل.
1. أداء العمل على أوراق العمل.
1.  احفظ ملف Excel الجديد بأوراق عمل جديدة عن طريق استدعاء ملف[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) صف دراسي[يحفظ](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook#a77072cfb929787df9ad1f38b02f58349)طريقة.



{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AddingWorksheetsToNewExcelFile.cpp" >}}
## **الوصول إلى أوراق العمل باستخدام فهرس الورقة**
يوضح نموذج التعليمات البرمجية التالي كيفية الوصول إلى أي ورقة عمل أو الحصول عليها عن طريق تحديد الفهرس الخاص بها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-AccessingWorksheetsUsingSheetIndex.cpp" >}}
## **إزالة أوراق العمل باستخدام فهرس الورقة**
 تعمل إزالة أوراق العمل حسب الاسم بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا كنت لا تعرف اسم ورقة العمل ، فاستخدم إصدارًا محملاً بشكل زائد من ملف[RemoveAt](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection#addabcc7d7d76874694018fb3ba37b72c)الطريقة التي تأخذ فهرس ورقة العمل بدلاً من اسم الورقة الخاص بها.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManageWorksheets-RemovingWorksheetsUsingSheetIndex.cpp" >}}
