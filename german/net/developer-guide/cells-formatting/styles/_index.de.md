---
title: Stil für Zellen abrufen und festlegen
description: Erfahren Sie in Aspose.Cells for .NET, wie Sie Daten formatieren und formatieren, einschließlich Textformatierung, Zahlenformatierung, Datumsformatierung und anderen Styling-Optionen. Unser Leitfaden hilft Ihnen bei der Erstellung professionell aussehender Tabellenkalkulationen mit attraktiver Formatierung.
keywords: Aspose.Cells for .NET, data formatting, styling, text formatting, number formatting, date formatting, styling options, spreadsheets, attractive formatting, professional-looking.
linktitle: Stile
type: docs
weight: 50
url: /de/net/styling-and-data-formatting/
---
{{% alert color="primary" %}} 

Aspose.Cells for .NET 4.4.2 führte zwei neue Methoden zum Formatieren von Zellen ein: Cell.GetStyle und Cell.SetStyle. In diesem Artikel wird der Cell.GetStyle/SetStyle-Ansatz untersucht, um Ihnen bei der Beurteilung zu helfen, welche Technik am besten zu Ihnen passt.

{{% /alert %}} 
##  **Formatierung Cells**
Es gibt zwei Möglichkeiten, eine Zelle zu formatieren, wie unten dargestellt.
###  **Verwenden von GetStyle()**
Mit dem folgenden Codeteil wird beim Formatieren für jede Zelle ein Style-Objekt initiiert. Wenn sehr viele Zellen formatiert werden, wird viel Speicher verbraucht, da das Style-Objekt ein großes Objekt ist. Diese Style-Objekte werden erst freigegeben, wenn die Workbook.Save-Methode aufgerufen wird.



**C#**

{{< highlight "csharp" >}}

cell.GetStyle().Font.IsBold = true;



{{< /highlight >}}
###  **Verwenden von SetStyle()**
Der erste Ansatz ist einfach und unkompliziert. Warum haben wir also den zweiten Ansatz hinzugefügt?

Wir haben den zweiten Ansatz hinzugefügt, um die Speichernutzung zu optimieren. Nachdem Sie mit der Methode Cell.GetStyle ein Style-Objekt abgerufen haben, ändern Sie es und setzen Sie es mit der Methode Cell.SetStyle wieder auf diese Zelle zurück. Dieses Style-Objekt wird nicht beibehalten und von GC erfasst, wenn nicht darauf verwiesen wird.

Beim Aufruf der Methode Cell.SetStyle wird das Style-Objekt nicht für jede Zelle gespeichert. Stattdessen vergleichen wir dieses Style-Objekt mit einem internen Style-Objektpool, um zu sehen, ob es wiederverwendet werden kann. Für jedes Workbook-Objekt werden nur Style-Objekte beibehalten, die sich von den vorhandenen unterscheiden. Das bedeutet, dass es für jede Excel-Datei nur mehrere Hundert statt Tausender Style-Objekte gibt. Für jede Zelle bleibt nur ein Index zum Style-Objektpool erhalten.



**C#**

{{< highlight "csharp" >}}

Style style = cell.GetStyle();

style.Font.IsBold = true;

cell.SetStyle(style);
{{< /highlight >}}

##  **Vorabthemen**
- [Erstellen Sie ein Style-Objekt mit der CellsFactory-Klasse](/cells/de/net/create-style-object-using-cellsfactory-class/)
- [Ändern Sie einen vorhandenen Stil](/cells/de/net/modify-an-existing-style/)
- [Stilobjekte wiederverwenden](/cells/de/net/reusing-style-objects/)
- [Verwenden integrierter Stile](/cells/de/net/using-built-in-styles/)


