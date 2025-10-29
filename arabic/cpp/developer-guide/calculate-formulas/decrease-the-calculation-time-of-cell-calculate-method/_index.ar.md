---
title: خفض وقت حساب طريقة Cell.Calculate باستخدام C++
linktitle: خفض وقت حساب Cell.Calculate
description: يقدم هذا المقال كيفية استخدام مكتبة Aspose.Cells لتقليل وقت حساب أسلوب الحساب في خلايا Microsoft Excel. من خلال تحميل ملف Excel موجود أو إنشاء ملف جديد، يمكننا استخدام الأساليب المقدمة من Aspose.Cells لتحسين أداء أسلوب الحساب في الخلية وتحسين أدائه. وأخيرًا، نحفظ الملف المعدل على القرص.
keywords: Aspose.Cells، Excel، أساليب حساب الخلية، تحسين، أداء، تقليل وقت الحساب
type: docs
weight: 100
url: /ar/cpp/decrease-the-calculation-time-of-cell-calculate-method/
---

## **سيناريوهات الاستخدام المحتملة**

عادةً، نوصي المستخدمين باستدعاء طريقة [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/calculateformula/) مرة واحدة ثم الحصول على القيم المحسوبة للخلايا الفردية. لكن أحيانًا، لا يرغب المستخدمون في حساب كامل دفتر العمل. إنهم فقط يرغبون في حساب خلية واحدة. يوفر Aspose.Cells الخاصية [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/) التي يمكنك ضبطها إلى **false**، مما يقلل بشكل كبير من وقت حساب الخلايا الفردية. لأنه عندما تكون الخاصية التكرارية مضبوطة على **true**، يتم إعادة حساب جميع التوابع في كل استدعاء. ولكن عندما تكون الخاصية التكرارية **false**، يُحسب التوابع المعتمدة مرة واحدة فقط ولا يُعاد حسابها في الاستدعاءات التالية.

## **تخفيض وقت حساب الخلية لوسيلة (.Calculate())**

توضح الشفرة النموذجية التالية استخدام خاصية [**CalculationOptions.GetRecursive()**](https://reference.aspose.com/cells/cpp/aspose.cells/calculationoptions/getrecursive/). يرجى تنفيذ هذه الشفرة مع [ملف إكسل النموذجي](5113710.xlsx) والتحقق من إخراج وحدة التحكم الخاص بها. ستجد أن ضبط الخاصية التكرارية على **false** قد قلل بشكل كبير من وقت الحساب. يرجى أيضًا قراءة التعليقات لفهم أفضل لهذه الخاصية.

```c++
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

void TestCalcTimeRecursive(bool isRecursive) {
    Workbook* workbook = new Workbook();
    CalculationOptions options;
    options.SetRecursive(isRecursive);

    auto start = std::chrono::high_resolution_clock::now();
    workbook->CalculateFormula(&options);
    auto end = std::chrono::high_resolution_clock::now();

    auto duration = std::chrono::duration_cast<std::chrono::milliseconds>(end - start).count();
    std::cout << "Time (recursive=" << isRecursive << "): " << duration << " ms" << std::endl;

    delete workbook;
}

int main() {
    Aspose::Cells::Startup();

    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);

    Aspose::Cells::Cleanup();
    return 0;
}
```

```cpp
#include <iostream>
#include <chrono>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std::chrono;

void TestCalcTimeRecursive(bool rec) {
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    Workbook wb(srcDir + u"sample.xlsx");
    Worksheet ws = wb.GetWorksheets().Get(0);
    CalculationOptions opts;
    opts.SetRecursive(rec);

    auto start = high_resolution_clock::now();
    for (int i = 0; i < 1000000; i++) {
        ws.GetCells().Get(u"A1").Calculate(opts);
    }
    auto stop = high_resolution_clock::now();

    auto duration = duration_cast<milliseconds>(stop - start);
    long estimatedTime = duration.count() / 1000;
    std::cout << "Recursive " << rec << ": " << estimatedTime << " seconds" << std::endl;
}

int main() {
    Aspose::Cells::Startup();
    TestCalcTimeRecursive(true);
    TestCalcTimeRecursive(false);
    Aspose::Cells::Cleanup();
    return 0;

}
```

## **مخرجات الوحدة**

هذه هي مخرجات وحدة التحكم للشفرة النموذجية أعلاه عند تنفيذها باستخدام [ملف إكسل النموذجي](5113710.xlsx) على جهازنا. يرجى ملاحظة أن الإخراج الخاص بك قد يختلف، لكن الوقت المنقضي بعد ضبط الخاصية التكرارية إلى **false** دائمًا ما يكون أقل من عند ضبطها على **true**.

{{< highlight java >}}

Recursive True: 96 seconds

Recursive False: 42 seconds

{{< /highlight >}}
{{< app/cells/assistant language="cpp" >}}
