---
title: Использование пользовательских XML частей в Aspose.Cells с C++
linktitle: Используйте пользовательские XML части
type: docs
weight: 390
url: /ru/cpp/use-custom-xml-parts-in-aspose-cells/
description: Узнайте, как программно использовать пользовательские XML части в Excel файлах с помощью Aspose.Cells и C++.
---

## Использование пользовательских XML-частей в Aspose.Cells

Пользовательские XML-части — это XML-данные, сохраняемые различными приложениями, такими как SharePoint, внутри файла Excel. Эти данные используются различными приложениями, которым они необходимы. Microsoft Excel не использует эти данные, поэтому интерфейс для их добавления отсутствует. Вы можете просмотреть эти данные, изменив расширение файла с **.xlsx** на **.zip**, а затем открыв его через **WinZip**. Также ZIP-файл можно открыть с помощью сторонней программы для работы с ZIP-архивами, например WinRAR или WinZip. Данные хранятся внутри папки **customXml**.

Вы можете добавлять пользовательские XML-части, используя Aspose.Cells через метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/).

Следующий пример использует метод [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) для добавления **Book Catalog XML** с именем **BookStore**. На изображении показан результат этого кода. Как видно, XML-каталог книг добавлен внутри узла BookStore, который является названием этого свойства.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++ код для использования пользовательских XML-частей

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

    // The sample XML that will be injected to Workbook
    U16String booksXML = uR"(<catalog>
   <book>
      <title>Complete C#</title>
      <price>44</price>
   </book>
   <book>
      <title>Complete Java</title>
      <price>76</price>
   </book>
   <book>
      <title>Complete SharePoint</title>
      <price>55</price>
   </book>
   <book>
      <title>Complete PHP</title>
      <price>63</price>
   </book>
   <book>
      <title>Complete VB.NET</title>
      <price>72</price>
   </book>
</catalog>)";

    // Create an instance of Workbook class
    Workbook workbook;

    // Add Custom XML Part to ContentTypePropertyCollection
    workbook.GetContentTypeProperties().Add(u"BookStore", booksXML);

    // Save the resultant spreadsheet
    workbook.Save(outDir + u"output.xlsx");

    std::cout << "Custom XML part added and workbook saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Связанная статья

- [Добавление пользовательских свойств, видимых в панели информации документа](/cells/ru/cpp/adding-custom-properties-visible-inside-document-information-panel/)
{{< app/cells/assistant language="cpp" >}}
