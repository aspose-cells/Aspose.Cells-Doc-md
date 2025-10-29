---
title: Импорт XML в рабочую книгу Excel с помощью C++
linktitle: Сопоставления XML
type: docs
weight: 210
url: /ru/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Импорт данных из XML файла в Microsoft Excel с помощью Aspose.Cells и C++.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет импортировать карту XML внутри книги с помощью метода [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Вы можете импортировать карту XML в Microsoft Excel, следуя следующим шагам:

- Выберите вкладку **Разработчик**.
- Нажмите **Импорт** в разделе XML и следуйте необходимым шагам.

Для завершения импорта вам потребуется предоставить свои XML-данные. Вот [пример XML-данных](5115037.txt), который вы можете использовать для тестирования.

{{% /alert %}}

## **Импорт XML-схемы с использованием Microsoft Excel**

На следующем скриншоте показано, как импортировать XML-схему с использованием Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Импорт XML-схемы с использованием Aspose.Cells**

Следующий пример кода показывает, как использовать метод [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/). Он создает [выходной Excel-файл](5115036.xlsx), как показано на этом скриншоте.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

```c++
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

    // Create a workbook
    Workbook workbook;

    // URL that contains your XML data for mapping
    U16String XML(u"http://www.aspose.com/docs/download/attachments/434475650/sampleXML.txt");

    // Import your XML Map data starting from cell A1
    workbook.ImportXml(XML, u"Sheet1", 0, 0);

    // Save workbook
    U16String outputPath = outDir + u"output_out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Workbook saved successfully with imported XML data!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Расширенные темы**
- [Добавить XML-отображение внутри книги с использованием метода XmlMapCollection.Add](/cells/ru/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Экспорт XML-данных, связанных с XML-схемой, внутри книги](/cells/ru/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Найдите имя корневого элемента XML-карты.](/cells/ru/cpp/find-the-root-element-name-of-xml-map/)
- [Привязка ячеек к элементам XML-отображения](/cells/ru/cpp/link-cells-to-xml-map-elements/)
{{< app/cells/assistant language="cpp" >}}
