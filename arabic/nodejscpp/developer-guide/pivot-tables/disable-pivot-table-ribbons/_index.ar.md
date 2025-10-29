---
title: تعطيل شريط جدول الدوران
type: docs
weight: 90
url: /ar/nodejs-cpp/disable-pivot-table-ribbons/
description: كيفية تعطيل شريط أدوات الجدول المحوري باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells لـ Node.js إكسل، مكتبة إكسل Node.js، تعطيل شرائط أدوات الجدول المحوري باستخدام Aspose.Cells for Node.js via C++
---

{{% alert color="primary" %}}

تقارير الجدول المحوري مفيدة ولكنها عرضة للأخطاء إذا لم يكن لدى المستخدمين المستهدفين معرفة تفصيلية ببرنامج إكسل لتكوين هذه التقارير. في مثل هذه الحالات، ستريد المؤسسات تقييد المستخدمين من القدرة على تعديل تقرير يعتمد على الجدول المحوري. الميزات الشائعة مثل إضافة فلاتر إضافية، slicers، حقول، أو تغيير الترتيب في التقرير ليست موصى بها لكل مستخدم. من ناحية أخرى، يجب أن يكون هؤلاء المستخدمون قادرين على تحديث التقرير واستخدام الفلاتر أو slicers الحالية. توفر طريقة Aspose.Cells for Node.js via C++ هذه القدرة للمطورين لتقييد المستخدمين من تعديل هذه التقارير أثناء إنشائها. لذلك، يوفر إكسل ميزة لتعطيل شريط أدوات الجدول المحوري، وهو نفس ما يقدمه Aspose.Cells for Node.js via C++، أي يمكن للمطور تعطيل الشريط الذي يحتوي على أدوات تعديل هذه التقارير.

{{% /alert %}}

## **كيفية تعطيل شريط أدوات الجدول المحوري باستخدام Aspose.Cells for Node.js via C++**

يوضح الكود التالي هذه الميزة عن طريق الوصول إلى جدول دوران من ورقة ومن ثم ضبط [**setEnableWizard**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setEnableWizard-boolean-) إلى **false**. يمكن تنزيل ملف جدول الدوران المثالي من هذا [الرابط](pivot_table_test.xlsx).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-DisablePivotTableRibbon.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
