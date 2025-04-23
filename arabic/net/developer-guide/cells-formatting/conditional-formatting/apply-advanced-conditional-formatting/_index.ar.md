---
title: تطبيق التنسيق المشروط المتقدم
description: كيفية استخدام مكتبة Aspose.Cells في C# لتطبيق التنسيق المشروط المتقدم. من خلال ضبط هذه المعايير، يمكنك السيطرة بشكل أفضل على كيفية ظهور ومظهر الخلايا.
keywords: Aspose.Cells، تنسيق مشروط متقدم، C#، مشروط، تنسيق
type: docs
weight: 70
url: /ar/net/apply-advanced-conditional-formatting/
---

{{% alert color="primary" %}} 

إصدارات Microsoft Excel 2007 والأحدث (2010/2013/2016) توفر بعض الميزات المتقدمة لتنسيق المشروطات. على سبيل المثال، تتيح لك تطبيق تظليل الخلية والحدود والرموز الملونة والسهام والعلمات وتنسيق الخطوط، وما إلى ذلك، مما أصبح متطورًا تمامًا.

{{% /alert %}} 
## **تطبيق تنسيق مشروط متقدم إلى ملفات Microsoft Excel**
يمكن للتنسيق المشروط:

- إضافة شريط بيانات مظللة لتحسين الأرقام الأساسية بشكل بصري من خلال تضمين مخطط بياني بسيط في الخلايا.
- تظليل الخلايا تلقائيًا بمقاييس الألوان بناءً على علاقتها بقيم في خلايا أخرى في النطاق. تظليل الإعدادات الافتراضية القيمة الأدنى باللون الأحمر متحركًا صعودًا إلى القيمة الأعلى باللون الأخضر.
- استخدام مجموعات الرموز بالطريقة نفسها كمقاييس الألوان، ولكن بدلاً من تظليل الخلايا، يضيف رموز صغيرة، مثل السهام وأضواء المرور، إلى الخلايا.

تدعم Aspose.Cells بشكل كامل التنسيق المشروط المقدم من Microsoft Excel 2007 والأحدث في تنسيق XLSX على الخلايا في وقت التشغيل. يوضح هذا المثال تمرينًا لأنواع التنسيق المشروط المتقدمة بما في ذلك مجموعات الرموز، أشرطة البيانات، مقاييس الألوان، فترات الزمن، القاع/القمة وقواعد أخرى بمجموعات مختلفة من السمات.

- [**Adding Color Scale Conditional Formattings**](/cells/ar/net/adding-2-color-scale-and-3-color-scale-conditional-formattings/)
- [**Adding Above Average Conditional Formattings**](/cells/ar/net/how-to-add-above-average-conditional-formatting/)
- [**Adding DataBars Conditional Formattings**](/cells/ar/net/how-to-add-databars-conditional-formatting/)
- [**Adding IonSets Conditional Formattings**](/cells/ar/net/how-to-add-icon-sets-conditional-formatting/)
- [**Adding Text Conditional Formattings**](/cells/ar/net/how-to-add-text-conditional-formatting/)
- [**Adding TimePeriods Conditional Formattings**](/cells/ar/net/how-to-add-time-periods-conditional-formatting/)
- [**Adding Top10 Conditional Formattings**](/cells/ar/net/how-to-add-top10-conditional-formatting/)


### **حساب اللون المختار من قبل Microsoft Excel لتنسيق المشروط مع المقياس اللوني**
تتيح لك Aspose.Cells حساب اللون الذي اختاره Microsoft Excel عند استخدام تنسيق مشروط بمقياس الألوان في ملف قالب. Consulte el código de ejemplo a continuación para aprender cómo calcular el color seleccionado por Microsoft Excel.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Formatting-ComputeColorChoosenByMSExcel-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
