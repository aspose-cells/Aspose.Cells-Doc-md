---
title: Gestione commenti nel foglio di lavoro
type: docs
weight: 110
url: /it/net/aspose-cells-gridweb/manage-comment-in-worksheet/
keywords: GridWeb,comment
description: Questo articolo presenta come lavorare con i commenti in GridWeb.
---

{{% alert color="primary" %}} 

Questo argomento discute l'aggiunta, l'accesso e la rimozione dei commenti dai fogli di lavoro. I commenti sono utili per aggiungere note o informazioni utili per gli utenti che lavoreranno sul foglio. Gli sviluppatori hanno la flessibilità di aggiungere commenti a qualsiasi cella del foglio di lavoro.

{{% /alert %}} 
## **Lavorare con i commenti**
### **Aggiunta di commenti**
Per aggiungere un commento al foglio di lavoro, seguire i passaggi seguenti:

1. Aggiungi il controllo Aspose.Cells.GridWeb al modulo Web.
1. Accedi al foglio di lavoro a cui si stanno aggiungendo commenti.
1. Aggiungi un commento a una cella.
1. Imposta una nota per il nuovo commento.

**Un commento è stato aggiunto al foglio di lavoro** 

![todo:image_alt_text](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Accesso ai commenti**
Per accedere a un commento:

1. Accedere alla cella che contiene il commento.
1. Ottenere il riferimento della cella.
1. Passare il riferimento alla raccolta Comment per accedere al commento.
1. Ora è possibile modificare le proprietà del commento.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Rimozione dei commenti**
Per rimuovere un commento:

1. Accedere alla cella come spiegato sopra.
1. Utilizzare il metodo RemoveAt della raccolta Comment per rimuovere il commento.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
