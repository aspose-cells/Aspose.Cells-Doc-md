---
title: إدارة فواصل الصفحات
type: docs
weight: 30
url: /ar/cpp/managing-page-breaks/
---
{{% alert color="primary" %}} 

وفقًا للتعريف ، فاصل الصفحة هو مكان في تدفق النص حيث تنتهي إحدى الصفحات وتبدأ الصفحة التالية. Microsoft يتيح Excel للمستخدمين إضافة فواصل الصفحات إلى أي خلية محددة بورقة العمل.

موقع الخلية حيث تمت إضافة فاصل الصفحة وانتهاء الصفحة وجميع البيانات المتبقية بعد طباعة فاصل الصفحة على الصفحة التالية أثناء الطباعة. بكلمات بسيطة ، تقسم فواصل الصفحات ورقة العمل إلى صفحات متعددة وفقًا لمواصفاتك. يمكنك أيضًا إضافة فواصل صفحات إلى أوراق العمل الخاصة بك في وقت التشغيل باستخدام Aspose.Cells. يسمح Aspose.Cells للمطورين بإضافة نوعين من فواصل الصفحات:

- فاصل صفحة أفقي
- فاصل صفحة عمودي

في بقية المناقشة ، سنصف كيف يمكنك إضافة فواصل صفحات أفقية أو عمودية إلى أوراق العمل الخاصة بك باستخدام Aspose.Cells.

{{% /alert %}} 
## **فواصل الصفحة**
 Aspose.Cells يوفر فئة[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) يمثل ملف Excel. ال[IWorkbook](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_workbook) فئة تحتوي على[أوراق عمل](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet_collection)مجموعة تسمح بالوصول إلى كل ورقة عمل في ملف Excel.

 يتم تمثيل ورقة العمل بواسطة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet) صف دراسي. ال[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)توفر فئة مجموعة واسعة من الأساليب المستخدمة لإدارة ورقة العمل. لإضافة فواصل الصفحات ، استخدم ملف[AddPageBreaks](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a5f8dd5624b81e0ee2e7455f2b83380f6) طريقة[IWorksheet](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet)صف دراسي.
### **مضيفا فواصل الصفحات**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-Worksheets-ManagingPageBreaks-AddingPageBreaks.cpp" >}}
