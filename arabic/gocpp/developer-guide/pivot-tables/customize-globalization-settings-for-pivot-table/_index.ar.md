---
title: تخصيص إعدادات التدويل للجدول المحوري باستخدام Golang عبر C++
linktitle: تخصيص إعدادات العالمية لجدول محوري
type: docs
weight: 50
url: /ar/go-cpp/customize-globalization-settings-for-pivot-table/
description: تعلم كيفية تخصيص إعدادات التوطين في الجدول المحوري باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 أحيانًا تريد تخصيص نص *المجموع الكلي للجدول المحوري، المجموع الفرعي، المجموع الكلي، جميع العناصر، عناصر متعددة، تسميات الأعمدة، تسميات الصفوف، القيم الفارغة* وفقًا لمتطلباتك. يتيح لك Aspose.Cells for C++ تخصيص إعدادات التوطين للجدول المحوري للتعامل مع مثل هذه السيناريوهات. يمكنك أيضًا استخدام هذه الميزة لتغيير التسميات إلى لغات أخرى مثل العربية، الهندية، البولندية، وغيرها.

## **تخصيص إعدادات العالمية لجدول محوري**

 يوضح الكود النموذجي التالي كيفية تخصيص إعدادات التوطين للجدول المحوري في C++. ينشئ فصل *CustomPivotTableGlobalizationSettings* المشتق من الفصل [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) ويجاوز جميع الأساليب الضرورية. تُرجع هذه الأساليب نصوصًا مخصصة لمختلف عناصر الجدول المحوري. ثم يُخصص هذا التنفيذ لخاصية [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/). يقوم المثال بتحميل [ملف Excel المصدر](40468488.xlsx)، تحديث بيانات الجدول المحوري، وحفظه كـ [ملف PDF المخرجات](40468487.pdf). يُظهر لقطة الشاشة أدناه التسميات المخصصة في الإخراج.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}
