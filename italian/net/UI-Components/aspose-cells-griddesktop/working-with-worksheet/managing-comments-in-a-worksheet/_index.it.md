---
title: Gestione dei commenti in un foglio di lavoro
type: docs
weight: 110
url: /it/net/managing-comments-in-a-worksheet/
---
{{% alert color="primary" %}} 

In MS Excel, è necessario conoscere la funzione dei commenti che consente agli utenti di aggiungere commenti alle celle. Questa funzione è utile nei casi in cui è necessario fornire alcune informazioni agli utenti quando stanno per inserire valori nelle celle. Ogni volta che un utente posiziona il cursore del mouse su una cella commentata, viene visualizzato un piccolo messaggio popup per fornire alcune informazioni all'utente. Utilizzando Aspose.Cells.GridDesktop, gli sviluppatori possono creare commenti sulle celle. In questo argomento, spiegheremo in dettaglio l'utilizzo di questa funzione.

{{% /alert %}} 
## **Aggiunta di commenti**
Per aggiungere un commento a una cella utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungere**Commento** al foglio di lavoro specificando la cella (utilizzando il nome o il numero di riga e colonna) in cui verrà aggiunto il commento.

 Il codice seguente aggiungerà commenti al file**b2** e**b4** celle del foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AddingComments.cs" >}}


**Commenti** raccolta nel**Foglio di lavoro** L'oggetto fornisce un overload**Aggiungere** metodo. Gli sviluppatori possono utilizzare qualsiasi versione sovraccaricata di**Aggiungere** metodo in base alle loro specifiche esigenze.
## **Accesso ai commenti**
Per accedere e modificare un commento esistente nel foglio di lavoro, gli sviluppatori possono accedere al commento dal file**Commenti** raccolta del**Foglio di lavoro** specificando la cella (utilizzando il nome della cella o la sua posizione in termini di numero di riga e colonna) in cui è inserito il commento. Una volta effettuato l'accesso al commento, gli sviluppatori possono modificarne il testo in fase di esecuzione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-AccessingComments.cs" >}}
## **Rimozione di commenti**
 Per rimuovere un commento esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi**Rimuovere** commento dal**Commenti** raccolta del**Foglio di lavoro** specificando la cella (utilizzando il nome o il numero di riga e colonna) contenente il commento.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingComments-RemovingComments.cs" >}}
