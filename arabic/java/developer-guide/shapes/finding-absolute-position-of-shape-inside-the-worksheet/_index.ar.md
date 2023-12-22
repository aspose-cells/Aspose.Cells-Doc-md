---
title: العثور على الموضع المطلق للشكل داخل ورقة العمل
type: docs
weight: 7000
url: /ar/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: تعرف على كيفية البحث عن الموضع المطلق للشكل داخل ورقة العمل من خلال واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: How to Find Absolute Position of Shape in Java, Get Absolute Position of Shape using Java, Obtain Absolute Position of Shape inside the Worksheet via Java, Measure absolute position of Shape with Java.
---
{{% alert color="primary" %}}

 في بعض الأحيان، تحتاج إلى معرفة الموضع المطلق للشكل في ورقة العمل. Aspose.Cells يوفر[**الشكل.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) و[**الشكل.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) خصائص لهذا الغرض. تُرجع هذه الخصائص الموضع المطلق للشكل في ورقة العمل بالبكسل.

{{% /alert %}}

##  **شرح خصائص Shape.getLeftToCorner() وShape.getTopToCorner()**

 تشرح لقطة الشاشة هذه المسافات التي يمكن أن تقطعها[**الشكل.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) و[**الشكل.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner)قياس الخصائص.

**كيفية قياس الموقف المطلق**

![ما يجب القيام به:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

يعرض نموذج التعليمات البرمجية التالي الموضع المطلق للشكل الأول في ورقة العمل بالبكسل. يعرض الكود الإخراج التالي في وحدة التحكم:

{{< highlight "java" >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
