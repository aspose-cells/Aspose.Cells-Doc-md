---
title: Abrufen und Festlegen des Stils für Zellen
linktitle: Stile
type: docs
weight: 50
url: /de/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 führte zwei neue Methoden zum Formatieren von Zellen ein: Cell.GetStyle und Cell.SetStyle. Dieser Artikel untersucht den Cell.GetStyle/SetStyle-Ansatz, um Ihnen bei der Beurteilung zu helfen, welche Technik am besten zu Ihnen passt.

{{% /alert %}} 
## **Formatierung Cells**
Es gibt zwei Möglichkeiten, eine Zelle zu formatieren, wie unten dargestellt.
### **Verwendung von GetStyle()**
Mit dem folgenden Codestück wird für jede Zelle beim Formatieren ein Style-Objekt initiiert. Wenn sehr viele Zellen formatiert werden, wird viel Speicher verbraucht, da das Style-Objekt ein großes Objekt ist. Diese Style-Objekte werden erst freigegeben, wenn die Workbook.Save-Methode aufgerufen wird.



**C#**

{{< highlight "csharp" >}}

 cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
### **SetStyle() verwenden**
Der erste Ansatz ist einfach und unkompliziert, warum haben wir also den zweiten Ansatz hinzugefügt?

Wir haben den zweiten Ansatz hinzugefügt, um die Speichernutzung zu optimieren. Nachdem Sie die Methode Cell.GetStyle zum Abrufen eines Style-Objekts verwendet haben, ändern Sie es und verwenden Sie die Methode Cell.SetStyle, um es auf diese Zelle zurückzusetzen. Dieses Style-Objekt wird nicht beibehalten und .NET GC sammelt es, wenn es nicht referenziert wird.

Beim Aufrufen der Methode Cell.SetStyle wird das Style-Objekt nicht für jede Zelle gespeichert. Stattdessen vergleichen wir dieses Style-Objekt mit einem internen Style-Objektpool, um zu sehen, ob es wiederverwendet werden kann. Für jedes Workbook-Objekt werden nur Style-Objekte beibehalten, die sich von den vorhandenen unterscheiden. Das bedeutet, dass für jede Excel-Datei nur mehrere hundert Style-Objekte statt Tausende vorhanden sind. Für jede Zelle wird nur ein Index zum Style-Objektpool beibehalten.



**C#**

{{< highlight "csharp" >}}

 Stil style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(Stil);


## **Themen vorantreiben**
- [Erstellen Sie ein Style-Objekt mit der CellsFactory-Klasse](/cells/de/net/create-style-object-using-cellsfactory-class/)
- [Ändern Sie einen vorhandenen Stil](/cells/de/net/modify-an-existing-style/)
- [Stilobjekte wiederverwenden](/cells/de/net/reusing-style-objects/)
- [Verwenden von integrierten Stilen](/cells/de/net/using-built-in-styles/)


