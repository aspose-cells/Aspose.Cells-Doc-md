---
title: العثور على الموقع المطلق للشكل داخل ورقة العمل
type: docs
weight: 7000
url: /ar/java/finding-absolute-position-of-shape-inside-the-worksheet/
description: تعلم كيفية العثور على الموقع المطلق للشكل داخل ورقة العمل من خلال واجهات برمجة التطبيقات Aspose.Cells for Java.
keywords: كيفية العثور على الموقع المطلق للشكل في جافا، الحصول على الموقع المطلق للشكل باستخدام جافا، الحصول على الموقع المطلق للشكل داخل ورقة العمل via Java، قياس الموقع المطلق للشكل بجافا.
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى معرفة الموقع المطلق لشكل على ورقة عمل. توفر Aspose.Cells الخصائص [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) و [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner) لهذا الغرض. تعيد هذه الخصائص الموقع المطلق للشكل في ورقة عمل بوحدات البكسل.

{{% /alert %}}

## **شرح خصائص Shape.getLeftToCorner() و Shape.getTopToCorner()**

تشرح هذه اللقطة الشاشة ما الذي تقوم به الخصائص [**Shape.getLeftToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#LeftToCorner) و [**Shape.getTopToCorner()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#TopToCorner).

**كيفية قياس الموقع المطلق**

![todo:image_alt_text](finding-absolute-position-of-shape-inside-the-worksheet_1.png)

الشيفة العينية لأول شكل في ورقة العمل بالبكسل تُعرض في الكود العيني التالي. يعرض الكود الإخراج التالي في وحدة التحكم:

{{< highlight java >}}

Absolute Position of this Shape is (320, 180)

{{< /highlight >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FindAbsolutePositionOfShape-FindAbsolutePositionOfShape.java" >}}
{{< app/cells/assistant language="java" >}}
