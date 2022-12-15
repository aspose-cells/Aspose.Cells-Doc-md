---
title: Aspose.Cells for Java 16.11.0 Note di rilascio
type: docs
weight: 20
url: /it/java/aspose-cells-for-java-16-11-0-release-notes/
---
|**Chiave** |**Riepilogo** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-42042 | Supporta etichette subtotale/totale in altre lingue| Nuova caratteristica|
|CELLSJAVA-41994 | Il testo di Cell va in overflow nella cella successiva| Insetto|
|CELLSJAVA-42039 | CalculateFormula ha problemi a ricalcolare le celle con riferimento alle celle con formule| Insetto|
|CELLSJAVA-42050 | caratteri di controllo ebraici non vengono visualizzati correttamente nel PDF| Insetto|
|CELLSJAVA-42020 | La conversione da XLS a PDF richiede troppo tempo| Insetto|
|CELLSJAVA-42017 | Problema di layout durante la conversione del foglio di calcolo in PDF| Insetto|
|CELLSJAVA-42023 | Le etichette dell'asse X si sovrappongono alla legenda durante il rendering in PDF| Insetto|
|CELLSJAVA-42022 | L'immagine non si ridimensiona bene e il suo file SVG non è corretto| Insetto|
|CELLSJAVA-42003 | Rendering errato del grafico durante la conversione del foglio di calcolo in HTML| Insetto|
|CELLSJAVA-41986 | Gli spazi vengono omessi dal testo nell'output PNG di Chart| Insetto|
|CELLSJAVA-41438 | Selezione o stato di controllo non salvato durante il salvataggio in PDF| Insetto|
|CELLSJAVA-41339 |Il testo e l'allineamento del testo sono incasinati nel file (01_il_letame_attrezzo_baltico_20131215_ incl_logo.xlsx)| Insetto|
|CELLSJAVA-42056 | L'estensione dell'oggetto tabella/elenco di MS Excel modifica la formattazione delle celle| Insetto|
|CELLSJAVA-42055 | L'aggiunta di Arc a una nuova cartella di lavoro genera un foglio di calcolo potenzialmente non sicuro| Insetto|
|CELLSJAVA-42038 |Risoluzione della colonna della tabella interrotta se contenente '[' ]| Insetto|
|CELLSJAVA-42021 | Problema con l'estensione del contenuto dell'oggetto tabella/elenco di Excel relativo alle formule| Insetto|
|CELLSJAVA-42019 | Formula errata restituita da una cella del foglio di lavoro| Insetto|
|CELLSJAVA-42004 |java.lang.NullPointerException, in Workbook ctor durante il caricamento del file XLSX| Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà Workbook.AbsolutePath**
Ottiene e imposta il percorso assoluto del file. Utilizzato solo per collegamenti esterni.
#### **Aggiunge la classe GlobalizationSettings e la proprietà WorkbookSettings.GlobalizationSettings**
Ottiene e imposta le impostazioni di globalizzazione.
#### **Rimuove il metodo Cell.GetConditionalStyle() obsoleto**
Utilizzare invece il metodo Cell.GetConditionalFormattingResult().
#### **Rimuove il metodo obsoleto Cells.MaxDataRowInColumn(int column)**
Utilizzare invece il metodo Cells.GetLastDataRow(int).
#### **Rimuove la proprietà PageSetup.Draft obsoleta**
Usare invece la proprietà PageSetup.PrintDraft.
#### **Rimuove la proprietà AutoFilter.FilterColumnCollection obsoleta**
Utilizzare invece la proprietà AutoFilter.FilterColumns.
#### **Rende obsoleto il costruttore Style e aggiunge la classe CellsFactory**
Utilizzare invece il metodo CellsFactory.CreateStyle().
#### **Rimuove la proprietà TickLabels.Rotation obsoleta**
Utilizzare invece la proprietà TickLabels.RotationAngle.
#### **Aggiunge il metodo GridHyperlinkCollection.GetHyperlink(GridCell cell).**
Ottiene l'oggetto Hyperlink della cella. Se non è presente alcun collegamento ipertestuale della cella, restituisce null.
#### **Aggiunge il metodo GridHyperlinkCollection.GetHyperlink(int row,int column).**
Ottiene l'oggetto Hyperlink della cella. Se non è presente alcun collegamento ipertestuale della cella, restituisce null.
