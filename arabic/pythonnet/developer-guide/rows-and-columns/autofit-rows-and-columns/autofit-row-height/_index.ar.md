---
title: تكييف ارتفاع الصف تلقائياً عند تحميل الملف
type: docs
weight: 120
url: /ar/python-net/autofit-row-height/
description: تعلُّم كيفية تناسب الصفوف التي ليست أرتافها مخصصة من خلال Aspose.Cells لبرنامج Python via .NET.
keywords: مكتبة بايثون لإكسل، ضبط ارتفاع الصف تلقائيًا عند تحميل الملف باستخدام بايثون، تعديل ارتفاع الصف تلقائيًا عند فتح ملف إكسل بواسطة Python. 
---

## **سيناريوهات الاستخدام المحتملة**
ارتفاع الصف يتطابق تلقائيًا مع خط المحتوى، ولكن عندما لا يتطابق ارتفاع الصف المخبأ مع ارتفاع المحتوى في الملف، سيقوم MS Excel تلقائيًا بضبط ارتفاع الصف عند تحميل الملف، بينما لن يقوم Aspose.Cells لبرنامج Python via .NET بضبطه تلقائيًا لتحسين الأداء. إذا كنت بحاجة إلى استخدام برنامج Aspose.Cells لبرنامج Python via .NET لمطابقة ارتفاع السطر تلقائيًا عند تحميل الملف، يمكنك تحقيق الهدف من خلال المعلمة [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/).

يرجى الرجوع إلى البيانات التالية للصورة. يمكننا مراقبة ارتفاع الصف المخزن في السطر 11 وهو 15، ولكن أكسل ضبط آلياً ارتفاع الصف عند تحميل الملف.
<br>
<img src="1.png" width=70% />

## **ضبط ارتفاع الصف باستخدام مكتبة Aspose.Cells لبرنامج Python إكسل**
إذا قمت بتحميل الملف مباشرة وحفظه في تنسيق PDF، فلن يتم عرض البيانات بالكامل في ملف PDF لأن ارتفاع الصف المخزن 15 فقط.
<br>
<img src="2.png" width=70% />
<br>
إذا قمت بتعيين المعلمة [LoadOptions.AutoFitterOptions.only_auto](https://reference.aspose.com/cells/python-net/aspose.cells/autofitteroptions/only_auto/) على true عند تحميل الملف، سيقوم Aspose.Cells لبرنامج Python via .NET بضبط ارتفاع الصف تلقائيًا. يمكن لارتفاع السطر المضبط تلبية متطلبات عرض النص بشكل فعال.
<br>
<img src="3.png" width=70% />

## **كود عينة بايثون**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "RowsColumns-Rows-autofit-row-height.py" >}}
{{< app/cells/assistant language="python-net" >}}
