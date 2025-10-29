---
title: إنشاء جداول محورية ورسوم بيانية محورية
type: docs
weight: 20
url: /ar/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: كيفية إضافة الجداول المحورية والرسوم البيانية المحورية باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel، مكتبة Excel Node.js، إضافة الجداول والرسوم البيانية المحورية باستخدام مكتبة Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

الجدول المحوري هو ملخص تفاعلي للسجلات. على سبيل المثال، قد تحتوي على مئات الإدخالات الخاصة بالفواتير في قائمة داخل صفحة العمل. يمكن للجدول المحوري إجمالي الفواتير حسب العميل، المنتج أو التاريخ. باستخدام مايكروسوفت إكسل يمكن بسرعة إعادة ترتيب المعلومات في الجدول المحوري عن طريق سحب الأزرار إلى موقع جديد.

الرسم البياني المحوري هو تمثيل رسومي تفاعلي للبيانات في الجدول المحوري. تم إدخال الرسوم البيانية المحورية في إكسل 2000. باستخدام الرسم البياني المحوري يصبح أسهل فهم البيانات نظرًا لأن الجدول المحوري يقوم تلقائيًا بإنشاء المجاميع الفرعية والمجاميع.

Aspose.Cells for Node.js via C++ يدعم [الجداول المحورية](/cells/ar/nodejs-cpp/create-pivot-tables-and-pivot-charts/) و [الرسوم البيانية المحورية](/cells/ar/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **إضافة جداول و مخططات محورية باستخدام Aspose.Cells for Node.js via C++**

توفر Aspose.Cells for Node.js via C++ مجموعة مميزة من الفئات المستخدمة لإنشاء جداول محورية. تُستخدم هذه الفئات لإنشاء وتعيين كائنات الجدول المحوري، والتي تعمل كأساس لبناء كائن الجدول المحوري:

- PivotField، حقل في تقرير جدول محوري.
- PivotFields، مجموعة من جميع كائنات PivotField في جدول محوري.
- PivotTable، تقرير PivotTable على صفحة العمل.
- PivotTables، مجموعة من جميع كائنات PivotTable على صفحة العمل.

### **تحضير لاستخدام Aspose.Cells for Node.js via C++**
1. تثبيت Aspose.Cells for Node.js via C++ من NPM، استخدم الأمر التالي: $ npm install aspose.cells.node.
1. يمكنك أيضًا اتباع التعليمات خطوة بخطوة حول كيفية تثبيت "Aspose.Cells for Node.js via C++" لبيئة المطور الخاصة بك.


### **كيفية إضافة جدول محوري باستخدام Aspose.Cells for Node.js via C++**

لإنشاء جدول محوري باستخدام Aspose.Cells for Node.js via C++:

1. أضف بعض البيانات إلى خلايا ورق العمل باستخدام طريقة put_value لكائن الخلية. يمكنك أيضًا استخدام ملف قالب مملوء بالفعل بالبيانات. ستُستخدم البيانات كمصدر بيانات الجدول المحوري.
1. أضف جدول محوري إلى ورقة العمل عن طريق استدعاء طريقة add في مجموعة PivotTables (مغلّفة في كائن الورقة).
1. الوصول إلى كائن PivotTable الجديد من مجموعة PivotTables عن طريق تمرير الفهرس الخاص به. ثم استخدم أي من كائنات جدول الجدول المحوري المحتوية في كائن PivotTable لإدارة الجدول.

تم إعطاء أمثلة الكود أدناه.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **كيفية إضافة مخطط محوري باستخدام مكتبة Aspose.Cells for Node.js via C++**

لإنشاء مخطط Pivot باستخدام Aspose.Cells for Node.js via C++:

1. أضف رسم بياني.
1. قم بتعيين PivotSource للرسم البياني للإشارة إلى جدول محوري موجود في جدول البيانات.
1. قم بتعيين سمات أخرى.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
