---
title: Wie man ein Bild in eine Zelle mit C++ einfügt
linktitle: Wie man ein Bild in eine Zelle einfügt
type: docs
weight: 130
url: /de/cpp/how-to-insert-picture-in-cell/
description: Lernen Sie, wie Sie mit Aspose.Cells und C++ ein Bild in eine Zelle einfügen.
keywords: Wie man ein Bild in einer Zelle einfügt, ein Bild über Zellen einfügt, ein Bild in einer Zelle platziert, ein Bild über Zellen platziert, wie man ein Bild in einer Zelle platziert, wie man ein Bild über Zellen platziert, zwischen Bild in Zelle und Bild über Zellen wechseln, zwischen Platz in Zelle und Platz über Zellen wechseln.
---

## **Mögliche Verwendungsszenarien**
Das Bild verleiht Ihrem Arbeitsblatt einen Hauch von Helligkeit und bietet eine visuelle Darstellung des Inhalts. Es erleichtert auch das Verständnis der Daten und das Erkennen von Erkenntnissen. Obwohl Sie Bilder in Excel seit vielen Jahren verwenden können, wurde die Funktion, dass Bilder tatsächliche Zellenwerte werden, erst kürzlich aktiviert. Selbst wenn das Layout des Bildes geändert wird, bleibt es an die Daten gebunden. Sie können es in Tabellen, Sortierungen, Filtern, in Formeln verwenden usw.!

## **Wie man ein Bild in eine Zelle einfügt mit Excel**
Zum Einfügen eines Bildes in eine Zelle in Excel befolgen Sie diese Schritte:

1. Gehen Sie zum Register 'Einfügen' und klicken Sie auf die Option 'Bilder'.
2. Wählen Sie **Platzieren in Zelle** aus. Wählen Sie eine der folgenden Quellen aus dem Dropdown-Menü 'Bild einfügen von' aus (**Dieses Gerät**, **Stockbilder** und **Online-Bilder**). Dieses Gerät zum Einfügen eines Bildes von Ihrem Gerät. Stockbilder zum Einfügen eines Bildes aus Stockbildern. Online-Bilder zum Einfügen eines Bildes aus dem Web.
<br>
<img src="1.png" width=60% />
3. Bild auswählen und Bild in Zelle einfügen.
<br>
<img src="8.png" width=60% />

## **Wie man ein Bild über Zellen in Excel einfügt**
Zum Einfügen eines Bildes über Zellen in Excel befolgen Sie diese Schritte:

1. Gehen Sie zum Register 'Einfügen' und klicken Sie auf die Option 'Bilder'.
2. Wählen Sie **Über Zellen platzieren** aus. Wählen Sie eine der folgenden Quellen aus dem Dropdown-Menü 'Bild einfügen von' aus (**Dieses Gerät**, **Stockbilder** und **Online-Bilder**). Dieses Gerät zum Einfügen eines Bildes von Ihrem Gerät. Stockbilder zum Einfügen eines Bildes aus Stockbildern. Online-Bilder zum Einfügen eines Bildes aus dem Web.
<br>
<img src="2.png" width=60% />
3. Bild auswählen und Bild über Zellen einfügen.
<br>
<img src="3.png" width=60% />

## **Wie man von Bild in Zelle zu Bild über Zellen in Excel wechselt**
Sie können ganz einfach von **Bild in Zelle** zu **Bild über Zellen** wechseln. Befolgen Sie bitte diese Schritte:
1. Klicken Sie mit der rechten Maustaste auf die Zelle und wählen Sie **Bild in Zelle** > **Über Zellen platzieren**. 
<br>
<img src="4.png" width=60% />
2. Das Ergebnis nach dem Umschalten lautet wie folgt:
<br>
<img src="5.png" width=60% />

## **Wie man von Bild über Zellen zu Bild in Zelle in Excel wechselt**
Sie können ganz einfach von **Bild über Zellen** zu **Bild in Zelle** wechseln. Befolgen Sie bitte diese Schritte:
1. Klicken Sie mit der rechten Maustaste auf das Bild und wählen Sie **In Zelle platzieren**. 
<br>
<img src="6.png" width=60% />
2. Das Ergebnis nach dem Umschalten lautet wie folgt:
<br>
<img src="7.png" width=60% />

## **So fügen Sie ein Bild in eine Zelle mit C++ ein**
Bild in Zelle mit Aspose.Cells einfügen. Bitte beachten Sie den folgenden Beispielcode. Nach Ausführung des Beispielcodes wird ein Bild in eine Zelle eingefügt.
1. Instanziieren Sie ein Workbook-Objekt. 
2. Holen Sie sich die Zelle, in die Sie das Bild einfügen möchten.
3. Setzen Sie die Eigenschaft Cell.EmbeddedImage. 
4. Schließlich wird die Arbeitsmappe im [XLSX-Ausgabeformat](out.xlsx) gespeichert. 

## **Beispielcode**

```c++
#include <iostream>
#include <fstream>
#include <vector>
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Get cell D8
    Cell d8 = worksheet.GetCells().Get(u"D8");

    // Read image file into byte vector
    std::ifstream file("aspose.png", std::ios::binary);
    std::vector<uint8_t> imageData((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    // Convert to Aspose's Vector and set embedded image in cell D8
    d8.SetEmbeddedImage(Vector<uint8_t>(imageData.data(), imageData.size()));

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
