---
title: Aspose.Cells for Java 8.8.3 Note di rilascio
type: docs
weight: 80
url: /it/java/aspose-cells-for-java-8-8-3-release-notes/
---
## **1) Aspose.Cells**

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-41866|Come impostare le proprietà della voce della legenda per le opzioni di testo|Nuova caratteristica|
|CELLSJAVA-41865|Crea una casella di testo in cui ogni riga ha un diverso allineamento orizzontale|Nuova caratteristica|
|CELLSJAVA-41873|La conversione in HTML rende le righe vuote ridondanti|Insetto|
|CELLSJAVA-41869|L'allineamento del testo viene modificato dopo aver salvato nuovamente un file XLS modello|Insetto|
|CELLSJAVA-41854|File Excel con DataBars non convertito correttamente in HTML|Insetto|
|CELLSJAVA-41851|Il grafico pivot creato con Aspose.Cells non viene visualizzato in Excel 2016 per MAC|Insetto|
|CELLSJAVA-41840|Aspose.Cells aggiunge null alla fine del percorso per le risorse HTML|Insetto|
|CELLSJAVA-41878|Le API LightCells generano eventi solo per la prima colonna della riga|Insetto|
|CELLSJAVA-41859|I bordi Cell vengono visualizzati dopo aver salvato nuovamente XLS|Insetto|
|CELLSJAVA-41888|L'immagine del logo viene persa durante la conversione di XLS in PDF|Insetto|
|CELLSJAVA-41874|La posizione del carattere è diversa nel PDF renderizzato rispetto a un file XLS|Insetto|
|CELLSJAVA-41852|Sovrapposizione di testo quando i fogli di lavoro vengono convertiti in EMF su Linux|Insetto|
|CELLSJAVA-41823|La densità del testo e le interruzioni di riga sono diverse rispetto al PDF generato da Excel|Insetto|
|CELLSJAVA-41822|Il testo viene tagliato e sovrapposto durante il rendering del foglio di calcolo in PDF|Insetto|
|CELLSJAVA-41856|Problemi nel rendering del grafico in PDF|Insetto|
|CELLSJAVA-41855|L'apertura e il salvataggio del file Excel modifica le linee di tendenza|Insetto|
|CELLSJAVA-41890|La cartella di lavoro salva due volte, il contenuto salvato la seconda volta sarà diverso dalla prima volta|Insetto|
|CELLSJAVA-41884|Problema con PageBreaks che non vengono ordinati prima del salvataggio nel file Excel|Insetto|
|CELLSJAVA-41876|File danneggiato se aperto, salvato, riaperto e salvato dalle API Aspose.Cells|Insetto|
|CELLSJAVA-41867|I valori degli assi del grafico sono stati modificati dopo aver salvato nuovamente un file XLS|Insetto|
|CELLSJAVA-41861|NullReferenceException durante il caricamento di un file XLS di Excel|Insetto|
|CELLSJAVA-41298|Impossibile ottenere informazioni accurate sulla formattazione delle forme WordArt dalle API Aspose.Cells|Insetto|
|CELLSJAVA-40366|Icona incorporata - non stampa|Insetto|
|CELLSJAVA-41883|CellsException: tipo di funzione del componente aggiuntivo sconosciuto: 9, in Workbook.calculateFormula|Eccezione|
|CELLSJAVA-41858|CellsException: Errore nel calcolo di Cell[0BMW CAN Bus Codes V0.4!R4], in Workbook.calculateFormula|Eccezione|
|CELLSJAVA-41870|java.lang.ArrayIndexOutOfBoundsException: 4 in Workbook.save durante il nuovo salvataggio di XLS|Eccezione|
|CELLSJAVA-41864|Eccezione: java.lang.IllegalStateException: codifica non valida: null al nuovo salvataggio di un file XLS|Eccezione|
## **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. il forum di supporto Aspose.Cells.
### **Aggiunge il metodo Cell.GetCharacters(flag).**
Restituisce tutti gli oggetti Characters.
### **Aggiunge la proprietà OleObject.AutoLoad**
Specifica se l'applicazione host per l'oggetto incorporato deve essere chiamata per caricare automaticamente i dati dell'oggetto all'apertura della cartella di lavoro padre.
### **Aggiunge la proprietà HTMLLoadOptions.SupportDivTag**
 Indica se supportare il layout di<div> tag quando il file html contiene<div> tags.Il valore predefinito è false.
### **Aggiunge la proprietà HtmlSaveOptions.ExportGridLines**
Indicare se esportare le linee della griglia. Il valore predefinito è falso.
### **Aggiunge la proprietà ShapeTextAlignment.TextShapeType**
Specifica la geometria preimpostata che verrà utilizzata per deformare la forma su una parte di testo.
### **Aggiunge il metodo LoadOptions.SetPaperSize(PaperSizeType).**
Imposta il formato carta di stampa predefinito dall'impostazione predefinita della stampante.
### **Elimina il metodo Workbook.Decrypt() obsoleto**
Impostare WorkbookSettings.Password come null.
### **Aggiunge la proprietà ListObject.Comment**
Ottiene e imposta il commento della tabella.
### **Aggiunge il metodo ShapeCollection.AddActiveXControl()**
Aggiunge il controllo ActiveX.

{{% alert color="primary" %}} 

Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.8.3 sono inclusi anche in questo Aspose.Cells for Java v8.8.3.

{{% /alert %}}
