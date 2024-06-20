---
title: تخصيص المخططات
description: تعلم كيفية تخصيص المخططات في Aspose.Cells for .NET. سيوضح دليلنا لك كيفية تعديل تخطيطات المخطط، وإضافة وتنسيق سلاسل البيانات، وضبط المحاور، وتطبيق خيارات التنسيق المختلفة لتعزيز مظهر مخططاتك وقابلية استخدامها.
keywords: Aspose.Cells for .NET، الرسم البياني، تخصيص، تخطيطات، سلاسل بيانات، محاور، تنسيق، مظهر، قابلية الاستخدام.
type: docs
weight: 40
url: /ar/net/customizing-charts/
---

{{% alert color="primary" %}}

## **إنشاء مخططات مخصصة**

حتى الآن، عندما تحدثنا عن المخططات، نظرنا إلى المخططات القياسية التي تحتوي على إعدادات تنسيق قياسية لها. نحدد فقط مصدر البيانات، ونضبط بعض الخصائص، ويتم إنشاء المخطط بإعدادات التنسيق الافتراضية الخاصة به. ومع ذلك، تدعم واجهات برمجة التطبيقات في Aspose.Cells أيضًا إنشاء مخططات مخصصة تسمح للمطورين بإنشاء مخططات بإعدادات تنسيق خاصة بهم.

يمكن للمطورين إنشاء مخططات مخصصة أثناء التشغيل باستخدام Aspose.Cells.

يتألف المخطط من سلاسل بيانات. يُمثل كل سلسلة بيانات في Aspose.Cells بواسطة [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series) كائن في حين تعمل كائن [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection) كمجموعة لأشياء [**Series**](https://reference.aspose.com/cells/net/aspose.cells.charts/series). عند إنشاء مخطط مخصص، يحظى المطورون بحرية استخدام أنواع مختلفة من المخططات لسلاسل بيانات مختلفة (التي تم جمعها في الكائن [**SeriesCollection**](https://reference.aspose.com/cells/net/aspose.cells.charts/seriescollection)).

الكود المثال أدناه يوضح كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخطط عمودي لأول سلسلة بيانات ومخطط خطي للسلسلة الثانية. النتيجة هي أننا نضيف مخطط عمودي، مع مخطط خطي، إلى ورقة العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Charts-ManipulateChart-HowToCreateCustomChart-1.cs" >}}

{{% alert color="primary" %}}

حاليًا، تدعم Aspose.Cells فقط مخططات مخصصة تجمع ما بين مخططات البيتزا، الخطية، العمودية، وعمود الكتل ولكن سيتم دعم مخططات أخرى في الإصدارات القادمة.

{{% /alert %}}
