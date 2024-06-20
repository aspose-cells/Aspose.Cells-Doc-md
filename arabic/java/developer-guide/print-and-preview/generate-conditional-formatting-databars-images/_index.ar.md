---
title: إنشاء بيانات شكل معايرة شريطية للصور
type: docs
weight: 170
url: /ar/java/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

أحيانًا ، تحتاج إلى إنشاء صور شرائط البيانات التنسيقية الشرطية. يمكنك استخدام طريقة Aspose.Cells [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) لإنشاء هذه الصور. توضح هذه المقالة كيفية إنشاء صورة DataBar باستخدام Aspose.Cells.

{{% /alert %}}

## **مثال**

كود العينة التالي ينشئ صورة DataBar للخلية C1. أولاً، يتم الوصول إلى كائن الشرط النمطي للخلية، ومن ثم يتم الوصول من هذا الكائن إلى كائن DataBar واستخدام طريقته [**DataBar.toImage()**](https://reference.aspose.com/cells/java/com.aspose.cells/databar#toImage(com.aspose.cells.Cell,%20com.aspose.cells.ImageOrPrintOptions)) لإنشاء صورة للخلية. في النهاية، يتم حفظ الصورة على القرص.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-GenerateDatabarImage-1.java" >}}
