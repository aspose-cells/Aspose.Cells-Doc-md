---
title: تصدير CSS الورقة في HTML المخرج بشكل منفصل باستخدام جولانغ عبر C++
linktitle: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج
type: docs
weight: 80
url: /ar/go-cpp/export-worksheet-css-separately-in-output/
description: تعلم كيفية تصدير CSS ورقة العمل بشكل منفصل عند تحويل ملفات إكسل إلى HTML باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

يقدم Aspose.Cells ميزة تصدير CSS ورقة العمل بشكل منفصل عند تحويل ملف إكسل إلى HTML. يرجى استخدام الخاصية [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/) لهذا الغرض وتعيينها إلى **صحيح** أثناء حفظ ملف إكسل إلى تنسيق HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

يقوم الكود العيني التالي بإنشاء ملف Excel، وإضافة نص في الخلية **B5** بلون **أحمر** ثم يحفظه بتنسيق HTML باستخدام خاصية [**HtmlSaveOptions.GetExportWorksheetCSSSeparately()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportworksheetcssseparately/). يُرجى رؤية [HTML الناتج](60489766.zip) الذي تم إنشاؤه من الكود للإطلاع. ستجد ملفًا بعنوان **stylesheet.css** داخله كنتيجة للكود العيني.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml.go" >}}
## **تصدير مصنف يحتوي على ورقة واحدة إلى HTML**

عندما يتم تحويل مصنف يحتوي على عدة أوراق إلى HTML باستخدام Aspose.Cells، يتم إنشاء ملف HTML بالإضافة إلى مجلد يحتوي على ملفات CSS وملفات HTML متعددة. عند فتح هذا الملف في المتصفح، تكون علامات التبويب مرئية. نفس السلوك مطلوب لمصنف يحتوي على ورقة عمل واحدة عند تحويله إلى HTML. سابقًا، لم يتم إنشاء مجلد منفصل لمصنفات الورق الواحد، وتم إنشاء ملف HTML فقط. هذا الملف لا يُظهر علامة تبويب عند فتحه في المتصفح. ينشئ MS Excel مجلد وHTML مناسبين للورقة الواحدة أيضًا، ولذلك تم تنفيذ نفس السلوك باستخدام واجهات برمجة تطبيقات Aspose.Cells. يمكن تنزيل ملف النموذج من الرابط التالي للاستخدام في الكود النموذجي أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportWorksheetCssSeparatelyInOutputHtml-1.go" >}}
