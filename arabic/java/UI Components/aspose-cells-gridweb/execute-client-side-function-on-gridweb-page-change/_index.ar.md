---
title: تنفيذ وظيفة جانب العميل عند تغيير صفحة GridWeb
type: docs
weight: 70
url: /ar/java/execute-client-side-function-on-gridweb-page-change/
---
## **سيناريوهات الاستخدام الممكنة**
تحتاج أحيانًا إلى تنفيذ وظيفة جانب العميل عندما تتغير صفحة GridWeb. Aspose.Cells.GridWeb يوفر خاصية OnPageChangeClientFunction لهذا الغرض. يرجى تعيين هذه الخاصية مع وظيفة جانب العميل التي تريد تنفيذها.
## **تنفيذ وظيفة جانب العميل عند تغيير صفحة GridWeb**
يشرح كود جافا التالي كيفية الاستفادة من خاصية GridWebBean.setOnPageChangeClientFunction (). يقوم بتعيين الخاصية مع وظيفة جانب العميل المسماة MyOnPageChange. يرجى ملاحظة أن هذه الخاصية صالحة فقط إذا قمت بتمكين الترحيل مثل GridWebBean.setEnablePaging (صواب). الآن ، كلما قمت بتغيير صفحة GridWeb ، فسوف تستدعي وظيفة جانب العميل MyOnPageChange التي تطبع**فهرس الصفحة الحالية** على ال**وحدة التحكم** كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](execute-client-side-function-on-gridweb-page-change_1.png)
## **عينة من الرموز**
هذا هو رمز وظيفة جانب العميل MyOnPageChange التي سيتم تنفيذها بسبب هذا السطر مثل Gridweb.setOnPageChangeClientFunction ("MyOnPageChange") ؛

{{< highlight "java" >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

توضح التعليمات البرمجية التالية كيفية تمكين الترحيل وتعيين خاصية OnPageChangeClientFunction.

{{< highlight "java" >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
