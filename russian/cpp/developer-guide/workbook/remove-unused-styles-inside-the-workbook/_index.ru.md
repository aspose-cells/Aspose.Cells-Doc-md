---  
title: Удалить неиспользуемые стили внутри рабочей книги с помощью C++  
linktitle: Удалить неиспользуемые стили внутри книги  
type: docs  
weight: 340  
url: /ru/cpp/remove-unused-styles-inside-the-workbook/  
description: Удалите неиспользуемые стили в Excel рабочей книге с помощью Aspose.Cells и C++.  
---  

{{% alert color="primary" %}}  

Неиспользуемые стили в Excel файлах занимают не только место, но и вызывают проблемы с производительностью при преобразовании в разные форматы, такие как PDF, HTML и др. Aspose.Cells предоставляет [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/) для удаления всех неиспользуемых стилей внутри рабочей книги.  

{{% /alert %}}  

Следующий код показывает использование [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/removeunusedstyles/). Код загружает [шаблон Excel файла](5115520.xlsx), который можно скачать по предоставленной ссылке. Он содержит неиспользуемый стиль под названием **AsposeStyle**; этот стиль и все остальные неиспользуемые стили будут удалены после выполнения кода.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-C
    // Path to the documents directory.
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Load template Excel file containing unused styles
    U16String templateFilePath = srcDir + u"Template-With-Unused-Custom-Style.xlsx";
    Workbook workbook(templateFilePath);

    // Remove all unused styles inside the template
    // This will also remove AsposeStyle which is an unused style inside the template
    workbook.RemoveUnusedStyles();

    // Save the file
    U16String outputFilePath = srcDir + u"output_out.xlsx";
    workbook.Save(outputFilePath);

    std::cout << "Unused styles removed and file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
