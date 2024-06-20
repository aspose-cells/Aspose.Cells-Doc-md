---
title: ترتيب البيانات
type: docs
weight: 130
url: /ar/net/sort-data-of-excel/
description: تعلم كيفية فرز البيانات باستخدام واجهة البرمجة التطبيقية Aspose.Cells for .NET.
keywords: فرز البيانات بترتيب تصاعدي أو تنازلي، فرز البيانات بناءً على لون الخلفية
---

{{% alert color="primary" %}}

فرز البيانات هو واحد من الميزات المفيدة في Microsoft Excel. يتيح للمستخدمين ترتيب البيانات لجعلها أسهل في المسح. تتيح Aspose.Cells للمطورين ترتيب بيانات ورقة العمل ترتيب أبجدي أو رقمي والذي يعمل بنفس الطريقة التي يقوم بها Microsoft Excel لفرز البيانات.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1. حدد **البيانات** من قائمة **الترتيب**. سيتم عرض مربع الحوار للترتيب.
1. حدد خيار الفرز.

عموماً، يتم إجراء الفرز على قائمة - المعرفة بأنها مجموعة متواصلة من البيانات حيث يتم عرض البيانات في أعمدة.

## **فرز البيانات مع Aspose.Cells**

يوفر Aspose.Cells الفئة [**DataSorter**](https://reference.aspose.com/cells/net/aspose.cells/datasorter) المستخدمة لفرز البيانات بترتيب تصاعدي أو تنازلي. تحتوي الفئة على بعض الأعضاء المهمة، على سبيل المثال، خصائص مثل Key1 ... Key3 و Order1 ... Order3. يتم استخدام هذه الأعضاء لتعريف المفاتيح المرتبة وتحديد ترتيب ترتيب المفتاح.

يجب عليك تعريف المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. توفر الفئة الطريقة [**Sort**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/sort/index) المستخدمة لأداء فرز البيانات بناءً على بيانات الخلية في ورقة العمل.

تقبل الطريقة [**Sort**](https://reference.aspose.com/cells/net/aspose.cells.datasorter/sort/methods/1) البيانات التالية:

- [**Aspose.Cells.Cells**](https://reference.aspose.com/cells/net/aspose.cells/cells)، الخلايا للورقة العمل الأساسية.
- [**Aspose.Cells.CellArea**](https://reference.aspose.com/cells/net/aspose.cells/cellarea)، نطاق الخلايا. قم بتحديد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ الكود أدناه، يتم فرز البيانات بشكل مناسب.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-Handling-DataSorting-1.cs" >}}

{{% alert color="primary" %}}

إذا كنت ترغب في فرز *من اليسار إلى اليمين*، استخدم السمة [**DataSorter.SortLeftToRight**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/properties/sortlefttoright).

{{% /alert %}}

### **فرز البيانات مع لون الخلفية**

يوفر Excel ميزات لفرز البيانات بناءً على لون الخلفية. نفس الميزة متوفرة باستخدام Aspose.Cells باستخدام DataSorter حيث يمكن استخدام [**SortOnType**](https://reference.aspose.com/cells/net/aspose.cells/sortontype).CellColor في [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey) لفرز البيانات بناءً على لون الخلفية. يتم وضع جميع الخلايا التي تحتوي على اللون المحدد في [**AddKey()**](https://reference.aspose.com/cells/net/aspose.cells/datasorter/methods/addkey)، الوظيفة في الأعلى أو الأسفل وفقًا لإعداد SortOrder ولم يتم تغيير ترتيب بقية الخلايا على الإطلاق.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-SortDataInColumnWithBackgroundColor-1.cs" >}}

## **مواضيع متقدمة**
- [فرز البيانات في العمود بقائمة فرز مخصصة](/cells/ar/net/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/net/specifying-sort-warning-while-sorting-data/)
