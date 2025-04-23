---
title: اكتشاف ما إذا كان المشروع VBA محميًا
type: docs
weight: 20
url: /ar/net/find-out-if-vba-project-is-protected/
---

## **اكتشاف ما إذا كان المشروع VBA محميًا في C#**

يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف Excel الخاص بك محميًا أم لا باستخدام خاصية [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) في Aspose.Cells.

## **الكود المثالي**

الرمز العيني التالي ينشئ عملاق عمل ثم يتحقق ما إذا كان مشروعه VBA محميًا أم لا. ثم يحمي مشروع VBA ويتحقق مرة أخرى ما إذا كان مشروعه VBA محميًا أم لا. يرجى الرجوع إلى إخراجها للمرجع. قبل الحماية، [**VbaProject.IsProtected**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) يرجع **false** ولكن بعد الحماية، يرجع **true**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **مخرجات الوحدة**

هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
