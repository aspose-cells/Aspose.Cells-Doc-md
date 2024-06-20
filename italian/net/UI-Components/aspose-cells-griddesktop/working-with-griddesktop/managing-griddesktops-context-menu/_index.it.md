---
title: Gestione del menu contestuale di GridDesktop
type: docs
weight: 40
url: /it/net/aspose-cells-griddesktop/manage-griddesktops-context-menu/
keywords: GridDesktop, contesto, menu contestuale
description: Questo articolo illustra come personalizzare il menu contestuale in GridDesktop.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridDesktop ha un menu contestuale che contiene tutti i comandi comunemente usati. Il controllo consente di nascondere/mostrare gli elementi di menu. Inoltre, è possibile aggiungere nuovi elementi di menu con gestori di eventi al menu.

{{% /alert %}} 
## **Introduzione**
La classe ContextMenuManager è utilizzata per gestire gli elementi del menu contestuale. L'attributo GridDesktop.ContextMenuManager ottiene l'istanza dell'oggetto ContextMenuManager. Ad esempio, l'attributo ContextMenuManager.MenuItemAvailable_Copy ottiene o imposta un valore indicante se l'elemento di menu contestuale **Copia** è disponibile o meno. Allo stesso modo, abbiamo tutti gli attributi corrispondenti per diversi elementi del menu contestuale.

**IMPORTANTE:** Per impostazione predefinita, tutti gli elementi del menu contestuale sono visibili nell'elenco.
## **Gestione del menu contestuale**
### **Nascondere gli elementi del menu contestuale**
Per eseguire questa operazione, diamo prima un'occhiata al menu contestuale predefinito di GridDesktop.

**Menu predefinito di GridDesktop** 

![todo:image_alt_text](managing-griddesktops-context-menu_1.png)

Ora, nascondi alcuni elementi di menu utilizzando il codice seguente:



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-HideContextMenuItem.cs" >}}



Dopo aver eseguito il codice precedente, alcuni elementi di menu non saranno visibili per gli utenti:

**Alcuni elementi di menu sono nascosti** 

![todo:image_alt_text](managing-griddesktops-context-menu_2.png)
### **Aggiunta di nuovi elementi di menu**
Aggiungi una nuova voce al menu contestuale alla lista utilizzando il seguente frammento di codice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-AddContextMenuItem.cs" >}}


Specifichiamo anche un gestore eventi per il nuovo comando/opzione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithGrid-ManagingContextMenu-EventHandler.cs" >}}



Dopo aver eseguito il codice sopra, una nuova voce di menu può essere vista nel menu contestuale. Comparirà anche un messaggio quando si fa clic sulla cella.

**Una nuova voce di menu è stata aggiunta alla lista** 

![todo:image_alt_text](managing-griddesktops-context-menu_3.png)
