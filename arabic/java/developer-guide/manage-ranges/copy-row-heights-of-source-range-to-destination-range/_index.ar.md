---
title: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة
type: docs
weight: 250
url: /ar/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

في بعض الأحيان يحتاج المستخدم إلى نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة. توفر Aspose.Cells مؤشر [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) لهذا الغرض. عندما تقوم بتعيين [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) بخصائص [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS)، سيتم نسخ ارتفاعات كل الصفوف داخل النطاق المصدر إلى النطاق الوجهة.

{{% /alert %}} 
## **نسخ أطوال الصفوف من النطاق المصدر إلى النطاق الهدف**
يشرح الكود العيني التالي كيفية استخدام مؤشر [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW_HEIGHTS) لنسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة. عند فتح ملف إكسل المخرج الذي تم إنشاؤه بواسطة هذا الكود في Microsoft Excel، ستلاحظ أن ارتفاعات الصفوف في النطاق الوجهة تطابق تمامًا ارتفاعات الصفوف في النطاق المصدر.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
