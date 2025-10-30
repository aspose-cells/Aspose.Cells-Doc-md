---
title: XML in Excel Arbeitsmappe mit C++ importieren
linktitle: XML Maps
type: docs
weight: 210
url: /de/cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: Daten aus einer XML Daten Datei in Microsoft Excel mit Aspose.Cells in C++ importieren.
---

{{% alert color="primary" %}}

Aspose.Cells erlaubt das Importieren der XML-Karte innerhalb des Arbeitsbuchs mit der [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/)-Methode. Sie können XML-Map mit Microsoft Excel mit den folgenden Schritten importieren:

- Klicken Sie auf die **Entwickler**-Registerkarte.
- Klicken Sie auf **Importieren** im XML-Bereich und befolgen Sie die erforderlichen Schritte.

Sie müssen Ihre XML-Daten bereitstellen, um den Import abzuschließen. Hier ist ein [Beispiel-XML-Daten](5115037.txt), das Sie für Tests verwenden können.

{{% /alert %}}

## **Importieren Sie eine XML-Map mit Microsoft Excel**

Der folgende Screenshot zeigt, wie man eine XML-Map mit Microsoft Excel importiert.

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Importieren Sie eine XML-Map mit Aspose.Cells**

Der folgende Beispielcode zeigt, wie die [**Workbook.ImportXml()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/importxml/)-Methode verwendet wird. Es erzeugt die [Ausgabedatei Excel](5115036.xlsx), wie in diesem Screenshot gezeigt.

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

## **Erweiterte Themen**
- [XML Map innerhalb der Arbeitsmappe mit der XmlMapCollection.Add Methode hinzufügen](/cells/de/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [Exportieren Sie XML-Daten, die mit der XML-Map in der Arbeitsmappe verknüpft sind](/cells/de/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [Finden Sie den Namen des Stammelements der XML-Map](/cells/de/cpp/find-the-root-element-name-of-xml-map/)
- [Zellen mit XML-Map-Elementen verknüpfen](/cells/de/cpp/link-cells-to-xml-map-elements/)
{{< app/cells/assistant language="cpp" >}}
