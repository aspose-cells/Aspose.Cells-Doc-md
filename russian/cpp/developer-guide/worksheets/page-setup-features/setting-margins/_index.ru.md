---
title: Настройка полей с помощью C++
linktitle: Настройка полей
type: docs
weight: 20
url: /ru/cpp/setting-margins/
description: Узнайте, как установить поля листа Excel с помощью C++. Этот гид охватывает установку полей страницы, центрирование содержимого и настройку полей заголовка и подвала программным способом с использованием Aspose.Cells for C++.
keywords: установить поля листа Excel по центру c++, установить поля заголовков и подвалов листа c++
---

{{% alert color="primary" %}}

Aspose.Cells полностью поддерживает параметры настройки страниц Microsoft Excel. Разработчики могут настраивать параметры страницы для листов, чтобы контролировать процесс печати. В данном разделе рассматривается, как использовать Aspose.Cells для настройки полей страницы.

{{% /alert %}}

## **Установка полей**

Aspose.Cells предоставляет класс, [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/), представляющий файл Excel. Класс [**Workbook**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/) содержит коллекцию [**Worksheets**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheetcollection/), которая позволяет получить доступ к каждому листу Excel. Лист представлен классом [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/).

Класс [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/) предоставляет свойство [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), используемое для установки параметров настройки страницы для листа. Атрибут [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) — это объект класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), который позволяет разработчикам задавать различные параметры макета страницы для распечатываемого листа. Класс [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) содержит различные свойства и методы для установки параметров настройки страницы.

### **Поля страницы**

Установка полей страницы (слева, справа, сверху, снизу) с помощью элементов класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/). Ниже приведены некоторые методы, используемые для указания полей страницы:

- [**GetLeftMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getleftmargin/)
- [**GetRightMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getrightmargin/)
- [**GetTopMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/gettopmargin/)
- [**GetBottomMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getbottommargin/)

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Set bottom, left, right, and top page margins
    pageSetup.SetBottomMargin(2);
    pageSetup.SetLeftMargin(1);
    pageSetup.SetRightMargin(1);
    pageSetup.SetTopMargin(3);

    // Save the Workbook
    workbook.Save(outDir + u"SetMargins_out.xls");

    std::cout << "Margins set successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Центрирование на странице**

Можно разместить что-либо по горизонтали и вертикали по центру страницы. Для этого существуют полезные элементы класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), [**GetCenterHorizontally()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcenterhorizontally/) и [**GetCenterVertically()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getcentervertically/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Center on page Horizontally and Vertically
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered page setup!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Поля верхнего и нижнего колонтитулов**

Установка полей заголовка и подвала с помощью элементов класса [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/), таких как [**GetHeaderMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getheadermargin/) и [**GetFooterMargin()**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/getfootermargin/).

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

    // Create a workbook object
    Workbook workbook;

    // Get the worksheets in the workbook
    WorksheetCollection worksheets = workbook.GetWorksheets();

    // Get the first (default) worksheet
    Worksheet worksheet = worksheets.Get(0);

    // Get the pagesetup object
    PageSetup pageSetup = worksheet.GetPageSetup();

    // Specify Header / Footer margins
    pageSetup.SetHeaderMargin(2);
    pageSetup.SetFooterMargin(2);

    // Save the Workbook
    workbook.Save(outDir + u"CenterOnPage_out.xls");

    std::cout << "Workbook saved successfully with centered header and footer margins!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
