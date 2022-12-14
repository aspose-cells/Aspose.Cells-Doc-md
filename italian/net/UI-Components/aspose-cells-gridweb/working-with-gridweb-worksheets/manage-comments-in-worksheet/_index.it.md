---
title: Gestisci i commenti nel foglio di lavoro
type: docs
weight: 110
url: /it/net/manage-comments-in-worksheet/
---
{{% alert color="primary" %}} 

Questo argomento illustra l'aggiunta, l'accesso e la rimozione di commenti dai fogli di lavoro. I commenti sono utili per aggiungere note o informazioni utili per gli utenti che lavoreranno con il foglio. Gli sviluppatori hanno la flessibilità di aggiungere commenti a qualsiasi cella del foglio di lavoro.

{{% /alert %}} 
## **Lavorare con i commenti**
### **Aggiunta di commenti**
Per aggiungere un commento al foglio di lavoro, procedi nel seguente modo:

1. Aggiungere il controllo Aspose.Cells.GridWeb al Web Form.
1. Accedi al foglio di lavoro a cui stai aggiungendo commenti.
1. Aggiungi un commento a una cella.
1. Imposta una nota per il nuovo commento.

**È stato aggiunto un commento al foglio di lavoro** 

![cose da fare:immagine_alt_testo](manage-comments-in-worksheet_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AddComments.cs" >}}
### **Accesso ai commenti**
Per accedere a un commento:

1. Accedi alla cella che contiene il commento.
1. Ottieni il riferimento della cella.
1. Passare il riferimento alla raccolta Comment per accedere al commento.
1. Ora è possibile modificare le proprietà del commento.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-AccessComments.cs" >}}
### **Rimozione di commenti**
Per rimuovere un commento:

1. Accedi alla cella come spiegato sopra.
1. Utilizzare il metodo RemoveAt della raccolta Comment per rimuovere il commento.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-ManageComments.aspx-RemoveComments.cs" >}}
