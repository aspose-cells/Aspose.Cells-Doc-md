---
title: إدارة أوراق العمل في ملفات Microsoft Excel.
linktitle: أوراق العمل
type: docs
weight: 90
url: /ar/python-net/manage-worksheets/
description: يوضح هذا المقال كيفية إدارة ورق العمل في ملفات Microsoft Excel باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة Python Excel، كيفية إدارة ورق العمل في ملفات Microsoft Excel باستخدام Python، إضافة ورق العمل في Python، إزالة ورق العمل في Python، كيفية إضافة ورق العمل إلى ملف Excel جديد باستخدام Python، كيفية إضافة ورق العمل إلى جدول البيانات بتصميم باستخدام Python، كيفية الوصول إلى أوراق العمل باستخدام اسم الورقة في Python، كيفية إزالة أوراق العمل باستخدام اسم الورقة في Python، كيفية إزالة أوراق العمل باستخدام فهرس الورقة في Python، كيفية تنشيط الأوراق وجعل خلية محددة بأستخدام Python.
---


{{% alert color="primary" %}}

يمكن للمطورين إنشاء وإدارة أوراق العمل بشكل سهل في ملفات مايكروسوفت إكسل برمجيًا باستخدام واجهة برمجة التطبيقات المرنة لـ Aspose.Cells. يصف هذا الموضوع الطرق لإضافة وإزالة أوراق العمل في ملفات مايكروسوفت إكسل.

{{% /alert %}}

توفر Aspose.Cells فئة، [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)، تمثل ملف إكسل. تحتوي الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) على مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/) تتيح الوصول إلى كل ورقة عمل في ملف إكسل.

تمثل ورقة العمل بفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet). توفر الفئة [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) مجموعة واسعة من الخصائص والأساليب لإدارة أوراق العمل.

## **كيفية إضافة أوراق عمل إلى ملف Excel جديد**

لإنشاء ملف Excel جديد برمجياً:

1. إنشاء كائن من الفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).
1. استدعاء الطريقة [**add**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/add/#str) من الفئة [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). يتم إضافة ورقة عمل فارغة تلقائياً إلى ملف إكسل. يمكن الإشارة إليها عن طريق تمرير فهرس الورقة الجديدة إلى مجموعة [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/worksheets/).
1. الحصول على مرجع ورقة العمل.
1. القيام بالعمل على أوراق العمل.
1. حفظ ملف إكسل الجديد مع أوراق جديدة بتوجيه طريقة [**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat) لفئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToNewExcelFile-1.py" >}}

## **كيفية إضافة أوراق العمل إلى جدول البيانات بتصميم**

عملية إضافة أوراق العمل إلى جدول إكسل للمصمم هي نفس عملية إضافة ورقة عمل جديدة، باستثناء أن ملف إكسل موجود بالفعل ويجب فتحه قبل إضافة الأوراق. يمكن فتح جدول إكسل للمصمم بواسطة فئة [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AddingWorksheetsToDesignerSpreadSheet-1.py" >}}

## **كيفية الوصول إلى أوراق العمل باستخدام اسم الورقة**

الوصول إلى أي ورقة عمل عن طريق تحديد اسمها أو فهرسها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-AccessingWorksheetsusingSheetName-1.py" >}}

## **كيفية إزالة أوراق العمل باستخدام اسم الورقة**

لإزالة أوراق العمل من ملف، ادع الطريقة [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) من فئة [**WorksheetCollection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection). امرر اسم الورقة إلى الطريقة [**remove_by_name**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_name/#str) لإزالة ورقة عمل معينة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetName-1.py" >}}

## **كيفية إزالة أوراق العمل باستخدام فهرس الورقة**

يعمل إزالة الأوراق عن طريق الاسم بشكل جيد عندما يكون اسم ورقة العمل معروفًا. إذا كنت لا تعرف اسم ورقة العمل، استخدم الطريقة [**remove_by_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/remove_by_index/#int) التي تأخذ فهرس الورقة العمل بدلاً من اسمها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-RemovingWorksheetsUsingSheetIndex-1.py" >}}

## **كيفية تنشيط الأوراق وجعل خلية محددة في ورقة العمل**

أحيانًا، تحتاج ورقة عمل معينة إلى أن تكون نشطة ومعروضة عندما يفتح المستخدم ملف إكسل في إكسل. بالمثل، قد ترغب في تنشيط خلية معينة وتعيين شريطي التمرير لعرض الخلية النشطة.
تمتلك Aspose.Cells القدرة على القيام بكل هذه المهام.

ورقة العمل النشطة هي الورقة التي تعمل عليها: اسم الورقة النشطة على علامة التبويب يكون سميك افتراضيًا.

الخلية النشطة هي الخلية المحددة، الخلية التي يتم إدخال البيانات فيها عند بدء الكتابة. تكون خلية واحدة فقط نشطة في وقت واحد. يتم تمييز الخلية النشطة بحد ثقيل.

### **كيفية تنشيط الأوراق وجعل خلية محددة في ورقة العمل**

توفر Aspose.Cells استدعاءات API محددة لتفعيل ورقة وخلية. على سبيل المثال، تعد خاصية [**Aspose.Cells.WorksheetCollection.active_sheet_index**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection/active_sheet_index/) مفيدة لضبط الورقة النشطة في دفتر العمل.
بالمثل، تستخدم الخاصية [**Aspose.Cells.Worksheet.active_cell**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/active_cell/) لضبط والحصول على خلية نشطة في ورقة العمل.

للتأكد من أن شريطي التمرير الأفقي أو العمودي في موضع فهرس الصف والعمود الذي تريد عرض البيانات المحددة فيه، استخدم الخصائص [**Aspose.Cells.Worksheet.first_visible_row**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_row/) و [**Aspose.Cells.Worksheet.first_visible_column**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/first_visible_column/).

تُظهر الشفرة المثالية التالية كيفية تفعيل ورقة عمل وجعل خلية نشطة فيها. في الناتج المولد، ستتم تمرير أشرطة التمرير لجعل الصف الثاني والعمود الثاني أول صف وعمود مرئيين لديها.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Worksheets-Management-MakeCellActive-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
