---
title: Gestione del menu contestuale di GridDesktops
type: docs
weight: 40
url: /it/net/managing-griddesktops-context-menu/
---
{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop ha un menu contestuale che contiene tutti i comandi comunemente usati. Il controllo consente di nascondere/mostrare voci di menu. Inoltre, è possibile aggiungere al menu nuove voci di menu con gestori di eventi.

{{% /alert %}} 
## **introduzione**
La classe ContextMenuManager viene utilizzata per gestire le voci del menu contestuale. L'attributo GridDesktop.ContextMenuManager ottiene l'istanza dell'oggetto ContextMenuManager. Ad esempio, l'attributo ContextMenuManager.MenuItemAvailable_Copy ottiene o imposta un valore che indica se la voce del menu contestuale **Copia** è disponibile o meno. Allo stesso modo, abbiamo tutti gli attributi corrispondenti per le diverse voci del menu contestuale.

**IMPORTANTE:** Per impostazione predefinita, tutte le voci del menu contestuale sono visibili nell'elenco.
## **Gestione del menu contestuale**
### **Nascondere le voci del menu contestuale**
Per eseguire questa attività, per prima cosa diamo un'occhiata al menu contestuale predefinito di GridDesktop.

**Menu predefinito di GridDeskop** 

![cose da fare:immagine_alt_testo](managing-griddesktops-context-menu_1.png)

Ora nascondi alcune voci di menu usando il codice qui sotto:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Dopo aver eseguito il codice sopra, alcune voci di menu non saranno visibili per gli utenti:

**Alcune voci di menu sono nascoste** 

![cose da fare:immagine_alt_testo](managing-griddesktops-context-menu_2.png)
### **Aggiunta di nuove voci di menu**
Aggiungi una nuova voce di menu contestuale all'elenco utilizzando il seguente frammento di codice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Specifichiamo anche un gestore di eventi per il nuovo comando/opzione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Dopo aver eseguito il codice precedente, è possibile visualizzare una nuova voce di menu nel menu contestuale. Apparirà anche un messaggio quando si fa clic sulla cella.

**Una nuova voce di menu viene aggiunta all'elenco** 

![cose da fare:immagine_alt_testo](managing-griddesktops-context-menu_3.png)
