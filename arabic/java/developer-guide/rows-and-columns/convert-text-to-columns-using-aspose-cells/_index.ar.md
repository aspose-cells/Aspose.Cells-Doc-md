---
title: تحويل النص إلى أعمدة باستخدام Aspose.Cells
type: docs
weight: 70
url: /ar/java/convert-text-to-columns-using-aspose-cells/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك تحويل النص إلى أعمدة باستخدام Microsoft Excel. تتوفر هذه الميزة من خلال *Data Tools* تحت علامة التبويب *Data*. لتقسيم محتويات العمود إلى عدة أعمدة، يجب أن تحتوي البيانات على فاصل معين مثل فاصلة (أو أي حرف آخر) بناءً عليه يقسم Microsoft Excel محتويات الخلية إلى عدة خلايا. كما يوفر Aspose.Cells هذه الميزة عبر طريقة [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-).
## **تحويل النص إلى أعمدة باستخدام Aspose.Cells**
يوضح رمز العينة التالي استخدام طريقة [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-). يضيف الكود أولاً أسماء بعض الأشخاص في العمود أ من الورقة الأولى. يتم فصل الاسم الأول واسم العائلة بفاصلة. ثم يطبق طريقة [TextToColumns](https://reference.aspose.com/cells/java/com.aspose.cells/cells#textToColumns-int-int-int-com.aspose.cells.TxtLoadOptions-) على العمود أ ويحفظه كملف إكسل إخراج. إذا فتحت ملف الإكسل الإخراجي، سترى أن الأسماء الأولى في العمود أ واسم العائلة في العمود ب كما هو موضح في هذا لقطة الشاشة.

![todo:image_alt_text](convert-text-to-columns-using-aspose-cells_1.png)
## **الكود المثالي**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-rows_cloumns-ConvertTexttoCols-ConvertTexttoCols.java" >}}
{{< app/cells/assistant language="java" >}}
