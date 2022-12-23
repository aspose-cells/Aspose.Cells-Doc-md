---
title: اكتشف ما إذا كان VBA Project محميًا
type: docs
weight: 20
url: /ar/net/find-out-if-vba-project-is-protected/
---
## **اكتشف ما إذا كان VBA Project محميًا في C#**

 يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف Excel الخاص بك محميًا أم لا باستخدام Aspose.Cells[**VbaProject. محمي**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected)خاصية.

## **عينة من الرموز**

نموذج التعليمات البرمجية التالي بإنشاء مصنف ثم ثم يتحقق ما إذا كان مشروع VBA الخاص به محميًا أم لا. ثم يحمي مشروع VBA ويتحقق مرة أخرى مما إذا كان مشروع VBA محميًا أم لا. يرجى الاطلاع على إخراج وحدة التحكم الخاصة به كمرجع. قبل الحماية ،[**VbaProject. محمي**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isprotected) عائدات**خاطئة** ولكن بعد الحماية ، يعود**حقيقي**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookVBAProject-FindoutifVBAProjectisProtected.cs" >}}

## **إخراج وحدة التحكم**

هذا هو إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه كمرجع.

{{< highlight "java" >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}
