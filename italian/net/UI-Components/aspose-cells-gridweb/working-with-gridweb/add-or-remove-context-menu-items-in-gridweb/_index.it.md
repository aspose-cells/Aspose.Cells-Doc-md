---
title: Aggiungi o rimuovi voci dal menu contestuale in GridWeb
type: docs
weight: 130
url: /it/net/aspose-cells-gridweb/add-or-remove-context-menu-items-in-gridweb/
keywords: GridWeb,menu,menu
description: Questo articolo illustra come aggiungere o rimuovere voci dal menu contestuale in GridWeb.
---

{{% alert color="primary" %}} 

È possibile aggiungere voci di menu contestuale utilizzando il markup ASP.NET o utilizzando il codice .NET. È inoltre possibile rimuovere le voci di menu contestuale utilizzando il codice .NET. Si prega di utilizzare i metodi GridWeb.CustomCommandButtons.Add() e GridWeb.CustomCommandButtons.Remove() o RemoveAt() a tale scopo.

{{% /alert %}} 
## **Aggiungi voce di menu contestuale utilizzando il markup ASP.NET**
Il seguente markup ASP.NET aggiunge una voce di menu contestuale in GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem-InitContextMenuItem.aspx" >}}



Ecco il markup completo ASP.NET che crea un GridWeb con la voce di menu contestuale sopra. Si prega di notare l'attributo OnCustomCommand="GridWeb1_CustomCommand". È il nome dell'event handler che verrà chiamato quando la voce di menu contestuale verrà cliccata.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem-InitContextMenuItem.aspx" >}}



Ecco come appare la voce di menu contestuale dopo essere stata aggiunta utilizzando il markup ASP.NET sopra.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_1.png)

Questo è il codice dell'event handler che viene eseguito quando si clicca sulla voce di menu contestuale. Il codice controlla innanzitutto il nome del comando, se corrisponde al nostro comando, aggiunge un testo nella cella A1 della scheda attiva di GridWeb e imposta la larghezza della prima colonna a 40 unità per rendere visibile il testo.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-InitContextMenuItem.aspx-HandleContextMenuItemCommand.cs" >}}


Ecco come appare il GridWeb quando si clicca sulla voce di menu contestuale.

![todo:image_alt_text](add-or-remove-context-menu-items-in-gridweb_2.png)
## **Aggiungere voci di menu contestuale in Aspose.Cells.GridWeb utilizzando il codice**
Questo codice mostra come aggiungere voci di menu contestuale all'interno di un GridWeb utilizzando il codice.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-AddContextMenuItem.cs" >}}
## **Rimuovere voci di menu contestuale in Aspose.Cells.GridWeb utilizzando il codice**
Questo codice mostra come rimuovere voci di menu contestuale utilizzando i metodi CustomCommandButtons.Remove() e CustomCommandButtons.RemoveAt().



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-AddRemoveContextMenuItem.aspx-RemoveContextMenuItem.cs" >}}
