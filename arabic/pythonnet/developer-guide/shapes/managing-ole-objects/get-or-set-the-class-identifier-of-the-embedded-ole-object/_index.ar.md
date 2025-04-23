---
title: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن
type: docs
weight: 200
url: /ar/python-net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---

## **سيناريوهات الاستخدام المحتملة**
 توفر Aspose.Cells لـ Python via .NET الخاصية [OleObject.class_identifier](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/class_identifier) التي يمكنك استخدامها للحصول على أو تعيين معرف الفئة لكائن OLE المدمج. معرف فئة OLE هو في الواقع GUID، أي معرف فريد عالميًا. دائمًا ما يكون GUID بطول 16 بايت، لذا فإن معرفات الفئة تكون أيضًا بطول 16 بايت. وغالبًا ما توجد داخل سجل Windows وتوفر معلومات لتطبيق المضيف حول كيفية فتح عنصر OLE المضمن الذي يحتوي على موارد متعددة مضمنة داخل التطبيق العميل.

## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**
الصورة المصغرة التالية تظهر معرف فئة كائن Ole أي GUID الذي تم قراءته من [ملف الإكسل العيني](5115190.xls) الذي يحتوي على كائن Ole مضمن PowerPoint.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **الكود المثالي**
يرجى رؤية الرمز المصدري المعاين المنفذ مع [ملف الإكسل العيني العيني](5115190.xls) ومخرجات الوحدة التي تطبع معرف الفئة الخاص بـ كائن Ole أي GUID. الGUID المُطبوع مطابق تمامًا لما هو موضح داخل الصورة المصغرة.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-GetSetClassIdentifierEmbedOleObject.py" >}}

### **مخرجات الوحدة**
هذه هي إخراج وحدة التحكم للرمز العينية أعلاه عند تنفيذه بملف إكسل [مثالي] (5115190.xls).

{{< highlight java >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
