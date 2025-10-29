---
title: Настройка заголовков и подвалов с помощью C++
linktitle: Установка заголовков и нижних колонтитулов
type: docs
weight: 30
url: /ru/cpp/setting-headers-and-footers/
description: В этой статье объясняется, как программно вставить изображение в заголовок и подвал листов Excel с помощью настройки заголовков и подвалов с помощью команд скрипта, используя API или библиотеку C++.
keywords: вставка изображения в заголовок или подвал Excel c++, установка команд скриптов заголовка и подвала Excel c++
---

{{% alert color="primary" %}}

Заголовки и нижние колонтитулы - это строки текста, отображаемые ниже верхнего поля или выше нижнего поля соответственно. Также возможно добавить заголовки и нижние колонтитулы к листам. Заголовки и нижние колонтитулы могут использоваться для отображения полезной информации, такой как номер страницы, имя автора, название темы или дата и время. Заголовки и нижние колонтитулы управляются с использованием настроек разметки страницы.

{{% /alert %}}

## **Настройка колонтитулов и подвалов**

Aspose.Cells позволяет добавлять заголовки и нижние колонтитулы к листам во время выполнения, но мы рекомендуем устанавливать заголовки и нижние колонтитулы вручную в предварительно разработанном файле для печати. Вы можете использовать Microsoft Excel в качестве графического инструмента для установки заголовков и нижних колонтитулов для экономии усилий и времени разработки. Aspose.Cells может импортировать файл и сохранить настройки.

Чтобы добавить верхние и нижние колонтитулы во время выполнения, Aspose.Cells предоставляет специальные вызовы API и команды сценариев для форматирования верхних и нижних колонтитулов.

### **Скриптовые команды**

Команды сценариев - это специальные команды, которые позволяют задавать форматирование верхних и нижних колонтитулов.

|**Сценарные команды**|**Описание**|
| :- | :- |
|&P|Текущий номер страницы|
|&G|Картинка|
|&N|Общее количество страниц|
|&D|Текущая дата|
|&T|Текущее время|
|&A|Имя листа|
|&F|Имя файла без пути|
|&&Text|Показывает &Text. Например: &&WO будет отображаться как &WO|
|&"\<FontName>"|Представляет имя шрифта. Например: &"Arial"|
|&"\<FontName>, \<FontStyle>"|Представляет имя шрифта со стилем. Например: &"Arial,Bold"|
|&\<FontSize>|Представляет размер шрифта. Например: “&14abc”. Однако, если за этой командой следует обычное число для печати в заголовке, его следует отделить пробелом от размера шрифта. Например: “&14 123”.

### **Установить заголовки и нижние колонтитулы**

Класс [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) предоставляет два метода, [**SetHeader**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheader/) и [**SetFooter**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooter/), используемых для добавления заголовка и колонтитула в лист. Эти методы принимают только два параметра:

- **Раздел** - раздел, куда следует поместить заголовок или колонтитул. Существуют три раздела: слева, по центру и справа, представленные соответственно 0, 1 и 2.
- **Сценарий** - сценарий, используемый для заголовка или колонтитула. В этом сценарии содержатся команды сценариев для форматирования заголовков или колонтитулов.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook excel;

    // Get the first worksheet's PageSetup
    PageSetup pageSetup = excel.GetWorksheets().Get(0).GetPageSetup();

    // Set worksheet name at the left section of the header
    pageSetup.SetHeader(0, u"&A");

    // Set current date and time at the central section of the header with custom font
    pageSetup.SetHeader(1, u"&\"Times New Roman,Bold\"&D-&T");

    // Set current file name at the right section of the header with custom font
    pageSetup.SetHeader(2, u"&\"Times New Roman,Bold\"&12&F");

    // Set a string at the left section of the footer with custom font for part of the string
    pageSetup.SetFooter(0, u"Hello World! &\"Courier New\"&14 123");

    // Set the current page number at the central section of the footer
    pageSetup.SetFooter(1, u"&P");

    // Set page count at the right section of the footer
    pageSetup.SetFooter(2, u"&N");

    // Save the workbook
    excel.Save(u"SetHeadersAndFooters_out.xls");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Вставка изображения в заголовок или колонтитул**

Класс [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) имеет два дополнительных метода, [**SetHeaderPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setheaderpicture/) и [**SetFooterPicture**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/setfooterpicture/), используемых для добавления изображений в заголовок и колонтитул. Эти методы принимают параметры:

- **Секция** - раздел заголовка или колонтитула, в который будет помещено изображение. Существуют три секции: слева, по центру и справа, представленные значениями 0, 1 и 2 соответственно.
- **Массив байтов** - графические данные (двоичные данные должны быть записаны в буфер массива байтов).

После выполнения нижеприведенного кода и открытия файла проверьте заголовок листа:

1. На меню **Файл** выберите **Настройка страницы**. Будет отображено диалоговое окно.
1. Выберите вкладку **Шапка/Нижний колонтитул**.

```cpp
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace std;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Creating a Workbook object
    Workbook workbook;

    // Creating a string variable to store the url of the logo/picture
    U16String logo_url = srcDir + u"aspose-logo.jpg";

    // Declaring a FileStream object
    ifstream inFile;

    // Declaring a byte array
    vector<uint8_t> binaryData;

    // Opening the logo/picture in the stream
    inFile.open(logo_url.ToUtf8(), ios::binary);

    if (inFile.is_open())
    {
        // Get the size of the file
        inFile.seekg(0, ios::end);
        size_t fileSize = inFile.tellg();
        inFile.seekg(0, ios::beg);

        // Resize the byte array to the size of the file
        binaryData.resize(fileSize);

        // Read the file into the byte array
        inFile.read(reinterpret_cast<char*>(binaryData.data()), fileSize);

        // Creating a PageSetup object to get the page settings of the first worksheet of the workbook
        PageSetup pageSetup = workbook.GetWorksheets().Get(0).GetPageSetup();

        // Convert std::vector to Aspose::Cells::Vector
        Aspose::Cells::Vector<uint8_t> asposeBinaryData(binaryData.data(), static_cast<int32_t>(binaryData.size()));

        // Setting the logo/picture in the central section of the page header
        pageSetup.SetHeaderPicture(1, asposeBinaryData);

        // Setting the script for the logo/picture
        pageSetup.SetHeader(1, u"&G");

        // Setting the Sheet's name in the right section of the page header with the script
        pageSetup.SetHeader(2, u"&A");

        // Saving the workbook
        workbook.Save(outDir + u"InsertImageInHeaderFooter_out.xls");

        // Closing the FileStream object
        inFile.close();
    }
    else
    {
        cerr << "Failed to open the image file." << endl;
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
