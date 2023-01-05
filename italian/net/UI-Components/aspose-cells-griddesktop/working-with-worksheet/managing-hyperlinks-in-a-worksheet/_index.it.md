---
title: Gestione dei collegamenti ipertestuali in un foglio di lavoro
type: docs
weight: 90
url: /it/net/managing-hyperlinks-in-a-worksheet/
---
{{% alert color="primary" %}} 

Utilizzando Aspose.Cells.GridDesktop, è anche possibile aggiungere collegamenti ipertestuali a valori semplici memorizzati nelle celle di un foglio di lavoro. Diciamo che in alcune celle potresti avere alcuni valori che vorresti collegare a informazioni più dettagliate su una pagina web. In tal caso, sarebbe desiderabile aggiungere un collegamento ipertestuale a quella cella in modo che se un utente fa clic sulla cella, venga indirizzato a quella pagina web. In questo argomento, spiegheremo come gli sviluppatori possono aggiungere e manipolare i collegamenti ipertestuali nei loro fogli di lavoro.

{{% /alert %}} 
## **Aggiunta di collegamenti ipertestuali**
Per aggiungere un collegamento ipertestuale a una cella utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Accedi a un file desiderato**Cell** nel foglio di lavoro che verrà collegato tramite collegamento ipertestuale
- Aggiungi un valore alla cella da collegare tramite collegamento ipertestuale
-  Aggiungere**Collegamento ipertestuale** al foglio di lavoro specificando il nome della cella su cui verrà applicato il collegamento ipertestuale

**Collegamenti ipertestuali** raccolta nel**Foglio di lavoro** L'oggetto fornisce un overload**Aggiungere** metodo. Gli sviluppatori possono utilizzare qualsiasi versione sovraccaricata di**Aggiungere** metodo in base alle loro specifiche esigenze.

 Sotto il codice verrà aggiunto un collegamento ipertestuale a**B2** e**C3** celle del foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Accesso ai collegamenti ipertestuali**
Una volta aggiunto un collegamento ipertestuale a una cella, potrebbe anche essere necessario accedere e modificare il collegamento ipertestuale in fase di esecuzione. Per fare ciò, gli sviluppatori possono semplicemente accedere al collegamento ipertestuale dal file**Collegamenti ipertestuali** raccolta del**Foglio di lavoro** specificando la cella (utilizzando il nome della cella o la sua posizione in termini di numero di riga e colonna) a cui viene aggiunto il collegamento ipertestuale. Una volta effettuato l'accesso al collegamento ipertestuale, gli sviluppatori possono modificarne l'URL in fase di esecuzione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Rimozione di collegamenti ipertestuali**
 Per rimuovere un collegamento ipertestuale esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi**Rimuovere** collegamento ipertestuale da**Collegamenti ipertestuali** raccolta del**Foglio di lavoro** specificando la cella con collegamento ipertestuale (usando il suo nome o il numero di riga e colonna).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Se desideri aggiungere un collegamento ipertestuale a una cella e desideri visualizzare l'URL del collegamento ipertestuale nella cella anziché un valore, non aggiungere alcun valore alla cella e aggiungi semplicemente il collegamento ipertestuale a quella cella. In questo modo, la cella verrà collegata a un collegamento ipertestuale e anche l'URL del collegamento ipertestuale verrà visualizzato nella cella come relativo valore.

{{% /alert %}}
