---
title: Предотвратить экспорт скрытого содержимого листа при сохранении в HTML с помощью C++
linktitle: Предотвратить экспорт скрытого содержимого листа
type: docs
weight: 210
url: /ru/cpp/prevent-exporting-hidden-worksheet-contents-on-saving-to/
description: Узнайте, как предотвратить экспорт скрытого содержимого листов при сохранении книг Excel в HTML с помощью Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Вы можете сохранять книги Excel в HTML. Однако, если в книге есть скрытые листы, Aspose.Cells по умолчанию экспортирует скрытое содержимое листа в выходной каталог HTML (_files), который содержит файлы, такие как листы, изображения, tabstrip.htm, stylesheet.css и т. д. Иногда экспорт содержимого скрытых листов таким образом нецелесообразен. Например, если скрытый лист содержит изображения, которые не должны быть экспортированы в каталог _files.

{{% /alert %}}

Aspose.Cells предоставляет свойство [**HtmlSaveOptions.GetExportHiddenWorksheet()**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlsaveoptions/getexporthiddenworksheet/). По умолчанию оно установлено в **true**, и скрытые листы экспортируются в HTML. Если вы установите его в **false**, Aspose.Cells не будет экспортировать содержимое скрытых листов.

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

    // Path of input excel file
    U16String inputFilePath = srcDir + u"WorkbookWithHiddenContent.xlsx";

    // Path of output HTML file
    U16String outputFilePath = outDir + u"HtmlWithoutHiddenContent_out.html";

    // Create workbook object
    Workbook workbook(inputFilePath);

    // Create HTML save options
    HtmlSaveOptions options;

    // Do not export hidden worksheet contents
    options.SetExportHiddenWorksheet(false);

    // Save the workbook
    workbook.Save(outputFilePath, options);

    std::cout << "Workbook saved successfully without hidden content!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
