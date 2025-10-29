--- 
title: كيفية التحقق من حالة التجميد بدون إكسل باستخدام ++C 
linktitle: الحالة المجمدة 
type: docs 
weight: 190 
url: /ar/cpp/how-to-check-frozen-state-of-excel-worksheet 
description: في هذا المقال، ستتعلم كيفية فحص الحالة المجمدة لورقة عمل Excel برمجياً باستخدام C++ مع API Aspose.Cells. 
--- 

## **مقدمة** 

في هذا المقال، سوف نتعلم كيفية فحص الحالة المجمدة لورقة عمل Excel برمجياً. يمكننا ببساطة معرفة ما إذا كانت ورقة العمل مجمدة أو مقسمة في MS Excel. لكن هل هناك طريقة لمعرفة ما إذا كانت مجمدة أو مقسمة باستخدام C++؟ يمكننا فعل ذلك باستخدام Aspose.Cells for C++. 

## **هل النوافذ مجمدة** 
باستخدام Aspose.Cells for C++، يمكننا التحقق مما إذا كانت النافذة مجمدة وكم عدد الصفوف والأعمدة المقفلة. 

يرجى استخدام خاصية [**GetPaneState()**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getpanestate/) للتحقق من حالة ألواح النافذة والحصول على الصفوف والأعمدة المقفلة باستخدام طريقة [**Worksheet::GetFreezedPanes**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getfreezedpanes/). 
1. إنشاء سجل العمل لفتح الملف. 
2. التحقق ما إذا كانت ورقة العمل مجمدة. 
3. احصل على الصفوف والأعمدة المقفلة. 

```c++
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create the workbook from the specified file
    Workbook workbook(u"Frozen.xlsx");

    // Get the first worksheet from the workbook
    Worksheet sheet = workbook.GetWorksheets().Get(0);

    // Check whether the worksheet is frozen
    if (sheet.GetPaneState() == PaneStateType::Frozen || sheet.GetPaneState() == PaneStateType::FrozenSplit)
    {
        int32_t row = 0, column = 0;
        int32_t rows = 0, columns = 0;

        // Get the locked rows and columns
        sheet.GetFreezedPanes(row, column, rows, columns);

        // Output the details if needed (just for demonstration)
        std::cout << "Frozen panes at Row: " << row << ", Column: " << column << ", Total Frozen Rows: " 
                  << rows << ", Total Frozen Columns: " << columns << std::endl;
    }

    Aspose::Cells::Cleanup();
}
``` 

{{< app/cells/assistant language="cpp" >}}
