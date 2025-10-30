---
title: Formatieren Sie Bereiche mit C++
linktitle: Bereiche formatieren
type: docs
weight: 105
url: /de/cpp/how-to-format-a-range/
description: Erfahren Sie, wie Sie Bereiche in Excel mit Aspose.Cells und C++ formatieren. Wenden Sie Stile, Schriftarten und Farben programmatisch auf Zellbereiche an.
---

## **Mögliche Verwendungsszenarien**
Wenn Sie einen Stil auf einen Bereich anwenden möchten, können Sie die Bereichsformatierung verwenden.

## **Wie formatiert man einen Bereich in Excel**

Um einen Zellenbereich in Excel zu formatieren, können Sie die von Excel bereitgestellten integrierten Formatierungsoptionen verwenden. So formatieren Sie einen Zellenbereich direkt in Excel:

1. Öffnen Sie Excel und öffnen Sie die Arbeitsmappe, die den zu formatierenden Bereich enthält.

2. Wählen Sie den zu formatierenden Zellenbereich aus. Sie können klicken und ziehen, um den Bereich auszuwählen, oder Sie können Tastenkombinationen wie Umschalttaste + Pfeiltasten verwenden, um die Auswahl zu erweitern.

3. Wenn der Bereich ausgewählt ist, klicken Sie mit der rechten Maustaste auf den ausgewählten Bereich und wählen Sie "Zellen formatieren" im Kontextmenü aus. Alternativ können Sie zum Start-Tab im Excel-Ribbon gehen, auf die Dropdown-Liste "Format" in der Gruppe "Zellen" klicken und "Zellen formatieren" auswählen.

4. Das Dialogfeld "Zellen formatieren" wird angezeigt. Hier können Sie verschiedene Formatierungsoptionen auswählen, die auf den ausgewählten Bereich angewendet werden sollen. Sie können beispielsweise den Schriftstil, die Schriftgröße, die Schriftfarbe, das Zahlenformat, die Rahmen, die Hintergrundfarbe usw. ändern. Erkunden Sie die verschiedenen Registerkarten im Dialogfeld, um auf verschiedene Formatierungsoptionen zuzugreifen.

5. Nachdem Sie die gewünschten Formatierungsänderungen vorgenommen haben, klicken Sie auf die Schaltfläche "OK", um die Formatierung auf den ausgewählten Bereich anzuwenden.

## **Wie formatiert man einen Bereich mit C++**

Um einen Bereich mit Aspose.Cells zu formatieren, können Sie die folgenden Methoden verwenden:
1. [Range.ApplyStyle(Style style, StyleFlag flag)](https://reference.aspose.com/cells/cpp/aspose.cells/range/applystyle/)
2. [Range.SetStyle(Style style)](https://reference.aspose.com/cells/cpp/aspose.cells/range/setstyle/)

## **Beispielcode**
In diesem Beispiel erstellen wir eine Excel-Arbeitsmappe, fügen einige Beispiel-Daten hinzu, greifen auf das erste Arbeitsblatt zu, definieren zwei Bereiche („A1:C3“ und „A4:C5“). Dann erstellen wir neue Stile, legen verschiedene Formatierungsoptionen fest (z.B. Schriftfarbe, Fett), und wenden den Stil auf den Bereich an. Schließlich speichern wir die Arbeitsmappe in einer neuen Datei.
<br>
![todo:image_alt_text](format-range.png)

```c++
#include <iostream>
#include "Aspose.Cells.h"
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook workbook;
    Worksheet ws = workbook.GetWorksheets().Get(0);
    Cells cells = ws.GetCells();

    Cell cell = cells.Get(u"A1");
    cell.PutValue(u"Fruit");
    cell = cells.Get(u"B1");
    cell.PutValue(u"Count");
    cell = cells.Get(u"C1");
    cell.PutValue(u"Price");

    cell = cells.Get(u"A2");
    cell.PutValue(u"Apple");
    cell = cells.Get(u"A3");
    cell.PutValue(u"Mango");
    cell = cells.Get(u"A4");
    cell.PutValue(u"Blackberry");
    cell = cells.Get(u"A5");
    cell.PutValue(u"Cherry");

    cell = cells.Get(u"B2");
    cell.PutValue(5);
    cell = cells.Get(u"B3");
    cell.PutValue(3);
    cell = cells.Get(u"B4");
    cell.PutValue(6);
    cell = cells.Get(u"B5");
    cell.PutValue(4);

    cell = cells.Get(u"C2");
    cell.PutValue(5);
    cell = cells.Get(u"C3");
    cell.PutValue(20);
    cell = cells.Get(u"C4");
    cell.PutValue(30);
    cell = cells.Get(u"C5");
    cell.PutValue(60);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Range range = worksheet.GetCells().CreateRange(u"A1:C3");
    Style style = workbook.CreateStyle();
    style.GetFont().SetColor(Color::Red());
    style.GetFont().SetIsBold(true);

    StyleFlag flag;
    flag.SetFont(true);
    range.ApplyStyle(style, flag);

    Range range2 = worksheet.GetCells().CreateRange(u"A4:C5");
    Style style2 = workbook.CreateStyle();
    style2.GetFont().SetColor(Color::Blue());
    style2.GetFont().SetIsItalic(true);
    range2.SetStyle(style2);

    workbook.Save(u"output.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```
{{< app/cells/assistant language="cpp" >}}
