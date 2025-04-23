---
title: Определить, является ли размер бумаги листа автоматически настроенным с помощью C++
linktitle: Определение автоматического размера бумаги листа
type: docs
weight: 90
url: /ru/cpp/determine-if-paper-size-of-worksheet-is-automatic/
description: Эта статья объясняет, как использовать C++ API или образец кода библиотеки для определения, является ли размер бумаги листа автоматически настроенным программно.
keywords: определить, автоматически ли размер бумаги листа c++
---

## **Возможные сценарии использования**

Чаще всего размер бумаги листа автоматический. Когда он автоматический, его часто устанавливают как *Letter*. Иногда пользователь устанавливает размер бумаги листа согласно своим требованиям. В этом случае размер бумаги не является автоматическим. Вы можете определить, является ли размер бумаги листа автоматическим, используя свойство [**PageSetup.IsAutomaticPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/isautomaticpapersize/) класса **Worksheet**.

## **Определение автоматического размера бумаги листа**

В приведенном ниже образце кода загружаются следующие два файлы Excel

- [samplePageSetupIsAutomaticPaperSize-False.xlsx](48496681.xlsx)
- [samplePageSetupIsAutomaticPaperSize-True.xlsx](48496682.xlsx)

и определяет, является ли размер бумаги их первого листа автоматическим. В Microsoft Excel вы можете проверить, является ли размер бумаги автоматическим, через окно настройки страницы, как показано на этом скриншоте.

![todo:image_alt_text](determine-if-paper-size-of-worksheet-is-automatic_1.png)

## **Образец кода**

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C

    // Source directory path
    U16String sourceDir(u"..\\Data\\01_SourceDirectory\\");

    // Load the first workbook having automatic paper size false
    Workbook wb1(sourceDir + u"samplePageSetupIsAutomaticPaperSize-False.xlsx");

    // Load the second workbook having automatic paper size true
    Workbook wb2(sourceDir + u"samplePageSetupIsAutomaticPaperSize-True.xlsx");

    // Access the first worksheet of both workbooks
    Worksheet ws11 = wb1.GetWorksheets().Get(0);
    Worksheet ws12 = wb2.GetWorksheets().Get(0);

    // Print the PageSetup.IsAutomaticPaperSize property of both worksheets
    std::wcout << u"First Worksheet of First Workbook - IsAutomaticPaperSize: " << ws11.GetPageSetup().IsAutomaticPaperSize() << std::endl;
    std::wcout << u"First Worksheet of Second Workbook - IsAutomaticPaperSize: " << ws12.GetPageSetup().IsAutomaticPaperSize() << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Вывод в консоль**

Вот вывод в консоль приведенного выше образца кода при выполнении с данными образцами файлов Excel.

{{< highlight java >}}

First Worksheet of First Workbook - IsAutomaticPaperSize: False

First Worksheet of Second Workbook - IsAutomaticPaperSize: True

{{< /highlight >}}
