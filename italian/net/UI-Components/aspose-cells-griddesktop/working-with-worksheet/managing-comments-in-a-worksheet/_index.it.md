---
title: Gestione Commenti in un Foglio di Lavoro
type: docs
weight: 110
url: /it/net/aspose-cells-griddesktop/manage-comments-in-a-worksheet/
keywords: GridDesktop,commento,commenti
description: Questo articolo introduce come lavorare con i commenti in GridDesktop.
---

{{% alert color="primary" %}} 

In MS Excel, devi essere familiare con la funzionalità dei commenti che consente agli utenti di aggiungere commenti alle celle. Questa funzionalità è utile nei casi in cui è necessario fornire alcune informazioni agli utenti quando stanno per inserire valori nelle celle. Ogni volta che un utente posiziona il cursore del mouse su una cella commentata, compare un piccolo messaggio a comparsa per fornire alcune informazioni all'utente. Utilizzando Aspose.Cells.GridDesktop, gli sviluppatori possono creare commenti sulle celle. In questo argomento, spiegheremo dettagliatamente l'uso di questa funzionalità.

{{% /alert %}} 
## **Aggiunta di commenti**
Per aggiungere un commento a una cella utilizzando Aspose.Cells.GridDesktop, segui i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Aggiungi **Commento** al foglio di lavoro specificando la cella (utilizzando il suo nome o il numero di riga e colonna) in cui verrà aggiunto il commento.

Il codice seguente aggiungerà commenti alle celle **b2** e **b4** del foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


La collezione **Comments** nell'oggetto **Worksheet** fornisce un metodo **Add** sovraccaricato. Gli sviluppatori possono utilizzare qualsiasi versione sovraccaricata del metodo **Add** in base alle loro esigenze specifiche.
## **Accesso ai commenti**
Per accedere e modificare un commento esistente nel foglio di lavoro, gli sviluppatori possono accedere al commento dalla collezione **Comments** della classe **Worksheet** specificando la cella (utilizzando il nome della cella o la sua posizione in termini di numeri di riga e colonna) in cui è stato inserito il commento. Una volta che il commento è stato accesso, gli sviluppatori possono modificare il suo testo durante l'esecuzione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Rimozione dei commenti**
Per rimuovere un commento esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi **rimuovere** il commento dalla collezione **Comments** della classe **Worksheet** specificando la cella (utilizzando il suo nome o il numero di riga e colonna) contenente il commento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
