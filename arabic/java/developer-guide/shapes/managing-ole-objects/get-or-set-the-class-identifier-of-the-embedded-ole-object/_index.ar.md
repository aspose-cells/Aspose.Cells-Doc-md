---
title: الحصول على أو تعيين معرّف الفئة لكائن OLE المضمن
type: docs
weight: 920
url: /ar/java/get-or-set-the-class-identifier-of-the-embedded-ole-object/
---
## **سيناريوهات الاستخدام الممكنة**
 يوفر Aspose.Cells ملف[OleObject.ClassIdentifier](https://reference.aspose.com/cells/java/com.aspose.cells/oleobject#ClassIdentifier)الخاصية التي يمكنك استخدامها للحصول على معرف الفئة لكائن أول مضمن أو تعيينه. معرفات فئة كائن Ole هي في الواقع GUIDs مثل المعرفات الفريدة عالميًا. طول المعرف الفريد العمومي (GUID) دائمًا هو 16 بايت ، وبالتالي فإن معرفات الفئة تكون أيضًا بطول 16 بايت. غالبًا ما يتم العثور عليها داخل سجل Windows وتوفر معلومات لاستضافة التطبيق حول كيفية فتح كائن أول مضمن يحتوي على العديد من الموارد المضمنة داخل تطبيق العميل.
## **الحصول على أو تعيين معرّف الفئة لكائن OLE المضمن**
 تُظهر لقطة الشاشة التالية معرّف فئة كائن Ole ، أي GUID الذي تمت قراءته من ملف[نموذج ملف اكسل](5473378.xls) تحتوي على كائن أول PowerPoint المضمن.

![ما يجب القيام به: image_بديل_نص](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)
## **عينة من الرموز**
 يرجى الاطلاع على نموذج التعليمات البرمجية التالي الذي تم تنفيذه باستخدام[نموذج ملف اكسل](5473378.xls) وإخراج وحدة التحكم الخاصة به الذي يطبع ملف*معرف الفئة*من Ole Object أي GUID. المعرف الفريد العمومي المطبوع هو نفسه تمامًا كما هو موضح في لقطة الشاشة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetSettheClassIdentifier-GetSettheClassIdentifier.java" >}}
## **إخراج وحدة التحكم**
 هذا هو إخراج وحدة التحكم لنموذج التعليمات البرمجية أعلاه عند تنفيذه بامتداد[نموذج ملف اكسل](5473378.xls).

{{< highlight "java" >}}

 DC020317-E6E2-4A62-B9FA-B3EFE16626F4

{{< /highlight >}}
