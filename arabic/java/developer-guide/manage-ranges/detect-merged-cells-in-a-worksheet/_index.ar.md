---
title: الكشف عن الخلايا المدمجة في ورقة البيانات
type: docs
weight: 3000
url: /ar/java/detect-merged-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

في Microsoft Excel، يمكن دمج عدة خلايا في خلية واحدة. يُستخدم هذا غالبًا لإنشاء جداول معقدة أو لإنشاء خلية تحتوي على عنوان يمتد عبر عدة أعمدة.

تتيح Aspose.Cells لك التعرف على مناطق الخلايا المدمجة في ورقة البيانات. يمكنك أيضًا إلغاء دمجها. يوفر هذا المقال أبسط الأسطر لأداء المهمة باستخدام Aspose.Cells.

يقدم هذا المقال تعليمات موجزة حول كيفية العثور ثم إلغاء دمج الخلايا في ورقة البيانات.

{{% /alert %}}

## **عرض**

يستخدم هذا المثال ملف Microsoft Excel قالبي يسمى **تجربة الدمج**. يحتوي على بعض مناطق الخلايا المدمجة في ورقة تسمى أيضًا تجربة الدمج.

**ملف القالب**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_1.png)

يوفر Aspose.Cells الطريقة [**Cells.getMergedCells**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#MergedCells) التي تُستخدم للحصول على ArrayList من مناطق الخلايا المدمجة.

عند تنفيذ الكود أدناه، يُمسح محتوى الورقة ويُلغى دمج كل مناطق الخلايا قبل حفظ الملف مرة أخرى.

**ملف الإخراج**

![todo:image_alt_text](detect-merged-cells-in-a-worksheet_2.png)

## **مثال الكود**

يرجى الاطلاع على الكود النموذجي التالي لمعرفة كيفية التعرف على مناطق الخلايا المدمجة في ورقة البيانات وإلغاء دمجها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-DetectMergedCells-DetectMergedCells.java" >}}

## **مقالات ذات صلة**

- [دمج وتقسيم الخلايا](/cells/ar/java/merging-and-unmerging-cells/).
