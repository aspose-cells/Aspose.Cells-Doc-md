---
title: Aspose.Cells for .NET 19.7 Note di rilascio
type: docs
weight: 60
url: /it/net/aspose-cells-for-net-19-7-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 19.7](https://www.nuget.org/packages/Aspose.Cells/19.7.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42029|Supporto per l'aggiunta di una sorta di evento/meccanismo di richiamata che notifica l'avanzamento della conversione|Nuova caratteristica|
|CELLSNET-46791|Supporta più visualizzazioni ma non visualizzazione personalizzata|Nuova caratteristica|
|CELLSNET-46808|Supporta la lettura di singole celle della tabella del file XLS.|Nuova caratteristica|
|CELLSNET-46775|La larghezza della forma raggruppata non può essere impostata|Aumento|
|CELLSNET-46785|Il caso dell'abbreviazione è diverso per le stesse parole: HtmlSaveOptions e HTMLLoadOptions, JsonLayoutOptions e JSONUtility, ODSLoadOptions e OdsSaveOptions.|Aumento|
|CELLSNET-46811|Supporta i tag HeadingPairs e TitlesOfParts del file XLS.|Aumento|
|CELLSNET-46783|CalculateFormula è molto lento|Prestazione|
|CELLSNET-46746|CalculateFormula: le formule non influiscono sui grafici|Insetto|
|CELLSNET-46772|PDF errato creato mancando la grafica|Insetto|
|CELLSNET-46802|Grafico reso in modo diverso in XLS rispetto a PDF|Insetto|
|CELLSNET-46806|Il grafico combinato esegue il rendering in PDF in modo errato|Insetto|
|CELLSNET-41449|XLSB con file di tabelle pivot complessi|Insetto|
|CELLSNET-43921|Il rendering da XLSX a XLSB produce un file danneggiato|Insetto|
|CELLSNET-44593|Il file Excel di output non è buono durante la conversione da HTML a Excel|Insetto|
|CELLSNET-46794|Cells shift quando l'HTML viene convertito in XLSX|Insetto|
|CELLSNET-46809|I formati condizionali hanno oscurato tutte le celle nella colonna (colonne B, C e D)|Insetto|
|CELLSNET-46778|CalculateFormula() interrompe la rappresentazione UNICHAR()|Insetto|
|CELLSNET-46781|System.Globalization.CultureInfo.CurrentCulture è stato modificato|Insetto|
|CELLSNET-46244|GridDesktop Copia e incolla con gli errori di commento fuori|Insetto|
|CELLSNET-46774|Testo nelle righe distorto durante la conversione di un file di grandi dimensioni in PDF|Insetto|
|CELLSNET-46798|Problema con la conversione di Excel in PDF|Insetto|
|CELLSNET-46797|Lo stile del carattere sottolineato viene ignorato durante il rendering del foglio Excel in BMP/Tiff|Insetto|
|CELLSNET-46664|I tag HeadingPairs e TitlesOfParts vengono nuovamente ripristinati dopo la riconversione degli XLS ripuliti nel formato di file XLSM|Insetto|
|CELLSNET-46782|Smart Marker non aggiorna il riferimento alla formula tra fogli|Insetto|
|CELLSNET-46784|Indicatori intelligenti: problema con la visualizzazione di oggetti elenco JSON con proprietà|Insetto|
|CELLSNET-46800|Apri/Salva rimuove CheckBox.AlternativeText|Insetto|
|CELLSNET-46807|Parte del testo mancante durante la conversione di XLS in PDF|Insetto|
|CELLSNET-42168|IndexOutOfRangeException: in Workbook.SaveToStream|Eccezione|
|CELLSNET-46248|L'eccezione viene generata durante la lettura del file HTML.|Eccezione|
|CELLSNET-46792|Eccezione quando si tenta di eliminare colonne vuote in una cartella di lavoro specifica|Eccezione|
|CELLSNET-46799|Eccezione sollevata durante la conversione del file XLSX in PDF|Eccezione|
|CELLSNET-46803|Eccezione "Riferimento oggetto non impostato su un'istanza di un oggetto" durante il caricamento di un file XLSX|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Obsoleta la classe HTMLLoadOptions e aggiunta la classe HtmlLoadOptions**
Utilizzare invece la classe HtmlLoadOptions.
#### **Obsoleta la classe ODSLoadOptions e aggiunta la classe OdsLoadOptions**
Utilizzare invece la classe OdsLoadOptions.
#### **Rende obsoleta la classe JSONUtility e aggiunge la classe JsonUtility**
Usa invece la classe JsonUtility.
#### **Aggiorna lo spazio dei nomi Aspose.Cells.ODS come Aspose.Cells.Ods e aggiorna classi/enum/proprietà ODS* come Ods**
Usa invece classi/enum/proprietà aggiornate.
#### **Aggiunge l'interfaccia IPageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
#### **Aggiunge la classe PageSavingArgs**
Informazioni per un processo di salvataggio della pagina.
#### **Aggiunge la classe PageStartSavingArgs**
Le informazioni per una pagina avviano il processo di salvataggio.
#### **Aggiunge la classe PageEndSavingArgs**
Le informazioni per una pagina terminano il processo di salvataggio.
#### **Aggiunge la proprietà PdfSaveOptions.PageSavingCallback**
Controlla/Indica l'avanzamento del processo di salvataggio della pagina.
