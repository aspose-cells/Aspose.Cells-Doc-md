---
title: Aspose.Cells for Java 16.12.0 Note di rilascio
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-16-12-0-release-notes/
---
|**Chiave** |**Sommario** |**Categoria** |
|:- |:- |:- |
|CELLSJAVA-42043 | Specificare le posizioni dei punti della carta| Nuova caratteristica|
|CELLSJAVA-42073 | XLSM viene danneggiato dopo l'operazione di nuovo salvataggio| Insetto|
|CELLSJAVA-42060 | La larghezza di DataBar non è corretta durante la conversione del foglio di calcolo in HTML| Insetto|
|CELLSJAVA-42016 | Orange Row non è inclusa nella SOMMA della tabella pivot| Insetto|
|CELLSJAVA-42006 | L'immagine è tagliata nell'output HTML| Insetto|
|CELLSJAVA-42067 | Grafico mancante durante la conversione del foglio di calcolo in HTML| Insetto|
|CELLSJAVA-41983 | L'altezza della riga non è corretta durante la conversione da XLSX a HTML| Insetto|
|CELLSJAVA-42089 | La formula DCOUNTA Excel non viene valutata correttamente dal motore di calcolo della formula Aspose.Cells| Insetto|
|CELLSJAVA-42081 | Problema con la formattazione condizionale di DataBar durante il salvataggio di un file XLSM come PDF| Insetto|
|CELLSJAVA-42100 |Lo spazio tra alcuni caratteri viene rimosso in alcuni punti del file di output PDF| Insetto|
|CELLSJAVA-42078 | Le etichette del grafico non vengono visualizzate/renderizzate allo stesso modo (come per il file Excel originale) nel file di output PDF| Insetto|
|CELLSJAVA-42077 | Problema con gli attributi dei caratteri di TextBox nell'output PDF| Insetto|
|CELLSJAVA-42064 | Il colore e le dimensioni del contenuto di TextBox vengono modificati durante la conversione del foglio di lavoro in EMF| Insetto|
|CELLSJAVA-42063 | Il colore e le dimensioni del contenuto di TextBox vengono modificati durante la conversione del foglio di calcolo in PDF| Insetto|
|CELLSJAVA-42059 | Le parole ebraiche non vengono visualizzate correttamente durante la conversione di un file Excel nel formato file PDF| Insetto|
|CELLSJAVA-42053 | Il contenuto in TextBox viene ritagliato durante il rendering del foglio di calcolo su PDF| Insetto|
|CELLSJAVA-42052 | Le linee freccia sono fuori posto durante il rendering del foglio di calcolo su PDF| Insetto|
|CELLSJAVA-42049 | Problema con l'immagine SVG del grafico nel file HTML sottoposto a rendering| Insetto|
|CELLSJAVA-42036 | La sostituzione dei caratteri non sembra avere effetto per la legenda del grafico durante l'utilizzo di Chart.toPdf()| Insetto|
|CELLSJAVA-42024 | Legenda sovrapposta al testo nel grafico PDF| Insetto|
|CELLSJAVA-42070 |Valori ShapeXPx e ShapeYPx di ChartPoint errati| Insetto|
|CELLSJAVA-42083 | Rendering incompleto della forma Rectangle durante la conversione da XLS a HTML| Insetto|
|CELLSJAVA-42104 | Il testo viene troncato durante la conversione del foglio di calcolo nel formato file PDF| Insetto|
|CELLSJAVA-42098 | Pagine aggiuntive vengono aggiunte perché alcune pagine non vengono visualizzate completamente in una pagina PDF| Insetto|
|CELLSJAVA-42097 | SheetRender - Indice di colonna non valido| Insetto|
|CELLSJAVA-42093 | L'estensione della tabella di Excel modifica i dati| Insetto|
|CELLSJAVA-42092 | L'apertura e il salvataggio del file durante l'utilizzo di SheetRender danneggia il file Excel di output| Insetto|
|CELLSJAVA-42085 | L'impostazione del testo della forma modifica lo stile del testo| Insetto|
|CELLSJAVA-42074 | Il testo di alcune celle come C2 e C3 non viene visualizzato in grassetto| Insetto|
|CELLSJAVA-42058 | Il metodo Worksheet.autoFitColumns non sembra avere effetto quando il carattere richiesto non è presente in Linux| Insetto|
|CELLSJAVA-42054 | Colore di sfondo imprevisto applicato alle caselle di testo durante il rendering del foglio di calcolo su PDF| Insetto|
|CELLSJAVA-42072 | java.lang.ArrayIndexOutOfBoundsException in Workbook.calculateFormula(false)| Eccezione|
|CELLSJAVA-42066 | CellsException su Workbook.save durante la conversione da XLS a PDF| Eccezione|
|CELLSJAVA-42101 |Eccezione formula non valida all'apertura del file Excel| Eccezione|
|CELLSJAVA-42080 | Eccezione al salvataggio della cartella di lavoro| Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge le proprietà BuiltInDocumentPropertyCollection.ScaleCrop e BuiltInDocumentPropertyCollection.LinksUpToDate**
Ottiene e imposta alcune proprietà predefinite del documento.
### **Elimina la proprietà DataLabels.Rotation obsoleta**
Usare invece la proprietà DataLabels.RotationAngle.
### **Elimina la proprietà Title.Rotation obsoleta**
Utilizzare invece la proprietà Title.RotationAngle.
### **Elimina la proprietà DataLabels.Background obsoleta**
Usare invece la proprietà DataLabels.BackgroundMode.
### **Elimina la proprietà DisplayUnitLabel.Rotation obsoleta**
Utilizzare invece la proprietà DisplayUnitLabel.RotationAngle.
### **Elimina il metodo Title.getCharacters() obsoleto**
Utilizzare invece il metodo Title.characters().
### **Aggiunge la classe LoadFilter e la proprietà LoadOptions.LoadFilter**
Consente all'utente di controllare quali dati devono essere caricati durante il caricamento di una cartella di lavoro dal file modello.
### **Proprietà LoadOptions.LoadDataFilterOptions obsoleta**
Utilizzare invece la proprietà LoadOptions.LoadFilter. Esempio: LoadOptions.LoadFilter = new LoadFilter(LoadDataFilterOptions.All & ~LoadDataFilterOptions.Chart);
### **Proprietà LoadOptions.OnlyLoadDocumentProperties obsoleta**
Utilizzare invece la proprietà LoadOptions.LoadFilter. Utilizzo: LoadOptions.LoadFilter = new LoadFilter(LoadDataFilterOptions.DocumentProperties);
### **Proprietà LoadOptions.LoadDataAndFormatting obsoleta**
Utilizzare invece la proprietà LoadOptions.LoadFilter. Utilizzo: LoadOptions.LoadFilter = new LoadFilter(LoadDataFilterOptions.CellData);
### **Proprietà LoadOptions.LoadDataOptions obsoleta**
Usa invece la proprietà LoadFilter, l'utente può estendere LoadFilter per filtrare il foglio di lavoro e i dati.
### **Aggiunge il metodo Workbook.ExportXml(string mapName, string path).**
Esporta dati XML.
### **Aggiunge enum FileFormatType.OTS**
Rappresenta il formato file OTS.
### **Aggiunge il metodo WorksheetCollection.CreateRange()**
Crea un intervallo.
### **Aggiunge la proprietà FontConfigs.PreferSystemFontSubstitutes**
Indicare se utilizzare prima i font sostitutivi di sistema o meno quando un font non è presentato e il sostituto di questo font non è impostato.
