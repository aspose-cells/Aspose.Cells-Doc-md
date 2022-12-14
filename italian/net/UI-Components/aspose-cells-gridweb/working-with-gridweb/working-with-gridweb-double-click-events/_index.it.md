---
title: Lavorare con gli eventi doppio clic di GridWeb
type: docs
weight: 80
url: /it/net/working-with-gridweb-double-click-events/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridWeb contiene tre tipi di eventi doppio clic:

- CellDoubleClick, attivato quando si fa doppio clic su una cella.
- ColumnDoubleClick, attivato quando si fa doppio clic sull'intestazione di una colonna.
- RowDoubleClick, attivato quando si fa doppio clic su un'intestazione di riga.

Questo argomento illustra come abilitare gli eventi di doppio clic in Aspose.Cells.GridWeb. Discute anche la creazione di gestori di eventi per questi eventi.

{{% /alert %}} 
## **Abilitazione degli eventi doppio clic**
Tutti i tipi di eventi doppio clic possono essere abilitati sul lato client impostando la proprietà EnableDoubleClickEvent del controllo GridWeb su true.

{{% alert color="primary" %}} 

Per impostazione predefinita, la proprietà EnableDoubleClickEvent è impostata su false. Ciò significa che gli eventi doppio clic non sono abilitati per impostazione predefinita. Per implementare tali eventi, abilita prima la funzione.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-EnableDoubleClickEvents.cs" >}}



Una volta abilitati gli eventi di doppio clic, è possibile creare gestori di eventi per qualsiasi evento di doppio clic. Questi gestori di eventi eseguono attività specifiche quando viene attivato un determinato evento di doppio clic.
## **Gestione degli eventi DoubleClick**
Per creare un gestore eventi in Visual Studio:

1.  Fare doppio clic su un evento nel file**Eventi** elenco nel riquadro Proprietà.

Per questo esempio, abbiamo implementato gestori di eventi per vari eventi di doppio clic.
### **Doppio clic Cell**
Il gestore eventi per l'evento CellDoubleClick fornisce un argomento del tipo CellEventArgs, che fornisce le informazioni complete della cella su cui si fa doppio clic.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-CellDoubleClickEvent.cs" >}}
### **Fare doppio clic sull'intestazione della colonna**
Il gestore eventi per l'evento ColumnDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della colonna per l'intestazione su cui è stato fatto doppio clic e altre informazioni.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-ColumnDoubleClickEvent.cs" >}}
### **Fare doppio clic sull'intestazione della riga**
Il gestore eventi per l'evento RowDoubleClick fornisce un argomento del tipo RowColumnEventArgs che fornisce il numero di indice della riga per l'intestazione su cui è stato fatto doppio clic e altre informazioni correlate.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-HandleDoubleClickEvents.aspx-RowDoubleClickEvent.cs" >}}
