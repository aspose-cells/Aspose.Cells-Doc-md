---
title: إضافة أو إزالة عناصر القائمة السياقية في GridWeb
type: docs
weight: 130
url: /ar/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb, contextmenu, menu
description: يقدم هذا المقال كيفية إضافة أو إزالة عناصر القائمة السياقية في GridWeb.
---

{{% alert color="primary" %}} 

يمكنك إضافة عناصر قائمة السياق باستخدام علامات ASP.NET أو باستخدام رمز .NET. يمكنك أيضًا إزالة عناصر قائمة السياق باستخدام رمز .NET. يرجى استخدام GridWeb.CustomCommandButtons.Add() و GridWeb.CustomCommandButtons.Remove() أو الأساليب RemoveAt() لهذه الأغراض.

{{% /alert %}} 
## **إضافة عنصر قائمة السياق باستخدام علامات ASP.NET**
العلامات ASP.NET التالية تضيف عنصر قائمة السياق في GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



إليك العلامات الكاملة لـ ASP.NET التي تنشئ GridWeb مع عنصر قائمة السياق السابق. يرجى ملاحظة الخاصية OnCustomCommand="GridWeb1_CustomCommand". إنها اسم معالج الحدث الذي سيتم استدعاؤه عند النقر على عنصر قائمة السياق الخاص بك.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



هذا هو شكل عنصر قائمة السياق بعد إضافته باستخدام العلامات ASP.NET السابقة.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

هذا هو كود معالج الحدث الذي يتم تنفيذه عند النقر على عنصر قائمة السياق. يتحقق الكود أولاً من اسم الأمر، إذا كان يتطابق مع الأمر الخاص بنا، يضيف نصًا في الخلية A1 لورقة العمل النشطة في GridWeb ويضبط عرض العمود الأول إلى 40 وحدة لجعل النص مرئيًا.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


هذا هو شكل GridWeb عند النقر على عنصر قائمة السياق.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **إضافة عناصر قائمة السياق في Aspose.Cells.GridWeb باستخدام الكود**
يوضح هذا الكود كيفية إضافة عنصر قائمة سياق داخل GridWeb باستخدام الكود.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **إزالة عناصر قائمة سياق في Aspose.Cells.GridWeb باستخدام الكود**
يظهر هذا الكود كيفية إزالة عنصر من قائمة السياق باستخدام أساليب CustomCommandButtons.Remove() و CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
