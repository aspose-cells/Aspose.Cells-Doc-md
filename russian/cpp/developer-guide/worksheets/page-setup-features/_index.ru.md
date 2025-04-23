---
title: Функции настройки страницы с помощью C++
linktitle: Функции настройки страницы
type: docs
weight: 60
url: /ru/cpp/page-setup-features/
description: Узнайте, как настроить параметры страницы в файлах Excel с помощью Aspose.Cells и C++.
---

## **Возможности настройки страницы**

Aspose.Cells предоставляет широкий набор функций для настройки параметров страницы в файлах Excel. Эти функции позволяют управлять различными аспектами макета страницы, такими как поля, ориентация, размер бумаги и другие.

### **Настройка полей страницы**

Вы можете задать поля страницы для листа с помощью класса `PageSetup`. Ниже показан пример установки верхнего, нижнего, левого и правого полей:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageMargins() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set page margins
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetTopMargin(1.0);
    pageSetup.SetBottomMargin(1.0);
    pageSetup.SetLeftMargin(0.75);
    pageSetup.SetRightMargin(0.75);

    // Save the workbook
    workbook.Save("PageMargins.xlsx");
}
```

### **Настройка ориентации страницы**

Вы можете установить ориентацию страницы — портрет или альбом — с помощью класса `PageSetup`. Ниже пример установки альбомной ориентации:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageOrientation() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrientation(PageOrientationType::Landscape);
    workbook.Save("PageOrientation.xlsx");
}
```

### **Настройка размера бумаги**

Вы можете задать размер бумаги для печати с помощью класса `PageSetup`. Ниже пример установки размера A4:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPaperSize() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPaperSize(PaperSizeType::PaperA4);
    workbook.Save("PaperSize.xlsx");
}
```

### **Настройка области печати**

Вы можете определить конкретный диапазон ячеек для печати с помощью класса `PageSetup`. Ниже пример установки области печати:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintArea() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintArea("A1:D10");

    // Save the workbook
    workbook.Save("PrintArea.xlsx");
}
```

### **Настройка разрывов страниц**

Вы можете вставлять разрывы страниц в лист для контроля, где заканчивается страница и начинается новая. Ниже пример вставки горизонтального разрыва страницы:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPageBreaks() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Insert a horizontal page break at row 10
    worksheet.GetHorizontalPageBreaks().Add("A10");

    // Save the workbook
    workbook.Save("PageBreaks.xlsx");
}
```

### **Настройка заголовка и нижнего колонтитула**

Вы можете настроить заголовок и нижний колонтитул листа с помощью класса `PageSetup`. Ниже пример установки пользовательского заголовка и нижнего колонтитула:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetHeaderFooter() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set custom header and footer
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&CHeader Text");
    pageSetup.SetFooter(0, "&CFooter Text");

    // Save the workbook
    workbook.Save("HeaderFooter.xlsx");
}
```

### **Настройка заголовков для печати**

Вы можете указать строки или столбцы для повторения вверху или слева каждого распечатываемого листа с помощью класса `PageSetup`. Ниже пример установки заголовков для печати:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintTitles() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print titles
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintTitleRows("$1:$1");
    pageSetup.SetPrintTitleColumns("$A:$A");

    // Save the workbook
    workbook.Save("PrintTitles.xlsx");
}
```

### **Настройка качества печати**

Вы можете задать качество печати для листа с помощью класса `PageSetup`. Ниже пример установки качества печати:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintQuality() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print quality
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintQuality(600);

    // Save the workbook
    workbook.Save("PrintQuality.xlsx");
}
```

### **Настройка порядка печати**

Вы можете установить порядок печати для листа с помощью класса `PageSetup`. Ниже пример установки порядка "Слева направо, затем вниз":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintOrder() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetOrder(PrintOrderType::OverThenDown);
    workbook.Save("PrintOrder.xlsx");
}
```

### **Настройка отображения сетки при печати**

Вы можете управлять тем, будет ли отображаться сетка при печати, используя класс `PageSetup`. Следующий пример демонстрирует, как включить печать сетки:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintGridlines() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of gridlines
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintGridlines(true);

    // Save the workbook
    workbook.Save("PrintGridlines.xlsx");
}
```

### **Настройка отображения заголовков при печати**

