---
title: تنفيذ وظيفة جانب العميل عند تغيير صفحة GridWeb
type: docs
weight: 140
url: /ar/net/execute-client-side-function-on-gridweb-page-change/
---
## **سيناريوهات الاستخدام الممكنة**
تحتاج أحيانًا إلى تنفيذ وظيفة جانب العميل عندما تتغير صفحة GridWeb. Aspose.Cells.GridWeb يوفر خاصية OnPageChangeClientFunction لهذا الغرض. يرجى تعيين هذه الخاصية مع وظيفة جانب العميل التي تريد تنفيذها.
## **تنفيذ وظيفة جانب العميل عند تغيير صفحة GridWeb**
يشرح علامة aspx التالية كيفية الاستفادة من خاصية OnPageChangeClientFunction. يقوم بتعيين الخاصية مع وظيفة جانب العميل المسماة MyOnPageChange. يرجى ملاحظة أن هذه الخاصية صالحة فقط إذا قمت بتمكين الترحيل ، مثل EnablePaging = "true". الآن ، كلما قمت بتغيير صفحة GridWeb ، فسوف تستدعي وظيفة جانب العميل MyOnPageChange التي تطبع**فهرس الصفحة الحالية** على ال**وحدة التحكم** كما هو موضح في لقطة الشاشة هذه.

![ما يجب القيام به: image_بديل_نص](execute-client-side-function-on-gridweb-page-change_1.png)
## **عينة من الرموز**
هذا هو رمز دالة جانب العميل MyOnPageChange التي سيتم تنفيذها بسبب إعداد OnPageChangeClientFunction = خاصية "MyOnPageChange" في GridWeb. هذا هو توصيف صفحة aspx كاملة.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples.GridWeb-CSharp-GridWebBasics-CallClientsideScriptforGridWeb.aspx-CallClientsideScriptforGridWeb.cs" >}}
