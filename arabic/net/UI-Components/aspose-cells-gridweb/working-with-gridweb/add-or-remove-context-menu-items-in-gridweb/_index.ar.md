---
title: إضافة أو إزالة عناصر قائمة السياق في GridWeb
type: docs
weight: 130
url: /ar/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

يمكنك إضافة عناصر قائمة السياق باستخدام ترميز ASP.NET أو باستخدام كود .NET. يمكنك أيضًا إزالة عناصر قائمة السياق باستخدام كود .NET. الرجاء استخدام GridWeb.CustomCommandButtons.Add () و GridWeb.CustomCommandButtons.Remove () أو RemoveAt () لهذه الأغراض.

{{% /alert %}} 
## **إضافة عنصر قائمة السياق باستخدام توصيف ASP.NET**
تضيف علامة ASP.NET التالية عنصر قائمة السياق في GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



هنا هو ترميز ASP.NET الكامل الذي ينشئ GridWeb مع عنصر قائمة السياق أعلاه. يرجى ملاحظة السمة OnCustomCommand = "GridWeb1_CustomCommand". إنه اسم معالج الحدث الذي سيتم استدعاؤه عند النقر فوق عنصر قائمة السياق.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



هذا هو شكل عنصر قائمة السياق بعد إضافته باستخدام ترميز ASP.NET أعلاه.

![ما يجب القيام به: image_بديل_نص](add-or-remove-context-menu-items-in-gridweb_1.png)

هذا هو رمز معالج الحدث الذي يتم تنفيذه عند النقر فوق عنصر قائمة السياق. يتحقق الرمز أولاً من اسم الأمر ، إذا كان يطابق الأمر الخاص بنا ، فإنه يضيف نصًا في الخلية A1 من ورقة عمل GridWeb النشطة ويعين عرض العمود الأول إلى 40 وحدة لجعل النص مرئيًا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


هذه هي الطريقة التي يبدو بها GridWeb عند النقر فوق عنصر قائمة السياق.

![ما يجب القيام به: image_بديل_نص](add-or-remove-context-menu-items-in-gridweb_2.png)
## **أضف عناصر قائمة السياق في Aspose.Cells.GridWeb باستخدام التعليمات البرمجية**
يوضح هذا الرمز كيفية إضافة عنصر قائمة السياق داخل GridWeb باستخدام التعليمات البرمجية.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **قم بإزالة عناصر قائمة السياق في Aspose.Cells.GridWeb باستخدام التعليمات البرمجية**
يوضح هذا الرمز كيفية إزالة عنصر قائمة السياق باستخدام أساليب CustomCommandButtons.Remove () و CustomCommandButtons.RemoveAt ().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
