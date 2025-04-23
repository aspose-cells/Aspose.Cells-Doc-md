---
title: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج
type: docs
weight: 80
url: /ar/net/export-worksheet-css-separately-in-output/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells ميزة تصدير ورقة العمل CSS بشكل منفصل عند تحويل ملف Excel الخاص بك إلى HTML. يرجى استخدام خاصية [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) لهذا الغرض وضبطها على **صحيحة** أثناء حفظ ملف Excel بتنسيق HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

يقوم الكود العيني التالي بإنشاء ملف Excel، وإضافة نص في الخلية **B5** بلون **أحمر** ثم يحفظه بتنسيق HTML باستخدام خاصية [**HtmlSaveOptions.ExportWorksheetCSSSeparately**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately). يُرجى رؤية [HTML الناتج](60489766.zip) الذي تم إنشاؤه من الكود للإطلاع. ستجد ملفًا بعنوان **stylesheet.css** داخله كنتيجة للكود العيني.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **تصدير جدول عمل واحد إلى HTML**

عند تحويل جدول عمل يحتوي على عدة أوراق عمل إلى HTML باستخدام Aspose.Cells، يتم إنشاء ملف HTML جنبًا إلى مجلد يحتوي على CSS وعدة ملفات HTML. عند فتح هذا الملف HTML في المتصفح، تظهر علامات التبويب. نفس السلوك مطلوب لجدول عمل ذي ورقة عمل واحدة عند تحويله إلى HTML. في السابق، لم يتم إنشاء مجلد منفصل لأوراق العمل ذات الورقة الواحدة وتم إنشاء ملف HTML واحد فقط. هذا الملف HTML لا يظهر علامة تبويب عند فتحه في المتصفح. يقوم MS Excel بإنشاء مجلد و HTML مناسب لورقة عمل واحدة أيضًا وبالتالي يتم تنفيذ نفس السلوك باستخدام واجهات برمجة التطبيقات Aspose.Cells. يمكن تنزيل الملف العيني من الرابط التالي لاستخدامه في الكود العيني أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
