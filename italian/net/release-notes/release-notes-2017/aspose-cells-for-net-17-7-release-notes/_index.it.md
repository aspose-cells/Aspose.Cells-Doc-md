---
title: Aspose.Cells for .NET 17.7 Note di rilascio
type: docs
weight: 60
url: /it/net/aspose-cells-for-net-17-7-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 17.7](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-17.7/).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-45437|Supporta errori e valore booleano nella versione locale russa nel rendering da Excel a PDF|Nuova caratteristica|
|CELLSNET-45456|Leggere i dati, la formula e lo stile delle celle dal file dei numeri|Nuova caratteristica|
|CELLSNET-45483|Supporto per modificare il valore iniziale dell'indice di riga su 0 (invece di 1) in Aspose.Cells.GridDesktop|Nuova caratteristica|
|CELLSNET-45434|GridWeb ViewPanel non è sempre visibile|Nuova caratteristica|
|CELLSNET-45224|Rendering della tabella pivot in GridDesktop|Nuova caratteristica|
|CELLSNET-45490|Genera errore o eccezione quando viene assegnato un nome errato alla proprietà ListObject.DisplayName|Aumento|
|CELLSNET-45470|Link Source DataSource vs. OriginalDataSource vs. Excel=>Dati => Modifica collegamenti|Aumento|
|CELLSNET-45439|GridDesktop.GetVersion() necessario per verificare il numero di versione di GridDesktop in fase di esecuzione|Aumento|
|CELLSNET-45457|L'applicazione si blocca durante il tentativo di ottenere la proprietà dell'immagine|Prestazione|
|CELLSNET-45388|La forma della freccia non viene visualizzata correttamente nei rendering da foglio a immagine (.jpg).|Insetto|
|CELLSNET-45426|I dati del grafico non sono in grado di aggiornare i dati dalla tabella pivot|Insetto|
|CELLSNET-45447|File Excel danneggiato durante l'aggiunta di una tabella pivot dopo l'importazione dei dati di origine|Insetto|
|CELLSNET-45396|Errore di formattazione quando il file Excel viene convertito in HTML|Insetto|
|CELLSNET-45402|Cell.DisplayStringValue non corrisponde ai valori originali|Insetto|
|CELLSNET-45479|Aspose.Cells 17.5 - Errata firma digitale con certificato DSA|Insetto|
|CELLSNET-45420|L'impostazione DefaultFont non funziona|Insetto|
|CELLSNET-45364|Alcune forme/oggetti vengono tagliati nel PDF di output|Insetto|
|CELLSNET-45491|Nell'immagine di output del grafico sono apparse alcune sfocature nere associate alle etichette dei dati|Insetto|
|CELLSNET-45476|Il formato della data delle etichette dell'asse X viene modificato e sovrascritto nelle voci della legenda|Insetto|
|CELLSNET-45471|Il testo "III.LowerQualityAboveSML" nella seconda pagina del PDF è danneggiato|Insetto|
|CELLSNET-45454|I colori delle bolle vengono leggermente modificati per grafici diversi anche utilizzando le stesse righe di codice|Insetto|
|CELLSNET-45452|I grafici sparkline non vengono visualizzati correttamente nel PDF di output|Insetto|
|CELLSNET-45493|Il ridimensionamento di ListObject non comporta la formattazione personalizzata|Insetto|
|CELLSNET-45482|Alcune forme vengono perse nel file XLS durante l'estrazione e il reinserimento delle immagini|Insetto|
|CELLSNET-45466|Alcuni bordi aggiuntivi vengono aggiunti automaticamente|Insetto|
|CELLSNET-45464|Il tipo di asse del grafico viene modificato dopo Workbook.Combine()|Insetto|
|CELLSNET-45463|L'altezza delle righe e le dimensioni del grafico si riducono quando si utilizza il metodo Workbook.Combine()|Insetto|
|CELLSNET-45462|Quando il foglio di lavoro non dispone delle impostazioni di PageSetup, viene restituito un valore errato per la dimensione della carta|Insetti|
|CELLSNET-45453|Formattazione del foglio di lavoro modificata dopo Workbook.Combine()|Insetto|
|CELLSNET-45428|Cells.DeleteBlankRows/DeleteBlankColumns rimuove i grafici nel foglio di lavoro|Insetto|
|CELLSNET-45488|GridWeb non visualizza tutte le righe e rileva un errore|Insetto|
|CELLSNET-45438|La rotazione del testo della cella a 90 gradi rovina l'allineamento del testo della cella|Insetto|
|CELLSNET-45425|GridWeb aggiunge spazio alla voce del menu a discesa di Excel|Insetto|
|CELLSNET-42363|Problema con le didascalie dei campi pivot nella tabella pivot (GridWeb)|Insetto|
|CELLSNET-45486|NullReferenceException si è verificata durante il salvataggio della cartella di lavoro di Excel (con celle unite) nel formato di file HTML|Eccezione|
|CELLSNET-45478|Eccezione all'apertura di un file MHTML danneggiato tramite API Aspose.Cells|Eccezione|
|CELLSNET-45467|System.ArgumentOutOfRangeException' si è verificata durante il caricamento di un file MHTML|Eccezione|
|CELLSNET-45485|Si è verificata un'eccezione durante il calcolo di una formula valida|Eccezione|
|CELLSNET-45433|L'eccezione si verifica all'apertura di fd1507a97b7f40fb85f9725535ecd215.xlsb|Eccezione|
|CELLSNET-45432|L'eccezione si verifica all'apertura di 0c29bc12429844fe983c2a152fa9b744.xlsb|Eccezione|
|CELLSNET-45431|L'eccezione si verifica all'apertura di 000bc1ec5fda4528a18f267f4dfe4a98.xlsb|Eccezione|
|CELLSNET-45430|L'eccezione si verifica in caso di apertura non riuscita_a_salvato_in_xlsb_type.xlsx|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge i metodi GlobalizationSettings.GetBooleanValueString()/GetErrorValueString()**
Ottiene il valore della stringa di visualizzazione personalizzata per il valore booleano e di errore della cella durante la formattazione/il rendering.
#### **Rimuove il metodo ValidationCollection.Add() obsoleto**
Usare invece il metodo ValidationCollection.Add(CellArea).
#### **Aggiunge la proprietà PdfSaveOptions.CheckWorkbookDefaultFont**
Indica se provare a utilizzare prima il carattere predefinito della cartella di lavoro per mostrare i caratteri il cui carattere non è impostato correttamente.
#### **Aggiunge la proprietà ImageOrPrintOptions.CheckWorkbookDefaultFont**
Indica se provare a utilizzare prima il carattere predefinito della cartella di lavoro per mostrare i caratteri il cui carattere non è impostato correttamente.
#### **Aggiunge FileFormatType.Numbers, LoadFormat.Numbers e SaveFormat.Numbers enum**
Rappresenta il formato di file del foglio di calcolo Numbers di Apple Inc/.
#### **Aggiunge il metodo Worksheet.AdvancedFilter()**
Filtra i dati utilizzando criteri complessi.
#### **Aggiunge la proprietà WorkbookSettings.SignificantDigits**
Ottiene e imposta il numero di cifre significative.
#### **Rende obsoleta la proprietà Validation.AreaList e aggiunge la proprietà Validation.Areas**
Ottiene tutta l'area che contiene le impostazioni di convalida dei dati.
#### **Aggiunge la proprietà PageSetup.IsAutomaticPaperSize**
Indica se il formato carta è automatico.
#### **Aggiunge il metodo FontSettingCollection.Replace()**
Sostituisce il testo della forma.
#### **Aggiunge Cells.importResultSet(ResultSet rs, int rowIndex, int columnIndex, opzioni ImportTableOptions)/Cells.importResultSet(ResultSet rs, String startCell, opzioni ImportTableOptions) (solo for Java)**
Supporta l'importazione di ResultSet con più opzioni.
#### **Aggiunge la proprietà GridWorksheet.CustomColumnCaption**
Ottiene o imposta la didascalia di colonna personalizzata per il foglio di lavoro: Aspose.Cells.GridDesktop.
#### **Aggiunge la proprietà GridWorksheet.CustomRowCaption**
Ottiene o imposta la didascalia della riga personalizzata per il foglio di lavoro: Aspose.Cells.GridDesktop.
#### **Aggiunge il metodo GridDesktop.GetVersion()**
Ottieni la versione di rilascio.
#### **Aggiunge la funzione GridWebInstance.resize() nel client GridWeb js, (GridWebInstance è l'oggetto di controllo GridWeb)**
Rende il controllo GridWeb compatibile con le dimensioni correnti della finestra del browser.


#### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Leggi il foglio di calcolo dei numeri sviluppato da Apple Inc. utilizzando Aspose.Cells](/cells/it/net/read-numbers-spreadsheet-developed-by-apple-inc-using-aspose-cells/)
- [Impostare la proprietà DefaultFont di PdfSaveOptions e ImageOrPrintOptions in modo che abbia la priorità](/cells/it/net/set-defaultfont-property-of-pdfsaveoptions-and-imageorprintoptions-to-have-priority/)
- [Applica il filtro avanzato di Microsoft Excel per visualizzare i record che soddisfano i criteri complessi](/cells/it/net/apply-advanced-filter-of-microsoft-excel-to-display-records-meeting-complex-criteria/)
- [Implementa errori e valore booleano in russo o in qualsiasi altra lingua](/cells/it/net/implement-errors-and-boolean-value-in-russian-or-any-other-language/)
- [Determinare se il formato carta del foglio di lavoro è automatico](/cells/it/net/determine-if-paper-size-of-worksheet-is-automatic/)
- [Rendering della tabella pivot in GridDesktop](/cells/it/net/render-pivottable-in-griddesktop/)
- [Riga personalizzata e didascalia colonna personalizzata del foglio di lavoro GridDesktop](/cells/it/net/custom-row-and-custom-column-caption-of-griddesktop-worksheet/)
- [Trova la versione di GridDesktop in fase di esecuzione](/cells/it/net/find-griddesktop-version-at-runtime/)
- [Ridimensiona GridWeb nella finestra del browser](/cells/it/net/resize-gridweb-in-the-browser-window/)
