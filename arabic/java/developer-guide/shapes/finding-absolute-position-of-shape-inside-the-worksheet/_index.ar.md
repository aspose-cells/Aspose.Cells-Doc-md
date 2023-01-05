---
title: البحث عن الموضع المطلق للشكل داخل ورقة العمل
type: docs
weight: 7000
url: /ar/java/finding-absolute-position-of-shape-inside-the-worksheet/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تحتاج إلى معرفة الموضع المطلق للشكل في ورقة العمل. يوفر Aspose.Cells ملف[**Shape.getLeftToCorner ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) و[**Shape.getTopToCorner ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) خصائص لهذا الغرض. ترجع هذه الخصائص الموضع المطلق لشكل في ورقة عمل بالبكسل.

{{% /alert %}}

## **شرح خصائص Shape.getLeftToCorner () و Shape.getTopToCorner ()**

توضح لقطة الشاشة هذه المسافات[**Shape.getLeftToCorner ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) و[**Shape.getTopToCorner ()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)قياس الخصائص.

**قياس الموقف المطلق**

![ما يجب القيام به: image_بديل_نص](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

يعرض نموذج التعليمات البرمجية التالي الموضع المطلق للشكل الأول في ورقة عمل بالبكسل. يعرض الرمز الإخراج التالي في وحدة التحكم:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
