---
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells
type: docs
weight: 70
url: /ar/java/convert-text-to-columns-using-aspose-cells/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تحويل نصك إلى أعمدة باستخدام Microsoft Excel. تتوفر هذه الميزة من *Data Tools* في علامة التبويب *Data*. من أجل تقسيم محتوى العمود إلى عدة أعمدة, يجب أن يحتوي البيانات على فاصل محدد مثل فاصلة (أو أي حرف آخر) بناءً على الذي يقوم Microsoft Excel بتقسيم محتوى الخلية إلى خلايا متعددة. توفر Aspose.Cells أيضا هذه الميزة من خلال [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) طريقة.
## **تحويل النص إلى أعمدة باستخدام Aspose.Cells**
يشرح الكود النموذجي التالي استخدام طريقة [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)). يضيف الكود أولاً أسماء بعض الأشخاص في العمود أ من الورقة العمل الأولى. الاسم الأول والأخير منفصلان بحرف مسافة. ثم يطبق طريقة [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns\(int,%20int,%20int,%20com.aspose.cells.TxtLoadOptions\)) على العمود أ ويحفظه كملف إكسيل الناتج. إذا قمت بفتح [ملف الإكسيل الناتج](25395230.xlsx), سترى أن الأسماء الأولى في العمود أ بينما الأسماء الأخيرة في العمود ب كما هو موضح في هذه اللقطة.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
