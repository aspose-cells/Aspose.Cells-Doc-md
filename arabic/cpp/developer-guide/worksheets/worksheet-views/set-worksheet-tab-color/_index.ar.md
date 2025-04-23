---
title: تغيير لون علامة التبويب للورقة باستخدام ++C
linktitle: تعيين لون علامة التبويب للورقة العمل
type: docs
weight: 120
url: /ar/cpp/set-worksheet-tab-color/
description: يعرض هذا المقال شفرة عينة لضبط لون علامة تبويب ورقة العمل في إكسل برمجياً باستخدام API أو المكتبة C++.
keywords: ضبط لون علامة تبويب إكسل باستخدام ++C، الشفرة لضبط لون علامة تبويب إكسل باستخدام ++C
---

{{% alert color="primary" %}}

تسمح Aspose.Cells لك بتغيير لون علامات تبويب ورق العمل الفردية لتمييزها عن البقية. على سبيل المثال، يمكنك جعل تكاليف بلون أحمر، ومبيعات بلون أخضر، وأصول بلون أزرق، وما إلى ذلك.

{{% /alert %}}

## **ضبط لون علامة تبويب ورق العمل باستخدام Microsoft Excel**
1. انقر بزر الماوس الأيمن فوق علامة تبويب في ورقة العلامات في أسفل ورقة العمل الحالية.
1. حدد **لون العلامة التبويب**.
1. حدد لونًا من اللوحة.
1. انقر على **موافق**.

## **تعيين لون علامة تبويب الورقة العمل باستخدام Aspose.Cells**
الشيفرة المثالية أدناه تظهر كيفية تعيين لون علامة تبويب باستخدام Aspose.Cells.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Path of input Excel file
    U16String inputFilePath = srcDir + u"Book1.xlsx";

    // Path of output Excel file
    U16String outputFilePath = outDir + u"worksheettabcolor.out.xls";

    // Create workbook
    Workbook workbook(inputFilePath);

    // Get the first worksheet in the book
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the tab color to red
    worksheet.SetTabColor(Color::Red());

    // Save the Excel file
    workbook.Save(outputFilePath);

    std::cout << "Worksheet tab color set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
