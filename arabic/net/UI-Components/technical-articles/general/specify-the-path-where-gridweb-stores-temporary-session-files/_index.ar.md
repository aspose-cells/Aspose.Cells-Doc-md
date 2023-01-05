---
title: حدد المسار حيث يقوم GridWeb بتخزين ملفات الجلسة المؤقتة
type: docs
weight: 50
url: /ar/net/specify-the-path-where-gridweb-stores-temporary-session-files/
---
{{% alert color="primary" %}} 

عندما يكون وضع جلسة GridWeb هو ViewState ، فإنه يخزن ملفات الجلسة المؤقتة داخل دليل قاعدة التطبيق. في بعض الأحيان ، لا بأس من تخزين ملفات الجلسات المؤقتة هناك لأن Application Base Directory قد لا يكون لديه أذونات الكتابة عليه. في مثل هذه الحالات ، يطرح GridWeb مثل هذا الاستثناء

{{< highlight "java" >}}

 [UnauthorizedAccessException: Access to

the path 'D:\inetpub\wwwroot\AsposeExcelTest\gwb_tempGridWeb1' is denied.]{{< /highlight >}}

الحل للمشكلة أعلاه هو منح حق الوصول للكتابة إلى Application Base Directory أو تغيير مسار ملفات جلسة GridWeb المؤقتة التي لها حق الوصول للكتابة باستخدام خاصية GridWeb.SessionStorePath. يجب أن يكون هذا المسار متعلقًا بـ Application Base Directory.

{{% /alert %}} 
## **حدد المسار حيث يقوم GridWeb بتخزين ملفات الجلسة المؤقتة**
يحدد نموذج التعليمات البرمجية التالي المسار حيث يخزن GridWeb ملفات جلسة العمل المؤقتة.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Articles-SpecifySessionStorePath.aspx-SpecifySessionStorePath.cs" >}}
