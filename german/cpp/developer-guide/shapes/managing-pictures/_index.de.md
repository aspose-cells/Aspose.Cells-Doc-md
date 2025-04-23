---
title: Bilder mit C++ verwalten
linktitle: Bilder verwalten
type: docs
weight: 10
url: /de/cpp/managing-pictures/
description: Fügen Sie Bilder in Tabellenblätter mit der API Aspose.Cells for C++ hinzu, positionieren und verwalten Sie sie.
---

Aspose.Cells ermöglicht es Entwicklern, Bilder zur Laufzeit zu Tabellenkalkulationen hinzuzufügen. Darüber hinaus kann die Positionierung dieser Bilder zur Laufzeit kontrolliert werden, was in den folgenden Abschnitten detaillierter erläutert wird.

Dieser Artikel erklärt, wie man Bilder hinzufügt und wie man ein Bild einfügt, das den Inhalt bestimmter Zellen zeigt.

## **Bilder hinzufügen**

Das Hinzufügen von Bildern zu einer Tabelle ist sehr einfach. Es dauert nur wenige Zeilen Code:
Rufen Sie einfach die [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/)-Methode des [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/) auf (eingeschlossen im [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Objekt). Die [**Add**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/add/)-Methode nimmt die folgenden Parameter an:

- **Index der oberen linken Zeile**, der Index der oberen linken Zeile.
- **Index der oberen linken Spalte**, der Index der oberen linken Spalte.
- **Bilddateiname**, der Name der Bilddatei inklusive des Pfads.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Add worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add image to worksheet at F6 (row 5, column 5)
    U16String imagePath = srcDir + u"logo.jpg";
    worksheet.GetPictures().Add(5, 5, imagePath);

    // Save workbook
    U16String outputPath = outDir + u"output.xls";
    workbook.Save(outputPath);

    std::cout << "Worksheet with image created successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Bilder positionieren**

Es gibt zwei mögliche Methoden, um die Positionierung von Bildern mithilfe von Aspose.Cells zu kontrollieren:

- Proportionale Positionierung: Definieren Sie eine Position proportional zur Zeilenhöhe und -breite.
- Absolute Positionierung: Legen Sie die genaue Position auf der Seite fest, an der das Bild eingefügt wird, z.B. 40 Pixel links und 20 Pixel unterhalb des Zellrands.

### **Proportionale Positionierung**

Entwickler können die Bilder proportional zur Zeilenhöhe und Spaltenbreite mit den Eigenschaften [**UpperDeltaX**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltax/) und [**UpperDeltaY**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getupperdeltay/) des [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-Objekts positionieren. Ein [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-Objekt kann durch Übergabe seines Bildindex vom [**PictureCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picturecollection/)-Objekt erhalten werden. Dieses Beispiel platziert ein Bild in die Zelle F6.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create workbook object
    Workbook workbook;

    // Add new worksheet and get reference
    int sheetIndex = workbook.GetWorksheets().Add();
    Worksheet worksheet = workbook.GetWorksheets().Get(sheetIndex);

    // Add picture to worksheet at (5,5) position
    U16String imagePath = outDir + u"logo.jpg";
    int pictureIndex = worksheet.GetPictures().Add(5, 5, imagePath);

    // Access added picture and set positioning
    Drawing::Picture picture = worksheet.GetPictures().Get(pictureIndex);
    picture.SetUpperDeltaX(200);
    picture.SetUpperDeltaY(200);

    // Save modified workbook
    U16String outputPath = outDir + u"book1.out.xls";
    workbook.Save(outputPath);

    std::cout << "Picture added and positioned successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

### **Absolute Positionierung**

Entwickler können auch die Bilder absolut positionieren, indem sie die Eigenschaften [**Left**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getleft/) und [**Top**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/gettop/) des [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-Objekts verwenden. Dieses Beispiel platziert ein Bild in der Zelle F6, 60 Pixel von links und 10 Pixel von oben der Zelle entfernt.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access worksheet collection and add new sheet
    WorksheetCollection worksheets = workbook.GetWorksheets();
    int sheetIndex = worksheets.Add();

    // Get reference to newly added worksheet
    Worksheet worksheet = worksheets.Get(sheetIndex);

    // Add picture to worksheet at row 5, column 5 (cell F6)
    PictureCollection pictures = worksheet.GetPictures();
    int pictureIndex = pictures.Add(5, 5, srcDir + u"logo.jpg");

    // Access added picture and set position
    Picture picture = pictures.Get(pictureIndex);
    picture.SetLeft(60);
    picture.SetTop(10);

    // Save modified workbook
    workbook.Save(outDir + u"book1.out.xls");

    std::cout << "Workbook with inserted picture saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Einfügen eines Bildes basierend auf Zellverweis**

Mit Aspose.Cells können Sie den Inhalt einer Arbeitsblattzelle in eine Bildform darstellen. Sie können das Bild mit der Zelle verknüpfen, die die Daten enthält, die Sie anzeigen möchten. Da die Zelle oder Zellenbereich mit dem Grafikobjekt verknüpft ist, erscheinen Änderungen, die Sie an den Daten in dieser Zelle oder dem Zellenbereich vornehmen, automatisch im Grafikobjekt.

Fügen Sie ein Bild hinzu, indem Sie die [**AddPicture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addpicture/)-Methode des [**ShapeCollection**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/) (eingeschlossen im [**Worksheet**](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/)-Objekt) aufrufen. Geben Sie den Zellbereich mit dem Attribut [**GetFormula**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/getformula/) des [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-Objekts an.

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Source and output directories
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Create new workbook
    Workbook workbook;

    // Access first worksheet and cells collection
    WorksheetCollection worksheets = workbook.GetWorksheets();
    Worksheet worksheet = worksheets.Get(0);
    Cells cells = worksheet.GetCells();

    // Set cell values
    cells.Get(u"A1").PutValue(U16String(u"A1"));
    cells.Get(u"C10").PutValue(U16String(u"C10"));

    // Add picture to worksheet
    auto shapes = worksheet.GetShapes();
    Picture pic = shapes.AddPicture(0, 3, 10, 6, Vector<uint8_t>());

    // Set picture formula and update values
    pic.SetFormula(u"A1:C10");
    shapes.UpdateSelectedValue();

    // Save workbook
    U16String outputPath = outDir + u"output.out.xls";
    workbook.Save(outputPath);

    std::cout << "File saved successfully." << std::endl;

    Aspose::Cells::Cleanup();
}
```

## **Erweiterte Themen**
- [Hinzufügen eines bedingten Symbolsets mit dem Zelltext](/cells/de/cpp/add-conditional-icons-set-with-the-cell-text/)
- [Verknüpftes Bild aus Webadresse einfügen](/cells/de/cpp/insert-a-linked-picture-from-web-address/)
- [Bild anhand von Zellenverweis einfügen](/cells/de/cpp/insert-a-picture-based-on-cell-reference/)
- [Laden Sie ein Web-Bild von einer URL in eine Excel-Arbeitsmappe](/cells/de/cpp/load-a-web-image-from-a-url-into-an-excel-worksheet/)
