---
title: ترتيب البيانات
type: docs
weight: 130
url: /ar/nodejs-cpp/sort-data-of-excel/
description: تعلم كيفية فرز البيانات باستخدام واجهة برمجة التطبيقات Aspose.Cells for Node.js via C++.
keywords: فرز البيانات بترتيب تصاعدي أو تنازلي، فرز البيانات بناءً على لون الخلفية
---

{{% alert color="primary" %}}

فرز البيانات هو واحد من العديد من الميزات المفيدة في Microsoft Excel. يسمح للمستخدمين بترتيب البيانات لتسهيل المسح. تتيح Aspose.Cells for Node.js via C++ للمطورين فرز بيانات ورقة العمل أبجدياً أو رقمياً، والذي يعمل بنفس طريقة فرز البيانات في Microsoft Excel.

{{% /alert %}}

## **فرز البيانات في Microsoft Excel**

لفرز البيانات في Microsoft Excel:

1. حدد **البيانات** من قائمة **الترتيب**. سيتم عرض مربع الحوار للترتيب.
1. حدد خيار الفرز.

عموماً، يتم إجراء الفرز على قائمة - المعرفة بأنها مجموعة متواصلة من البيانات حيث يتم عرض البيانات في أعمدة.

## **فرز البيانات مع Aspose.Cells**

توفر Aspose.Cells for Node.js via C++ الصف [**DataSorter**](https://reference.aspose.com/cells/nodejs-cpp/datasorter) المستخدم لفرز البيانات بطريقة تصاعدية أو تنازلية. يحتوي الصنف على بعض الأعضاء المهمة، على سبيل المثال، خصائص مثل Key1 ... Key3 و Order1 ... Order3. تُستخدم هذه الأعضاء لتعريف المفاتيح المرتبة وتحديد ترتيب فرز المفاتيح.

يجب عليك تعريف المفاتيح وتعيين ترتيب الفرز قبل تنفيذ فرز البيانات. توفر الفئة الطريقة [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) المستخدمة لأداء فرز البيانات بناءً على بيانات الخلية في ورقة العمل.

تقبل الطريقة [**DataSorter.sort**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#sort-cells-cellarea-) البيانات التالية:

- [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)، الخلايا للورقة العمل الأساسية.
- [**CellArea**](https://reference.aspose.com/cells/nodejs-cpp/cellarea)، نطاق الخلايا. قم بتحديد منطقة الخلية قبل تطبيق فرز البيانات.

يستخدم هذا المثال ملف القالب "Book1.xls" الذي تم إنشاؤه في Microsoft Excel. بعد تنفيذ الكود أدناه، يتم فرز البيانات بشكل مناسب.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataSorting-1.js" >}}

{{% alert color="primary" %}}

إذا كنت ترغب في فرز *من اليسار إلى اليمين*، استخدم السمة [**DataSorter.setSortLeftToRight**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#setSortLeftToRight-boolean-).

{{% /alert %}}

### **فرز البيانات مع لون الخلفية**

يقدم إكسل ميزات لفرز البيانات استنادًا إلى لون الخلفية. يتم تقديم نفس الميزة باستخدام Aspose.Cells for Node.js via C++ باستخدام DataSorter حيث يمكن استخدام [**SortOnType**](https://reference.aspose.com/cells/nodejs-cpp/sortontype/).CellColor في [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) لفرز البيانات استنادًا إلى لون الخلفية. جميع الخلايا التي تحتوي على اللون المحدد في الدالة [**DataSorter.addKey**](https://reference.aspose.com/cells/nodejs-cpp/datasorter/#addColorKey-number-sortontype-sortorder-color-) تُوضع في الأعلى أو الأسفل حسب إعداد SortOrder وترتيب باقي الخلايا لا يتغير على الإطلاق.

فيما يلي الملفات العينية التي يمكن تنزيلها لاختبار هذه الميزة:

[sampleBackGroundFile.xlsx](81920906.xlsx)

[outputsampleBackGroundFile.xlsx](81920907.xlsx)

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-SortDataInColumnWithBackgroundColor-1.js" >}}

## **مواضيع متقدمة**
- [فرز البيانات في العمود بقائمة فرز مخصصة](/cells/ar/nodejs-cpp/sort-data-in-column-with-custom-sort-list/)
- [تحديد تحذير الفرز أثناء فرز البيانات](/cells/ar/nodejs-cpp/specifying-sort-warning-while-sorting-data/)

{{< app/cells/assistant language="nodejs-cpp" >}}
