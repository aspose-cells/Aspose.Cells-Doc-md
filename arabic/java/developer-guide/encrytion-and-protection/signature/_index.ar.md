---
title: تعيين والتحقق من صحة التوقيعات الرقمية
linktitle: إمضاء
type: docs
weight: 100
url: /ar/java/assign-and-validate-digital-signatures/
description: التوقيع الرقمي لملف Excel والتحقق منه. لحماية أصالة محتوى مصنف في ملف Excel ، يمكنك إضافة توقيع رقمي باستخدام رموز C# مع Aspose.Cells لـ .Net.
---
{{% alert color="primary" %}}

 يوفر التوقيع الرقمي ضمانًا بأن ملف المصنف صالح ولم يغيره أحد. يمكنك إنشاء توقيع رقمي شخصي باستخدام ملف**SELFCERT** أداة يتم شحنها مع Microsoft مجموعة Office أو أي أداة أخرى. يمكنك حتى شراء توقيع رقمي. بعد إنشاء توقيع رقمي أو الحصول عليه ، يجب إرفاقه بمصنفك. يشبه إرفاق التوقيع الرقمي ختم الظرف. إذا وصل مغلف مغلقًا ، فلديك بعض التأكيد على أنه لم يعبث أحد بمحتوياته.

 Aspose.Cells for Java API توفير[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) فصول لتوقيع جداول البيانات وكذلك التحقق من صحتها.

{{% /alert %}}

## **التوقيع على جداول البيانات**

تتطلب عملية التوقيع شهادة كما تمت مناقشته أعلاه. إلى جانب الشهادة ، يجب أن يكون لدى الشخص كلمة المرور الخاصة به لتوقيع جداول البيانات بنجاح باستخدام Aspose.Cells API.

يوضح مقتطف الكود التالي استخدام Aspose.Cells for Java API لتوقيع جدول بيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 في حالة عدم تطابق كلمة المرور المحددة مع كلمة المرور الخاصة بالشهادة ، يتم استثناء النوع*javax.crypto.BadPaddingException* سوف يتم إلقاؤها.

{{% /alert %}}

## **التحقق من صحة جداول البيانات**

يوضح مقتطف الكود التالي استخدام Aspose.Cells for Java API للتحقق من صحة جدول البيانات.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
