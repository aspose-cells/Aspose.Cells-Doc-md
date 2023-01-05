---
title: إنشاء صور أشرطة بيانات التنسيق الشرطي
type: docs
weight: 170
url: /ar/java/generate-conditional-formatting-databars-images/
---
{{% alert color="primary" %}}

 في بعض الأحيان ، تحتاج إلى إنشاء صور لأشرطة بيانات التنسيق الشرطي. يمكنك استخدام Aspose.Cells[**DataBar.toImage ()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)طريقة لتوليد هذه الصور. يوضح هذا المقال كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

## **مثال**

 ينشئ نموذج التعليمات البرمجية التالي صورة DataBar للخلية C1. أولاً ، يصل إلى كائن شرط التنسيق للخلية ، ثم من هذا الكائن ، يصل إلى كائن DataBar ويستخدم[**DataBar.toImage ()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) طريقة لتوليد صورة الخلية. أخيرًا ، يحفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
