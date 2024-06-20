---
title: Implementazione della funzionalità di binding dei dati GridDesktop nei fogli di lavoro
type: docs
weight: 10
url: /it/net/aspose-cells-griddesktop/implementing-data-binding-feature-in-worksheets/
keywords: GridDesktop, binding dei dati, dati, bind
description: Questo articolo introduce come fare il binding dei dati in GridDesktop.
---

{{% alert color="primary" %}} 

Il binding dei dati è una funzionalità eccitante offerta dal framework Microsoft .NET. Sappiamo che il controllo DataGrid offerto da Microsoft supporta il binding dei dati, il che significa che un DataGrid può essere collegato a qualsiasi origine dei dati (utilizzando oggetti DataSet, DataTable e DataView). Questa funzionalità ha reso la vita degli sviluppatori molto più semplice. Sulla base dello stesso concetto, Aspose.Cells.GridDesktop supporta anche il binding dei dati, che consente agli sviluppatori di collegare i fogli di lavoro a qualsiasi origine dati. Questo articolo esplora la funzionalità.

{{% /alert %}} 
## **Creazione di un database di esempio**
1. Creare un database di esempio da utilizzare nell'esempio. Abbiamo utilizzato Microsoft Access per creare un database di esempio con una tabella Prodotti (schema di seguito). 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Sono stati aggiunti tre record falsi alla tabella Prodotti.
   **Record nella tabella Prodotti** 

![todo:image_alt_text](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Creare un'applicazione di esempio**
Ora creare un'applicazione desktop semplice in Visual Studio e fare quanto segue.

1. Trascina il controllo "GridControl" dalla casella degli strumenti e rilascialo sul modulo.
1. Trascina quattro pulsanti dalla casella degli strumenti in fondo al modulo e imposta la loro proprietà di testo rispettivamente come **Collega foglio di lavoro**, **Aggiungi riga**, **Elimina riga** e **Aggiorna al Database**.
## **Aggiunta di Namespace e Dichiarazione di Variabili Globali**
Poiché questo esempio utilizza un database Microsoft Access, aggiungi il namespace System.Data.OleDb nella parte superiore del codice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


Ora puoi utilizzare le classi contenute in questo namespace.

1. Dichiarare le variabili globali.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Riempimento DataSet con Dati dal Database**
Ora connettiti al database di esempio per recuperare e riempire i dati in un oggetto DataSet.

1. Utilizzare l'oggetto OleDbDataAdapter per connettersi al nostro database di esempio e riempire un DataSet con i dati recuperati dalla tabella Prodotti nel database, come mostrato nel codice sottostante.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Collegamento foglio di lavoro con DataSet**
Collega il foglio di lavoro con la tabella Prodotti del DataSet:

1. Accedi a un foglio di lavoro desiderato.
1. Collega il foglio di lavoro con la tabella Prodotti del DataSet.

Aggiungi il seguente codice all'evento di clic del pulsante **Collega foglio di lavoro**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Impostazione Intestazioni Colonne del Foglio di Lavoro**
Ora il foglio di lavoro vincolato carica con successo i dati, ma gli header delle colonne sono etichettati di default come A, B e C. Sarebbe meglio impostare gli header delle colonne con i nomi delle colonne nella tabella del database.

Per impostare gli header delle colonne del foglio di lavoro:

1. Ottenere le didascalie per ogni colonna del DataTable (Prodotti) nel DataSet.
1. Assegnare le didascalie agli header delle colonne del foglio di lavoro.

Aggiungere il codice scritto nell'evento di clic del pulsante **Vincola foglio di lavoro** con il seguente snippet di codice. In questo modo, gli header delle colonne precedenti (A, B e C) saranno sostituiti con ProductID, ProductName e ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Personalizzazione della larghezza e dello stile delle colonne**
Per migliorare ulteriormente l'aspetto del foglio di lavoro, è possibile impostare la larghezza e lo stile delle colonne. Ad esempio, a volte, l'header della colonna o il valore all'interno della colonna consiste in un lungo numero di caratteri che non si adattano dentro la cella. Per risolvere tali problemi, Aspose.Cells.GridDesktop supporta la modifica delle larghezze delle colonne.

Aggiungere il seguente codice al pulsante **Vincola foglio di lavoro**. Le larghezze delle colonne verranno personalizzate in base alle nuove impostazioni.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


Aspose.Cells.GridDesktop supporta anche l'applicazione di stili personalizzati alle colonne. Il seguente codice, aggiunto al pulsante **Vincola foglio di lavoro**, personalizza gli stili delle colonne per renderli più presentabili.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


Ora eseguire l'applicazione e fare clic sul pulsante **Vincola foglio di lavoro**.
## **Aggiunta di righe**
Per aggiungere nuove righe a un foglio di lavoro, utilizzare il metodo AddRow della classe Worksheet. Questo aggiunge una riga vuota in basso e viene aggiunta una nuova DataRow al data source (qui, viene aggiunta una nuova DataRow alla DataTable del DataSet). Gli sviluppatori possono aggiungere quante righe desiderano chiamando di nuovo il metodo AddRow. Quando una riga è stata aggiunta, gli utenti possono inserire valori al suo interno.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Eliminazione delle righe**
Aspose.Cells.GridDesktop supporta anche l'eliminazione delle righe chiamando il metodo RemoveRow della classe Worksheet. Rimuovere una riga utilizzando Aspose.Cells.GridDesktop richiede l'indice della riga da eliminare.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


Aggiungere il codice sopra al pulsante **Elimina riga** e eseguire l'applicazione. Alcuni record vengono visualizzati prima che la riga venga rimossa. Selezionando una riga e facendo clic sul pulsante **Elimina riga** verrà rimossa la riga selezionata.
## **Salvataggio delle modifiche nel database**
Infine, per salvare qualsiasi modifica apportata dagli utenti al foglio di lavoro nel database, utilizzare il metodo Update dell'oggetto OleDbDataAdapter. Il metodo Update prende il data source (DataSet, DataTable ecc.) del foglio di lavoro per aggiornare il database.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1. Aggiungere il codice sopra al pulsante **Aggiorna al database**.
1. Eseguire l'applicazione.
1. Eseguire alcune operazioni sui dati del foglio di lavoro, magari aggiungendo nuove righe e modificando o rimuovendo dati esistenti.
1. Quindi fare clic su **Aggiorna al Database** per salvare le modifiche nel database.
1. Controllare il database per verificare che i record della tabella siano stati aggiornati di conseguenza.
