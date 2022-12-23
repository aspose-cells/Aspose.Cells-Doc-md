---
title: تصدير ورقة العمل CSS بشكل منفصل في الإخراج HTML
type: docs
weight: 80
url: /ar/java/export-worksheet-css-separately-in-output-html/
---
## **سيناريوهات الاستخدام الممكنة**

يوفر Aspose.Cells ميزة لتصدير ورقة العمل CSS بشكل منفصل عند تحويل ملف Excel الخاص بك إلى HTML. الرجاء استخدام الخاصية HtmlSaveOptions.ExportWorksheetCSS بشكل منفصل لهذا الغرض وتعيينها على "true" أثناء حفظ ملف Excel بتنسيق HTML.

## **تصدير ورقة العمل CSS بشكل منفصل في الإخراج HTML**

ينشئ نموذج التعليمات البرمجية التالي ملف Excel ، ويضيف بعض النص في الخلية B5 باللون الأحمر ثم يحفظه بتنسيق HTML باستخدام الخاصية HtmlSaveOptions.ExportWorksheetCSSSeparately. الرجاء مراجعة[الإخراج HTML](60489780.zip)تم إنشاؤها بواسطة رمز كمرجع. ستجد styleheet.css بداخله كنتيجة لعينة التعليمات البرمجية.

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **تصدير مصنف ذو ورقة واحدة إلى HTML**

عندما يتم تحويل مصنف متعدد الأوراق إلى HTML باستخدام Aspose.Cells ، فإنه ينشئ ملف HTML مع مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح هذا الملف HTML في المستعرض ، تظهر علامات التبويب. مطلوب نفس السلوك لمصنف يحتوي على ورقة عمل واحدة عند تحويله إلى HTML. في وقت سابق لم يتم إنشاء مجلد منفصل للمصنفات ذات الورقة المفردة وتم إنشاء ملف HTML فقط. لا يظهر ملف HTML مثل علامة التبويب عند فتحه في المستعرض. يقوم Excel بإنشاء مجلد مناسب و HTML للأوراق الفردية أيضًا وبالتالي يتم تنفيذ نفس السلوك باستخدام Aspose.Cells. يمكن تنزيل ملف نموذج من الرابط التالي لاستخدامه في نموذج التعليمات البرمجية أدناه:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **عينة من الرموز**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
