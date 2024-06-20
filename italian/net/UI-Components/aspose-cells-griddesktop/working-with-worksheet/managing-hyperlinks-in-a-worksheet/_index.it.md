---
title: Gestione degli Ipercollegamenti in un Foglio di Lavoro
type: docs
weight: 90
url: /it/net/aspose-cells-griddesktop/manage-hyperlinks-in-a-worksheet/
keywords: GridDesktop,iper,collegamento,ipercollegamento,ipercollegamenti
description: Questo articolo introduce come lavorare con l iperlink in GridDesktop.
---

{{% alert color="primary" %}} 

Utilizzando Aspose.Cells.GridDesktop, è anche possibile aggiungere collegamenti ipertestuali a valori semplici memorizzati nelle celle di un foglio di lavoro. Supponiamo che in alcune celle tu abbia dei valori che vorresti collegare a informazioni più dettagliate su una pagina web. In tal caso, sarebbe auspicabile aggiungere un collegamento ipertestuale a quella cella in modo che se un utente fa clic sulla cella, verrà indirizzato a quella pagina web. In questo argomento, spiegheremo come gli sviluppatori possono aggiungere e manipolare collegamenti ipertestuali nei loro fogli di lavoro.

{{% /alert %}} 
## **Aggiunta di Collegamenti Ipotestuali**
Per aggiungere un collegamento ipertestuale a una cella utilizzando Aspose.Cells.GridDesktop, seguire i passaggi seguenti:

- Aggiungi il controllo Aspose.Cells.GridDesktop al tuo **Form**
- Accedere a qualsiasi **Foglio di lavoro** desiderato
- Accedere a una **Cella** desiderata nel foglio di lavoro che sarà collegata ipertestualmente
- Aggiungere un certo valore alla cella per cui si desidera il collegamento ipertestuale
- Aggiungere un **Collegamento ipertestuale** al foglio di lavoro specificando il nome della cella a cui verrà applicato il collegamento ipertestuale

La raccolta **Collegamenti ipertestuali** nell'oggetto **Foglio di lavoro** fornisce un metodo **Aggiungi** sovraccaricato. Gli sviluppatori possono utilizzare qualsiasi versione sovraccaricata del metodo **Aggiungi** in base alle loro esigenze specifiche.

Il codice seguente aggiungerà un collegamento ipertestuale alle celle **B2** e **C3** del foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AddHyperlink.cs" >}}
## **Accesso ai collegamenti ipertestuali**
Una volta che un collegamento ipertestuale sarà stato aggiunto a una cella, potrebbe essere necessario accedere e modificare il collegamento ipertestuale a tempo di esecuzione. Per farlo, gli sviluppatori possono semplicemente accedere al collegamento ipertestuale dalla raccolta **Collegamenti ipertestuali** del **Foglio di lavoro** specificando la cella (utilizzando il nome della cella o la sua posizione in termini di numero di riga e colonna) a cui è stato aggiunto il collegamento ipertestuale. Una volta che il collegamento ipertestuale è stato accesso, gli sviluppatori possono modificarne l'URL a tempo di esecuzione.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-AccessHyperlink.cs" >}}
## **Rimozione dei collegamenti ipertestuali**
Per rimuovere un collegamento ipertestuale esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi **Rimuovere** il collegamento ipertestuale dalla raccolta **Collegamenti ipertestuali** del **Foglio di lavoro** specificando la cella collegata ipertestualmente (utilizzando il suo nome o il numero di riga e colonna).



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingHyperlinks-RemoveHyperlink.cs" >}}

{{% alert color="primary" %}} 

Se vuoi aggiungere un collegamento ipertestuale a una cella e desideri visualizzare l'URL del collegamento ipertestuale nella cella invece di un certo valore, non aggiungere alcun valore alla cella e aggiungi semplicemente il collegamento ipertestuale a quella cella. Facendo così, la cella verrà collegata ipertestualmente e l'URL del collegamento ipertestuale verrà visualizzato anche nella cella come suo valore.

{{% /alert %}}
