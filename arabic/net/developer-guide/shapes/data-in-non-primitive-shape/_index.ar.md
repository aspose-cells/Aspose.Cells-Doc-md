---
title: البيانات في شكل غير الذي يتميز ببساطة
type: docs
weight: 300
url: /ar/net/data-in-non-primitive-shape/
---

## **الوصول إلى بيانات الشكل غير الذي يتميز ببساطة**

في بعض الأحيان، تحتاج إلى الوصول إلى البيانات من شكل ليس مدمجًا. يطلق على الأشكال المدمجة ، الأشكال الأساسية ، ويطلق على الأشكال التي ليست كذلك ، الأشكال غير الأساسية. على سبيل المثال، يمكنك تحديد أشكالك الخاصة باستخدام خطوط متصلة مختلفة.

## **الشكل غير الأساسي**

في Aspose.Cells، يتم تعيين الأشكال غير الأساسية نوع [**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype). يمكنك التحقق من نوعها باستخدام الخاصية [**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype).

الوصول إلى بيانات الشكل باستخدام الخاصية [**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths). تُعيد جميع المسارات المتصلة التي تشكل الشكل غير الأساسي. هذه المسارات تكون من نوع [**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath) التي تحمل قائمة بجميع القطاعات التي بدورها تحتوي على النقاط في كل قطاع.

|**يظهر مثالًا على شكل غير أساسي**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
