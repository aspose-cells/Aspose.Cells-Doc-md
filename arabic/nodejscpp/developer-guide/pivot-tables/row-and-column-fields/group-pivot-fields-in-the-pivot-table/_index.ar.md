---
title: تجميع حقول الجدول المحوري في جدول الدوران
type: docs
weight: 80
url: /ar/nodejs-cpp/group-pivot-fields-in-the-pivot-table/
description: كيفية تجميع حقول Pivot في جدول Pivot باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ إكسل، مكتبة إكسل Node.js، كيفية تجميع حقول Pivot في جدول Pivot باستخدام مكتبة إكسل Aspose.Cells for Node.js via C++.
---

## **سيناريوهات الاستخدام المحتملة**

يسمح لك مايكروسوفت إكسل بتجميع حقول Pivot لجدول Pivot. عندما يكون هناك كمية كبيرة من البيانات المتعلقة بحقل Pivot، يكون من المفيد غالبًا تجميعها في أقسام. كما يوفر Aspose.Cells for Node.js via C++ هذه الميزة باستخدام أسلوب [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-).

## **كيفية تجميع حقول الجدول المحوري**

يقوم الكود العيني التالي بتحميل ملف الإكسل العيني وينفذ عمليات التجميع على الحقل المحوري الأول باستخدام طريقة [**PivotTable.groupBy()**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield/#groupBy-date-date-pivotgroupbytypearray-number-boolean-). ثم يقوم بتحديث وحساب بيانات الجدول المحوري ويحفظ الدفتر كملف إكسل جديد. توضح الصورة الناتجة تأثير الكود العيني على ملف الإكسل العيني. كما يظهر في الصورة، تم تجميع الحقل المحوري الأول الآن حسب الشهور والربع.

![todo:image_alt_text](group-pivot-fields-in-the-pivot-table_1.png)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-GroupPivotFieldsInPivotTable.js" >}}
{{< app/cells/assistant language="nodejs-cpp" >}}
