---
title: وظيفة التوحيد
type: docs
weight: 20
url: /ar/nodejs-cpp/consolidation-function/
description: كيفية تطبيق وظيفة التوحيد ConsolidationFunction على حقول البيانات في الجدول المحوري باستخدام Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel، مكتبة Excel Node.js، وظيفة التوحيد إلى حقول البيانات في الجدول المحوري باستخدام مكتبة Aspose.Cells for Node.js via C++.
---

## **وظيفة التوحيد**

يمكن استخدام Aspose.Cells for Node.js via C++ لتطبيق وظيفة التوحيد على حقول البيانات (أو حقول القيمة) في الجدول المحوري. في Microsoft Excel، يمكنك النقر بزر الماوس الأيمن على حقل القيمة ثم اختيار **إعدادات حقل القيمة...** ثم التبديل إلى علامة التبويب **تلخيص القيم بواسطة**. من هناك، يمكنك اختيار أي وظيفة توحيد تفضّلها مثل Sum، Count، Average، Max، Min، Product، Count مميز، وغيرها.

توفر Aspose.Cells for Node.js via C++ تعداد [**ConsolidationFunction**](https://reference.aspose.com/cells/nodejs-cpp/consolidationfunction/) لدعم وظائف التوحيد التالية.

- ConsolidationFunction.Average
- ConsolidationFunction.Count
- ConsolidationFunction.CountNums
- ConsolidationFunction.DistinctCount
- ConsolidationFunction.Max
- ConsolidationFunction.Min
- ConsolidationFunction.Product
- ConsolidationFunction.StdDev
- ConsolidationFunction.StdDevp
- ConsolidationFunction.Sum
- ConsolidationFunction.Var
- ConsolidationFunction.Varp

## **كيفية تطبيق وظيفة التوحيد على حقول البيانات في الجدول المحوري باستخدام Aspose.Cells for Node.js via C++**

يطبق الكود التالي وظيفة تجميع **المتوسط** على الحقل الأول من البيانات (أو حقل القيمة) ووظيفة تجميع **عدد فريد** على الحقل الثاني من البيانات (أو حقل القيمة).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-ConsolidationFunctions-1.js" >}}

{{% alert color="primary" %}}

وظيفة التوحيد DISTINCT_COUNT مدعومة فقط في Microsoft Excel 2013.

{{% /alert %}}
{{< app/cells/assistant language="nodejs-cpp" >}}
