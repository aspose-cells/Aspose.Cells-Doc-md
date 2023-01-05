---
title: دمج Aspose.Cells شبكة التحكم مع Visual Studio.NET
type: docs
weight: 10
url: /ar/net/integrate-aspose-cells-grid-controls-with-visual-studio-net/
---
{{% alert color="primary" %}} 

 يمكن لمطوري Visual Studio.NET سحب عناصر التحكم بسهولة من ملف**صندوق الأدوات** على Windows أو نموذج ويب. يمكن تنزيل مجموعة الشبكة Aspose.Cells باستخدام مثبت MSI ، أو كمجموعة من حزم DLL. تشرح هذه المقالة ما يجب فعله للتأكد من إمكانية استخدام عناصر تحكم Aspose.Cells.Grid في Visual Studio.NET عند تثبيتها باستخدام مكتبات DLL بدلاً من المثبت.

{{% /alert %}} 
## **دمج Aspose.Cells شبكة التحكم مع Visual Studio.NET**
لدمج عناصر تحكم الشبكة Aspose.Cells مع Visual Studio.NET:

1. افتح صندوق الأدوات.
1. حدد علامة التبويب عام (أو أي علامة تبويب أخرى تريد إضافة عناصر تحكم إليها).
1. انقر بزر الماوس الأيمن فوق علامة التبويب عام.
1.  في Visual Studio.NET 2003: حدد**إضافة / إزالة العناصر** من القائمة.
1. في Visual Studio.NET 2005 ، حدد**اختر العناصر** من القائمة. سيظهر مربع حوار Customize Toolbox (هذه العملية هي نفسها إلى حد ما بالنسبة لأحدث VS.NET IDEs (على سبيل المثال VS.NET 2013/2015 أو أحدث)).
1.  انقر**تصفح** وحدد موقع ملفات Aspose.Cells.GridDesktop.dll و Aspose.Cells.GridWeb.dll.
1.  حدد مكتبات DLL ثم انقر فوق "موافق"**فتح**. سيحتوي مربع حوار Customize Toolbox الآن على عناصر تحكم من Aspose.Cells Grid Suite. سيتم تمييز عناصر التحكم المضافة حديثًا بواسطة مربع الحوار.
1.  انقر**نعم** لإضافة عناصر التحكم إلى Visual Studio.NET Toolbox الخاص بك.

 سيتم إضافة عناصر تحكم الشبكة Aspose.Cells إلى Toolbox's**عام** التبويب. فقط عنصر التحكم GridWeb غير نشط. هذا لأننا نعمل على تطبيق Windows Forms. يتوفر GridWeb فقط عندما تعمل على نماذج الويب بينما يمكن استخدام GridDesktop مع نماذج Windows فقط.
