---
title: HTML باستخدام C++
linktitle: HTML
type: docs
weight: 230
url: /ar/cpp/convert-excel-to-html/
description: تحويل إكسل إلى تنسيق HTML و MHTML باستخدام Aspose.Cells مع C++.
---

## **تحويل دفتر العمل في إكسل إلى HTML**
يوفر API Aspose.Cells دعمًا للتصدير إلى تنسيق HTML. لهذا الغرض، يستخدم Aspose.Cells فئة [**HtmlSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions) لتوفير المرونة للتحكم في عدة جوانب من مخرجات HTML.

يوضح المثال التالي كيفية حفظ المصنف كملف HTML باستخدام C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    Workbook workbook(u"Book1.xlsx");

    // Save file to HTML format
    workbook.Save(u"out.html");

    std::cout << "Workbook saved to HTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **تحويل دفتر العمل في إكسل إلى ملفات MHTML**
يجمع MHTML بين HTML العادي والموارد الخارجية (أي المحتوى المرتبط عادة، مثل الصور والرسوم المتحركة والصوت، وغيرها) في ملف واحد. يُستخدم للبريد الإلكتروني بامتداد ملف .mht. يدعم Aspose.Cells قراءة وكتابة ملفات MHTML.

يعرض المثال التالي كيفية حفظ المصنف كملف MHTML باستخدام C++:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Load your source workbook
    U16String inputFilePath(u"Book1.xlsx");
    std::unique_ptr<Workbook> workbook = std::make_unique<Workbook>(inputFilePath);

    // Save file to mhtml format
    U16String outputFilePath(u"out.mht");
    workbook->Save(outputFilePath, SaveFormat::MHtml);

    std::cout << "Workbook saved to MHTML format successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **مواضيع متقدمة**
- [تلائم الأعمدة والصفوف تلقائيًا أثناء تحميل HTML في دفتر العمل](/cells/ar/cpp/autofit-columns-and-rows-while-loading-html-in-workbook/)
- [تجنب العلامة العلمية للأرقام الكبيرة أثناء الاستيراد من HTML](/cells/ar/cpp/avoid-exponential-notation-of-large-numbers-while-importing-from/)
- [تغيير نوع الوصلة HTML المستهدفة](/cells/ar/cpp/change-the-html-link-target-type/)
- [تحويل Excel إلى HTML مع تلميحة](/cells/ar/cpp/convert-excel-to-html-with-tooltip/)
- [Create Transparent Image of Excel Worksheet](/cells/ar/cpp/create-transparent-image-of-excel-worksheet/)
- [حذف المسافات الزائدة بعد فاصلة السطر أثناء استيراد HTML](/cells/ar/cpp/delete-redundant-spaces-after-line-break-while-importing/)
- [تعطيل كشف التعليقات عند الاستخدام التسلسلي لأسفل عند الحفظ في HTML](/cells/ar/cpp/disable-downlevel-revealed-comments-while-saving-to/)
- [تعطيل تصدير النصوص الإطار وخصائص المستند](/cells/ar/cpp/disable-exporting-frame-scripts-and-document-properties/)
- [Excel إلى HTML - استخدام خيار PresentationPreference لتحسين التخطيط](/cells/ar/cpp/excel-to-html-use-presentationpreference-option-for-better-layout/)
- [استبعاد الأنماط غير المستخدمة أثناء تحويل Excel إلى HTML](/cells/ar/cpp/exclude-unused-styles-during-excel-to-html-conversion/)
- [توسيع النص من اليمين إلى اليسار أثناء تصدير ملف Excel إلى HTML](/cells/ar/cpp/expanding-text-from-right-to-left-while-exporting-excel-file-to/)
- [تصدير DataBar، ColorScale و IconSet لتنسيق الشروط أثناء تحويل Excel إلى HTML](/cells/ar/cpp/export-databar-colorscale-and-iconset-conditional-formatting-while-excel-to-html-conversion/)
- [تصدير التعليقات أثناء حفظ ملف Excel إلى HTML](/cells/ar/cpp/export-comments-while-saving-excel-file-to/)
- [تصدير خصائص المصنف والصفحة العمل في Excel إلى تحويل HTML](/cells/ar/cpp/export-document-workbook-and-worksheet-properties-in-excel-to-html-conversion/)
- [تصدير Excel إلى HTML مع خطوط الشبكة](/cells/ar/cpp/export-excel-to-html-with-gridlines/)
- [تصدير نطاق المنطقة المطبوعة إلى HTML](/cells/ar/cpp/export-print-area-range-to/)
- [تصدير نمط الحدود المماثل عند عدم دعم نمط الحدود من قبل متصفحات الويب](/cells/ar/cpp/export-similar-border-style-when-border-style-is-not-supported-by-web-browsers/)
- [تصدير ورق العمل CSS بشكل منفصل في ملف HTML الناتج](/cells/ar/cpp/export-worksheet-css-separately-in-output/)
- [إخفاء المحتوى المتداخل باستخدام CrossHideRight أثناء الحفظ إلى HTML](/cells/ar/cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/)
- [بادئة أنماط عناصر الجدول باستخدام خاصية HtmlSaveOptions.TableCssId](/cells/ar/cpp/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [منع تصدير محتويات ورقة العمل المخفية عند الحفظ في HTML](/cells/ar/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/)
- [الاعتراف بالعلامات مغلقة ذاتياً](/cells/ar/cpp/recognise-self-closing-tags/)
- [إظهار تعبئة التدرج لـ WordArt أثناء تحويل جداول البيانات إلى HTML](/cells/ar/cpp/render-gradient-fill-for-the-wordart-while-converting-spreadsheets-to/)
- [تعيين عرض العمود إلى وحدة قابلة للتطويل مثل em أو النسبة المئوية](/cells/ar/cpp/set-column-width-to-scalable-unit-like-em-or-percent/)
- [تعيين الخط الافتراضي أثناء تقديم جدول بيانات إلى HTML](/cells/ar/cpp/set-default-font-while-rendering-spreadsheet-to/)
- [تحديد كيفية تقاطع السلسلة في HTML الناتج باستخدام HtmlCrossType](/cells/ar/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
- [دعم تخطيط علامات DIV أثناء تحميل HTML إلى دفتر عمل Excel](/cells/ar/cpp/support-the-layout-of-div-tags-while-loading-html-to-excel-workbook/)
- [تمكين خصائص CSS المخصصة أثناء الحفظ إلى HTML](/cells/ar/cpp/enable-css-custom-properties-while-saving-to-html/)
{{< app/cells/assistant language="cpp" >}}
