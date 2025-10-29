---  
title: اكتشف ما إذا كان مشروع VBA محميًا باستخدام Golang عبر C++  
linktitle: اكتشاف ما إذا كان المشروع VBA محميًا  
type: docs  
weight: 20  
url: /ar/go-cpp/find-out-if-vba-project-is-protected/  
description: تحقق مما إذا كان مشروع VBA في ملف Excel محميًا باستخدام Aspose.Cells مع Golang عبر C++  
---  

## **اكتشف إذا ما كان مشروع VBA محميًا في C++**

يمكنك معرفة ما إذا كان مشروع VBA (تطبيقات Visual Basic) لملف إكسل الخاص بك محميًا أم لا باستخدام Aspose.Cells property [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/).

## **الكود المثالي**

يقوم الرمز العملي التالي بإنشاء دفتر عمل ثم يتحقق مما إذا كان مشروع VBA محميًا أم لا. ثم يقوم بحماية مشروع VBA ويعيد التحقق مما إذا كان محميًا أم لا. يرجى مراجعة الناتج في وحدة التحكم كمرجع. قبل الحماية، يعيد [**VbaProject.IsProtected**](https://reference.aspose.com/cells/go-cpp/vbaproject/isprotected/) القيمة **خطأ** ولكن بعد الحماية، يعيد القيمة **صحيح**.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FindOutIfVbaProjectIsProtected.go" >}}
## **مخرجات الوحدة**

هذا هو إخراج المجموعة الخرجية للرمز العيني أعلاه للمرجع.

{{< highlight java >}}

IsProtected - Before Protecting VBA Project: False

IsProtected - After Protecting VBA Project: True

{{< /highlight >}}  
