---
title: تخصيص المخططات
description: تعلم كيفية تخصيص الرسوم البيانية في Aspose.Cells للبايثون via .NET. سيرشدك دليلنا إلى كيفية تعديل تخطيطات الرسوم البيانية، إضافة وتنسيق سلاسل البيانات، ضبط المحاور، وتطبيق خيارات تنسيق متعددة لتعزيز مظهر واستخدام رسوماتك البيانية.
keywords: Aspose.Cells للبايثون via .NET، رسم بياني، التخصيص، التخطيطات، سلاسل البيانات، المحاور، التنسيق، المظهر، الاستخدام.
type: docs
weight: 40
url: /ar/python-net/customizing-charts/
---


## **إنشاء مخططات مخصصة**

حتى الآن، عندما ناقشنا الرسوم البيانية، نظرنا إلى الرسوم البيانية القياسية التي لها إعدادات تنسيقها الافتراضية. نحن فقط نحدد مصدر البيانات، نضبط بعض الخصائص، ويتم إنشاء الرسم البياني بتنسيقه الافتراضي. لكن واجهات برمجة التطبيقات Aspose.Cells للبايثون via .NET تدعم أيضًا إنشاء رسومات بيانية مخصصة تتيح للمطورين إنشاء رسومات بيانية بتنسيقاتهم الخاصة.

يمكن للمطورين إنشاء رسومات بيانية مخصصة في وقت التشغيل باستخدام Aspose.Cells للبايثون via .NET.

يتكون الرسم البياني من سلسلة بيانات. يتم تمثيل كل سلسلة بيانات في Aspose.Cells للبايثون via .NET بواسطة كائن [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) بينما [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection) يمثل مجموعة من [**Series**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/series) من الكائنات. عند إنشاء رسم بياني مخصص، يكون للمطورين الحرية في استخدام أنواع مختلفة من الرسوم البيانية لمجموعات البيانات المختلفة (المجمعة في كائن [**SeriesCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.charts/seriescollection)).

الكود المثال أدناه يوضح كيفية إنشاء مخططات مخصصة. في هذا المثال، سنستخدم مخطط عمودي لأول سلسلة بيانات ومخطط خطي للسلسلة الثانية. النتيجة هي أننا نضيف مخطط عمودي، مع مخطط خطي، إلى ورقة العمل.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Charts-ManipulateChart-HowToCreateCustomChart-1.py" >}}

{{% alert color="primary" %}}

حاليًا، يدعم Aspose.Cells للبايثون via .NET فقط الرسوم البيانية المخصصة التي تجمع بين الدوائر، الخطوط، الأعمدة، ومخططات الأعمدة المكدسة، ولكن سيتم دعم المزيد من الرسوم البيانية في الإصدارات المستقبلية.

{{% /alert %}}
{{< app/cells/assistant language="python-net" >}}
