---
title: البيانات في شكل غير بدائي
type: docs
weight: 500
url: /ar/java/data-in-non-primitive-shape/
---
## **الوصول إلى البيانات ذات الشكل غير البدائي**

في بعض الأحيان ، تحتاج إلى الوصول إلى البيانات من شكل غير مضمن. تسمى الأشكال المضمنة الأشكال البدائية ؛ تلك التي لا تسمى غير بدائية. على سبيل المثال ، يمكنك تحديد الأشكال الخاصة بك باستخدام خطوط مختلفة متصلة منحنى.

## **شكل غير بدائي**

 في Aspose.Cells ، يتم تخصيص النوع للأشكال غير البدائية[**نوع تلقائي**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) . يمكنك التحقق من نوعها باستخدام ملف[**Shape.getAutoShapeType ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)طريقة.

 قم بالوصول إلى بيانات الشكل باستخدام ملف[**Shape.getPaths ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)طريقة. تقوم بإرجاع جميع المسارات المتصلة التي تشكل الشكل غير البدائي. هذه المسارات من النوع ShapePath الذي يحتوي على قائمة بجميع المقاطع التي بدورها تحتوي على النقاط في كل مقطع.

يوضح مقتطف الشفرة التالي استخدام[**Shape.getPaths ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)طريقة للوصول إلى معلومات المسار ذات الشكل غير البدائي.

**يعرض مثالاً لشكل غير بدائي** 

![ما يجب القيام به: image_بديل_نص](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
