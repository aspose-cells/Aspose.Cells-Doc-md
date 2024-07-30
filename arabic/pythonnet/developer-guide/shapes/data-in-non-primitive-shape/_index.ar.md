---
title: البيانات في شكل غير الذي يتميز ببساطة
type: docs
weight: 300
url: /ar/python-net/data-in-non-primitive-shape/
description: يوضح هذا المقال البيانات بشكل غير أولية من خلال Aspose.Cells لـ نظام Python via .NET API.
keywords: مكتبة بيانات Excel لـ Python، البيانات بشكل غير أولية باستخدام Python، كيفية الوصول إلى بيانات الشكل غير الأولية باستخدام Python.
---

## **الوصول إلى بيانات الشكل غير الذي يتميز ببساطة**

في بعض الأحيان، تحتاج إلى الوصول إلى البيانات من شكل ليس مدمجًا. يطلق على الأشكال المدمجة ، الأشكال الأساسية ، ويطلق على الأشكال التي ليست كذلك ، الأشكال غير الأساسية. على سبيل المثال، يمكنك تحديد أشكالك الخاصة باستخدام خطوط متصلة مختلفة.

## **الشكل غير الأساسي**

في Aspose.Cells لـ نظام Python via .NET، يتم تعيين أشكال غير أولية النوع [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype). يمكنك التحقق من نوعها باستخدام الخاصية [**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type).

الوصول إلى بيانات الشكل باستخدام الخاصية [**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths). تُعيد جميع المسارات المتصلة التي تشكل الشكل غير الأساسي. هذه المسارات تكون من نوع [**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath) التي تحمل قائمة بجميع القطاعات التي بدورها تحتوي على النقاط في كل قطاع.

|**يظهر مثالًا على شكل غير أساسي**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
