---
title: Настройка различных заголовков и нижних колонтитулов для разных страниц с помощью C++
linktitle: Настройка различных заголовков и нижних колонтитулов
type: docs
weight: 35
url: /ru/cpp/setting-different-headers-and-footers-for-pages-to-excel/
description: В этой статье представлен пример кода, показывающий, как программно установить различные заголовки и нижние колонтитулы настроек страницы листа Excel с помощью C++ API. Вы можете установить заголовки и нижние колонтитулы для первой страницы, нечетных страниц и четных страниц.
keywords: установить заголовок и нижний колонтитул Excel для первой страницы c++, установить для нечетных страниц c++, установить для четных страниц c++
---

{{% alert color="primary" %}}

MS Excel поддерживает установку различных заголовков и нижних колонтитулов для первой страницы, нечетных страниц и четных страниц, начиная с Excel 2007.
Aspose.Cells поддерживает ту же функцию.

{{% /alert %}}

## **Установка разных заголовков и нижних колонтитулов в MS Excel**

**![Установка различных заголовков и нижних колонтитулов](difpage.png)**

1. Нажмите **Макет страницы > Печать заголовков > Заголовок/нижний колонтитул**.
1. Установите флажок **Разные для нечетных и четных страниц** или **Первая страница особенная**.
1. Введите разные заголовки и нижние колонтитулы.

## **Установка разных заголовков и нижних колонтитулов с использованием Aspose.Cells**

Aspose.Cells ведет себя так же, как Excel.
Устанавливает флаги [PageSetup.IsHFDiffOddEven](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdiffoddeven/) и [PageSetup.IsHFDiffFirst](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/ishfdifffirst/) 
1. Введите разные заголовки и нижние колонтитулы.

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook wb;

    // Get the first worksheet's page setup
    PageSetup pageSetup = wb.GetWorksheets().Get(0).GetPageSetup();

    // Set different headers for odd and even pages
    pageSetup.SetIsHFDiffOddEven(true);
    pageSetup.SetHeader(1, u"I am the header of the Odd page.");
    pageSetup.SetEvenHeader(1, u"I am the header of the Even page.");

    // Set a different header for the first page
    pageSetup.SetIsHFDiffFirst(true);
    pageSetup.SetFirstPageHeader(1, u"I am the header of the First page.");

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
