---
title: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن
type: docs
weight: 200
url: /ar/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **سيناريوهات الاستخدام المحتملة**
يوفر Aspose.Cells خاصية [OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier) التي يمكنك استخدامها للحصول على أو ضبط معرف الفئة لكائن OLE المضمن. معرفات فصيلة كائنات OLE هي في الواقع GUIDs أي معرفات الوحدة الفريدة عالميًا. ويتكون GUID دائمًا من 16 بايتًا، ولذلك فإن معرفات الفئة هي أيضًا بطول 16 بايتًا. غالبًا ما تُستخدم داخل سجل Windows وتوفر معلومات لتطبيق المضيف حول كيفية فتح كائن OLE المضمن الذي يحتوي على موارد مضمنة مختلفة داخل تطبيق العميل.
## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**
الصورة المصغرة التالية تظهر معرف فئة كائن Ole أي GUID الذي تم قراءته من [ملف الإكسل العيني](5115190.xls) الذي يحتوي على كائن Ole مضمن PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **الكود المثالي**
يرجى رؤية الرمز المصدري المعاين المنفذ مع [ملف الإكسل العيني العيني](5115190.xls) ومخرجات الوحدة التي تطبع معرف الفئة الخاص بـ كائن Ole أي GUID. الGUID المُطبوع مطابق تمامًا لما هو موضح داخل الصورة المصغرة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **مخرجات الوحدة**
هذه هي إخراج وحدة التحكم للرمز العينية أعلاه عند تنفيذه بملف إكسل [مثالي] (5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
