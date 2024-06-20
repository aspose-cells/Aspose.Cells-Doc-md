---
title: تصدير ورقة العمل CSS بشكل منفصل في ملف HTML الناتج
type: docs
weight: 80
url: /ar/java/export-worksheet-css-separately-in-output-html/
---

## **سيناريوهات الاستخدام المحتملة**

توفر Aspose.Cells ميزة تصدير ورقة العمل CSS بشكل منفصل عند تحويل ملف Excel الخاص بك إلى HTML. يرجى استخدام خاصية HtmlSaveOptions.ExportWorksheetCSSSeparately لهذا الغرض وتعيينها كـ true أثناء حفظ ملف Excel إلى تنسيق HTML.

## **تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج**

ينشئ الرمز البريدي المعاين أدناه ملف Excel ، ويضيف بعض النص في الخلية B5 بلون أحمر ثم يقوم بحفظه في تنسيق HTML باستخدام خاصية HtmlSaveOptions.ExportWorksheetCSSSeparately. يرجى الاطلاع على [HTML الناتج](60489780.zip) الذي تم إنشاؤه بواسطة الرمز للإشارة. ستجد ملف stylesheet.css داخله كنتيجة للرمز البريدي.

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "HTML-ExportWorksheetCSSSeparatelyInOutputHTML.java" >}}

## **تصدير جدول عمل واحد إلى HTML**

عند تحويل كتاب عمل يحتوي على ورق العمل المتعددة إلى HTML بواسطة Aspose.Cells ، يقوم بإنشاء ملف HTML مع مجلد يحتوي على CSS وملفات HTML متعددة. عند فتح هذا الملف HTML في المتصفح ، تكون علامات التبويب مرئية. نفس السلوك مطلوب لورقة العمل ذات ورقة واحدة عند تحويلها إلى HTML. في السابق ، لم يتم إنشاء مجلد منفصل لكتب العمل ذات الورقة العمل الفردية وتم إنشاء ملف HTML فقط. لا تظهر مثل هذا الملفات ال HTML علامة تبويب عند فتحها في المتصفح. يقوم Excel بإنشاء مجلد و HTML مناسبة لورقة العمل الفردية أيضًا وبالتالي يتم تنفيذ نفس السلوك باستخدام Aspose.Cells. يمكن تحميل ملف العينة من الرابط التالي لاستخدامه في الرمز العيني أدناه:

[sampleSingleSheet.xlsx](79527948.xlsx)

## **الكود المثالي**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-SetSingleSheetTabNameInHtml-1.java" >}}
