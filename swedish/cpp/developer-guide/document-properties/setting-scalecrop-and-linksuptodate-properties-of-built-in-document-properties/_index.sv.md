---
title: Ställa in ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper med C++
linktitle: Ställa in ScaleCrop och LinksUpToDate egenskaper
type: docs
weight: 320
url: /sv/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Lär dig att ställa in ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper med Aspose.Cells for C++.
---

## **Möjliga användningsscenario**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) och [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) är två utökade inbyggda dokumentegenskaper som definieras i OpenXml-formatet. Syftet med dessa egenskaper är:

## **1) ScaleCrop**
Detta element indikerar visningsläget för miniatyrbilden av dokumentet. Ange detta element till **TRUE** för att aktivera skalning av miniatyrbilden av dokumentet. Ange detta element till **FALSE** för att aktivera urskärning av miniatyrbilden för att visa endast sektioner som passar i displayen.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **2) LinksUpToDate**
Detta element indikerar om hyperlänkar i ett dokument är uppdaterade. Ange detta element till **TRUE** för att ange att hyperlänkar är uppdaterade. Ange detta element till **FALSE** för att ange att hyperlänkar är föråldrade.

De möjliga värdena för denna komponent definieras av W3C XML Schema boolean-datatypen.

## **Skärmbild som visar dessa egenskaper i app.xml-filen**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Ställ in ScaleCrop- och LinksUpToDate-egenskaper för inbyggda dokumentegenskaper**
Följande exempel kod ställer in de utökade inbyggda egenskaperna [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) och [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) för arbetsboken. Kontrollera den [genererade excel-filen](5115500.xlsx), byt extension till .zip och extrahera innehållet för att visa app.xml som i skärmbilderna ovan.

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

    // Instantiating a Workbook object.
    Workbook workbook;

    // Setting ScaleCrop and LinksUpToDate BuiltIn Document Properties.
    workbook.GetBuiltInDocumentProperties().SetScaleCrop(true);
    workbook.GetBuiltInDocumentProperties().SetLinksUpToDate(true);

    // Saving the Excel file.
    workbook.Save(outDir + u"output.xls", SaveFormat::Auto);

    std::cout << "Excel file saved successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
{{< app/cells/assistant language="cpp" >}}
