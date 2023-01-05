---
title: تفعيل GridWeb EditBox
type: docs
weight: 110
url: /ar/net/enable-gridweb-editbox/
---
{{% alert color="primary" %}} 

مربع تحرير GridWeb هو شريط أدوات يتم عرضه في الجزء العلوي من عنصر التحكم الذي يمكنك استخدامه لرؤية / إدخال البيانات / الصيغة أو نسخها إلى الخلايا. يعرض أيضًا اسم الخلية التي تقوم بتحريرها. بعد النقر فوق الإطار أو عند البدء في كتابة البيانات أو كتابة رمز يساوي (=) ، سيتم تنشيط مربع التحرير.

{{% /alert %}} 
## **ضبط مربع التحرير Aspose.Cells.GridWeb**
يوفر عنصر التحكم GridWeb خاصية ShowCellEditBox التي يمكن للمطورين تعيينها إلى "True" لجعل شريط الأدوات يعمل. القيمة الافتراضية للسمة هي False. عند تعيين قيمته إلى "True" ، سيظهر مربع التحرير أعلى عنصر تحكم GridWeb.

{{% alert color="primary" %}} 

 لتمكين هذه الميزة ، تحتاج إلى استيراد ملف "jquery.js" إلى مشروعك وإحالته في صفحة (صفحات) aspx الخاصة بك لجعله يعمل. يمكنك تنزيل أرشيف jQuery من<https://jqueryui.com/download/all/> ووضع ملف (ملفات) المكتبة في مجلد ما في المشروع وإضافة مرجع إلى ملف المكتبة عبر<script> علامة في نموذج الويب .aspx الخاص بك على النحو التالي. جميع إصدارات jQuery الأخيرة على ما يرام.

{{< highlight "csharp" >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**التحكم في GridWeb باستخدام مربع التحرير** 

![ما يجب القيام به: image_بديل_نص](enable-gridweb-editbox_1.png)
### **مثال**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
