---
title: ترتيب البيانات
type: docs
weight: 130
url: /ar/python-net/sort-data-of-excel/
description: تعلم كيفية فرز البيانات باستخدام Aspose.Cells for Python via .NET API.
keywords: مكتبة بيثون إكسل، فرز البيانات في بيثون ترتيب تصاعدي أو تنازلي، فرز البيانات في بيثون بناءً على لون الخلفية.
---

{{% alert color="primary" %}}

فرز البيانات هو أحد الميزات المفيدة في Microsoft Excel. يتيح للمستخدمين ترتيب البيانات لجعلها أسهل في المسح. يتيح Aspose.Cells for Python via .NET للمطورين فرز بيانات الورقة العمل بترتيب أبجدي أو رقمي الذي يعمل بنفس الطريقة التي يعمل بها Microsoft Excel لفرز البيانات.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1. حدد **البيانات** من قائمة **الترتيب**. سيتم عرض مربع الحوار للترتيب.
1. حدد خيار الفرز.

عموماً، يتم إجراء الفرز على قائمة - المعرفة بأنها مجموعة متواصلة من البيانات حيث يتم عرض البيانات في أعمدة.

## **فرز البيانات باستخدام Aspose.Cells لمكتبة Excel لغة Python**

توفر Aspose.Cells for for Python via .NET الفئة [**DataSorter**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter) التي تستخدم لفرز البيانات بترتيب تصاعدي أو تنازلي. تحتوي الفئة على بعض الأعضاء الهامة، على سبيل المثال، خصائص مثل Key1 ... Key3 و Order1 ... Order3. يتم استخدام هذه الأعضاء لتحديد المفاتيح المرتبة وتحديد ترتيب ترتيب المفتاح.

يجب عليك تعريف المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. توفر الفئة الطريقة [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) المستخدمة لأداء فرز البيانات بناءً على بيانات الخلية في ورقة العمل.

تقبل الطريقة [**sort**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort/#aspose.cells.Cells-aspose.cells.CellArea) البيانات التالية:

- [**aspose.cells.Cells**](https://reference.aspose.com/cells/python-net/aspose.cells/cells)، الخلايا للورقة العمل الأساسية.
- [**aspose.cells.CellArea**](https://reference.aspose.com/cells/python-net/aspose.cells/cellarea)، نطاق الخلايا. قم بتحديد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ الكود أدناه، يتم فرز البيانات بشكل مناسب.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DataSorting-1.py" >}}

{{% alert color="primary" %}}

إذا كنت ترغب في فرز *من اليسار إلى اليمين*، استخدم السمة [**DataSorter.sort_left_to_right**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/sort_left_to_right/).

{{% /alert %}}

### **فرز البيانات باللون الخلفية باستخدام Aspose.Cells لمكتبة Excel لغة Python**

توفر Excel ميزات لفرز البيانات بناءً على لون الخلفية. تتم توفير نفس الميزة باستخدام Aspose.Cells for for Python via .NET باستخدام DataSorter حيث [**SortOnType**](https://reference.aspose.com/cells/python-net/aspose.cells/sortontype/). يمكن استخدام CellColor في [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) لفرز البيانات بناءً على اللون الخلفية. يتم وضع جميع الخلايا التي تحتوي على اللون المحدد في [**add_key()**](https://reference.aspose.com/cells/python-net/aspose.cells/datasorter/add_key/#int-aspose.cells.SortOnType-aspose.cells.SortOrder-any) وفقًا لإعداد ترتيب الفرز ولا يتم تغيير ترتيب بقية الخلايا على الإطلاق.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-SortDataInColumnWithBackgroundColor-1.py" >}}

## **مواضيع متقدمة**
- [فرز البيانات في العمود بقائمة فرز مخصصة](/cells/ar/python-net/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/python-net/specifying-sort-warning-while-sorting-data/)
