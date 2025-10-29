---
title: الحصول أو تعيين معرف الفئة للكائن OLE المدمج باستخدام Golang عبر C++
linktitle: الحصول على أو تعيين معرف الفئة لكائن Ole المضمن
type: docs
weight: 200
url: /ar/go-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: تعلم كيفية الحصول على أو تعيين معرف فئة كائنات OLE المضمنة باستخدام Aspose.Cells مع Golang عبر C++.
---

## **سيناريوهات الاستخدام المحتملة**
توفر Aspose.Cells الخاصية [OleObject.GetClassIdentifier()](https://reference.aspose.com/cells/go-cpp/oleobject/getclassidentifier/) التي يمكنك استخدامها للحصول على أو تعيين معرف فئة كائن OLE المضمن. معرفات فئة كائن OLE هي في الواقع معرفات GUID، أي معرفات فريدة من نوعها على مستوى العالم. GUID دائمًا يكون بطول 16 بايت، لذلك فإن معرفات الفئة أيضًا تكون بطول 16 بايت. غالبًا ما توجد داخل سجل Windows وتوفر معلومات للتطبيق المضيف حول كيفية فتح كائنات OLE المضمنة التي تحتوي على موارد مضمنة مختلفة داخل تطبيق العميل.

## **الحصول على معرف الفئة الخاص بكائن OLE المضمّن أو تعيينه**
يعرض لقطة الشاشة التالية معرف فئة كائن OLE، أي GUID، الذي تم قراءته من [ملف إكسل نموذجي](5115190.xls) يحتوي على كائن PowerPoint OLE مدمج.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)

### **الكود المثالي**
يرجى الاطلاع على رمز المثال المرفق الذي تم تنفيذه باستخدام [ملف إكسل النموذجي](5115190.xls) وإخراجه في وحدة التحكم مع طباعة معرف فئة الكائن OLE، أي GUID. GUID المطبوع هو نفسه تمامًا كما هو موضح داخل لقطة الشاشة.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetOrSetTheClassIdentifierOfTheEmbeddedOleObject.go" >}}
### **مخرجات الوحدة**
هذه هي إخراج وحدة التحكم للرمز العينية أعلاه عند تنفيذه بملف إكسل [مثالي] (5115190.xls).

{{< highlight java >}}
DC020317-E6E2-4A62-B9FA-B3EFE16626F4
{{< /highlight >}}
