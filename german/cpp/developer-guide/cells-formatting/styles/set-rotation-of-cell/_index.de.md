---
title: So rotiert man den Text einer Zelle mit C++
linktitle: Wie man Text in einer Zelle dreht
type: docs
weight: 80
url: /de/cpp/how-to-rotate-text-of-cell/
description: C++ Code zur Drehung des Zellentexts mit der API Aspose.Cells for C++
keywords: c++ Drehung des Textes in einer Zelle, c++ Programm zur programmatischen Drehung des Textes in einer Zelle im Arbeitsbuch, programmatische Einstellung des Zellrotationswinkels im Arbeitsbuch, c++ wie man den Text in einer Zelle in Excel dreht
---

## **Text einer Zelle in Aspose.Cells drehen**

Aspose.Cells ist eine leistungsstarke C++-Komponente, die Entwicklern ermöglicht, Excel-Tabellen programmatisch zu bearbeiten. Eine der Funktionen von Aspose.Cells ist die Fähigkeit, Zellen zu rotieren, um die Ausrichtung des Textes anzupassen und die visuelle Darstellung Ihrer Daten zu verbessern. In diesem Dokument erfahren Sie, wie man Zellen mit Aspose.Cells rotiert.

## **Wie man den Text einer Zelle in Excel dreht**
Um eine Zelle in Excel zu drehen, können Sie die folgenden Schritte verwenden:
1. Öffnen Sie Excel und wählen Sie die Zelle oder den Zellenbereich aus, den Sie drehen möchten.
1. Klicken Sie mit der rechten Maustaste auf die ausgewählte Zelle(n) und wählen Sie "Zellen formatieren" aus dem Kontextmenü. Alternativ können Sie zum Register "Start" im Excel-Menüband gehen, auf die Dropdown-Schaltfläche "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.
1. In dem Dialogfeld "Zellen formatieren" wechseln Sie zum Register "Ausrichtung".
1. Im Abschnitt "Ausrichtung" sehen Sie die Optionen zum Drehen des Textes. Sie können den gewünschten Drehwinkel in Grad direkt in das Feld "Grad" eingeben. Positive Werte drehen den Text gegen den Uhrzeigersinn, und negative Werte drehen ihn im Uhrzeigersinn.
<br>
![todo:image_alt_text](alignment.png)
1. Nachdem Sie die gewünschte Rotation ausgewählt haben, klicken Sie auf "OK", um die Änderungen anzuwenden. Die ausgewählte(n) Zelle(n) wird/werden nun je nach gewähltem Rotationswinkel oder -orientierung gedreht.

## **Wie man den Text einer Zelle mit Aspose.Cells API dreht**

Die [**Style.GetRotationAngle()**](https://reference.aspose.com/cells/cpp/aspose.cells/style/getrotationangle/)-Eigenschaft macht es bequem, Zellen zu drehen. Um Zellen in Aspose.Cells zu drehen, müssen Sie die folgenden Schritte befolgen:
1. Laden Sie die Excel-Arbeitsmappe
<br>
Zunächst müssen Sie die Excel-Arbeitsmappe mit Aspose.Cells laden. Sie können die Workbook-Klasse verwenden, um eine vorhandene Excel-Datei zu öffnen oder eine neue zu erstellen. 

1. Zugriff auf das Arbeitsblatt
<br>
Sobald die Arbeitsmappe geladen ist, müssen Sie auf das Arbeitsblatt zugreifen, auf dem Sie die Zellen drehen möchten. Sie können entweder auf das Arbeitsblatt nach Index oder Namen zugreifen. 

1. Text der Zelle drehen
<br>
Nun, da Sie Zugriff auf das Arbeitsblatt haben, können Sie die Zellen drehen, indem Sie das Style-Objekt der gewünschten Zellen ändern. Das Style-Objekt ermöglicht es Ihnen, verschiedene Formatierungsoptionen festzulegen, einschließlich der Rotation. 

1. Arbeitsmappe speichern
<br>
Nachdem die Zellen gedreht wurden, können Sie die modifizierte Arbeitsmappe mithilfe der Save-Methode wieder in eine Datei oder einen Stream speichern.

## **C++ Beispielcode**

Bitte beachten Sie den folgenden Code, er erstellt ein Arbeitsmappenobjekt und setzt verschiedene Rotationswinkel für mehrere Zellen. Der Screenshot zeigt das Ergebnis nach der Ausführung des Beispielscodes.
<br>
<img src="rotation.png" width=80% />

```cpp
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main()
{
    Aspose::Cells::Startup();

    // Create a new workbook
    Workbook workbook;

    // Get the first worksheet
    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    // Row index of the cell
    int row = 0;
    // Column index of the cell
    int column = 0;

    // Get cell A1 and set its value
    Cell a1 = worksheet.GetCells().Get(row, column);
    a1.PutValue(u"a1 rotate text");
    Style a1Style = a1.GetStyle();

    // Set the rotation angle in degrees
    a1Style.SetRotationAngle(45);
    a1.SetStyle(a1Style);

    // Set column index to 1 for cell B1
    column = 1;
    Cell b1 = worksheet.GetCells().Get(row, column);
    b1.PutValue(u"b1 rotate text");
    Style b1Style = b1.GetStyle();

    // Set the rotation angle in degrees
    b1Style.SetRotationAngle(255);
    b1.SetStyle(b1Style);

    // Set column index to 2 for cell C1
    column = 2;
    Cell c1 = worksheet.GetCells().Get(row, column);
    c1.PutValue(u"c1 rotate text");
    Style c1Style = c1.GetStyle();

    // Set the rotation angle in degrees
    c1Style.SetRotationAngle(-90);
    c1.SetStyle(c1Style);

    // Set column index to 3 for cell D1
    column = 3;
    Cell d1 = worksheet.GetCells().Get(row, column);
    d1.PutValue(u"d1 rotate text");
    Style d1Style = d1.GetStyle();

    // Set the rotation angle in degrees
    d1Style.SetRotationAngle(-90);
    d1.SetStyle(d1Style);

    // Save the workbook
    workbook.Save(u"out.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
