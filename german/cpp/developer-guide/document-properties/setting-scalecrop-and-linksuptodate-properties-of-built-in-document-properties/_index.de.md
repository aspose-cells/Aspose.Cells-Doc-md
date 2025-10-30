---
title: Einstellung der Properties ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften mit C++
linktitle: Einstellungen der Properties ScaleCrop und LinksUpToDate
type: docs
weight: 320
url: /de/cpp/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
description: Erfahren Sie, wie Sie die Properties ScaleCrop und LinksUpToDate der integrierten Dokumenteigenschaften in Aspose.Cells for C++ festlegen.
---

## **Mögliche Verwendungsszenarien**
[GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) und [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) sind zwei erweiterte integrierte Dokumenteigenschaften, die im OpenXml-Format definiert sind. Die Zwecke dieser Eigenschaften sind wie folgt:

## **1) ScaleCrop**
Dieses Element zeigt den Anzeigemodus der Dokumentminiaturansicht an. Setzen Sie dieses Element auf **TRUE**, um das Skalieren der Dokumentminiaturansicht zu ermöglichen. Setzen Sie dieses Element auf **FALSE**, um das Beschränken der Dokumentminiatur auf die Anzeige nur von Abschnitten, die in die Anzeige passen, zu ermöglichen.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.

## **2) LinksUpToDate**
Dieses Element zeigt an, ob Hyperlinks in einem Dokument aktuell sind. Setzen Sie dieses Element auf **TRUE**, um anzuzeigen, dass die Hyperlinks aktualisiert sind. Setzen Sie dieses Element auf **FALSE**, um anzuzeigen, dass die Hyperlinks veraltet sind.

Die möglichen Werte für dieses Element sind durch den Datentyp boolean des W3C XML-Schemas definiert.

## **Screenshot, der diese Eigenschaften in der app.xml-Datei zeigt**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)

## **Einstellungen der Properties ScaleCrop und LinksUpToDate der Integrierten Dokumenteigenschaften**
Der folgende Beispielcode setzt die erweiterten integrierten Dokumenteigenschaften [GetScaleCrop()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getscalecrop/) und [GetLinksUpToDate()](https://reference.aspose.com/cells/cpp/aspose.cells.properties/builtindocumentpropertycollection/getlinksuptodate/) des Arbeitsblatts. Bitte prüfen Sie die [Ausgabedatei Excel](5115500.xlsx), die mit diesem Code erstellt wurde, ändern Sie ihre Erweiterung in .zip, extrahieren Sie den Inhalt und sehen Sie sich die app.xml wie im Screenshot oben an.

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
