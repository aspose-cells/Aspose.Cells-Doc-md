---
title: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن
type: docs
weight: 920
url: /ar/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **سيناريوهات الاستخدام المحتملة**
توفر Aspose.Cells خاصية [OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)  التي يمكنك استخدامها للحصول على معرف الصف العائم أو تعيينه. معرفات فئة الكائنات العائمة هي في الواقع GUIDs، أي معرفات فريدة عالمياً. يبلغ طول GUID دائمًا 16 بايتًا، لذلك تكون معرفات الفئة أيضًا طولها 16 بايتًا. غالبًا ما توجد داخل سجل Windows وتوفر معلومات لتطبيق الاستضافة حول كيفية فتح كائن OLE عائم مضمن يحتوي على موارد مضمنة مختلفة داخل تطبيق العميل.
## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**
يوضح اللقطة الشاشة التالية معرف فئة الكائن العائم أي GUID الذي تم قراءته من [ملف إكسل عينة](5473378.xls) الذي يحتوي على كائن OLE عائم مضمّن لبرنامج تقديم الطاقة.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **الكود المثالي**
يرجى الاطلاع على الشفرة المصدرية المثالية المنفذة مع [ملف إكسل عينة](5473378.xls) وإخراجها في نافذة الأوامر والتي تطبع *معرف الصف العائم* أي GUID. يتطابق GUID المطبوع تمامًا مع ما هو موضح داخل اللقطة الشاشة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **مخرجات الوحدة**
هذا هو إخراج نافذة الأوامر للشفرة المصدرية أعلاه عند تنفيذها مع [ملف إكسل عينة](5473378.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
