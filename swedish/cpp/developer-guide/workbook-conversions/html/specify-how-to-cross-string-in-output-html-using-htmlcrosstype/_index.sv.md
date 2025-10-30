---
title: Ange hur du korsar strängar i utdata HTML med HtmlCrossType i C++
linktitle: Ange HtmlCrossType i utdata HTML
type: docs
weight: 140
url: /sv/cpp/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/
description: Lär dig hur du kontrollerar strängoverflow i HTML utdata med Aspose.Cells for C++ och HtmlCrossType.
---

## **Möjliga användningsscenario**

När en cell innehåller text eller en sträng som är bredare än cellens bredd, överflödar strängen om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil till HTML kan du kontrollera detta överflöde genom att specificera kors-typen med [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)-enumerationen. Den har följande värden:

- **HtmlCrossType.Default**: Visa som MS Excel, beror på nästa cell. Om nästa cell är null kommer strängen att överlappa eller den kommer att avkortas.

- **HtmlCrossType.MSExport**: Visa strängen som MS Excel exporterar HTML.

- **HtmlCrossType.Cross**: Visa HTML-korssträngen, prestandan för att skapa stora HTML-filer kommer att vara mer än tio gånger snabbare än att ställa in värdet till Default eller FitToCell.

- **HtmlCrossType.FitToCell**: Visa endast strängen inom cellens bredd.

## **Ange hur man korsar sträng i utmatnings-HTML med HtmlCrossType**

Följande kodexempel laddar [exempel-Excelfil](51740732.xlsx) och sparar den i HTML-format genom att specificera olika [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/). Vänligen ladda ner de [utdata-HTMLs](51740734.zip) som genererades med denna kod. Exempel-Excelfilen innehåller en bild kantad med rött som visas i denna skärmbild, vilket visar effekten av [**HtmlCrossType**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype/)-värdena på utdata HTML.

![todo:image_alt_text](specify-how-to-cross-string-in-output-html-using-htmlcrosstype_1.png)

## **Exempelkod**

```c++
#include <iostream>
#include <string>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    U16String inputFilePath(u"sampleHtmlCrossStringType.xlsx");
    Workbook wb(inputFilePath);

    HtmlSaveOptions opts;
    opts.SetHtmlCrossStringType(HtmlCrossType::Default);
    opts.SetHtmlCrossStringType(HtmlCrossType::MSExport);
    opts.SetHtmlCrossStringType(HtmlCrossType::Cross);
    opts.SetHtmlCrossStringType(HtmlCrossType::FitToCell);

    int htmlCrossType = static_cast<int>(opts.GetHtmlCrossStringType());
    std::string numStr = std::to_string(htmlCrossType);
    U16String outputFilePath = U16String(u"out") + U16String(numStr.c_str()) + U16String(u".htm");
    wb.Save(outputFilePath, opts);

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
