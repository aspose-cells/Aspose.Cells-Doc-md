---
title: تكوين الخطوط لعرض أوراق العمل باستخدام C++
linktitle: تكوين الخطوط لرسم الجداول الخليوية
type: docs
weight: 10
url: /ar/cpp/configuring-fonts-for-rendering-spreadsheets/
description: تعلم كيف تقوم بتكوين الخطوط لعرض أوراق العمل كصور، PDF، وXPS باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 توفر واجهات برمجة تطبيقات Aspose.Cells القدرة على عرض أوراق العمل بصيغ الصور بالإضافة إلى تحويلها إلى PDF وXPS. لتعظيم دقة التحويل، من الضروري أن تكون الخطوط المستخدمة في ورقة العمل متاحة في الدليل الافتراضي للخطوط في نظام التشغيل. إذا لم تكن الخطوط المطلوبة موجودة، ستحاول واجهات برمجة التطبيقات Aspose.Cells استبدال الخطوط المطلوبة بالخطوط المتاحة.

## **اختيار الخطوط**

 فيما يلي العملية التي تتبعها واجهات برمجة تطبيقات Aspose.Cells خلف الكواليس:

1. تحاول الواجهة البرمجية الخارجية العثور على الخطوط في نظام الملفات تطابق اسم الخط المستخدم في الجدول الخليوي.
1. إذا لم يتمكن API من العثور على الخطوط بنفس الاسم تمامًا، فإنه يحاول استخدام الخط الافتراضي المحدد تحت الخاصية [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) في الـWorkbook.
1. إذا لم يتمكن API من تحديد موقع الخط المحدد في خاصية [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) للـWorkbook، فإنه يحاول استخدام الخط المحدد في [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) أو الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/).
1. إذا لم يتمكن API من تحديد موقع الخط المحدد في [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) أو الخاصية [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/)، فإنه يحاول استخدام الخط المحدد في الخاصية [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/).
1. إذا لم يتمكن API من تحديد موقع الخط المحدد في الخاصية [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/)، فإنه يحاول اختيار الخطوط الأنسب من جميع الخطوط المتاحة.
1. أخيرًا، إذا لم يتمكن API من العثور على أي خطوط على نظام الملفات، فإنه يعرض الورقة باستخدام خط Arial.

## **تعيين مجلدات الخط المخصصة**

 يبحث API الخاص بـ Aspose.Cells في الدليل الافتراضي لنظام تشغيل الخطوط المطلوبة. إذا كانت الخطوط المطلوبة غير متاحة في دليل الخطوط في النظام، يبحث API في أدلة مخصصة (محددة من قبل المستخدم). توفر فئة [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) عدة طرق لضبط أدلة الخطوط المخصصة، كما هو موضح أدناه:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): تُفيد هذه الطريقة إذا كان هناك مجلد واحد فقط يجب تعيينه.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): هذه الطريقة مفيدة عندما تكون الخطوط موجودة في عدة مجلدات، ويرغب المستخدم في تعيين جميع المجلدات بشكل منفصل بدلاً من دمج جميع الخطوط في مجلد واحد.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): هذا الآلية مفيدة عندما يرغب المستخدم في تحميل الخطوط من مجلدات متعددة، أو ملف خط واحد، أو بيانات الخط من مصفوفة من البايتات.

{{% alert color="primary" %}}

كلا الطريقتين [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) و [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) تقبلان معلمة ثنائية من النوع Boolean. تمرير **true** كالمعلمة الثانية سيوجه واجهات برمجة التطبيقات Aspose.Cells للبحث في المجلدات الفرعية عن ملفات الخطوط.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

يرجى استخدام أي من الطرق المذكورة أعلاه في بداية التطبيق، أي قبل استدعاء أي كائنات أخرى من واجهات برمجة التطبيقات Aspose.Cells.

{{% /alert %}}

{{% alert color="primary" %}}

إذا تم استخدام جميع الطرق المذكورة أعلاه لتحديد مصادر الخطوط، فسيتم اعتماد إعدادات آخرى فقط.

{{% /alert %}}

## **آلية الاستبدال للخطوط**

توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا القدرة على تحديد خطوط بديلة لأغراض العرض. هذه الآلية مفيدة عندما لا يتوفر الخط المطلوب على الجهاز الذي يتم عليه التحويل. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل للخط المطلوب أصلاً. لتحقيق ذلك، كشفت واجهات برمجة التطبيقات Aspose.Cells عن طريقة [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/)، التي تقبل معلمين اثنين. المعامل الأول هو من نوع **string**، والذي يجب أن يكون اسم الخط الذي يحتاج إلى استبداله. المعامل الثاني هو مصفوفة من نوع **string**. يمكن للمستخدمين توفير قائمة بأسماء الخطوط كبديل عن الاسم الأصلي للخط (المحدد في المعامل الأول).

إليك سيناريو استخدام بسيط:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **تجميع المعلومات**

بالإضافة إلى الطرق المذكورة أعلاه، توفر واجهات برمجة التطبيقات Aspose.Cells أيضًا وسائل لجمع المعلومات حول المصادر والاستبدالات التي تم إعدادها:

1. ترجع طريقة [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) مصفوفة من نوع [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/) تحتوي على قائمة بمصادر الخطوط المحددة. إذا لم يتم تعيين مصادر، ستعيد طريقة [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) مصفوفة فارغة.
1. تقبل طريقة [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) معلمة من نوع **string**، تتيح لك تحديد اسم الخط الذي تم تعيين استبداله. إذا لم يتم تعيين استبدال للخط المحدد، ستعيد طريقة [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) قيمة null.

## **الموضوعات المتقدمة**
- [تعيين الخط الافتراضي أثناء تقديم جدول البيانات إلى الصور](/cells/ar/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [تعيين خاصية DefaultFont من PdfSaveOptions و ImageOrPrintOptions لتكون لها الأولوية](/cells/ar/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [صيغ الخط المدعمة](/cells/ar/cpp/supported-font-formats/)
