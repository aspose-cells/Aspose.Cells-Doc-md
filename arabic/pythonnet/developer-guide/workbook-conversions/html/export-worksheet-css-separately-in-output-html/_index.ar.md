---
title: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج
type: docs
weight: 80
url: /ar/python-net/export-worksheet-css-separately-in-output/
---

## **سيناريوهات الاستخدام المحتملة**

يوفر Aspose.Cells لـ Python via .NET ميزة تصدير CSS ورقة العمل بشكل منفصل عند تحويل ملف Excel إلى HTML. يرجى استخدام خاصية [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately) لهذا الغرض وتعيينها على **true** أثناء حفظ ملف Excel بصيغة HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

يقوم الكود العيني التالي بإنشاء ملف Excel، وإضافة نص في الخلية **B5** بلون **أحمر** ثم يحفظه بتنسيق HTML باستخدام خاصية [**HtmlSaveOptions.export_worksheet_css_separately**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_worksheet_css_separately). يُرجى رؤية [HTML الناتج](60489766.zip) الذي تم إنشاؤه من الكود للإطلاع. ستجد ملفًا بعنوان **stylesheet.css** داخله كنتيجة للكود العيني.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.py" >}}

## **تصدير جدول عمل واحد إلى HTML**

عند تحويل دفتر عمل به عدة أوراق إلى HTML باستخدام Aspose.Cells لـ Python via .NET، ينشئ ملف HTML مع مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح ملف HTML هذا في المتصفح، تكون علامات التبويب مرئية. نفس السلوك مطلوب لدفتر عمل بورقة واحدة عند تحويله إلى HTML. في السابق، لم يُنشأ مجلد منفصل لدفاتر العمل ذات الورقة الواحدة وتم إنشاء ملف HTML فقط. لا يُظهر مثل هذا الملف علامات التبويب عند فتحه في المتصفح. يقوم MS Excel أيضًا بإنشاء مجلد وملف HTML مناسب لورقة واحدة، وبالتالي يتم تنفيذ نفس السلوك باستخدام واجهات برمجة التطبيقات Aspose.Cells لـ Python via .NET. يمكن تنزيل الملف النموذجي من الرابط التالي للاستخدام في الكود أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-SetSingleSheetTabNameInHtml-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
