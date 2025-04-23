---
title: تكييف ارتفاع الصف تلقائياً عند تحميل الملف
type: docs
weight: 120
url: /ar/net/autofit-row-height/
description: تعرف على كيفية تكييف الصفوف التي ليست ارتفاعها مخصصًا.
keywords: تكييف ارتفاع الصف تلقائياً عند تحميل الملف، ضبط ارتفاع الصف تلقائيًا عند فتح ملف إكسل. 
---

## **سيناريوهات الاستخدام المحتملة**
ارتفاع الصف يطابق تلقائياً خط النوعية، ولكن عندما لا يتطابق ارتفاع الصف المخزن مع ارتفاع المحتوى في الملف، سيقوم MS Excel بضبط ارتفاع الصف تلقائيًا عند تحميل الملف، بينما لن يقوم Aspose.Cells بضبطه تلقائيًا لتحسين الأداء. إذا كنت بحاجة إلى استخدام برنامج Aspose.Cells لتطابق ارتفاع الأسطر تلقائيًا عند تحميل الملفات، يمكنك تحقيق الهدف من خلال المعامل [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

يرجى الرجوع إلى البيانات التالية للصورة. يمكننا مراقبة ارتفاع الصف المخزن في السطر 11 وهو 15، ولكن أكسل ضبط آلياً ارتفاع الصف عند تحميل الملف.
<br>
<img src="1.png" width=70% />

## **ضبط ارتفاع الصف باستخدام Aspose.Cells**
إذا قمت بتحميل الملف مباشرة وحفظه في تنسيق PDF، فلن يتم عرض البيانات بالكامل في ملف PDF لأن ارتفاع الصف المخزن 15 فقط.
<br>
<img src="2.png" width=70% />
<br>
إذا قمت بتعيين المعامل [LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) إلى true عند تحميل الملف، فسيقوم Aspose.Cells بضبط ارتفاع الصف تلقائيًا. يمكن أن يلبي ارتفاع الصف المضبوط متطلبات عرض النص بشكل فعال.
<br>
<img src="3.png" width=70% />

## **شفرة C# عينة**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}
{{< app/cells/assistant language="csharp" >}}
