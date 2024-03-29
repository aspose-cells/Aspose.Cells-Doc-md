---
title: تعيين حدود النطاق
type: docs
weight: 600
url: /ar/java/set-range-border/
---
##  **سيناريوهات الاستخدام الممكنة**
عندما تريد تعيين الحدود لـ Range ، فلن تحتاج إلى تعيين كل خلية على حدة. يمكنك ضبط الحدود على النطاق. يقدم Aspose.Cells هذه الميزة.
توفر هذه المقالة نموذج التعليمات البرمجية الذي يستخدم Aspose.Cells لتعيين حدود النطاق.

##  **تعيين حدود النطاق في Excel**
لتعيين حد النطاق في Excel ، يمكنك اتباع الخطوات التالية:
1. حدد نطاق الخلايا الذي تريد تطبيق الحد عليه.
2. في علامة التبويب "الصفحة الرئيسية" على الشريط ، حدد موقع مجموعة "الخط".
3. ضمن مجموعة "الخط" ، انقر على زر القائمة المنسدلة "الحدود".
<br>
<img src="border.png" />
4. اختر نوع الحد الذي تريد تطبيقه من الخيارات في القائمة المنسدلة. يمكنك الاختيار من بين أنماط الحدود المحددة مسبقًا أو تخصيص حدودك الخاصة.
5. بمجرد تحديد نمط الحدود المطلوب ، سيتم تطبيق الحد على نطاق الخلايا المحدد.

##  **قم بتعيين حدود النطاق باستخدام Aspose.Cells**
يوضح هذا المثال كيفية:

1. قم بإنشاء مصنف.
1. أضف البيانات إلى الخلايا في ورقة العمل الأولى.
1.  إنشاء[**يتراوح**](https://reference.aspose.com/cells/java/com.aspose.cells/range/).
1. تعيين الحد الداخلي للمدى.
1. تعيين الحد الخارجي للنطاق.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Range-set-border.java" >}}