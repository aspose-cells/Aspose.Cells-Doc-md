---
title: اكتشاف ما إذا كان المشروع VBA محميًا
type: docs
weight: 80
url: /ar/java/find-out-if-vba-project-is-protected/
---

## **سيناريوهات الاستخدام المحتملة**
يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف Excel الخاص بك محميًا أم لا باستخدام [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) الطريقة
## **الكود المثالي**
الكود العيني التالي ينشئ دفتر عمل ثم يتحقق مما إذا كان مشروع VBA محميًا أم لا. ثم يحمي مشروع VBA ويتحقق مرة أخرى مما إذا كان مشروع VBA محميًا أم لا. يُرجى الرجوع إلى الإخراج في وحدة التحكم كمرجع. قبل الحماية، [VbaProject.isProtected()](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#IsProtected) تعيد **false** ولكن بعد الحماية، تعيد **true**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-WorkbookVBAProject-FindoutifVBAProjectisProtected.java" >}}
## **مخرجات الوحدة**
هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

 IsProtected - Before Protecting VBA Project: false

IsProtected - After Protecting VBA Project: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
