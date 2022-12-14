---
title: Aggiungi o rimuovi voci di menu contestuale in GridWeb
type: docs
weight: 130
url: /it/net/add-or-remove-context-menu-items-in-gridweb/
---
{{% alert color="primary" %}} 

È possibile aggiungere voci di menu di scelta rapida utilizzando il markup ASP.NET o utilizzando il codice .NET. Puoi anche rimuovere le voci del menu di scelta rapida utilizzando il codice .NET. Utilizzare i metodi GridWeb.CustomCommandButtons.Add() e GridWeb.CustomCommandButtons.Remove() o RemoveAt() per questi scopi.

{{% /alert %}} 
## **Aggiungi la voce del menu di scelta rapida utilizzando il markup ASP.NET**
Il markup ASP.NET seguente aggiunge una voce di menu di scelta rapida in GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Ecco il markup ASP.NET completo che crea un GridWeb con la voce del menu di scelta rapida sopra. Si prega di notare l'attributo OnCustomCommand="GridWeb1_CustomCommand". È il nome del gestore eventi che verrà chiamato quando si fa clic sulla voce del menu contestuale.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Ecco come appare la voce del menu di scelta rapida dopo essere stata aggiunta utilizzando il markup ASP.NET sopra.

![cose da fare:immagine_alt_testo](add-or-remove-context-menu-items-in-gridweb_1.png)

Questo è il codice del gestore eventi che viene eseguito quando si fa clic sulla voce del menu contestuale. Il codice controlla prima il nome del comando, se corrisponde al nostro comando, aggiunge un testo nella cella A1 del foglio di lavoro GridWeb attivo e imposta la larghezza della prima colonna su 40 unità per rendere visibile il testo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Ecco come appare GridWeb quando fai clic sulla voce del menu contestuale.

![cose da fare:immagine_alt_testo](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Aggiungi elementi del menu contestuale in Aspose.Cells.GridWeb utilizzando il codice**
Questo codice mostra come aggiungere una voce di menu di scelta rapida all'interno di un GridWeb utilizzando il codice.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Rimuovere le voci del menu contestuale in Aspose.Cells.GridWeb utilizzando il codice**
Questo codice mostra come rimuovere la voce del menu contestuale utilizzando i metodi CustomCommandButtons.Remove() e CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
