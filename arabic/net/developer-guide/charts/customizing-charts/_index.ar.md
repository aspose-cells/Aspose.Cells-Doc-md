---
title: تخصيص الرسوم البيانية
description: تعرف على كيفية تخصيص المخططات في Aspose.Cells for .NET. سيوضح لك دليلنا كيفية تعديل تخطيطات المخططات وإضافة سلاسل البيانات وتنسيقها وضبط المحاور وتطبيق خيارات التنسيق المتنوعة لتحسين مظهر المخططات وسهولة استخدامها.
keywords: Aspose.Cells for .NET, charting, customization, layouts, data series, axes, formatting, appearance, usability.
type: docs
weight: 40
url: /ar/net/customizing-charts/
---
{{% alert color="primary" %}}

##  **إنشاء مخططات مخصصة**

حتى الآن، عندما ناقشنا المخططات، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات التنسيق القياسية الخاصة بها. نقوم فقط بتعريف مصدر البيانات، وتعيين بعض الخصائص، ويتم إنشاء المخطط باستخدام إعدادات التنسيق الافتراضية الخاصة به. لكن Aspose.Cells APIs تدعم أيضًا إنشاء مخططات مخصصة تسمح للمطورين بإنشاء مخططات باستخدام إعدادات التنسيق الخاصة بهم.

يمكن للمطورين إنشاء مخططات مخصصة في وقت التشغيل باستخدام Aspose.Cells.

 يتكون المخطط من سلسلة بيانات. يتم تمثيل كل سلسلة بيانات في Aspose.Cells بواسطة أ[**مسلسل**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) كائن بينما[**مجموعة السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) الكائن بمثابة مجموعة من[**مسلسل**](https://reference.aspose.com/cells/net/aspose.cells.charts/series)أشياء. عند إنشاء مخطط مخصص، يتمتع المطورون بحرية استخدام أنواع مختلفة من المخططات لسلاسل بيانات مختلفة (تم جمعها في ملف[**مجموعة السلسلة**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)هدف).

يوضح رمز المثال أدناه كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخططًا عموديًا لسلسلة البيانات الأولى ومخططًا خطيًا للسلسلة الثانية. والنتيجة هي أننا نضيف مخططًا عموديًا، مقترنًا بمخطط خطي، إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

يدعم Aspose.Cells حاليًا فقط المخططات المخصصة التي تجمع بين المخططات الدائرية والخطية والعمودية ومكدس الأعمدة ولكن سيتم دعم المزيد من المخططات في الإصدارات المستقبلية.

{{% /alert %}}
