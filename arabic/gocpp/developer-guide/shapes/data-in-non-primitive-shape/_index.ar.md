---
title: البيانات في الشكل غير primitives مع Golang عبر C++
linktitle: البيانات في شكل غير الذي يتميز ببساطة
type: docs
weight: 300
url: /ar/go-cpp/data-in-non-primitive-shape/
description: الوصول إلى البيانات والتلاعب بها في الأشكال غير primitives باستخدام Aspose.Cells مع Golang عبر C++.
---

## **الوصول إلى بيانات الشكل غير الذي يتميز ببساطة**

في بعض الأحيان، تحتاج إلى الوصول إلى البيانات من شكل ليس مدمجًا. يطلق على الأشكال المدمجة ، الأشكال الأساسية ، ويطلق على الأشكال التي ليست كذلك ، الأشكال غير الأساسية. على سبيل المثال، يمكنك تحديد أشكالك الخاصة باستخدام خطوط متصلة مختلفة.

## **الشكل غير الأساسي**

في Aspose.Cells، يتم تعيين الأشكال غير الأساسية نوع [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/). يمكنك التحقق من نوعها باستخدام الخاصية [**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/).

الوصول إلى بيانات الشكل باستخدام الخاصية [**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/). تُعيد جميع المسارات المتصلة التي تشكل الشكل غير الأساسي. هذه المسارات تكون من نوع [**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/) التي تحمل قائمة بجميع القطاعات التي بدورها تحتوي على النقاط في كل قطاع.

|**يظهر مثالًا على شكل غير أساسي**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
