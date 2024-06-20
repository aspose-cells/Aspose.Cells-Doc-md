---
title: تمكين مربع التحرير في GridWeb
type: docs
weight: 110
url: /ar/net/aspose-cells-gridweb/enable-gridweb-editbox/
keywords: GridWeb, editbox, شريط الصيغ
description: يقدم هذا المقال كيفية العمل مع شريط الصيغ أو مربع التحرير في GridWeb.
---

{{% alert color="primary" %}} 

قسم تحرير GridWeb (المعروف في Excel باسم شريط الصيغ) هو شريط أدوات يتم تقديمه في الجزء العلوي من عناصر التحكم يمكنك استخدامه لعرض قيمة أو إدخالها أو نسخ البيانات/الصيغة للخلية المركزة. كما يظهر اسم الخلية التي تقوم بتحريرها. بعد النقر على الإطار أو عند بدء كتابة البيانات أو إدخال علامة تساوي (=)، سيتم تنشيط قسم التحرير.

{{% /alert %}} 
## **ضبط قسم التحرير في Aspose.Cells.GridWeb**
يوفر عنصر تحكم GridWeb خاصية ShowCellEditBox التي يمكن للمطورين تعيينها على "True" لإظهار شريط الأدوات. القيمة الافتراضية للسمة هي False. عند تعيين قيمتها على "True"، سيظهر قسم التحرير في الجزء العلوي من عنصر تحكم GridWeb.

{{% alert color="primary" %}} 

To enable this feature, you need to import "jquery.js" file to your project and refer it in your .aspx page(s) to make it work. You may download the jQuery archive from <https://jqueryui.com/download/all/> and put the library file(s) into some folder in the project and add reference to the library file via <script> tag in your .aspx web form as following. All the latest jQuery versions are OK.

{{< highlight csharp >}}

 <head id="Head1" runat="server">

  <title>Untitled Page</title>

  <script type="text/javascript" src="/jquery/jquery.js"></script>

</head>



{{< /highlight >}}

{{% /alert %}} 

**عنصر تحكم GridWeb مع قسم التحرير** 

![todo:image_alt_text](enable-gridweb-editbox_1.png)
### **مثال**


{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-DisplayCellEditBox.aspx-DisplayCellEditBox.cs" >}}
