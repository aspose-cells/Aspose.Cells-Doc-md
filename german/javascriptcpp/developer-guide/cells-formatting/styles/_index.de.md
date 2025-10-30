---
title: Holen und Setzen von Stil für Zellen
description: Entdecken Sie, wie Sie Daten in Aspose.Cells for JavaScript via C++ formatieren und stylen können, einschließlich Textformatierung, Zahlen und Datumformatierung sowie anderer Gestaltungsmöglichkeiten. Unser Leitfaden hilft Ihnen, professionell gestaltete Tabellen mit ansprechendem Format zu erstellen.
keywords: Aspose.Cells for JavaScript via C++, Datenformatierung, Styling, Textformatierung, Zahlenformatierung, Datumformatierung, Stiloptionen, Tabellen, attraktives Design, professionelles Aussehen.
linktitle: Stile
type: docs
weight: 50
url: /de/javascript-cpp/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells for JavaScript via C++ führte zwei neue Methoden zur Formatierung von Zellen ein: Cell.style und Cell.style. Dieser Artikel untersucht den Cell.style/style-Ansatz, um zu beurteilen, welche Technik am besten zu Ihnen passt.

{{% /alert %}} 
## **Formatierung von Zellen**
Es gibt zwei Möglichkeiten, eine Zelle zu formatieren, wie unten dargestellt.
### **Verwendung von Stil**
Mit folgendem Code wird für jede Zelle beim Formatieren ein Style-Objekt initialisiert. Wenn viele Zellen formatiert werden, verbraucht dies viel Speicher, da das Style-Objekt groß ist. Diese Style-Objekte werden erst freigegeben, wenn die Methode Workbook.save aufgerufen wird.

**JavaScript**

{{< highlight javascript >}}
cell.style.font.isBold = true;
{{< /highlight >}}
### **Verwendung von Stil**
Der erste Ansatz ist einfach und unkompliziert, warum haben wir also den zweiten Ansatz hinzugefügt?

Wir haben den zweiten Ansatz hinzugefügt, um den Speicherverbrauch zu optimieren. Nach der Verwendung der Cell.style-Eigenschaft zum Abrufen eines Style-Objekts können Sie dieses ändern und wieder zuweisen, indem Sie die Cell.style-Eigenschaft auf diese Zelle setzen. Dieses Style-Objekt wird nicht gespeichert und der JavaScript-Garbage-Collector wird es entfernen, wenn keine Referenz darauf besteht.

Beim Zuweisen der Cell.style-Eigenschaft wird das Style-Objekt nicht für jede Zelle gespeichert. Stattdessen vergleichen wir dieses Style-Objekt mit einem internen Style-Objekt-Pool, um zu prüfen, ob es wiederverwendet werden kann. Nur Style-Objekte, die sich von den bestehenden unterscheiden, werden für jedes Workbook beibehalten. Das bedeutet, dass für jede Excel-Datei nur einige hundert Style-Objekte vorhanden sind, anstatt Tausende. Für jede Zelle wird nur ein Index zum Style-Objekt-Pool gespeichert.

**JavaScript**

{{< highlight javascript >}}
let style = cell.style;

style.font.isBold = true;

cell.style = style;
{{< /highlight >}}

## **Erweiterte Themen**
- [Erstellen Sie Style-Objekt mit der Klasse CellsFactory](/cells/de/javascript-cpp/create-style-object-using-cellsfactory-class/)
- [Ändern eines bestehenden Stils](/cells/de/javascript-cpp/modify-an-existing-style/)
- [Wiederverwendung von Stil-Objekten](/cells/de/javascript-cpp/reusing-style-objects/)
- [Verwenden von eingebauten Stilen](/cells/de/javascript-cpp/using-built-in-styles/)
