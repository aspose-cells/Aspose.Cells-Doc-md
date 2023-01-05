---
title: البيانات في شكل غير بدائي
type: docs
weight: 300
url: /ar/net/data-in-non-primitive-shape/
---
## **الوصول إلى البيانات ذات الشكل غير البدائي**

في بعض الأحيان ، تحتاج إلى الوصول إلى البيانات من شكل غير مضمن. تسمى الأشكال المضمنة الأشكال البدائية ؛ تلك التي لا تسمى غير بدائية. على سبيل المثال ، يمكنك تحديد الأشكال الخاصة بك باستخدام خطوط مختلفة متصلة منحنى.

## **شكل غير بدائي**

في Aspose.Cells ، يتم تخصيص النوع للأشكال غير البدائية[**نوع تلقائي. ليس بدائي**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) . يمكنك التحقق من نوعها باستخدام ملف[**الشكل. نوع تلقائي**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)خاصية.

 قم بالوصول إلى بيانات الشكل باستخدام ملف[**الشكل**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)خاصية. تقوم بإرجاع جميع المسارات المتصلة التي تشكل الشكل غير البدائي. هذه المسارات من النوع[**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)يحتوي على قائمة بجميع الأجزاء التي تحتوي بدورها على النقاط في كل جزء.

|**يعرض مثالاً لشكل غير بدائي**|
|:- |
|![ما يجب القيام به: image_بديل_نص](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
