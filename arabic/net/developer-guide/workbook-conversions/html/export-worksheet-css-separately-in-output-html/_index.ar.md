---
title: تصدير ورقة العمل CSS بشكل منفصل في إخراج HTML
type: docs
weight: 80
url: /ar/net/export-worksheet-css-separately-in-output/
---
## **سيناريوهات الاستخدام الممكنة**

 يوفر Aspose.Cells ميزة لتصدير ورقة العمل CSS بشكل منفصل عندما تقوم بتحويل ملف Excel إلى HTML. يرجى استخدام[**HtmlSaveOptions.ExportWorksheetCSS بشكل منفصل**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately) لهذا الغرض وضبطه على**حقيقي** أثناء حفظ ملف Excel بتنسيق HTML.

## **تصدير ورقة العمل CSS بشكل منفصل في إخراج HTML**

ينشئ نموذج التعليمات البرمجية التالي ملف Excel ، ويضيف بعض النص في الخلية**ب 5** في**أحمر** color ثم يحفظها بتنسيق HTML باستخدام[**HtmlSaveOptions.ExportWorksheetCSS بشكل منفصل**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportworksheetcssseparately)منشأه. الرجاء مراجعة[إخراج HTML](60489766.zip) تم إنشاؤها بواسطة رمز كمرجع. سوف تجد**styleheet.css**بداخله كنتيجة لعينة التعليمات البرمجية.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportWorksheetCSSSeparatelyInOutputHTML.cs" >}}

## **تصدير مصنف واحد إلى HTML**

عندما يتم تحويل مصنف يحتوي على أوراق متعددة إلى HTML باستخدام Aspose.Cells ، فإنه ينشئ ملف HTML مع مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح ملف HTML هذا في المستعرض ، تظهر علامات التبويب. مطلوب نفس السلوك لمصنف يحتوي على ورقة عمل واحدة عندما يتم تحويله إلى HTML. في وقت سابق ، لم يتم إنشاء مجلد منفصل للمصنفات ذات الورقة المفردة وتم إنشاء ملف HTML فقط. لا يُظهر ملف HTML هذا علامة تبويب عند فتحه في المستعرض. يقوم MS Excel بإنشاء مجلد مناسب و HTML لصفحة واحدة أيضًا ، وبالتالي يتم تنفيذ نفس السلوك باستخدام واجهات برمجة تطبيقات Aspose.Cells. يمكن تنزيل نموذج الملف من الرابط التالي لاستخدامه في نموذج التعليمات البرمجية أدناه:

[sampleSingleSheet.xlsx](79527937.xlsx)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-SetSingleSheetTabNameInHtml-1.cs" >}}
