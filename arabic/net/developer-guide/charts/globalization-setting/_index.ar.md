---
title: تحويل الشارت إلى صورة متوطنة
description: تعرف على كيفية ضبط إعدادات العالمية للشارت باستخدام Aspose.Cells for .NET. يوضح دليلنا كيفية تكوين الشارت لدعم لغات متعددة وتنسيقات إقليمية لعرض النصوص بشكل صحيح والتواريخ والأرقام بلغات مختلفة.
keywords: Aspose.Cells for .NET، شارت، إعدادات العالمية، لغات متعددة، تنسيقات إقليمية، عرض، نصوص، تواريخ، أرقام.
linktitle: تعيين منطقة معربة
type: docs
weight: 50
url: /ar/net/convert-chart-to-localized-image/
alias: [/net/how-to-set-globalization-configuration-for-chart/]
---

{{% alert color="primary" %}}

في هذا الموضوع، سنريك كيفية تحويل الرسم البياني إلى صورة معربة، ستتعرف كيفية تعيين المنطقة المعربة لرسم بياني.

{{% /alert %}}

## **سيناريو**

في أي سيناريو سنحتاج إلى تعيين المنطقة المحلية لرسم بياني؟ 

عند فتح ملف xlsx برسم بياني في Excel، في هذه الحالة، يفترض أنك تفتحه باستخدام إعدادات المنطقة الإسبانية في Excel، يمكنك رؤية العناصر في منطقة الرسم البياني، مثل عنوان الرسم البياني والأسطورة، حيث تم ترجمتها إلى اللغة الإسبانية. ولكن عند حفظ هذا الرسم البياني كصورة باستخدام Aspose.Cells، قد تواجه المشكلة التالية: 

**![مشكلة عامة](GlobalIssue.png)**

في هذا السيناريو، فإن أسطورة الرسم البياني في الصورة الناتجة لا تكون كما هي في Excel، حيث تظل عرضت باللغة الإنجليزية افتراضيًا. يمكنك الآن حل هذه المشكلة عن طريق تعيين المنطقة المحلية للرسم البياني. مع الإعدادات الصحيحة، ستتم عرض العناصر التالية وفقًا لإعدادات التوطين الخاصة بك.

## **العناصر المدعومة**

يمكن عرض العناصر التالية في الرسم البياني وفقًا لإعدادات التوطين الخاصة بك.

|**العناصر المدعومة**|**القيمة الافتراضية في بيئة الإنجليزية**|
| :- | :- |
|اسم عنوان المحور|عنوان المحور|
|اسم وحدة المحور|مئات، آلاف...|
|اسم عنوان الرسم البياني|عنوان الرسم البياني|
|زيادة الأسطورة|زيادة|
|انخفاض الأسطورة|انخفاض|
|اسم الإجمالي في الأسطورة|مجموع|
|اسم آخر|آخر|
|اسم السلسلة|سلسلة|

## **خطوات التشغيل**

سيظهر لك المثال التالي بالتفصيل كيفية تعيين المنطقة المحلية لتحقيق الأثر الذي تريده.

- [كيفية تعيين المنطقة الصينية للرسم البياني](/cells/ar/net/convert-chart-to-image-for-chinese-region/)
- [كيفية تعيين المنطقة اليابانية للرسم البياني](/cells/ar/net/convert-chart-to-image-for-japanese-region/)

{{< app/cells/assistant language="csharp" >}}
