---
title: Доступ и обновление частей форматированного текста ячейки с помощью C++
linktitle: Редактирование текста с использованием разнообразного форматирования
type: docs
weight: 40
url: /ru/cpp/access-and-update-the-portions-of-rich-text-of-cell/
description: Узнайте, как получать доступ и обновлять части форматированного текста ячейки через API Aspose.Cells for C++.
keywords: Получить доступ и обновить обогащенный текст ячейки, получить обогащенный текст ячейки, отредактировать обогащенный текст ячейки, получить доступ к обогащенному тексту ячейки, обновить обогащенный текст ячейки, изменить обогащенный текст ячейки
---

{{% alert color="primary" %}}

Aspose.Cells позволяет получить доступ к обновлению разделов обогащенного текста ячейки. Для этой цели вы можете использовать методы [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) и [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/). Эти методы будут возвращать и принимать массивы объектов [**FontSetting**](https://reference.aspose.com/cells/cpp/aspose.cells/fontsetting/), которые вы сможете использовать для доступа и обновления различных свойств шрифта, таких как имя шрифта, цвет шрифта, полужирный и т. д.

{{% /alert %}}

## **Доступ и обновление частей Rich Text ячейки**

Следующий пример показывает использование методов [**Cell->GetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/getcharacters/) и [**Cell->SetCharacters()**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/setcharacters/) с помощью исходного файла Excel ([исходный файл](5112369.xlsx)). В исходном файле Excel в ячейке A1 есть богатый текст с 3 частями, каждая с разным шрифтом. Скрипт получает эти части и обновляет шрифт первой части на "Arial". Обновленная рабочая книга сохраняется как [выходной файл Excel](5112366.xlsx).

### C++ код для доступа и обновления частей богатого текста

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    U16String inputPath = srcDir + u"Sample.xlsx";
    U16String outputPath = outDir + u"Output.out.xlsx";

    Workbook workbook(inputPath);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cell cell = worksheet.GetCells().Get(U16String(u"A1"));

    std::cout << "Before updating the font settings...." << std::endl;

    Vector<FontSetting> fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    if (fnts.GetLength() > 0)
    {
        FontSetting& fs = fnts[0];
        fs.GetFont().SetName(u"Arial");
        cell.SetCharacters(fnts);
    }

    std::cout << std::endl << "After updating the font settings...." << std::endl;

    fnts = cell.GetCharacters();

    for (int i = 0; i < fnts.GetLength(); ++i)
    {
        FontSetting& fs = fnts[i];
        std::cout << fs.GetFont().GetName().ToUtf8() << std::endl;
    }

    workbook.Save(outputPath);

    Aspose::Cells::Cleanup();
    return 0;
}
```

### Вывод консоли, сгенерированный примерным кодом

Вот вывод в консоль при использовании [исходного файла Excel](5112369.xlsx):

{{< highlight java >}}

Before updating the font settings....
Century
Courier New
Verdana

After updating the font settings....
Arial
Courier New
Verdana

{{< /highlight >}}
