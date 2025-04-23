---
title: إضافة خلايا إلى نافذة مراقبة الصيغة في إكسل باستخدام C++
linktitle: إضافة خلايا إلى نافذة المراقبة للصيغ
description: تعلم كيفية استخدام Aspose.Cells for C++ لإضافة الخلايا إلى نافذة المراقبة للصيغ في إكسل. تحميل أو إنشاء ملف إكسل، التلاعب بالخلايا، تعيين الصيغ، وحفظ الملف المعدل.
keywords: Aspose.Cells، إكسل، نافذة مراقبة الصيغ، خلايا، الإضافة، C++
type: docs
weight: 60
url: /ar/cpp/add-cells-to-microsoft-excel-formula-watch-window/
---

## **سيناريوهات الاستخدام المحتملة**

نافذة مراقبة إكسل هي أداة مفيدة لمراقبة قيم الخلايا وصيغها بسهولة في نافذة. يمكنك فتح *نافذة المراقبة* في إكسل بالنقر على *الصيغ > نافذة المراقبة*. لديها زر *إضافة مراقبة* الذي يمكن استخدامه لإضافة خلايا للفحص. بالمثل، يمكنك استخدام [**Worksheet.CellWatches.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells/cellwatchcollection/add/) لإضافة خلايا إلى *نافذة المراقبة* باستخدام API الخاص بـ Aspose.Cells.

## **إضافة الخلايا إلى نافذة مراقبة صيغ Microsoft Excel**

الكود النموذجي التالي يحدد صيغة الخليتين C1 وE1 ويضيفهما إلى نافذة المراقبة. ثم يحفظ العمل كملف إكسل مخرجا [ملف إكسل الناتج](67338481.xlsx). إذا قمت بفتح ملف إكسل الناتج وعرض *نافذة المراقبة*، سترى كلا الخليتين كما هو موضح في لقطة الشاشة هذه.

![todo:image_alt_text](add-cells-to-microsoft-excel-formula-watch-window_1.png)

## **الكود المثالي**

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Access first worksheet
    Worksheet ws = wb.GetWorksheets().Get(0);

    // Put some integer values in cell A1 and A2
    ws.GetCells().Get(u"A1").PutValue(10);
    ws.GetCells().Get(u"A2").PutValue(30);

    // Access cell C1 and set its formula
    Cell c1 = ws.GetCells().Get(u"C1");
    c1.SetFormula(u"=Sum(A1,A2)");

    // Add cell C1 into cell watches by name
    ws.GetCellWatches().Add(c1.GetName());

    // Access cell E1 and set its formula
    Cell e1 = ws.GetCells().Get(u"E1");
    e1.SetFormula(u"=A2*A1");

    // Add cell E1 into cell watches by its row and column indices
    ws.GetCellWatches().Add(e1.GetRow(), e1.GetColumn());

    // Save workbook to output XLSX format
    wb.Save(u"outputAddCellsToMicrosoftExcelFormulaWatchWindow.xlsx", SaveFormat::Xlsx);

    std::cout << "Workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
