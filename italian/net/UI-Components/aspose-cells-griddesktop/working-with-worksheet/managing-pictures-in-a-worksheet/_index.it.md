---
title: Gestione delle immagini in un foglio di lavoro
type: docs
weight: 100
url: /it/net/managing-pictures-in-a-worksheet/
---
{{% alert color="primary" %}} 

La maggior parte delle persone crede che un'immagine possa spiegare le cose meglio delle parole. Ecco perché Aspose.Cells.GridDesktop supporta l'aggiunta di immagini ai fogli di lavoro per eseguire questa convinzione delle persone. In questo argomento, discuteremo dell'aggiunta e della manipolazione di immagini nei fogli di lavoro.

{{% /alert %}} 
## **Aggiunta di immagini**
Per aggiungere un collegamento ipertestuale a una cella utilizzando Aspose.Cells.GridDesktop, procedi nel seguente modo:

-  Aggiungi il controllo Aspose.Cells.GridDesktop al tuo**Modulo**
-  Accedi a qualsiasi desiderato**Foglio di lavoro**
-  Aggiungere**Immagine** al foglio di lavoro specificando il percorso del file dell'immagine e il nome della cella in cui verrà inserita l'immagine

**Immagini** raccolta nel**Foglio di lavoro** L'oggetto fornisce un overload**Aggiungere** metodo. Gli sviluppatori possono utilizzare qualsiasi versione sovraccaricata di**Aggiungere** metodo in base alle loro specifiche esigenze. Utilizzando queste versioni sovraccaricate di**Aggiungere** metodo, è possibile aggiungere un'immagine da file, stream o**Immagine** oggetto.

Di seguito è riportato il codice di esempio per l'aggiunta di immagini nei fogli di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AddingPictures.cs" >}}
## **Accesso alle immagini**
 Per accedere e modificare un'immagine esistente nel foglio di lavoro, gli sviluppatori possono accedere all'immagine dal file**Immagini** raccolta del**Foglio di lavoro** specificando la cella (utilizzando il nome della cella o la sua posizione in termini di numero di riga e colonna) in cui è inserita l'immagine. Una volta effettuato l'accesso all'immagine, gli sviluppatori possono modificarne l'immagine in fase di esecuzione.

Di seguito è riportato il codice di esempio per accedere e modificare le immagini in un foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-AccessAndModifyPicture.cs" >}}
## **Rimozione di immagini**
 Per rimuovere un'immagine esistente, gli sviluppatori possono semplicemente accedere a un foglio di lavoro desiderato e quindi**Rimuovere** immagine dal**Immagini** raccolta del**Foglio di lavoro** specificando la cella (usandone il nome o il numero di riga e colonna) che contiene l'immagine.

Nel codice sottostante viene mostrato come rimuovere le immagini dal foglio di lavoro.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-ManagingPictures-RemovePicture.cs" >}}
