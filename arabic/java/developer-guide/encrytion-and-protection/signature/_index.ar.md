---
title: تعيين والتحقق من التواقيع الرقمية
linktitle: توقيع
type: docs
weight: 100
url: /ar/java/assign-and-validate-digital-signatures/
description: توقيع ملف إكسل رقمي، التحقق. لحماية أصالة محتوى دفتر العمل في ملف إكسل، يمكنك إضافة توقيع رقمي باستخدام رموز C# مع Aspose.Cells لـ .Net.
---

{{% alert color="primary" %}}

يوفر التوقيع الرقمي الضمان بأن ملف ورق العمل صالح وأنه لم يقم أحد بتغييره. يمكنك إنشاء توقيع رقمي شخصي باستخدام أداة SELFCERT المرفقة مع حزمة Microsoft Office أو أي أداة أخرى. يمكنك حتى شراء توقيع رقمي. بعد إنشاء التوقيع الرقمي، يجب عليك إرفاقه بورق العمل الخاص بك. إرفاق توقيع رقمي مشابه لختم ظرف. إذا وصل ظرف مختوم، فإنك تمتلك بعض مستوى الضمان بأن لم يقم أحد بتلاعب محتوياته.

توفر واجهة برمجة التطبيق Aspose.Cells for Java الفئات [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) و [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) لتوقيع جداول البيانات بالإضافة إلى التحقق منها.

{{% /alert %}}

## **توقيع جداول البيانات**

يتطلب عملية التوقيع شهادة كما تم مناقشته أعلاه. إلى جانب الشهادة، يجب على الشخص أيضًا أن يكون لديه كلمة مرور لتوقيع جداول البيانات بنجاح باستخدام واجهة برمجة التطبيق Aspose.Cells.

يوضح مقتطف الكود التالي استخدام واجهة برمجة التطبيق Aspose.Cells for Java لتوقيع جدول بيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

في حالة عدم تطابق كلمة المرور المحددة مع كلمة المرور الخاصة بالشهادة، سيتم إثارة استثناء من نوع *javax.crypto.BadPaddingException*.

{{% /alert %}}

## **التحقق من جداول البيانات**

يوضح مقتطف الكود التالي استخدام واجهة برمجة التطبيق Aspose.Cells for Java للتحقق من جدول البيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}
