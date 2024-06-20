---
title: Lavorare con gli eventi di doppio clic in GridWeb
type: docs
weight: 80
url: /it/net/aspose-cells-gridweb/gridweb-double-click-event/
keywords: GridWeb, doppio clic, evento di clic, evento
description: Questo articolo introduce come utilizzare l evento di doppio clic in GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contiene tre tipi di eventi di doppio clic:

- CellDoubleClick, attivato quando viene effettuato un doppio clic su una cella.
- ColumnDoubleClick, attivato quando viene effettuato un doppio clic sull'intestazione di una colonna.
- RowDoubleClick, attivato quando viene effettuato un doppio clic sull'intestazione di una riga.

Questo argomento tratta su come abilitare eventi di doppio clic in Aspose.Cells.GridWeb. Tratta anche la creazione di gestori di eventi per questi eventi.

{{% /alert %}} 
## **Abilita eventi di doppio clic**
Tutti i tipi di eventi di doppio clic possono essere abilitati lato client impostando la proprietà EnableDoubleClickEvent del controllo GridWeb su true.

{{% alert color="primary" %}} 

Per impostazione predefinita, la proprietà EnableDoubleClickEvent è impostata su false. Ciò significa che gli eventi di doppio clic non sono abilitati per impostazione predefinita. Per implementare tali eventi, abilitare prima la funzionalità.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Una volta abilitati gli eventi di doppio clic, è possibile creare gestori di eventi per qualsiasi evento di doppio clic. Questi gestori di eventi eseguono attività specifiche quando un dato evento di doppio clic viene attivato.
## **Gestione degli eventi di doppio clic**
Per creare un gestore di eventi in Visual Studio:

1. Fare doppio clic su un evento nella lista degli **Eventi** nel riquadro Proprietà.

Per questo esempio, abbiamo implementato gestori di eventi per vari eventi di doppio clic.
### **Doppio clic cella**
Il gestore di eventi per l'evento CellDoubleClick fornisce un argomento del tipo CellEventArgs, che fornisce le informazioni complete della cella su cui è stato effettuato il doppio clic.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Doppio clic su intestazione colonna**
Il gestore di eventi per l'evento ColumnDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della colonna dell'intestazione su cui è stato effettuato il doppio clic e altre informazioni.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Doppio clic su intestazione riga**
Il gestore di eventi per l'evento RowDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della riga dell'intestazione su cui è stato effettuato il doppio clic e altre informazioni correlate.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
