---
title: Aspose.Cells for .NET 19.2 Note di rilascio
type: docs
weight: 110
url: /it/net/aspose-cells-for-net-19-2-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.2](https://www.nuget.org/packages/Aspose.Cells/19.2.0).

{{% /alert %}} 

|**Chiave**|**Sommario**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46582|Supporta la proprietà Range.Hyperlinks|Nuova caratteristica|
|CELLSNET-46534|Int32 può essere piccolo per l'attributo Cells.count|Aumento|
|CELLSNET-46552|Differenziare XLSX crittografato da PPTX crittografato e DOCX crittografato|Aumento|
|CELLSNET-46568|Impostazione dello stile del grafico Box Whisker|Aumento|
|CELLSNET-46573|Sostituisci i caratteri non validi con simboli adatti come le parentesi|Aumento|
|CELLSNET-46581|Apri/salva rimuove il testo alternativo della tabella|Aumento|
|CELLSNET-46584|Problema di prestazioni con le API Aspose.Cells|Prestazione|
|CELLSNET-46556|Il testo di TextBox viene tagliato|Insetto|
|CELLSNET-46565|I pittogrammi non sono visibili nell'output PDF in Excel al rendering PDF|Insetto|
|CELLSNET-46477|La formattazione condizionale nella tabella pivot non funziona in un foglio copiato|Insetto|
|CELLSNET-46547|Contenuto mancante da HTML alla conversione di Excel|Insetto|
|CELLSNET-46566|XLSX file corrotto dopo il salvataggio con le API Aspose.Cells|Insetto|
|CELLSNET-46572|XLSB è danneggiato durante l'aggiunta di più di 1 campo dati mentre XLSX funziona correttamente|Insetto|
|CELLSNET-46548|Problema NumberValue durante la conversione del formato di file da XLSX a PDF|Insetto|
|CELLSNET-46557|Valore di cella errato calcolato dal motore di calcolo della formula Aspose.Cells|Insetto|
|CELLSNET-46578|Worksheet.AutoFitColumns() non si adatta completamente alle colonne|Insetto|
|CELLSNET-46550|Testo delle etichette incasinato durante la conversione del grafico MS Excel in immagini|Insetto|
|CELLSNET-46558|segni di graduazione del grafico vengono persi durante la lettura e il salvataggio di un file ODS|Insetto|
|CELLSNET-46560|Il nome della serie viene perso quando si salva un file ODS|Insetto|
|CELLSNET-46561|Il bordo predefinito dell'area del tracciato nel grafico non dovrebbe essere visibile per il file ODS|Insetto|
|CELLSNET-46562|Le linee della griglia dell'asse X vengono rimosse durante la lettura e il salvataggio del file XLSX|Insetto|
|CELLSNET-46569|Le impostazioni di Imposta pagina sono state modificate dopo il caricamento e il salvataggio del file MS Excel|Insetto|
|CELLSNET-46574|Problema con il salvataggio e l'apertura dei file XLSB|Insetto|
|CELLSNET-46555|Viene sollevata un'eccezione durante la modifica di alcune proprietà|Eccezione|
|CELLSNET-46571|Eccezione durante l'apertura del file di output (dopo aver salvato nuovamente il file modello) in MS Excel|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà Cells.CountLarge**
Dal punto di vista funzionale è uguale alla proprietà Count, ad eccezione del fatto che la proprietà Count può generare un errore di overflow quando sono presenti troppe istanze di oggetti Cell.
#### **Aggiunge il metodo Hyperlink.Delete()**
Elimina questo collegamento ipertestuale.
#### **Aggiunge la proprietà Range.Hyperlinks**
Ottiene tutti i collegamenti ipertestuali nell'intervallo.
#### **Aggiunge enum CopyFormatType**
Rappresenta il tipo di formato di copia durante l'inserimento delle righe.
#### **Aggiunge la classe InsertOptions e il metodo Cells.InsertRows(int, int , InsertOptions)**
Inserimento di righe con alcune opzioni.
#### **Aggiunge i metodi FileFormatUtil.DetectFileFormat(Stream,String) e FileFormatUtil.DetectFileFormat(String,String)**
Rileva il formato file del file OOXML crittografato.
#### **Aggiunge le proprietà ListObject.AlternativeDescription e ListObject.AlternativeText**
Ottiene e imposta il testo alternativo e la descrizione della tabella.
#### **Aggiunge la proprietà Line.ThemeColor**
Ottiene e imposta il colore del tema della linea.
#### **Aggiunge la classe Mode3d e MsoModel3dFormat**
Incapsula l'oggetto che rappresenta un singolo modello 3D in un foglio di calcolo.
#### **Aggiunge l'enumerazione ImageType.Gltf**
Rappresenta il tipo di modello 3D.
