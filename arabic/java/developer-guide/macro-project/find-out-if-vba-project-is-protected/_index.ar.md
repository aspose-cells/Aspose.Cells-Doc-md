---
title: اكتشف ما إذا كان VBA Project محميًا
type: docs
weight: 80
url: /ar/java/find-out-if-vba-project-is-protected/
---
## **سيناريوهات الاستخدام الممكنة**
 يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف Excel الخاص بك محميًا أم لا باستخدام Aspose.Cells[VbaProject.isProtected ()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected)طريقة
## **عينة من الرموز**
 نموذج التعليمات البرمجية التالي بإنشاء مصنف ثم ثم يتحقق ما إذا كان مشروع VBA الخاص به محميًا أم لا. ثم يحمي مشروع VBA ويتحقق مرة أخرى مما إذا كان مشروع VBA محميًا أم لا. يرجى الاطلاع على إخراج وحدة التحكم الخاصة به كمرجع. قبل الحماية ،[VbaProject.isProtected ()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) عائدات**خاطئة** ولكن بعد الحماية ، يعود**حقيقي**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **إخراج وحدة التحكم**
هذا هو إخراج وحدة التحكم لعينة التعليمات البرمجية أعلاه كمرجع.

{{< highlight "java" >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
