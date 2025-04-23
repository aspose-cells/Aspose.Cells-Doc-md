---
title: Style für Zellen mit C++ abrufen und setzen
linktitle: Stile
type: docs
weight: 50
url: /de/cpp/styling-and-data-formatting/
description: Entdecken Sie, wie man Datenformatierung und styling in Aspose.Cells for C++ durchführt, einschließlich Textformatierung, Zahlenformatierung, Datumsformatierung und weiterer Styling Optionen. Unser Leitfaden hilft Ihnen, professionell aussehende Tabellen mit attraktiver Formatierung zu erstellen.
keywords: Aspose.Cells for C++, Datenformatierung, Styling, Textformatierung, Zahlenformatierung, Datumsformatierung, Styling Optionen, Tabellen, attraktive Gestaltung, professionell aussehende.
---

{{% alert color="primary" %}}

Aspose.Cells for C++ führte zwei neue Methoden zur Formatierung von Zellen ein: `Cell.GetStyle` und `Cell.SetStyle`. Dieser Artikel untersucht die `Cell.GetStyle`/-`SetStyle`-Technik, um Ihnen bei der Auswahl der besten Methode zu helfen.

{{% /alert %}}

## **Formatierung von Zellen**
Es gibt zwei Möglichkeiten, eine Zelle zu formatieren, wie unten dargestellt.

### **Mit GetStyle() verwenden**
Mit folgendem Code wird für jede Zelle beim Formatieren ein `Style`-Objekt initialisiert. Wenn viele Zellen formatiert werden, entsteht ein hoher Speicherverbrauch, da das `Style`-Objekt groß ist. Diese `Style`-Objekte werden erst freigegeben, wenn die `Workbook.Save`-Methode aufgerufen wird.

**C++**

```cpp
cell.GetStyle()->GetFont()->SetIsBold(true);
```

### **Mit SetStyle() verwenden**
Der erste Ansatz ist einfach und direkt, warum haben wir den zweiten Ansatz hinzugefügt?

Wir haben den zweiten Ansatz hinzugefügt, um den Speicherverbrauch zu optimieren. Nach der Verwendung der `Cell.GetStyle`-Methode zum Abruf eines `Style`-Objekts, kann es geändert und mit der `Cell.SetStyle`-Methode wieder an die Zelle gebunden werden. Dieses `Style`-Objekt wird nicht dauerhaft gespeichert, und die C++-Laufzeit sammelt es, wenn es nicht mehr referenziert wird.

Beim Aufruf der `Cell.SetStyle`-Methode wird das `Style`-Objekt nicht für jede Zelle gespeichert. Stattdessen vergleichen wir dieses `Style`-Objekt mit einem internen `Style`-Pool, um festzustellen, ob es wiederverwendbar ist. Nur `Style`-Objekte, die sich von bestehenden unterscheiden, werden für jedes `Workbook`-Objekt gespeichert. Das bedeutet, dass es nur wenige hundert `Style`-Objekte pro Excel-Datei gibt, statt Tausende. Für jede Zelle wird nur ein Index auf den `Style`-Pool gespeichert.

**C++**

```cpp
auto style = cell.GetStyle();
style->GetFont()->SetIsBold(true);
cell.SetStyle(style);
```

## **Erweiterte Themen**
- [Erstellen Sie Style-Objekt mit der Klasse CellsFactory](/cells/de/cpp/create-style-object-using-cellsfactory-class/)
- [Ändern eines bestehenden Stils](/cells/de/cpp/modify-an-existing-style/)
- [Wiederverwendung von Stil-Objekten](/cells/de/cpp/reusing-style-objects/)
- [Verwenden von eingebauten Stilen](/cells/de/cpp/using-built-in-styles/)
