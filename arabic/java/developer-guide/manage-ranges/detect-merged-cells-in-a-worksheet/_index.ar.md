---
title: كشف Cells مدمج في ورقة عمل
type: docs
weight: 3000
url: /ar/java/detect-merged-cells-in-a-worksheet/
---
{{% alert color="primary" %}}

في Microsoft Excel ، يمكن دمج عدة خلايا في خلية واحدة. غالبًا ما يستخدم هذا لإنشاء جداول معقدة أو لإنشاء خلية تحتوي على عنوان يمتد على عدة أعمدة.

Aspose.Cells يسمح لك بتعريف مساحات الخانات المدمجة في ورقة العمل. يمكنك إلغاء دمجهم أيضًا. توفر هذه المقالة أبسط سطور التعليمات البرمجية لأداء المهمة باستخدام Aspose.Cells.

توفر هذه المقالة إرشادات مضغوطة حول كيفية البحث عن الخلايا المدمجة ثم إلغاء دمجها في ورقة عمل.

{{% /alert %}}

## **برهنة**

 يستخدم هذا المثال قالب Microsoft ملف Excel يسمى**MergeTrial**. يحتوي على بعض مناطق الخلايا المدمجة في ورقة تسمى أيضًا تجربة الدمج.

**ملف القالب**

![ما يجب القيام به: image_بديل_نص](detect-merged-cells-in-a-worksheet_1.png)

 يوفر Aspose.Cells ملف[**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells)الطريقة التي يتم استخدامها للحصول على ArrayList من مناطق الخلايا المدمجة.

عندما يتم تنفيذ الكود أدناه ، فإنه يمسح محتويات الورقة ويفك جميع مناطق الخلايا قبل حفظ الملف مرة أخرى.

**ملف الإخراج**

![ما يجب القيام به: image_بديل_نص](detect-merged-cells-in-a-worksheet_2.png)

## **مثال رمز**

الرجاء مراجعة نموذج التعليمات البرمجية التالي لمعرفة كيفية تحديد مناطق الخلايا المدمجة في ورقة العمل وإلغاء دمجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **مقالات ذات صلة**

- [دمج الخلايا وتقسيمها](/cells/ar/java/merging-and-unmerging-cells/).