Вы можете управлять тем, будут ли отображаться заголовки строк и столбцов при печати, используя класс `PageSetup`. Следующий пример демонстрирует, как включить печать заголовков:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintHeadings() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable printing of headings
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintHeadings(true);

    // Save the workbook
    workbook.Save("PrintHeadings.xlsx");
}
```

### **Настройка черно-белой печати**

Вы можете управлять тем, печатать ли рабочий лист в черно-белом режиме, используя класс `PageSetup`. Следующий пример демонстрирует, как включить черно-белую печать:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintBlackAndWhite() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Enable black and white printing
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetBlackAndWhite(true);

    // Save the workbook
    workbook.Save("PrintBlackAndWhite.xlsx");
}
```

### **Настройка черновика печати**

Вы можете управлять тем, печатать ли рабочий лист в черновом режиме, используя класс `PageSetup`. Следующий пример показывает, как включить печать в черновом режиме:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintDraft() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintDraft(true);
    workbook.Save("PrintDraft.xlsx");
}
```

### **Настройка отображения комментариев при печати**

Вы можете управлять тем, будут ли комментарии печататься, используя класс `PageSetup`. Следующий пример показывает, как включить печать комментариев:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintComments() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintComments(PrintCommentsType::PrintInPlace);
    workbook.Save("PrintComments.xlsx");
}
```

### **Настройка отображения ошибок при печати**

Вы можете управлять способом отображения ошибок при печати, используя класс `PageSetup`. Следующий пример показывает, как установить параметр отображения ошибок:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintErrors() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetPrintErrors(PrintErrorsType::PrintErrorsBlank);
    workbook.Save("PrintErrors.xlsx");
}
```

### **Настройка области печати в соответствии с количеством страниц**

Вы можете управлять масштабированием области печати для размещения на определённом количестве страниц с помощью класса `PageSetup`. Следующий пример показывает, как задать отображение области печати, чтобы она помещалась по ширине и высоте на одну страницу:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintAreaFitToPages() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print area to fit to one page wide and one page tall
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFitToPagesWide(1);
    pageSetup.SetFitToPagesTall(1);

    // Save the workbook
    workbook.Save("PrintAreaFitToPages.xlsx");
}
```

### **Настройка масштаба печати**

Вы можете задать масштаб печати для рабочего листа, используя класс `PageSetup`. Следующий пример показывает, как установить масштаб в 50%:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintScale() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set print scale to 50%
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetZoom(50);

    // Save the workbook
    workbook.Save("PrintScale.xlsx");
}
```

### **Настройка центрирования по горизонтали и вертикали при печати**

Вы можете управлять тем, чтобы рабочий лист был центрирован по горизонтали и вертикали на странице при помощи класса `PageSetup`. Следующий пример показывает, как центрировать лист по горизонтали и вертикали:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintCenterHorizontallyAndVertically() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Center the worksheet horizontally and vertically
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetCenterHorizontally(true);
    pageSetup.SetCenterVertically(true);

    // Save the workbook
    workbook.Save("PrintCenterHorizontallyAndVertically.xlsx");
}
```

### **Настройка номера первой страницы для печати**

Вы можете задать номер первой страницы для печати с помощью класса `PageSetup`. Следующий пример показывает, как установить номер первой страницы:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintFirstPageNumber() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the first page number
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetFirstPageNumber(2);

    // Save the workbook
    workbook.Save("PrintFirstPageNumber.xlsx");
}
```

### **Настройка номера страницы при печати**

Вы можете управлять тем, будет ли отображаться номер страницы при печати, используя класс `PageSetup`. Следующий пример показывает, как включить отображение номера страницы:

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPrintPageNumber() {
    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    PageSetup pageSetup = worksheet.GetPageSetup();
    pageSetup.SetHeader(0, "&P");
    workbook.Save("PrintPageNumber.xlsx");
}
```

### **Настройка порядка печати страниц**

Вы можете задать порядок, в котором будут печататься страницы, используя класс `PageSetup`. Следующий пример показывает, как установить порядок страниц "Вниз, затем по горизонтали":

```cpp
#include <Aspose.Cells.h>

using namespace Aspose::Cells;

void SetPrintPageOrder() {
    // Create a new workbook
    Workbook workbook;

    // Access the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Set the page order to "Down, then Over"
    PageSetup
