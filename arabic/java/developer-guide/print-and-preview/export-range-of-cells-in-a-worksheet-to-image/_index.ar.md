---
title: تصدير مجموعة من الخلايا في ورقة عمل إلى صورة
type: docs
weight: 130
url: /ar/java/export-range-of-cells-in-a-worksheet-to-image/
---

{{% alert color="primary" %}}

يمكنك إنشاء صورة لورقة عمل باستخدام Aspose.Cells. ومع ذلك، في بعض الأحيان، تحتاج إلى تصدير مجموعة من الخلايا فقط في ورقة عمل إلى صورة. تشرح هذه المقالة كيفية تحقيق ذلك.

{{% /alert %}}

لأخذ صورة من النطاق، قم بتعيين منطقة الطباعة إلى النطاق المطلوب ثم قم بتعيين جميع الهوامش إلى 0. ثم قم بتعيين [**ImageOrPrintOptions.setOnePagePerSheet()**](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#OnePagePerSheet) إلى **true**.

الكود التالي يأخذ صورة من النطاق E8:H10. أدناه صورة للورقة العمل الأصلية المستخدمة في الكود. يمكنك تجربة الكود مع أي ورقة عمل.

**الملف الداخلي**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)

تنفيذ الكود ينشئ صورة من النطاق E8:H10 فقط.

**صورة الناتج**

![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_2.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-ExportRangeofCells-1.java" >}}

قد تجد أيضا المقالة [تحويل ورقة العمل إلى تنسيقات صور مختلفة](/cells/ar/java/converting-worksheet-to-different-image-formats/) مفيدة.
{{< app/cells/assistant language="java" >}}
