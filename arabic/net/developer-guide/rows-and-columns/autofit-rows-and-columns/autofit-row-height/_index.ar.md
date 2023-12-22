---
title: الاحتواء التلقائي لارتفاع الصف تلقائيًا عند تحميل الملف
type: docs
weight: 120
url: /ar/net/autofit-row-height/
description: تعرف على كيفية ملاءمة الصفوف التي لا يتم تخصيص ارتفاعها.
keywords: AutoFit Row Height when loading file, automatically adjust the row height when opening excel file. 
---
##  **سيناريوهات الاستخدام المحتملة**
 يتطابق ارتفاع الصف تلقائيًا مع خط المحتوى، ولكن عندما لا يتطابق ارتفاع الصف المخزن مؤقتًا مع ارتفاع المحتوى في الملف، سيقوم MS Excel تلقائيًا بضبط ارتفاع الصف عند تحميل الملف، بينما لن يتطابق Aspose.Cells وضبطه تلقائيًا لتحسين الأداء. إذا كنت بحاجة إلى استخدام برنامج Aspose.Cells لمطابقة ارتفاعات الأسطر تلقائيًا عند تحميل الملفات، فيمكنك تحقيق الهدف من خلال المعلمة[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/).

يرجى الرجوع إلى بيانات الصورة التالية. يمكننا أن نلاحظ أن ارتفاع صف ذاكرة التخزين المؤقت في السطر 11 هو 15، لكن Excel يقوم تلقائيًا بضبط ارتفاع الصف عند تحميل الملف.
<br>
<img src="1.png" width=70% />

##  **اضبط ارتفاع الصف باستخدام Aspose.Cells**
إذا قمت بتحميل الملف مباشرة وحفظته في PDF، فلن يتم عرض البيانات بالكامل في PDF لأن ارتفاع سطر ذاكرة التخزين المؤقت الخاص به هو 15 فقط.
<br>
<img src="2.png" width=70% />
<br>
 إذا قمت بتعيين المعلمة[LoadOptions.AutoFitterOptions.OnlyAuto](https://reference.aspose.com/cells/net/aspose.cells/autofitteroptions/onlyauto/) إلى صحيح عند تحميل الملف، ثم Aspose.Cells سوف يضبط ارتفاع الصف تلقائيًا. يمكن أن يلبي ارتفاع الخط المعدل متطلبات عرض النص بشكل فعال.
<br>
<img src="3.png" width=70% />

##  **C# نموذج الكود**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rows-autofit-row-height.cs" >}}