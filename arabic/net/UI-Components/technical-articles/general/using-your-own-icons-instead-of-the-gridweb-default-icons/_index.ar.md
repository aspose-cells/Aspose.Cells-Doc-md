---
title: استخدم الرموز الخاصة بك بدلاً من الرموز الافتراضية لـ GridWeb
type: docs
weight: 10
url: /ar/net/aspose-cells-gridweb/use-your-own-icons-instead-of-the-default-icons/
keywords: GridWeb، رمز، رموز
description: يوضح هذا المقال كيفية استخدام الرموز في GridWeb.
---

{{% alert color="primary" %}} 

في بعض الأحيان قد ترغب في استخدام رموز (صور) الخاصة بك بدلاً من الرموز الافتراضية لعنصر تحكم Aspose.Cells.GridWeb. يشرح هذا المقال كيفية فعل ذلك.

{{% /alert %}} 

تقع الرموز الافتراضية للعنصر التحكم في مسار URL "/acw_client/". يمكن أن يكون مسار الملف: "C:\Program Files\Aspose\Aspose.Cells for .NET\acw_client" بشكل افتراضي. يمكنك العثور على ملفات مثل submit.gif، save.gif وما إلى ذلك في تلك الدليل. إذا كنت ترغب في استبدال هذه الصور بالصور الخاصة بك، أضف قسمًا تكوينيًا إلى ملف web.config في تطبيق الويب الخاص بك.

**XML**

{{< highlight csharp >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

قد لاحظت أن هذا التكوين يؤثر فقط في مسار الصور للرقابة ولا يؤثر على مسار النصوص الخاص بالعميل للرقابة. على سبيل المثال، إذا قمت بتشغيل صفحتك بعنصر التحكم GridWeb وفحص ملف المصدر في المستعرض، قد تجد أن مسار acw_client _path الخاص بعنصر DIV الشبكة لا يزال يقول: "/yourApp/webform1.aspx/". في بعض الحالات، قد تحتاج إلى إعادة تعريف مسار النص الخاص بالعميل. لإجبار الرقابة على استخدام مسار الصور المعاد تعريفه كمسار النص الخاص بالعميل، أضف إعداد تكويني آخر في قسم appSettings
**XML**

{{< highlight csharp >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

هذا التكوين سيكون له تأثير فقط مع الرقابة المرخصة.

{{% /alert %}}
