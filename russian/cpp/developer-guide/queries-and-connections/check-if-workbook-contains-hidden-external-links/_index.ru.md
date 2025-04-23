---
title: Проверка наличия скрытых внешних ссылок в книге с помощью C++
linktitle: Проверка, содержит ли рабочая книга скрытые внешние ссылки
type: docs
weight: 230
url: /ru/cpp/check-if-workbook-contains-hidden-external-links/
description: Узнайте, как обнаружить скрытые внешние ссылки в книгах Excel с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**
Иногда в книге есть внешние ссылки, которые скрыты и их нельзя просмотреть в Microsoft Excel. Aspose.Cells извлекает все внешние ссылки, видимые или скрытые. Однако вы можете проверить свойство [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/), чтобы определить их видимость.

## **Проверка, содержит ли рабочая книга скрытые внешние ссылки**
Следующий пример кода загружает [исходный файл Excel](5115413.xlsx), содержащий скрытые внешние ссылки. Эти ссылки нельзя просмотреть в Microsoft Excel, но они присутствуют в книге. После вывода [ExternalLink.GetDataSource()](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/getdatasource/) и [ExternalLink.IsReferred](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isreferred/) свойств, он выводит свойство [ExternalLink.IsVisible](https://reference.aspose.com/cells/cpp/aspose.cells/externallink/isvisible/). В консольном выводе ниже видно, что все внешние ссылки скрыты.

### **Образец кода**
```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Loads the workbook which contains hidden external links
    Workbook workbook(srcDir + u"sample.xlsx");

    // Access the external link collection of the workbook
    ExternalLinkCollection links = workbook.GetWorksheets().GetExternalLinks();

    // Print all the external links and check their IsVisible property
    for (int i = 0; i < links.GetCount(); i++)
    {
        ExternalLink link = links.Get(i);
        std::cout << "Data Source: " << link.GetDataSource().ToUtf8() << std::endl;
        std::cout << "Is Visible: " << (link.IsVisible() ? "true" : "false") << std::endl;
        std::cout << std::endl;
    }

    Aspose::Cells::Cleanup();
}
```

### **Вывод в консоль**
Вот вывод консоли вышеприведенного образца кода при выполнении с заданным [образцовым файлом Excel](5115413.xlsx).

{{< highlight java >}}

Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls

Is Referred: True

Is Visible: False

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls

Is Referred: True

Is Visible: False

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls

Is Referred: True

Is Visible: False

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls

Is Referred: True

Is Visible: False

{{< /highlight >}}
