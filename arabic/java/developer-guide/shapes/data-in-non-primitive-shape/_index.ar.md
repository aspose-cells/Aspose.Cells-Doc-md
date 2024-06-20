---
title: البيانات في شكل غير الذي يتميز ببساطة
type: docs
weight: 500
url: /ar/java/data-in-non-primitive-shape/
---

## **الوصول إلى بيانات الشكل غير الذي يتميز ببساطة**

في بعض الأحيان، تحتاج إلى الوصول إلى البيانات من شكل ليس مدمجًا. يطلق على الأشكال المدمجة ، الأشكال الأساسية ، ويطلق على الأشكال التي ليست كذلك ، الأشكال غير الأساسية. على سبيل المثال، يمكنك تحديد أشكالك الخاصة باستخدام خطوط متصلة مختلفة.

## **الشكل غير الأساسي**

في Aspose.Cells ، يتم تعيين الأشكال غير الأساسية النوع [**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE). يمكنك التحقق من نوعها باستخدام الطريقة [**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType).

الوصول إلى بيانات الشكل باستخدام الطريقة [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths). إنها تعيد جميع المسارات المتصلة التي تشكل الشكل غير الأساسي. تكون هذه المسارات من نوع ShapePath التي تحتوي على قائمة بجميع الشرائح التي تحتوي على النقاط في كل شريحة.

يوضح المقطع البرمجي التالي استخدام الطريقة [**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths) للوصول إلى معلومات المسار الخاصة بالشكل غير الأساسي.

**يُظهر مثالًا لشكل غير أساسي** 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
