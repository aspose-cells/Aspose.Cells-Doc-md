---
title: Заголовки и основной шрифт темы с C++
linktitle: Шрифт темы заголовков и тела
description: Aspose.Cells — это библиотека C++ для работы с файлами таблиц. Она поддерживает установку шрифтов заголовков и основного текста темы в документах Excel, что позволяет пользователям настраивать внешний вид и стиль документа. В этой статье рассказывается, как использовать библиотеку Aspose.Cells для работы с шрифтами заголовков и основного текста в документах Excel.
keywords: Aspose.Cells, Документ Excel, Заголовок, Тело, Шрифт темы, Внешний вид, Стиль
type: docs
weight: 120
url: /ru/cpp/headings-and-body-theme-font/
---

{{% alert color="primary" %}}

По умолчанию шрифт автоматически изменится при изменении региональных настроек.

Если стандартный шрифт изменен, также изменится высота строк и ширина столбцов, и это может нарушить макет страницы.

Что вызвало изменение шрифта по умолчанию?

Если задан тематический шрифт Excel, Excel автоматически переключается между различными шрифтами в зависимости от текущей языковой среды.

{{% /alert %}}

## **Тематический шрифт заголовков и основного текста в Excel**

В Excel выберите вкладку Главная, откройте список шрифтов и вы увидите "Шрифты темы" с двумя шрифтами темы: Calibri Light (Заголовки) и Calibri (Основной текст) в верхней части с настройками региона для английского языка.

**![Тематические шрифты](Theme-Fonts.png)**

Если выбрано Шрифт темы, название шрифта будет отображаться по-разному в разных регионах.
Если вы не хотите, чтобы шрифт автоматически менялся в разных регионах, не выбирайте оба шрифта темы.

## **Изменение шрифта заголовков и основного текста программно**
С помощью Aspose.Cells for C++ можно проверить, является ли шрифт по умолчанию шрифтом темы, или установить шрифт темы с помощью свойства [**Font.GetSchemeType()**](https://reference.aspose.com/cells/cpp/aspose.cells/font/getschemetype/).

В следующем примере кода показано, как манипулировать тематическим шрифтом.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a workbook object
    Workbook workbook(u"Book1.xlsx");

    // Get the default style
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the font scheme type
    FontSchemeType schemeType = defaultStyle.GetFont().GetSchemeType();

    // Check if the font is a theme font
    if (schemeType == FontSchemeType::Major || schemeType == FontSchemeType::Minor)
    {
        std::cout << "It's theme font" << std::endl;
    }

    // Change theme font to normal font
    defaultStyle.GetFont().SetSchemeType(FontSchemeType::None);

    // Set the modified default style back to the workbook
    workbook.SetDefaultStyle(defaultStyle);

    Aspose::Cells::Cleanup();
    return 0;
}
```

## **Динамическое получение локального шрифта темы программно**
Иногда наши серверы и компьютеры пользователей не находятся в одном регионе. Как мы можем получить тот же шрифт, который пользователи хотят для обработки файлов?

Перед загрузкой файла необходимо установить региональные параметры системы с помощью свойства [**LoadOptions.GetRegion()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/getregion/).

Следующий пример показывает, как получить локальный шрифт темы.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Instantiate a new LoadOptions
    LoadOptions options;

    // Set the customer's region to Japan
    options.SetRegion(CountryCode::Japan);

    // Instantiate a new Workbook with the specified options
    Workbook workbook(u"Book1.xlsx", options);

    // Get the default style of the workbook
    Style defaultStyle = workbook.GetDefaultStyle();

    // Get the customer's local font name
    U16String localFontName = defaultStyle.GetFont().GetName();

    std::cout << "Local Font Name: " << localFontName.ToUtf8() << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```
