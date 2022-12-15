---
title: Aspose.Cells for .NET Note sulla versione 17.12
type: docs
weight: 10
url: /it/net/aspose-cells-for-net-17-12-release-notes/
---
{{% alert color="primary" %}} 

Questa pagina contiene le note di rilascio per Aspose.Cells for .NET 17.12.

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-45358|Ottieni CSS separatamente dal markup HTML durante l'esportazione in HTML utilizzando i flussi|Nuova caratteristica|
|CELLSNET-45697|Implementare Cell.FormulaLocal simile a Microsoft Interop FormulaLocal|Nuova caratteristica|
|CELLSNET-45801|Supporto per i componenti aggiuntivi di Office nel rendering da Excel a PDF|Nuova caratteristica|
|CELLSNET-45796|Indicatori intelligenti: come popolare automaticamente i dati nel secondo foglio di lavoro se i dati sono troppo grandi e non possono essere inseriti in un singolo foglio|Nuova caratteristica|
|CELLSNET-45791|Aggiorna "Mantieni cronologia modifiche" durante la condivisione della cartella di lavoro|Nuova caratteristica|
|CELLSNET-45746|Il testo nelle celle si sovrappone ad altre celle su Aspose.Cells.GridDesktop|Nuova caratteristica|
|CELLSNET-45774|Le immagini sono confuse in una forma immagine con riempimento trama|Aumento|
|CELLSNET-45731|L'aggiornamento della tabella pivot danneggia il file MS Excel|Insetto|
|CELLSNET-45794|La formula di matrice che include "MEDIAN" viene calcolata come vuota|Insetto|
|CELLSNET-45779|Cell l'allineamento del testo viene modificato nell'immagine convertita|Insetto|
|CELLSNET-45772|Una pagina persa durante la conversione del foglio di lavoro in immagine|Insetto|
|CELLSNET-45764|Lo stato di DataBars non è corretto nel PDF di output|Insetto|
|CELLSNET-45785|Serie "Nominale in Essere (mln)" Il posizionamento delle etichette dati è errato|Insetto|
|CELLSNET-45775|Manca l'etichetta del secondo asse verticale durante la conversione del grafico in immagine|Insetto|
|CELLSNET-45762|Chart.Calculate richiede più tempo e non funziona|Insetto|
|CELLSNET-45799|Il percorso assoluto cambia in percorso relativo quando si salva nuovamente un file XLSX|Insetto|
|CELLSNET-45797|SetArrayFormula: non trattata come formula di matrice|Insetto|
|CELLSNET-45792|Celle unite perse durante il copia incolla della colonna nelle colonne successive|Insetto|
|CELLSNET-45784|L'inserimento di una colonna fa sì che MS Excel richieda un messaggio di errore|Insetto|
|CELLSNET-45778|Impostazioni dei commenti modificate all'apertura e al salvataggio del file MS Excel|Insetto|
|CELLSNET-45773|Il formato di riempimento viene modificato per tutte le forme di testo nella cartella di lavoro anziché in quella selezionata|Insetto|
|CELLSNET-45770|Il file Xlsx è danneggiato dopo il caricamento e il salvataggio|Insetto|
|CELLSNET-45769|Il valore predefinito della proprietà OoxmlSaveOptions.ExportCellName è true anziché false|Insetto|
|CELLSNET-45768|Workbook.Save(Stream stream, SaveFormat saveFormat) ha esito negativo se il flusso non supporta Seek|Insetto|
|CELLSNET-45780|Problema con la visualizzazione dei dati del foglio di lavoro da destra a sinistra|Insetto|
|CELLSNET-45745|Errore quando si fa clic sulla barra di scorrimento su Aspose.Cells.GridDesktop|Insetto|
|CELLSNET-45777|Si verifica un errore Shape to Image durante la conversione di file Excel in PDF|Eccezione|
|CELLSNET-45804|Eccezione all'apertura di un file Excel (Strict Open XML Spreadsheet).|Eccezione|
|CELLSNET-45798|L'indice era al di fuori dei limiti dell'array - Eccezione durante il rendering del file Excel|Eccezione|
|CELLSNET-45795|È necessario immettere i dati per i criteri di convalida: si verifica un'eccezione durante il salvataggio della cartella di lavoro|Eccezione|
|CELLSNET-45781|ArgumentOutOfRangeException si verifica quando il foglio di lavoro viene copiato in un'altra cartella di lavoro|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge la proprietà HtmlSaveOptions.TableCssId**
Ottiene e imposta il prefisso del nome di tipo css come tr,col,td e così via, sono contenuti nell'elemento table che ha l'attributo specifico TableCssId. Il valore predefinito è "".
#### **Aggiunge la proprietà Cell.FormulaLocal**
Ottiene la formula formattata locale che può variare in base alle diverse impostazioni locali per i separatori, i nomi incorporati, i nomi delle funzioni e così via. Quelle impostazioni locali dipendono.
#### **Aggiunge il metodo GlobalizationSettings.GetLocalFunctionName(string standardName).**
Ottiene il nome della funzione dipendente dalle impostazioni locali in base al nome della funzione standard specificato.
#### **Aggiunge il metodo GlobalizationSettings.GetLocalBuiltInName(string standardName).**
Ottiene il testo dipendente dalle impostazioni locali per il nome incorporato in base al testo standard specificato.
#### **Aggiunge la proprietà GlobalizationSettings.ListSeparator**
Ottiene il separatore per elenco, parametri di funzione, ...ecc.
#### **Aggiunge la proprietà GlobalizationSettings.RowSeparatorOfFormulaArray**
Ottiene il separatore per le righe nei dati della matrice nella formula.
#### **Aggiunge la proprietà GlobalizationSettings.ColumnSeparatorOfFormulaArray**
Ottiene il separatore per gli elementi nei dati di riga della matrice nella formula.
#### **Aggiunge la proprietà HtmlSaveOptions.ExportWorksheetCSSSeparately**
Indica se esportare il css del foglio di lavoro separatamente. Il valore predefinito è falso.
#### **Aggiunge LoadDataFilterOptions.Structure per sostituire LoadDataFilterOptions.None**
LoadDataFilterOptions.None ha fornito indicazioni ambigue e ha causato confusione. È stato progettato per indicare che non carica nulla per i dati del foglio di lavoro. Ora ne forniamo uno nuovo (membro), ovvero la struttura per sostituirlo.
#### **Aggiunge l'enumerazione DataLabelShapeType**
Specifica la geometria della forma preimpostata da utilizzare per un grafico.
#### **Aggiunge la proprietà DataLabels.ShapeType**
Ottiene o imposta il tipo di forma dell'etichetta dati.
#### **Elimina alcuni FileFormatType obsoleti**
Elimina i tipi di formati di file obsoleti.
#### **Aggiunta proprietà WorksheetCollection.RevisionLogs, classe RevisionLogCollection e classe Revisions.RevisionLog**
Ottiene l'impostazione del registro delle revisioni.
#### **Aggiunge enum MsoDrawingType.WebExtension**
Rappresenta la forma dell'estensione Web.


