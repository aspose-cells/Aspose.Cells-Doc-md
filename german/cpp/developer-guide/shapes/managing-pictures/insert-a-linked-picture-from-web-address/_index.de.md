---
title: Fügen Sie ein verknüpftes Bild von einer Webadresse mit C++ ein
linktitle: Verknüpftes Bild aus Webadresse einfügen
type: docs
weight: 450
url: /de/cpp/insert-a-linked-picture-from-web-address/
description: Erfahren Sie, wie Sie ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt mit Aspose.Cells for C++ einfügen.
---

{{% alert color="primary" %}}

Manchmal müssen Sie ein Bild von der Webseite (http://) in ein Arbeitsblatt einfügen. Geben Sie dazu die URL des Bildes an, und das Bild wird jedes Mal heruntergeladen, wenn die Tabelle in Microsoft Excel geöffnet wird. Das Bild ist nicht physisch in das Excel-Dokument eingebettet, sondern verweist auf eine Webressource.

{{% /alert %}}

## **Verwendung von Microsoft Excel**

In Microsoft Excel (zum Beispiel 2007):

1. Klicken Sie auf das **Einfügen** Menü und wählen Sie **Bild** aus.
1. Geben Sie die Webadresse für das Bild im Dialogfeld Bild einfügen an.

## **Mit Aspose.Cells for C++ verwenden**

Aspose.Cells for C++ unterstützt das Hinzufügen eines verknüpften Bildes mit der Methode [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapecollection/addlinkedpicture/). Die Methode gibt ein [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/)-Objekt zurück.

Das folgende Beispiel zeigt, wie man ein verknüpftes Bild von einer Webadresse in ein Arbeitsblatt einfügt.

```cpp
#include <iostream>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;
using namespace Aspose::Cells::Drawing;

int main()
{
    Aspose::Cells::Startup();

    // Source directory path
    U16String srcDir(u"..\\Data\\01_SourceDirectory\\");

    // Output directory path
    U16String outDir(u"..\\Data\\02_OutputDirectory\\");

    // Instantiate a new Workbook
    Workbook workbook;

    // Insert a linked picture (from Web Address) to B2 Cell
    U16String imageUrl(u"http://www.aspose.com/Images/aspose-logo.jpg");
    Picture pic = workbook.GetWorksheets().Get(0).GetShapes().AddLinkedPicture(1, 1, 100, 100, imageUrl);

    // Set the height and width of the inserted image
    pic.SetHeightInch(1.04);
    pic.SetWidthInch(2.6);

    // Save the Excel file
    U16String outputPath = outDir + u"outLinkedPicture.out.xlsx";
    workbook.Save(outputPath);

    std::cout << "Linked picture inserted successfully!" << std::endl;

    Aspose::Cells::Cleanup();
}
```
