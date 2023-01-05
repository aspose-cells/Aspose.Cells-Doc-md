---
title: Arbeiten mit GridWeb Double Click Events
type: docs
weight: 80
url: /de/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb enthält drei Arten von Doppelklickereignissen:

- CellDoubleClick, wird ausgelöst, wenn auf eine Zelle doppelgeklickt wird.
- ColumnDoubleClick, wird ausgelöst, wenn auf eine Spaltenüberschrift doppelgeklickt wird.
- RowDoubleClick, wird ausgelöst, wenn auf eine Zeilenüberschrift doppelgeklickt wird.

In diesem Thema wird erläutert, wie Doppelklickereignisse in Aspose.Cells.GridWeb aktiviert werden. Außerdem wird das Erstellen von Ereignishandlern für diese Ereignisse erläutert.

{{% /alert %}} 
## **Aktivieren von Doppelklickereignissen**
Alle Arten von Doppelklickereignissen können clientseitig aktiviert werden, indem die EnableDoubleClickEvent-Eigenschaft des GridWeb-Steuerelements auf „true“ festgelegt wird.

{{% alert color="primary" %}} 

Standardmäßig ist die Eigenschaft „EnableDoubleClickEvent“ auf „false“ gesetzt. Das bedeutet, dass Doppelklickereignisse standardmäßig nicht aktiviert sind. Um solche Ereignisse zu implementieren, aktivieren Sie zuerst die Funktion.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Sobald Doppelklick-Ereignisse aktiviert sind, ist es möglich, Ereignishandler für beliebige Doppelklick-Ereignisse zu erstellen. Diese Ereignishandler führen bestimmte Aufgaben aus, wenn ein bestimmtes Doppelklickereignis ausgelöst wird.
## **Umgang mit Doppelklickereignissen**
So erstellen Sie einen Ereignishandler in Visual Studio:

1.  Doppelklicken Sie auf ein Ereignis in der**Veranstaltungen** Liste im Bereich Eigenschaften.

Für dieses Beispiel haben wir Ereignishandler für verschiedene Doppelklickereignisse implementiert.
### **Doppelklicken Sie auf Cell**
Der Ereignishandler für das CellDoubleClick-Ereignis stellt ein Argument vom Typ CellEventArgs bereit, das die vollständigen Informationen der Zelle bereitstellt, auf die doppelgeklickt wird.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Doppelklicken Sie auf die Spaltenüberschrift**
Der Ereignishandler für das ColumnDoubleClick-Ereignis stellt ein Argument des RowColumnEventArgs-Typs bereit, das die Indexnummer der Spalte für die Überschrift bereitstellt, auf die doppelt geklickt wurde, sowie weitere Informationen.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Doppelklicken Sie auf den Zeilenkopf**
Der Ereignishandler für das RowDoubleClick-Ereignis stellt ein Argument des RowColumnEventArgs-Typs bereit, das die Indexnummer der Zeile für den Header, auf den doppelgeklickt wurde, und andere zugehörige Informationen bereitstellt.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
