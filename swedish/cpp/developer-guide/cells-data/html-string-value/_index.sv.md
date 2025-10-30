---
title: Lägga till HTML rik text inne i cellen med C++
linktitle: HTML strängsvärde
type: docs
weight: 50
url: /sv/cpp/adding-html-rich-text-inside-the-cell/
description: Lär dig hur man lägger till HTML rik text i cellen via API et Aspose.Cells for C++.
keywords: Lägg till HTML Rich Text inuti cellen, Ange HTML Rich Text inuti cellen, Lägg till HTML Rich Text i cellen
---

{{% alert color="primary" %}}

Aspose.Cells stöder konvertering av Microsoft Excel-orienterad HTML till XLS/XLSX-format. Det innebär att den HTML som genereras av Microsoft Excel kan konverteras tillbaka till XLS/XLSX-format med hjälp av Aspose.Cells.

Likadant, om det finns enkel HTML, kan Aspose.Cells konvertera den till HTML Rich Text. Aspose.Cells erbjuder [**Cell::GetHtmlString**](https://reference.aspose.com/cells/cpp/aspose.cells/cell/gethtmlstring/)-metoden som kan ta sådan enkel HTML och konvertera den till formaterad celltext.

{{% /alert %}}

Nedan kodprov visar hur du lägger till HTML-rich text inuti cellen. Se skärmbilden av den resulterande Excel-filen.

![todo:image_alt_text](adding-html-rich-text-inside-the-cell_1)

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

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Access cell A1
    Cell cell = worksheet.GetCells().Get(u"A1");

    // Set HTML formatted text in the cell
    cell.SetHtmlString(u"<Font Style=\"FONT-WEIGHT: bold;FONT-STYLE: italic;TEXT-DECORATION: underline;FONT-FAMILY: Arial;FONT-SIZE: 11pt;COLOR: #ff0000;\">This is simple HTML formatted text.</Font>");

    // Save the workbook
    workbook.Save(outDir + u"output_out.xlsx");

    std::cout << "HTML formatted text added to cell A1 successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```

## Relaterade artiklar

- [Visa punktlistor genom att ställa in cellvärde med hjälp av HTML](/cells/sv/cpp/display-bullets-by-setting-cell-value-using/)
- [Hämta HTML5-sträng från cell](/cells/sv/cpp/get-html5-string-from-cell/)
{{< app/cells/assistant language="cpp" >}}
