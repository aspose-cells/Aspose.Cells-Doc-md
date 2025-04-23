---
title: HTML مع Node.js عبر C++
linktitle: HTML
type: docs
weight: 230
url: /ar/nodejs-cpp/convert-excel-to-html/
---

## **تحويل دفتر العمل في إكسل إلى HTML**
يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق HTML. لهذا الغرض، يستخدم Aspose.Cells فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) لتوفير المرونة للتحكم في عدة جوانب من مخرجات HTML.

يظهر المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف HTML باستخدام Node.js:

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to HTML format
workbook.save("out.html");
```


## **تحويل دفتر العمل في إكسل إلى ملفات MHTML**
يجمع MHTML بين HTML العادي والموارد الخارجية (أي المحتوى المرتبط عادة، مثل الصور والرسوم المتحركة والصوت، وغيرها) في ملف واحد. يُستخدم للبريد الإلكتروني بامتداد ملف .mht. يدعم Aspose.Cells قراءة وكتابة ملفات MHTML.

يظهر المثال البرمجي أدناه كيفية حفظ دفتر العمل كملف MHTML باستخدام Node.js:

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save file to mhtml format
workbook.save("out.mht");
```

## **مواضيع متقدمة**
- [تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل](/cells/ar/nodejs-cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML](/cells/ar/nodejs-cpp/avoid-exponential-notation-of-large-numbers-while-importing/)
- [تغيير نوع الوصلة HTML المستهدفة](/cells/ar/nodejs-cpp/change-the-html-link-target-type/)
- [تحويل Excel إلى HTML مع تلميحة](/cells/ar/nodejs-cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ar/nodejs-cpp/create-transparent-image-of-excel-worksheet/)
- [حذف المسافات الزائدة بعد فاصلة السطر أثناء استيراد HTML](/cells/ar/nodejs-cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML](/cells/ar/nodejs-cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [تعطيل تصدير النصوص الإطار وخصائص المستند](/cells/ar/nodejs-cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel إلى HTML - استخدام خيار PresentationPreference لتحسين التخطيط](/cells/ar/nodejs-cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML](/cells/ar/nodejs-cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML](/cells/ar/nodejs-cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [تصدير DataBar، ColorScale و IconSet لتنسيق الشروط أثناء تحويل Excel إلى HTML](/cells/ar/nodejs-cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [تصدير التعليقات أثناء حفظ ملف Excel إلى HTML](/cells/ar/nodejs-cpp/export-comments-while-saving-excel-file-to/)
- [تصدير خصائص المصنف والصفحة العمل في Excel إلى تحويل HTML](/cells/ar/nodejs-cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [تصدير Excel إلى HTML مع خطوط الشبكة](/cells/ar/nodejs-cpp/export-excel-to-html-with-gridlines/)
- [تصدير نطاق المنطقة المطبوعة إلى HTML](/cells/ar/nodejs-cpp/export-print-area-range-to/)
- [تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب](/cells/ar/nodejs-cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج](/cells/ar/nodejs-cpp/export-worksheet-css-separately-in-output/)
- [إخفاء المحتوى المتداخل باستخدام CrossHideRight أثناء الحفظ إلى HTML](/cells/ar/nodejs-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [بادئة أنماط عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId](/cells/ar/nodejs-cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [منع تصدير محتويات ورقة العمل المخفية عند الحفظ في HTML](/cells/ar/nodejs-cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [توفير مسار ملف HTML الخاص بورقة العمل المصدرة عبر واجهة IFilePathProvider](/cells/ar/nodejs-cpp/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/)
- [الاعتراف بالعلامات مغلقة ذاتياً](/cells/ar/nodejs-cpp/recognise-self-closing-tags/)
- [إظهار تعبئة التدرج لـ WordArt أثناء تحويل جداول البيانات إلى HTML](/cells/ar/nodejs-cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [تعيين عرض العمود إلى وحدة قابلة للتطويل مثل em أو النسبة المئوية](/cells/ar/nodejs-cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [تعيين الخط الافتراضي أثناء تقديم جدول بيانات إلى HTML](/cells/ar/nodejs-cpp/set-default-font-while-rendering-spreadsheet-to/)
- [تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType](/cells/ar/nodejs-cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [دعم تخطيط علامات DIV أثناء تحميل HTML إلى دفتر عمل Excel](/cells/ar/nodejs-cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)

- [تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML](/cells/ar/nodejs-cpp/enable-css-custom-properties-while-saving-to-html/)
