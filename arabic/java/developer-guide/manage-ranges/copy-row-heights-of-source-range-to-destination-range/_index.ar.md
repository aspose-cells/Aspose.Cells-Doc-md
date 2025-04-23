---
title: نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة
type: docs
weight: 250
url: /ar/java/copy-row-heights-of-source-range-to-destination-range/
---

{{% alert color="primary" %}} 

في بعض الأحيان يحتاج المستخدم إلى نسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة. يوفر Aspose.Cells التابع [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) لهذا الغرض. عند ضبط خاصية [PasteOptions.setPasteType()](https://reference.aspose.com/cells/java/com.aspose.cells/pasteoptions#PasteType) مع تعداد [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) سيتم نسخ ارتفاعات جميع الصفوف داخل النطاق المصدر إلى النطاق الوجهة.

{{% /alert %}} 
## **نسخ أطوال الصفوف من النطاق المصدر إلى النطاق الهدف**
الشيفرة النموذجية التالية تشرح كيفية استخدام عداد [PasteType.ROW_HEIGHTS](https://reference.aspose.com/cells/java/com.aspose.cells/pastetype#ROW-HEIGHTS) لنسخ ارتفاعات الصف من النطاق المصدر إلى النطاق الوجهة. عند فتح ملف إكسل الناتج الذي يتم إنشاؤه بواسطة هذا الرمز في Microsoft Excel، ستلاحظ أن ارتفاعات الصفوف في النطاق الوجهة مطابقة تمامًا لارتفاعات الصفوف في النطاق المصدر.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyRowHeights-CopyRowHeights.java" >}}
{{< app/cells/assistant language="java" >}}