#### **Esempi di utilizzo**
Si prega di controllare l'elenco degli argomenti della guida aggiunti nei documenti Wiki Aspose.Cells:

- [Popola automaticamente i dati degli indicatori intelligenti in altri fogli di lavoro se i dati sono troppo grandi](/cells/it/net/auto-populate-smart-marker-data-to-other-worksheets-if-data-is-too-large/)
- [Esporta foglio di lavoro CSS separatamente nell'output HTML](/cells/it/net/export-worksheet-css-separately-in-output/)
- [Implementare Cell.FormulaLocal simile a Excel VBA Range.FormulaLocal](/cells/it/net/implement-cell-formulalocal-similar-to-excel-vba-range-formulalocal/)
- [Anteporre agli stili degli elementi di tabella la proprietà HtmlSaveOptions.TableCssId](/cells/it/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/)
- [Renderizza i componenti aggiuntivi di Office durante la conversione di Excel in Pdf](/cells/it/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [Impostare il tipo di forma delle etichette dati del grafico](/cells/it/net/set-the-shape-type-of-data-labels-of-chart/)
- [Il testo fuoriesce dalla cella GridDesktop se è troppo lungo](/cells/it/net/text-overflows-from-griddesktop-cell-if-it-is-too-long/)
- [Aggiorna giorni conservando la cronologia dei registri di revisione nella cartella di lavoro condivisa](/cells/it/net/update-days-preserving-history-of-revision-logs-in-shared-workbook/)
