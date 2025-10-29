---
title: اكتشاف ما إذا كان المشروع VBA محميًا
type: docs
weight: 20
url: /ar/python-net/find-out-if-vba-project-is-protected/
---

## **اكتشاف ما إذا كان مشروع VBA محميًا في بايثون**

يمكنك معرفة ما إذا كان مشروع VBA (التطبيقات المرئية لبايثون) الخاص بملف إكسل الخاص بك محميًا أم لا باستخدام Aspose.Cells لبايثون via .NET باستخدام الخاصية [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected).

## **الكود المثالي**

الرمز العيني التالي ينشئ عملاق عمل ثم يتحقق ما إذا كان مشروعه VBA محميًا أم لا. ثم يحمي مشروع VBA ويتحقق مرة أخرى ما إذا كان مشروعه VBA محميًا أم لا. يرجى الرجوع إلى إخراجها للمرجع. قبل الحماية، [**VbaProject.is_protected**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_protected) يرجع **false** ولكن بعد الحماية، يرجع **true**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FindoutifVBAProjectisProtected.py" >}}

## **مخرجات الوحدة**

هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
