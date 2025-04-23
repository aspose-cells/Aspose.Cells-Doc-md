---
title: Holen und Setzen von Stil für Zellen
description: Entdecken Sie, wie Sie Datenformatierung und Stil in Aspose.Cells for Node.js via C++ durchführen, einschließlich Textformatierung, Zahlenformatierung, Datumsformatierung und andere Stiloptionen. Unser Leitfaden hilft Ihnen, professionell aussehende Tabellen mit attraktiver Formatierung zu erstellen.
keywords: Aspose.Cells for Node.js via C++, Datenformatierung, Styling, Textformatierung, Zahlenformatierung, Datumsformatierung, Stiloptionen, Tabellen, attraktive Formatierung, professionell aussehende Tabellen.
linktitle: Stile
type: docs
weight: 50
url: /de/nodejs-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for Node.js via C++ hat zwei neue Methoden zur Formatierung von Zellen eingeführt: Cell.getStyle und Cell.setStyle. Dieser Artikel untersucht den Ansatz Cell.getStyle/setStyle, um Ihnen bei der Bewertung zu helfen, welche Technik am besten zu Ihnen passt.

{{% /alert %}} 
## **Formatierung von Zellen**
Es gibt zwei Möglichkeiten, eine Zelle zu formatieren, wie unten dargestellt.
### **Verwendung von getStyle()**
Mit folgendem Code wird für jede Zelle beim Formatieren ein Style-Objekt initialisiert. Wenn viele Zellen formatiert werden, verbraucht dies viel Speicher, da das Style-Objekt groß ist. Diese Style-Objekte werden erst freigegeben, wenn die Methode Workbook.save aufgerufen wird.

**JavaScript**

{{< highlight javascript >}}
cell.getStyle().getFont().setIsBold(true);
{{< /highlight >}}
### **Verwendung von setStyle()**
Der erste Ansatz ist einfach und unkompliziert, warum haben wir also den zweiten Ansatz hinzugefügt?

Wir haben den zweiten Ansatz hinzugefügt, um den Speicherverbrauch zu optimieren. Nach Verwendung der Cell.getStyle-Methode, um ein Style-Objekt abzurufen, dieses zu modifizieren und mit der Cell.setStyle-Methode wieder auf die Zelle zu setzen. Dieses Style-Objekt wird nicht gespeichert und der JavaScript-Garbage-Collector wird es sammeln, wenn es nicht mehr referenziert wird.

Beim Aufrufen der Cell.setStyle-Methode wird das Style-Objekt nicht für jede Zelle gespeichert. Stattdessen vergleichen wir dieses Style-Objekt mit einem internen Style-Pool, um festzustellen, ob es wiederverwendet werden kann. Nur Style-Objekte, die sich von den vorhandenen unterscheiden, werden für jede Arbeitsmappe beibehalten. Das bedeutet, dass es nur einige hundert Style-Objekte pro Excel-Datei gibt, anstatt Tausende. Für jede Zelle wird nur ein Index zum Style-Pool gespeichert.

**JavaScript**

{{< highlight javascript >}}
let style = cell.getStyle();

style.getFont().setIsBold(true);

cell.setStyle(style);
{{< /highlight >}}

## **Erweiterte Themen**
- [Erstellen Sie Style-Objekt mit der Klasse CellsFactory](/cells/de/nodejs-cpp/create-style-object-using-cellsfactory-class/)
- [Ändern eines bestehenden Stils](/cells/de/nodejs-cpp/modify-an-existing-style/)
- [Wiederverwendung von Stil-Objekten](/cells/de/nodejs-cpp/reusing-style-objects/)
- [Verwenden von eingebauten Stilen](/cells/de/nodejs-cpp/using-built-in-styles/)

