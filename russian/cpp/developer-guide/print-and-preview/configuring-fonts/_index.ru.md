---
title: Настройка шрифтов для отображения таблиц с помощью C++
linktitle: Настройка шрифтов для визуализации электронных таблиц
type: docs
weight: 10
url: /ru/cpp/configuring-fonts-for-rendering-spreadsheets/
description: Узнайте, как настраивать шрифты для отображения таблиц в виде изображений, PDF и XPS с помощью Aspose.Cells for C++.
---

## **Возможные сценарии использования**

API Aspose.Cells позволяет отображать таблицы в изображениях и конвертировать их в PDF и XPS. Для повышения точности конвертации необходимо, чтобы используемые в таблице шрифты находились в стандартной папке шрифтов операционной системы. Если нужных шрифтов нет, API Aspose.Cells попытается заменить их доступными шрифтами.

## **Выбор шрифтов**

Ниже приведен процесс, который выполняет API Aspose.Cells за сценой:

1. API пытается найти шрифты на файловой системе, соответствующие точному имени шрифта, используемому в электронной таблице.
1. Если API не может найти шрифты с точным совпадением имени, оно пытается использовать шрифт по умолчанию, указанный в свойстве [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) книги.
1. Если API не может найти шрифт, заданный в свойстве [**DefaultStyle.Font**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getfont/) книги, оно пытается использовать шрифт, указанный в [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) или в [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/).
1. Если API не может найти шрифт, заданный в [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/cpp/aspose.cells/paginatedsaveoptions/~paginatedsaveoptions/) или в [**ImageOrPrintOptions.DefaultFont**](https://reference.aspose.com/cells/cpp/aspose.cells.rendering/imageorprintoptions/getdefaultfont/), он пытается использовать шрифт, указанный в [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/).
1. Если API не может найти шрифт, заданный в свойстве [**FontConfigs.DefaultFontName**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getdefaultfontname/), оно пытается выбрать наиболее подходящие шрифты из всех доступных.
1. В конце концов, если API не может найти никакие шрифты в файловой системе, оно отображает таблицу шрифтом Arial.

## **Установка пользовательских каталогов шрифтов**

API Aspose.Cells просматривает папку шрифтов операционной системы для поиска необходимых шрифтов. Если шрифты отсутствуют в системной папке, API ищет их в пользовательских (кастомных) папках. Класс [**FontConfigs**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/) предоставляет несколько способов установить пользовательские папки шрифтов, как описано ниже:

1. [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/): Этот метод полезен, если нужно установить только одну папку.
1. [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/): Этот метод полезен, когда шрифты находятся в нескольких папках, и пользователь хочет указать каждую папку отдельно, а не объединять все шрифты в одну.
1. [**FontConfigs.SetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsources/): Этот механизм полезен, когда пользователь хочет загрузить шрифты из нескольких папок, одного файла шрифта или данных шрифта из массива байт.

{{% alert color="primary" %}}

Оба метода [**FontConfigs.SetFontFolder**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolder/) и [**FontConfigs.SetFontFolders**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontfolders/) принимают второй параметр типа Boolean. Передача **true** в качестве второго параметра укажет API Aspose.Cells искать файлы шрифтов в подкаталогах.

{{% /alert %}}

```c++
#include <iostream>
#include <fstream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

Vector<uint8_t> GetDataFromFile(const U16String& file)
{
    std::string f = file.ToUtf8();
    // open a file 
    std::ifstream fileStream(f, std::ios::binary);

    if (!fileStream.is_open()) {
        std::cerr << "Failed to open the file." << std::endl;
        return 1;
    }

    // Get file size
    fileStream.seekg(0, std::ios::end);
    std::streampos fileSize = fileStream.tellg();
    fileStream.seekg(0, std::ios::beg);

    // Read file contents into uint8_t array
    uint8_t* buffer = new uint8_t[fileSize];
    fileStream.read(reinterpret_cast<char*>(buffer), fileSize);
    fileStream.close();

    Vector<uint8_t>data(buffer, fileSize);
    delete[] buffer;

    return data;
}

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String fontFolder1 = srcDir + u"Arial";
    U16String fontFolder2 = srcDir + u"Calibri";
    U16String fontFile = srcDir + u"arial.ttf";

    FontConfigs::SetFontFolder(fontFolder1, true);

    Vector<U16String> fontFolders{ fontFolder1 , fontFolder2 };

    FontConfigs::SetFontFolders(fontFolders, false);

    FolderFontSource sourceFolder(fontFolder1, false);
    FileFontSource sourceFile(fontFile);
    Vector<uint8_t> fontData = GetDataFromFile(fontFile);
    MemoryFontSource sourceMemory(fontData);

    Vector<FontSourceBase> fontSources{ sourceFolder ,sourceFile ,sourceMemory };

    FontConfigs::SetFontSources(fontSources);

    Aspose::Cells::Cleanup();
}
```

{{% alert color="primary" %}}

Пожалуйста, используйте любой из вышеупомянутых методов в начале приложения, то есть до вызова любых других объектов API Aspose.Cells.

{{% /alert %}}

{{% alert color="primary" %}}

Если все вышеперечисленные методы используются для установки источников шрифтов, то только последние настройки будут применены.

{{% /alert %}}

## **Механизм подстановки шрифтов**

API Aspose.Cells также предоставляет возможность указывать заменяющие шрифты для целей отображения. Этот механизм полезен, когда необходимый шрифт недоступен на машине, где должна проходить конвертация. Пользователи могут предоставить список имен шрифтов в качестве альтернативы изначально необходимому шрифту. Для этого API Aspose.Cells использует метод [**FontConfigs.SetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/setfontsubstitutes/), который принимает два параметра. Первый — это строка, в которой указывается имя шрифта, который нужно заменить. Второй — массив строк, в который можно включить список имен шрифтов в качестве заменителя исходного шрифта (указанного в первом параметре).

Вот простой сценарий использования:

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Substituting the Arial font with Times New Roman & Calibri
    Vector<U16String> substituteFonts{ u"Times New Roman", u"Calibri" };
    FontConfigs::SetFontSubstitutes(u"Arial", substituteFonts);

    Aspose::Cells::Cleanup();
}
```

## **Сбор информации**

Помимо вышеуказанных методов, API Aspose.Cells также предоставляет средства для сбора информации о том, какие источники и замены были установлены:

1. Метод [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) возвращает массив типа [**FontSourceBase**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsourcebase/), содержащий список указанных источников шрифтов. Если источники не были установлены, метод [**FontConfigs.GetFontSources**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsources/) вернет пустой массив.
1. Метод [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) принимает параметр типа **string**, позволяющий указать имя шрифта, для которого была установлена замена. Если замена для указанного имени шрифта не была установлена, метод [**FontConfigs.GetFontSubstitutes**](https://reference.aspose.com/cells/cpp/aspose.cells/fontconfigs/getfontsubstitutes/) вернет null.

## **Дополнительные темы**
- [Установите шрифт по умолчанию при отображении электронной таблицы в изображения](/cells/ru/cpp/set-default-font-while-rendering-spreadsheet-to-images/)
- [Установите свойство DefaultFont в PdfSaveOptions и ImageOrPrintOptions для приоритета](/cells/ru/cpp/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Поддерживаемые форматы шрифтов](/cells/ru/cpp/supported-font-formats/)
