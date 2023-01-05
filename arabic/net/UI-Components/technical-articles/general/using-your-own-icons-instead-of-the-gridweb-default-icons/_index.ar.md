---
title: استخدام الرموز الخاصة بك بدلاً من أيقونات الشبكة الافتراضية
type: docs
weight: 10
url: /ar/net/using-your-own-icons-instead-of-the-gridweb-default-icons/
---
{{% alert color="primary" %}} 

في بعض الأحيان قد ترغب في استخدام الرموز الخاصة بك (الصور) بدلاً من Aspose.Cells. الرموز الافتراضية للتحكم في شبكة الويب. تشرح هذه المقالة كيفية القيام بذلك.

{{% /alert %}} 

توجد الرموز الافتراضية لعنصر التحكم في مسار URL "/ acw_العميل / ". يمكن أن يكون مسار الملف:" C: \ Program Files \ Aspose \ Aspose.Cells for .NET \ acw_client "افتراضيًا. يمكنك العثور على ملفات مثل submit.gif و save.gif وما إلى ذلك في هذا المجلد. إذا كنت تريد استبدال هذه الصور بصورك الخاصة ، فأضف قسم التكوين إلى ملف web.config لتطبيق الويب الخاص بك.

**XML**

{{< highlight "csharp" >}}

 <appSettings>

 <add key="Aspose.Cells.GridWeb.acw_client_path" value="/acw_client/" />

</appSettings>



{{< /highlight >}}

ربما لاحظت أن هذا التكوين يؤثر فقط على مسار صور عناصر التحكم ولا يؤثر على مسار البرامج النصية للعميل لعنصر التحكم. على سبيل المثال ، إذا قمت بتشغيل صفحتك باستخدام عنصر تحكم GridWeb وتحقق من الملف المصدر في المستعرض ، فقد تجد أن ACW_ عميل_لا تزال خاصية المسار لعنصر DIV للشبكة تقول: "/yourApp/webform1.aspx/". في بعض الحالات ، قد تحتاج إلى إعادة تعريف مسار البرنامج النصي للعميل. لإجبار عنصر التحكم على استخدام مسار الصورة المعاد تعريفه كمسار البرنامج النصي للعميل ، أضف إعداد تكوين آخر في قسم إعدادات التطبيق
**XML**

{{< highlight "csharp" >}}

 <add key="Aspose.Cells.GridWeb.force_script_path" value="true" />



{{< /highlight >}}

{{% alert color="primary" %}} 

لن يسري هذا التكوين إلا مع عنصر التحكم المرخص.

{{% /alert %}}
