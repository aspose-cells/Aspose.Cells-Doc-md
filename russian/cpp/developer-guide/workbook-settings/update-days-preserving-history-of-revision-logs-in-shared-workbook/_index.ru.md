---
title: Обновление дней с сохранением истории журналов изменений в общем рабочем с помощью C++
linktitle: Обновление дней, сохраняющих историю журналов версий в общей книге
type: docs
weight: 80
url: /ru/cpp/update-days-preserving-history-of-revision-logs-in-shared-workbook/
description: Научитесь обновлять количество дней для сохранения истории в общем рабочем с помощью Aspose.Cells с C++.
---

## **Возможные сценарии использования**

Если вы делитесь книгой, у вас есть опция ***Сохранять историю изменений на протяжении N дней***, как показано на следующем скриншоте. Вы можете обновить количество дней для сохранения истории с помощью Aspose.Cells с [**WorksheetCollection.GetDaysPreservingHistory()**](https://reference.aspose.com/cells/cpp/aspose.cells.revisions/revisionlogcollection/getdayspreservinghistory/) свойством.

![todo:image_alt_text](update-days-preserving-history-of-revision-logs-in-shared-workbook_1.png)

## **Обновление дней, сохраняющих историю журналов версий в общей книге**

В следующем образце кода создается пустая книга, затем ее делят и обновляются журналы ревизии для сохранения истории на 7 дней, что обычно составляет 30 дней. Пожалуйста, обратитесь к [выходному файлу Excel](60489773.xlsx), созданному кодом в качестве справки.

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create empty workbook
    Workbook wb;

    // Share the workbook
    wb.GetSettings().SetShared(true);

    // Update DaysPreservingHistory of RevisionLogs
    wb.GetWorksheets().GetRevisionLogs().SetDaysPreservingHistory(7);

    // Save the workbook
    wb.Save(u"outputShared_DaysPreservingHistory.xlsx");

    std::cout << "Workbook shared and saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
