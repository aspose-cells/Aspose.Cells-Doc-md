---
title: Implementazione della funzionalità di associazione dati GridDesktop nei fogli di lavoro
type: docs
weight: 10
url: /it/net/implementing-griddesktops-data-binding-feature-in-worksheets/
---
{{% alert color="primary" %}} 

Il Data Binding è un'entusiasmante funzionalità offerta dal Framework Microsoft .NET. Sappiamo che il controllo DataGrid offerto da Microsoft supporta il data binding, il che significa che un DataGrid può essere associato a qualsiasi origine dati (utilizzando oggetti DataSet, DataTable e DataView). Questa funzione ha reso la vita degli sviluppatori molto più semplice. Sulla base dello stesso concetto, Aspose.Cells.GridDesktop supporta anche l'associazione dati, che consente agli sviluppatori di associare fogli di lavoro a qualsiasi origine dati. Questo articolo esplora la funzionalità.

{{% /alert %}} 
## **Creazione di un database di esempio**
1.  Creare un database di esempio da utilizzare con l'esempio. Abbiamo usato Microsoft Access per creare un database di esempio con una tabella Prodotti (schema sotto).

![cose da fare:immagine_alt_testo](implementing-griddesktops-data-binding-feature-in-worksheets_1.png)

1. Tre record fittizi vengono aggiunti alla tabella Prodotti.
   **Record nella tabella Prodotti** 

![cose da fare:immagine_alt_testo](implementing-griddesktops-data-binding-feature-in-worksheets_2.png)
## **Crea un'applicazione di esempio**
Ora crea una semplice applicazione desktop in Visual Studio e procedi come segue.

1. Trascina il controllo "GridControl" dalla casella degli strumenti e rilascialo sul modulo.
1. Rilascia quattro pulsanti dalla casella degli strumenti nella parte inferiore del modulo e imposta la loro proprietà di testo come**Rilega foglio di lavoro**, **Aggiungi riga**, **Elimina riga** e**Aggiorna al database** rispettivamente.
## **Aggiunta di namespace e dichiarazione di variabili globali**
Poiché questo esempio usa un database Access Microsoft, aggiungi lo spazio dei nomi System.Data.OleDb all'inizio del codice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingNamespaceToTheTop.cs" >}}


È ora possibile utilizzare le classi contenute in questo spazio dei nomi.

1. Dichiarare variabili globali.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeclareGlobalVariable.cs" >}}
## **Riempimento di DataSet con dati dal database**
Ora connettiti al database di esempio per recuperare e inserire i dati in un oggetto DataSet.

1. Utilizza l'oggetto OleDbDataAdapter per connetterti al nostro database di esempio e riempi un DataSet con i dati recuperati dalla tabella Products nel database, come mostrato nel codice seguente.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-FillDataSet.cs" >}}
## **Foglio di lavoro vincolante con DataSet**
Associa il foglio di lavoro alla tabella Prodotti del DataSet:

1. Accedi a un foglio di lavoro desiderato.
1. Associare il foglio di lavoro alla tabella Products del DataSet.

 Aggiungere il seguente codice al file**Associa foglio di lavoro** evento clic del pulsante.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-BindWorksheet.cs" >}}
## **Impostazione delle intestazioni di colonna del foglio di lavoro**
Il foglio di lavoro associato ora carica i dati correttamente, ma le intestazioni di colonna sono etichettate come A, B e C per impostazione predefinita. Sarebbe meglio impostare le intestazioni di colonna sui nomi delle colonne nella tabella del database.

Per impostare le intestazioni di colonna del foglio di lavoro:

1. Ottenere le didascalie per ogni colonna della DataTable (prodotti) nel DataSet.
1. Assegna le didascalie alle intestazioni delle colonne del foglio di lavoro.

 Aggiungi il codice scritto nel file**Associa foglio di lavoro** evento clic del pulsante con il seguente frammento di codice. In questo modo le vecchie intestazioni di colonna (A, B e C) verranno sostituite con ProductID, ProductName e ProductPrice.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SettingColumnHeader.cs" >}}
## **Personalizzazione della larghezza e degli stili delle colonne**
Per migliorare ulteriormente l'aspetto del foglio di lavoro, è possibile impostare la larghezza e gli stili delle colonne. Ad esempio, a volte, l'intestazione della colonna o il valore all'interno della colonna è costituito da un lungo numero di caratteri che non rientrano nella cella. Per risolvere tali problemi, Aspose.Cells.GridDesktop supporta la modifica della larghezza delle colonne.

 Aggiungere il seguente codice al file**Associa foglio di lavoro** pulsante. Le larghezze delle colonne verranno personalizzate in base alle nuove impostazioni.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-CustomizingStyle.cs" >}}


 Aspose.Cells.GridDesktop supporta anche l'applicazione di stili personalizzati alle colonne. Il seguente codice, aggiunto al**Associa foglio di lavoro** pulsante, personalizza gli stili delle colonne per renderle più presentabili.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-ApplyCustomStyle.cs" >}}


 Ora esegui l'applicazione e fai clic su**Associa foglio di lavoro** Pulsante.
## **Aggiunta di righe**
Per aggiungere nuove righe a un foglio di lavoro, utilizzare il metodo AddRow della classe Worksheet. Ciò aggiunge una riga vuota nella parte inferiore e un nuovo DataRow viene aggiunto all'origine dati (qui, un nuovo DataRow viene aggiunto alla DataTable del DataSet). Gli sviluppatori possono aggiungere tutte le righe che desiderano chiamando ripetutamente il metodo AddRow. Quando una riga è stata aggiunta, gli utenti possono inserirvi dei valori.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-AddingRows.cs" >}}
## **Eliminazione di righe**
Aspose.Cells.GridDesktop supporta anche l'eliminazione di righe chiamando il metodo RemoveRow della classe Worksheet. La rimozione di una riga utilizzando Aspose.Cells.GridDesktop richiede l'eliminazione dell'indice della riga.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-DeletingRows.cs" >}}


 Aggiungendo il codice sopra al file**Elimina riga** pulsante ed eseguire l'applicazione. Alcuni record vengono visualizzati prima che la riga venga rimossa. Selezionando una riga e facendo clic su**Elimina riga** pulsante rimuove la riga selezionata.
## **Salvataggio delle modifiche al database**
Infine, per salvare nel database eventuali modifiche apportate dagli utenti al foglio di lavoro, utilizzare il metodo Update dell'oggetto OleDbDataAdapter. Il metodo Update accetta l'origine dati (DataSet, DataTable e così via) del foglio di lavoro per aggiornare il database.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-DataBindingFeature-SavingChangesToDatabase.cs" >}}




1.  Aggiungi il codice sopra al file**Aggiorna al database** pulsante.
1. Eseguire l'applicazione.
1. Esegui alcune operazioni sui dati del foglio di lavoro, magari aggiungendo nuove righe e modificando o rimuovendo dati esistenti.
1.  Quindi fare clic**Aggiorna al database** per salvare le modifiche al database.
1. Controllare il database per verificare che i record della tabella siano stati aggiornati di conseguenza.
