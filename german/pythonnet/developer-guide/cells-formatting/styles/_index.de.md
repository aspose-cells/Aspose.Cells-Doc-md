---
title: Holen und Setzen von Stil für Zellen
description: Entdecken Sie, wie Sie Datenformatierung und Styling in Aspose.Cells für Python via .NET durchführen, einschließlich Textformatierung, Zahlenformatierung, Datumsformatierung und anderer Styling Optionen. Unser Leitfaden hilft Ihnen, professionell aussehende Tabellen mit ansprechender Formatierung zu erstellen.
keywords: Aspose.Cells für Python via .NET, Datenformatierung, Styling, Textformatierung, Zahlenformatierung, Datumsformatierung, Styling Optionen, Tabellen, ansprechende Formatierung, professionell aussehende.
linktitle: Stile
type: docs
weight: 50
url: /de/python-net/styling-and-data-formatting/
---

{{% alert color="primary" %}} 

Aspose.Cells für Python via .NET führte zwei neue Methoden zur Formatierung von Zellen ein: Cell.GetStyle und Cell.SetStyle. Dieser Artikel untersucht den Ansatz Cell.GetStyle/SetStyle, um zu helfen, welche Technik am besten zu Ihnen passt.

{{% /alert %}} 

## **Formatierung von Zellen**
Es gibt zwei Möglichkeiten, eine Zelle zu formatieren, wie unten dargestellt.

### **Mit GetStyle() verwenden**
Mit dem folgenden Code wird ein Style-Objekt für jede Zelle initiiert, wenn sie formatiert wird. Wenn viele Zellen formatiert werden, wird eine große Menge an Speicher verbraucht, da das Style-Objekt ein großes Objekt ist. Diese Style-Objekte werden erst freigegeben, wenn die Workbook.Save-Methode aufgerufen wird.


**Python**

{{< highlight python >}}

cell.get_style().font.is_bold = True

{{< /highlight >}}

### **Mit SetStyle() verwenden**
Der erste Ansatz ist einfach und unkompliziert, warum haben wir also den zweiten Ansatz hinzugefügt?

Wir haben den zweiten Ansatz hinzugefügt, um den Speicherverbrauch zu optimieren. Nach Verwendung der Cell.GetStyle-Methode zum Abrufen eines Style-Objekts, ändern Sie es und verwenden Sie die Cell.SetStyle-Methode, um es wieder auf diese Zelle zu setzen. Dieses Style-Objekt wird nicht erhalten und .NET GC sammelt es ein, wenn es nicht referenziert wird.

Beim Aufrufen der Cell.SetStyle-Methode wird das Style-Objekt nicht für jede Zelle gespeichert. Stattdessen vergleichen wir dieses Style-Objekt mit einem internen Style-Objektpool, um festzustellen, ob es wiederverwendet werden kann. Nur Style-Objekte, die sich von den vorhandenen unterscheiden, werden für jedes Workbook-Objekt behalten. Dies bedeutet, dass es für jede Excel-Datei nur einige hundert Style-Objekte gibt, anstelle von Tausenden. Für jede Zelle wird nur ein Index zum Style-Objektpool erhalten.



**Python**

{{< highlight python >}}

style = cell.get_style()
style.font.is_bold = True
cell.set_style(style)

{{< /highlight >}}

## **Erweiterte Themen**
- [Erstellen Sie Style-Objekt mit der Klasse CellsFactory](/cells/de/python-net/create-style-object-using-cellsfactory-class/)
- [Ändern eines bestehenden Stils](/cells/de/python-net/modify-an-existing-style/)
- [Wiederverwendung von Stil-Objekten](/cells/de/python-net/reusing-style-objects/)
- [Verwenden von eingebauten Stilen](/cells/de/python-net/using-built-in-styles/)


