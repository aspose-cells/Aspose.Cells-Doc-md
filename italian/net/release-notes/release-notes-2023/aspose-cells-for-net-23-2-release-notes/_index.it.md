---
title: Aspose.Cells for .NET 23.2 Note di rilascio
type: docs
weight: 11
url: /it/net/aspose-cells-for-net-23-2-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 23.2](https://www.nuget.org/packages/Aspose.Cells/23.2.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
| :- | :- | :- |
|CELLSNET-52620|Supporto per analizzare/leggere/salvare le funzioni SCAN e Lambda|
|CELLSNET-52666|Supporta più formati di impaginazione durante la conversione di Excel in pptx|
|CELLSNET-52627|Estrai lo stile della cella in un oggetto generico (es. JSON)|
|CELLSNET-52683|Cell.La formula non è uguale a quella visualizzata in MS Excel|
|CELLSNET-52691|Le formule sono calcolate in modo errato|
|CELLSNET-52519|Problema con la lettura dei grafici dal file Excel (generato da Aspose.Cells) al grafico Microsoft API|
|CELLSNET-52544|Grafico a PDF non uguale all'immagine|
|CELLSNET-52635| Il testo nel grafico in SVG ha una posizione errata|
|CELLSNET-52585|Impossibile caricare il file xps generato da System.Windows.Xps.Packaging.XpsDocument|
|CELLSNET-52622|Impossibile generare SVG con apice e pedice dal file Excel|
|CELLSNET-52692|Il testo viene perso nel documento XPS convertito|
|CELLSNET-52438| Perdita di dati durante il salvataggio di un grafico a tabella pivot|
|CELLSNET-52555|Differenza nella posizione del carattere/testo durante il rendering del foglio di lavoro selezionato su HTML|
|CELLSNET-52583|La conversione in Docx produce una pagina vuota in più|
|CELLSNET-52612|Problema nell'aprire PowerQuery dopo la modifica|
|CELLSNET-52613|La conversione di Numbers in Pptx produce risultati non funzionanti|
|CELLSNET-52630|Conversione da HTML a Excel: le tabelle non vengono visualizzate correttamente|
|CELLSNET-52631| Il salvataggio di un file XLSX come XLSB danneggia i colori e aggiunge filtri|
|CELLSNET-52639|La rotazione del titolo dell'asse del grafico viene reimpostata dopo la copia con Aspose.Cells|
|CELLSNET-52662| L'importazione Xml perde le formule nelle colonne calcolate|
|CELLSNET-52671|XmlImport danneggia il file durante il tentativo di aggiornare le tabelle pivot con la colonna calcolata|
|CELLSNET-52675|Lo stile della cella perso dopo l'importazione di xml.|
|CELLSNET-52684|Formattazione del commento persa durante la copia di Intervallo|
|CELLSNET-52690|JsonLayoutOptions non funziona.|
|CELLSNET-52696|Le operazioni sulle tabelle generano file excel corrotti|
|CELLSNET-52549|Salva foglio in HTML con SmartArt genera System.NullReferenceException|

##  **Pubblico API e modifiche incompatibili con le versioni precedenti**

Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.

###  **Aggiunge la proprietà ChartTextFrame.IsAutomaticRotation**

Indica se il testo del grafico viene ruotato automaticamente.

###  **Proprietà JsonLayoutOptions.IgnoreObjectTitle e JsonLayoutOptions.IgnoreArrayTitle obsolete**

Utilizzare invece la proprietà JsonLayoutOptions.IgnoreTitle.

###  **Aggiunge la proprietà JsonLayoutOptions.IgnoreTitle**

Ingorisce i titoli degli attributi Json durante la conversione di JSON in Excel.

###  **Aggiunge il metodo Style.ToJson()**

Converte lo stile dei file Excel in file json

###  **Aggiunge il metodo Cell.ToJson()**

Converte una cella di celle in un file json.

