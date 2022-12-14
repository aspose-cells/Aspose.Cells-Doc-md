---
title: Aspose.Cells for .NET 18.5 Note di rilascio
type: docs
weight: 80
url: /it/net/aspose-cells-for-net-18-5-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.5](https://www.nuget.org/packages/Aspose.Cells/18.5.1).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-46095|Implementa la funzione CEILING.PRECISE|Nuova caratteristica|
|CELLSNET-46023|Supporta il formato Strict Open XML Spreadsheet|Nuova caratteristica|
|CELLSNET-46080|Il colore dell'immagine dovrebbe essere nero durante la conversione in PDF|Aumento|
|CELLSNET-46087|Page Setup PrintErrorType non funziona nel rendering da Excel a PDF|Aumento|
|CELLSNET-46084|PageSetup.PrintDraft non ha effetto durante il salvataggio in PDF|Aumento|
|CELLSNET-46100|System.OutOfMemoryException durante la conversione di file Excel in PDF|Prestazione|
|CELLSNET-46033|Il campo della pagina denominato "Elemento assente Sì" viene perso durante l'aggiornamento|Insetto|
|CELLSNET-46096|Errore di calcolo quando si utilizza la catena di calcolo e il nome definito|Insetto|
|CELLSNET-46047|Alcune colonne scompaiono durante l'importazione di un file Excel in GridWeb|Insetto|
|CELLSNET-46110|La disposizione del testo non è corretta quando "Issue2 wrapping-no_costume_page_size.xlsx" viene convertito in PDF|Insetto|
|CELLSNET-46109|La disposizione del testo non è corretta quando "Issue2 wrapping.xlsx" viene convertito in PDF|Insetto|
|CELLSNET-46108|La disposizione del testo non è corretta quando "Issue3 wrapping.xlsx" viene convertito in PDF|Insetto|
|CELLSNET-46088|Il fattore di zoom Imposta pagina crea un numero errato di pagine nel PDF|Insetto|
|CELLSNET-46076|Eccezione durante il salvataggio di una cartella di lavoro in MemoryStream|Insetto|
|CELLSNET-46052|Alcune delle linee della griglia attorno ad alcune celle non vengono disegnate correttamente|Insetto|
|CELLSNET-46036|Il titolo del grafico è schiacciato dove i caratteri corrono tutti insieme nel rendering da Excel a PDF|Insetto|
|CELLSNET-46082|I colori della legenda del grafico a torta cambiano dopo il salvataggio in PDF e non corrispondono alle sezioni del grafico a torta|Insetto|
|CELLSNET-46104|Il salvataggio di XLSB in XLSM crea un file MS Excel corrotto|Insetto|
|CELLSNET-46098|Intervalli denominati persi durante la copia nella cartella di lavoro esistente|Insetto|
|CELLSNET-46077|Gli oggetti di disegno incorporati sono troppo stretti nel file di output quando si salva nuovamente un file XLSX|Insetto|
|CELLSNET-46068|Aspose.Cells restituisce un PDF vuoto quando si salva un file SpreadsheetML come PDF|Insetto|
|CELLSNET-46060|La perdita di dati si verifica durante la conversione di ODS nel formato di file XLSX|Insetto|
|CELLSNET-46057|L'intervallo denominato non si espande con il parametro "shift" dei marcatori intelligenti|Insetto|
|CELLSNET-46055|Utilizzando il parametro "shift" in Smart Markers, le righe generate non vengono visualizzate con lo stesso stile/formattazione|Insetto|
|CELLSNET-46048|La formattazione condizionale non funziona nei marcatori intelligenti con parametro di spostamento|Insetto|
|CELLSNET-42764|Testo ritagliato nelle celle di MS Excel se le righe del documento sono ridimensionate automaticamente|Insetto|
|CELLSNET-41678|Il ridimensionamento di un ListObject/Table non ne aggiorna le formattazioni condizionali|Insetto|
|CELLSNET-46059|Impossibile aprire il file XLS poiché genera un'eccezione durante il caricamento|Eccezione|
|CELLSNET-46097|Eccezione "Formula non valida:"'Nuovo' nome'!G11:G15"." durante l'aggiornamento dei dati del grafico pivot|Eccezione|
|CELLSNET-46075|Eccezione durante il rendering di un file Excel in PDF|Eccezione|
|CELLSNET-46101|NullReferenceExceptions all'apertura di file MS Excel su Mono Ubuntu Linux|Eccezione|
|CELLSNET-46085|Eccezione quando si utilizza il metodo ListObject.ConvertToRange|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge nuove proprietà Cell.IsTableFormula/IsArrayFormula per sostituire Cell.IsInTable/IsInArray**
Indica se una cella fa parte della formula della tabella o della formula di matrice. I vecchi nomi creano ambiguità, quindi li abbiamo resi obsoleti e ne abbiamo forniti di nuovi.
#### **Aggiunge la classe IndividualFontConfigs**
Rappresenta le configurazioni dei caratteri per ogni oggetto della cartella di lavoro.
#### **Aggiunge la proprietà LoadOptions.FontConfigs**
Ottiene e imposta le singole configurazioni dei caratteri.
#### **Elimina la proprietà FontSetting.ShapeFont obsoleta**
Usare invece la proprietà FontSetting.TextOptions.
#### **Aggiunge l'enumerazione OoxmlCompliance e la proprietà WorkbookSettings.Compliance**
Supporta il foglio di calcolo Strict Open Xml.
#### **Aggiunge il metodo GroupShape.Ungroup()**
Separa le forme.
#### **Aggiunge la proprietà MsoFormatPicture.Gamma**
Ottiene e imposta la gamma dell'immagine.
#### **Aggiunge le proprietà TextOptions.FarEastName e TextOptions.LatinName**
Ottiene e imposta l'Estremo Oriente e il nome latino del carattere.
