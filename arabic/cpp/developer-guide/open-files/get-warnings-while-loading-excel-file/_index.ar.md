---
title: الحصول على تحذيرات أثناء تحميل ملف Excel باستخدام C++
linktitle: الحصول على تحذيرات أثناء تحميل ملف إكسل
type: docs
weight: 110
url: /ar/cpp/get-warnings-while-loading-excel-file/
description: تعلم كيف تمسك وتعالج التحذيرات أثناء تحميل ملفات Excel باستخدام Aspose.Cells for C++.
---

## **سيناريوهات الاستخدام المحتملة**

 أحيانًا، يحاول المستخدم تحميل دفتر عمل معطوب بعض الشيء ولكنه لا يزال قابلاً للتحميل. في مثل هذه الحالات، يرمي Aspose.Cells تحذيرات أثناء تحميل دفتر العمل. يمكنك التقاط هذه التحذيرات من خلال تنفيذ الواجهة [**IWarningCallback**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/) وتعيين الخاصية [**LoadOptions.GetWarningCallback()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getwarningcallback/).

## **الحصول على تحذيرات أثناء تحميل ملف إكسل**

يشرح الكود النموذجي التالي كيفية الحصول على تحذيرات أثناء تحميل ملف Excel. يقوم الكود بتحميل ملف Excel عينة (sampleDuplicateDefinedName.xlsx)، والذي يرمي بتحذير [**DuplicateDefinedName**](https://reference.aspose.com/cells/cpp/aspose.cells/warningtype/) عند التحميل. ثم يتم التقاط هذا التحذير بواسطة طريقة [**IWarningCallback.Warning()**](https://reference.aspose.com/cells/cpp/aspose.cells/iwarningcallback/warning/)، والتي تطبع رسائل التحذير على وحدة التحكم. ثم يحفظ الكود دفتر العمل كـ ملف Excel مخرجي (outputDuplicateDefinedName.xlsx). إذا قمت بفتح ملف Excel النموذجي في Microsoft Excel، فسيعرض أيضًا هذا التحذير، كما هو موضح في لقطة الشاشة أدناه. يرجى أيضًا التحقق من مخرجات وحدة التحكم للكود أدناه لمزيد من الفهم.

![todo:image_alt_text](get-warnings-while-loading-excel-file_1.png)

## **الكود المثالي**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

class WarningCallback : public IWarningCallback {
public:
    void Warning(WarningInfo& warningInfo) override {
        if (warningInfo.GetType() == ExceptionType::DefinedName) {
            std::cout << "Defined Name Warning: " << warningInfo.GetDescription().ToUtf8() << std::endl;
        }
    }
};

int main() {
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    LoadOptions options;
    WarningCallback callback;
    options.SetWarningCallback(&callback);

    U16String inputFilePath = srcDir + u"sampleDuplicateDefinedName.xlsx";
    Workbook book(inputFilePath, options);

    U16String outputFilePath = outDir + u"outputDuplicateDefinedName.xlsx";
    book.Save(outputFilePath);

    std::cout << "Workbook saved successfully with warning handling!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **مخرجات الوحدة**

إليك مخرجات وحدة التحكم للكود أعلاه عند تنفيذه مع [ملف إكسل عيني](sampleDuplicateDefinedName.xlsx) المقدم.

{{< highlight java >}}

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Introduction!$D$16:$D$17

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:Panel!$B$228

Duplicate Defined Name Warning: Name:PRINT_AREA;ReferTo:'Queries '!$D$14:$D$16

{{< /highlight >}}
