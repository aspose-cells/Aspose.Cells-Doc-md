---
title: Aspose.Cells for Java Note sulla versione 17.12
type: docs
weight: 10
url: /it/java/aspose-cells-for-java-17-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for Java 17.12.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSJAVA-42479|Enumerazione LoadDataFilterOptions migliorata e rimozione dell'ambiguità|Aumento|
|CELLSJAVA-42460|Formato CSV: D2 e D6 sono IsString ma Aspose.Cells li tratta come IsNumeric|Aumento|
|CELLSJAVA-42457|Quando XLSX viene convertito in PDF, alcune linee nei grafici sono diverse|Insetto|
|CELLSJAVA-42465|Alcune dichiarazioni di classe CSS non hanno un prefisso nell'HTML di output|Insetto|
|CELLSJAVA-42456|Output HTML incoerente con l'origine - Conversione da Excel a HTML|Insetto|
|CELLSJAVA-42478|L'importazione di un valore lungo dal database HSQL genera un'eccezione|Insetto|
|CELLSJAVA-42466|L'equazione non viene visualizzata correttamente nel PDF di output|Insetto|
|CELLSJAVA-42475|Il grafico non è presente nel PDF di output|Insetto|
|CELLSJAVA-42459|Le etichette dati per il grafico non sono presenti nel PDF/immagine di output|Insetto|
|CELLSJAVA-42453|L'immagine del grafico non è uguale a Microsoft Excel|Insetto|
|CELLSJAVA-42447|Le etichette dati vengono visualizzate in modo errato nel formato del file HTML di output|Insetto|
|CELLSJAVA-42481|L'impostazione del nome della casella combinata non funziona per il file Excel di origine, ma se salvato nuovamente da Microsoft Excel funziona correttamente|Insetto|
|CELLSJAVA-42476|Microsoft Il foglio di lavoro con attivazione macro di Excel (.xlsm) viene danneggiato dopo l'apertura e il salvataggio tramite le API Aspose.Cells|Insetto|
|CELLSJAVA-42470|L'impostazione di una cella collegata alla casella di controllo fa sì che MS Excel richieda un messaggio di errore quando si apre il file di output in essa|Insetto|
|CELLSJAVA-42462|La lettura del file XLSB genera l'eccezione NullPointerException|Eccezione|
## **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
### **Aggiunge la proprietà HtmlSaveOptions.TableCssId**
Ottiene e imposta il prefisso del nome di tipo css come tr,col,td e così via, sono contenuti nell'elemento table che ha l'attributo specifico TableCssId. Il valore predefinito è "".
### **Aggiunge la proprietà Cell.FormulaLocal**
Ottiene la formula formattata locale che può variare in base alle diverse impostazioni locali per i separatori, i nomi incorporati, i nomi delle funzioni e così via. Quelle impostazioni locali dipendono.
### **Aggiunge il metodo GlobalizationSettings.GetLocalFunctionName(string standardName).**
Ottiene il nome della funzione dipendente dalle impostazioni locali in base al nome della funzione standard specificato.
### **Aggiunge il metodo GlobalizationSettings.GetLocalBuiltInName(string standardName).**
Ottiene il testo dipendente dalle impostazioni locali per il nome incorporato in base al testo standard specificato.
### **Aggiunge la proprietà GlobalizationSettings.ListSeparator**
Ottiene il separatore per elenco, parametri di funzione, ...ecc.
### **Aggiunge la proprietà GlobalizationSettings.RowSeparatorOfFormulaArray**
Ottiene il separatore per le righe nei dati della matrice nella formula.
### **Aggiunge la proprietà GlobalizationSettings.ColumnSeparatorOfFormulaArray**
Ottiene il separatore per gli elementi nei dati di riga della matrice nella formula.
### **Aggiunge la proprietà HtmlSaveOptions.ExportWorksheetCSSSeparately**
Indica se esportare il css del foglio di lavoro separatamente. Il valore predefinito è falso.
### **Aggiunge LoadDataFilterOptions.Structure per sostituire LoadDataFilterOptions.None**
LoadDataFilterOptions.None ha fornito indicazioni ambigue e ha causato confusione. È stato progettato per indicare che non carica nulla per i dati del foglio di lavoro. Ora ne forniamo uno nuovo (membro), ovvero la struttura per sostituirlo.
### **Aggiunge l'enumerazione DataLabelShapeType**
Specifica la geometria della forma preimpostata da utilizzare per un grafico.
### **Aggiunge la proprietà DataLabels.ShapeType**
Ottiene o imposta il tipo di forma dell'etichetta dati.
### **Elimina alcuni FileFormatType obsoleti**
Elimina i tipi di formati di file obsoleti.
### **Aggiunta proprietà WorksheetCollection.RevisionLogs, classe RevisionLogCollection e classe Revisions.RevisionLog**
Ottiene l'impostazione del registro delle revisioni.
### **Aggiunge enum MsoDrawingType.WebExtension**
Rappresenta la forma dell'estensione Web.


### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Popola automaticamente i dati degli indicatori intelligenti in altri fogli di lavoro se i dati sono troppo grandi](/cells/it/java/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Esporta foglio di lavoro CSS separatamente nell'output HTML](/cells/it/java/export-worksheet-css-separately-in-output-html/)
- [Implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal](/cells/it/java/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [Anteporre agli stili degli elementi di tabella la proprietà HtmlSaveOptions.TableCssId](/cells/it/java/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Renderizza i componenti aggiuntivi di Office durante la conversione di Excel in Pdf](/cells/it/java/render-office-add-ins-while-converting-excel-to-pdf/)
- [Impostare il tipo di forma delle etichette dati del grafico](/cells/it/java/set-the-shape-type-of-data-labels-of-chart/)
- [Aggiorna giorni conservando la cronologia dei registri di revisione nella cartella di lavoro condivisa](/cells/it/java/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
