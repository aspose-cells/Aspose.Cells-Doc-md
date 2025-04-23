---
title: Använd anpassade XML delar i Aspose.Cells med C++
linktitle: Använd anpassade XML delar
type: docs
weight: 390
url: /sv/cpp/use-custom-xml-parts-in-aspose-cells/
description: Lär dig hur du använder anpassade XML delar i Excel filer programmatiskt med Aspose.Cells och C++.
---

## Användning av anpassade XML-delar i Aspose.Cells

Anpassade XML-delar är XML-data som lagras av olika applikationer som SharePoint innanför en Excel-fil. Denna data används av olika applikationer som behöver den. Microsoft Excel använder inte denna data, så det finns ingen GUI för att lägga till den. Du kan se denna data genom att byta filändelsen på **.xlsx** till **.zip** och öppna den med **WinZip**. Du kan även öppna ZIP-filen med vilken third-party Windows-zip-arkivhanterare som helst, exempelvis WinRAR eller WinZip. Data finns i mappen **customXml**.

Du kan lägga till anpassade XML-delar med Aspose.Cells via [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) metoden.

Följande exempel använder metoden [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/) för att lägga till **Book Catalog XML**, som heter **BookStore**. Bilden nedan visar resultatet av denna kod. Som du kan se är Book Catalog XML tillagt inuti BookStore-noden, vilket är namnet på denna egenskap.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++-kod för att använda anpassade XML-delar

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

## Relaterad artikel

- [Lägga till synliga anpassade egenskaper inuti dokumentinformationen](/cells/sv/cpp/adding-custom-properties-visible-inside-document-information-panel/)
