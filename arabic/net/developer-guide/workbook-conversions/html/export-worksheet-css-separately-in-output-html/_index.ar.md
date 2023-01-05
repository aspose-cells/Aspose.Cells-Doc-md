---
title: تصدير ورقة العمل CSS بشكل منفصل في الإخراج HTML
type: docs
weight: 80
url: /ar/net/export-worksheet-css-separately-in-output/
---
## **سيناريوهات الاستخدام الممكنة**

 يوفر Aspose.Cells ميزة لتصدير ورقة العمل CSS بشكل منفصل عند تحويل ملف Excel الخاص بك إلى HTML. الرجاء استخدام[**HtmlSaveOptions.ExportWorksheetCSS بشكل منفصل**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) لهذا الغرض وضبطه على**حقيقي** أثناء حفظ ملف Excel بتنسيق HTML.

## **تصدير ورقة العمل CSS بشكل منفصل في الإخراج HTML**

ينشئ نموذج التعليمات البرمجية التالي ملف Excel ، ويضيف بعض النص في الخلية**ب 5** في**أحمر**color ثم يحفظه بتنسيق HTML باستخدام[**HtmlSaveOptions.ExportWorksheetCSS بشكل منفصل**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) خاصية. الرجاء مراجعة[الإخراج HTML](60489766.zip) التي تم إنشاؤها بواسطة رمز كمرجع. سوف تجد**styleheet.css**بداخله كنتيجة لعينة التعليمات البرمجية.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **تصدير مصنف ذو ورقة واحدة إلى HTML**

عندما يتم تحويل مصنف متعدد الأوراق إلى HTML باستخدام Aspose.Cells ، فإنه ينشئ ملف HTML مع مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح هذا الملف HTML في المستعرض ، تظهر علامات التبويب. مطلوب نفس السلوك لمصنف يحتوي على ورقة عمل واحدة عند تحويله إلى HTML. في وقت سابق لم يتم إنشاء مجلد منفصل للمصنفات ذات الورقة المفردة وتم إنشاء ملف HTML فقط. لا يظهر ملف HTML مثل علامة التبويب عند فتحه في المستعرض. يقوم MS Excel بإنشاء مجلد مناسب و HTML لورقة واحدة أيضًا ، وبالتالي يتم تنفيذ نفس السلوك باستخدام واجهات برمجة تطبيقات Aspose.Cells. يمكن تنزيل نموذج الملف من الرابط التالي لاستخدامه في نموذج التعليمات البرمجية أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
