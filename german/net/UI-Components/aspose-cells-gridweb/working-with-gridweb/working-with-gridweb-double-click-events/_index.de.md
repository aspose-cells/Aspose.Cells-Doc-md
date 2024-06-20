---
title: Arbeiten mit GridWeb Doppelklickereignissen
type: docs
weight: 80
url: /de/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb, Doppelklick, Klickevent, Ereignis
description: Dieser Artikel stellt vor, wie man das Doppelklick Ereignis in GridWeb verwendet.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb enthält drei Arten von Double-Click-Ereignissen:

- CellDoubleClick, ausgelöst, wenn auf eine Zelle doppelgeklickt wird.
- ColumnDoubleClick, ausgelöst, wenn auf eine Spaltenüberschrift doppelgeklickt wird.
- RowDoubleClick, ausgelöst, wenn auf eine Zeilenüberschrift doppelgeklickt wird.

In diesem Thema wird erläutert, wie Double-Click-Ereignisse in Aspose.Cells.GridWeb aktiviert werden können. Es wird auch die Erstellung von Ereignishandlern für diese Ereignisse erläutert.

{{% /alert %}} 
## **Aktivieren von Double-Click-Ereignissen**
Alle Arten von Double-Click-Ereignissen können clientseitig aktiviert werden, indem die Eigenschaft EnableDoubleClickEvent des GridWeb-Steuerelements auf true gesetzt wird.

{{% alert color="primary" %}} 

Standardmäßig ist die Eigenschaft EnableDoubleClickEvent auf false gesetzt. Dies bedeutet, dass Double-Click-Ereignisse standardmäßig nicht aktiviert sind. Um solche Ereignisse zu implementieren, muss zunächst die Funktion aktiviert werden.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Sobald Double-Click-Ereignisse aktiviert sind, ist es möglich, Ereignishandler für jedes Double-Click-Ereignis zu erstellen. Diese Ereignishandler führen spezifische Aufgaben aus, wenn ein bestimmtes Double-Click-Ereignis ausgelöst wird.
## **Behandlung von Doppelklickereignissen**
Um einen Ereignishandler in Visual Studio zu erstellen:

1. Doppelklicken Sie auf ein Ereignis in der **Ereignisse**-Liste im Eigenschaftenfenster.

In diesem Beispiel haben wir Ereignishandler für verschiedene Doppelklick-Ereignisse implementiert.
### **Zelle doppelklicken**
Der Ereignisbehandlungsroutinen für das CellDoubleClick-Ereignis stellt ein Argument vom Typ CellEventArgs bereit, das die vollständigen Informationen über die Zelle liefert, die doppelgeklickt wurde.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Spaltenkopf doppelklicken**
Der Ereignisbehandlungsroutinen für das ColumnDoubleClick-Ereigniss stellt ein Argument vom Typ RowColumnEventArgs bereit, das die Indexnummer der Spalte für den doppelgeklickten Kopf sowie andere Informationen liefert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Zeilenkopf doppelklicken**
Der Ereignisbehandilungsroutinen für das RowDoubleClick-Ereignis stellt ein Argument vom Typ RowColumnEventArgs bereit, das die Indexnummer der Reihe für den doppelgeklickten Kopf sowie andere relevante Informationen liefert.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
