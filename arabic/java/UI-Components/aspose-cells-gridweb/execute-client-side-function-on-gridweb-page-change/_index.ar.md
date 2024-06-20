---
title: تنفيذ وظيفة العميل على تغيير صفحة GridWeb
type: docs
weight: 70
url: /ar/java/execute-client-side-function-on-gridweb-page-change/
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان تحتاج إلى تنفيذ وظيفة العميل الخاصة بك عند تغيير صفحة GridWeb. يوفر Aspose.Cells.GridWeb خاصية OnPageChangeClientFunction لهذا الغرض. يرجى تعيين هذه الخاصية بوظيفة العميل التي تود تنفيذها.
## **تنفيذ وظيفة العميل على تغيير صفحة GridWeb**
الكود Java التالي يشرح كيفية الاستفادة من خاصية GridWebBean.setOnPageChangeClientFunction(). يقوم بتعيين الخاصية بوظيفة جانب العميل بالاسم MyOnPageChange. يرجى ملاحظة، هذه الخاصية صالحة فقط إذا قمت بتمكين التصفح أي GridWebBean.setEnablePaging(true). الآن، كلما قمت بتغيير صفحة GridWeb، سيتم استدعاء وظيفة جانب العميل MyOnPageChange التي تطبع **فهرس الصفحة الحالي** على **وحدة التحكم** كما هو موضح في هذا اللقطة.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **الكود المثالي**
هذا هو كود وظيفة العميل MyOnPageChange التي ستتم تنفيذها بسبب هذا السطر Gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< highlight java >}}

 function MyOnPageChange(index) {

	console.log("current page is:" + (index+1));

}

{{< /highlight >}}

الكود التالي يشرح كيفية تمكين التصفح وتعيين خاصية OnPageChangeClientFunction.

{{< highlight java >}}

 GridWebBean gridweb=BeanManager.getBean(request);

gridweb.setEnablePaging(true);

gridweb.setOnPageChangeClientFunction("MyOnPageChange");

{{< /highlight >}}
