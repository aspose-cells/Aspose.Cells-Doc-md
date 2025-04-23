---
title: Verwendung von benutzerdefinierten XML Teilen in Aspose.Cells mit C++
linktitle: Verwendung von benutzerdefinierten XML Teilen
type: docs
weight: 390
url: /de/cpp/use-custom-xml-parts-in-aspose-cells/
description: Erfahren Sie, wie Sie programmatisch benutzerdefinierte XML Teile in Excel Dateien mithilfe von Aspose.Cells und C++ verwenden.
---

## Verwendung von benutzerdefinierten XML-Teilen in Aspose.Cells

Benutzerdefinierte XML-Teile sind XML-Daten, die von verschiedenen Anwendungen wie SharePoint innerhalb einer Excel-Datei gespeichert werden. Diese Daten werden von verschiedenen Anwendungen benötigt und verarbeitet. Microsoft Excel verwendet diese Daten nicht, daher gibt es keine GUI, um sie hinzuzufügen. Sie können diese Daten anzeigen, indem Sie die Erweiterung **.xlsx** in **.zip** ändern und die Datei mit **WinZip** öffnen. Alternativ können Sie die ZIP-Datei auch mit einem beliebigen Drittanbieter-Windows-Zip-Programm wie WinRAR oder WinZip öffnen. Die Daten befinden sich im Ordner **customXml**.

Sie können benutzerdefinierte XML-Teile mit Aspose.Cells über die [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)-Methode hinzufügen.

Das folgende Beispiel zeigt, wie Sie mit der [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/cpp/aspose.cells.properties/contenttypepropertycollection/add/)-Methode die **Book Catalog XML** hinzufügen, deren Name **BookStore** ist. Das folgende Bild zeigt das Ergebnis dieses Codes. Wie Sie sehen können, ist das Book Catalog XML innerhalb des Knoten **BookStore** hinzugefügt worden, der der Name dieser Eigenschaft ist.

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++-Code zur Verwendung benutzerdefinierter XML-Teile

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

## Verwandter Artikel

- [Hinzufügen benutzerdefinierter Eigenschaften, die im Dokumentinformationsbereich sichtbar sind](/cells/de/cpp/adding-custom-properties-visible-inside-document-information-panel/)
