---
title: Importera XML till Excel arbetsbok med C++
linktitle: XML mappar
type: docs
weight: 210
url: /sv/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Importera data från en XML datafil till Microsoft Excel med Aspose.Cells och C++.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att importera XML-kartan inuti arbetsboken med hjälp av [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/)-metoden. Du kan importera XML-karta med Microsoft Excel med följande steg:

- Välj fliken **Developer**.
- Klicka på **Importera** i XML-avsnittet och följ de nödvändiga stegen.

Du måste tillhandahålla dina XML-data för att slutföra importen. Här är ett [prov-XML-data](5115037.txt) som du kan använda för testning.

{{% /alert %}}

## **Importera XML-karta med Microsoft Excel**

Följande skärmbild visar hur man importerar XML-karta med Microsoft Excel.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importera XML-karta med Aspose.Cells**

Följande exempel visar hur man använder [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/)-metoden. Det genererar den [utgångs-Excelfilen](5115036.xlsx) som visas i denna skärmbild.

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

## **Avancerade ämnen**
- [Lägg till XML-karta i arbetsboken med XmlMapCollection.Add-metoden](/cells/sv/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportera XML-data som är länkad till XML-karta inuti arbetsboken](/cells/sv/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Hitta rotresursnamnet på XML-kartan](/cells/sv/cpp/find-the-root-element-name-of-xml-map/)
- [Länka celler till XML-kartelement](/cells/sv/cpp/link-cells-to-xml-map-elements/)
{{< app/cells/assistant language="cpp" >}}
