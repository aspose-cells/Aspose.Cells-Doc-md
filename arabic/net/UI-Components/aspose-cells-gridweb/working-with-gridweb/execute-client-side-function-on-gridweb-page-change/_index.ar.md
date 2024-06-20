---
title: تنفيذ وظيفة العميل على تغيير صفحة GridWeb
type: docs
weight: 140
url: /ar/net/aspose-cells-gridweb/execute-client-side-function-on-gridweb-page-change/
keywords: GridWeb,client,js,javascript,function
description: يقدم هذا المقال كيفية العمل مع وظيفة js العميل في GridWeb.
---

## **سيناريوهات الاستخدام المحتملة**
في بعض الأحيان تحتاج إلى تنفيذ وظيفة العميل الخاصة بك عند تغيير صفحة GridWeb. يوفر Aspose.Cells.GridWeb خاصية OnPageChangeClientFunction لهذا الغرض. يرجى تعيين هذه الخاصية بوظيفة العميل التي تود تنفيذها.
## **تنفيذ وظيفة العميل على تغيير صفحة GridWeb**
يشرح العلامة التجارية aspx التالية كيفية الاستفادة من خاصية OnPageChangeClientFunction. يقوم بتعيين الخاصية بوظيفة العميل بالاسم MyOnPageChange. يرجى ملاحظة أن هذه الخاصية صالحة فقط إذا كنت قد قمت بتمكين التصفح أي EnablePaging="true". الآن، كلما قمت بتغيير صفحة GridWeb، سيقوم بعرض وظيفة العميل MyOnPageChange التي تطبع **فهرس الصفحة الحالية** على **الوحدة** كما هو موضح في هذا اللقطة الشاشة.

![todo:image_alt_text](execute-client-side-function-on-gridweb-page-change_1.png)
## **الكود المثالي**
هذا هو كود وظيفة العميل MyOnPageChange التي سيتم تنفيذها بسبب تعيين خاصية OnPageChangeClientFunction ="MyOnPageChange" في GridWeb. هذه هي العلامة التجارية الكاملة لصفحة aspx.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
