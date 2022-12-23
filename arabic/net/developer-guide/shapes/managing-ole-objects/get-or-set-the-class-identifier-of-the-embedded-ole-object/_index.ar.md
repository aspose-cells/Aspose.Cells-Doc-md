---
title: الحصول على أو تعيين معرّف الفئة لكائن OLE المضمن
type: docs
weight: 200
url: /ar/net/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **سيناريوهات الاستخدام الممكنة**
 يوفر Aspose.Cells ملف[OleObject.ClassIdentifier](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/classidentifier)الخاصية التي يمكنك استخدامها للحصول على أو تعيين معرف الفئة لكائن أول مضمن. معرفات فئة كائن Ole هي في الواقع GUIDs مثل المعرفات الفريدة عالميًا. طول المعرف الفريد العمومي (GUID) دائمًا هو 16 بايت ، وبالتالي فإن معرفات الفئة تكون أيضًا بطول 16 بايت. غالبًا ما يتم العثور عليها داخل سجل Windows وتوفر معلومات لاستضافة التطبيق حول كيفية فتح كائن أول مضمن يحتوي على العديد من الموارد المضمنة داخل تطبيق العميل.
## **الحصول على أو تعيين معرّف الفئة لكائن OLE المضمن**
 تُظهر لقطة الشاشة التالية معرّف فئة كائن Ole ، أي GUID الذي تمت قراءته من ملف[نموذج ملف اكسل](5115190.xls) تحتوي على كائن أول PowerPoint المضمن.

![ما يجب القيام به: image_بديل_نص](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
### **عينة من الرموز**
 يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي تم تنفيذه باستخدام[نموذج ملف اكسل](5115190.xls)وإخراج وحدة التحكم الخاصة به والذي يطبع معرّف فئة Ole Object ie GUID. المعرف الفريد العمومي المطبوع هو نفسه تمامًا كما هو موضح في لقطة الشاشة.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSetClassIdentifierEmbedOleObject-GetSetClassIdentifierEmbedOleObject.cs" >}}
### **إخراج وحدة التحكم**
 هذا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه عند تنفيذه بامتداد[نموذج ملف اكسل](5115190.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
