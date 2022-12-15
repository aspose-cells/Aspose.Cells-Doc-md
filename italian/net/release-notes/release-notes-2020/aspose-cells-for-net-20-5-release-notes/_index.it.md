---
title: Aspose.Cells for .NET 20.5 Note di rilascio
type: docs
weight: 30
url: /it/net/aspose-cells-for-net-20-5-release-notes/
---
{{% alert color="primary" %}}

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 20.5](https://www.nuget.org/packages/Aspose.Cells/20.5.0).

{{% /alert %}}

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42948|Supporta GridWeb su MVC|Nuova caratteristica|
|CELLSNET-46946|Supporto per Aspose.Cells.GridWeb in ASP.NET Core|Nuova caratteristica|
|CELLSNET-47251|Nuovo simbolo Excel “Operatori di intersezione impliciti”@ inserito|Aumento|
|CELLSNET-47303|Opzione per accedere alla cella attiva o alle celle selezionate dall'esterno di GridWeb|Aumento|
|CELLSNET-47243|Aspetta getdisplaystyle per un foglio di lavoro con righe 65536|Prestazione|
|CELLSNET-47044|Problema di formattazione della data nelle celle della prima colonna nella tabella pivot|Insetto|
|CELLSNET-47301|Le righe/colonne vengono nascoste esportando la tabella pivot in un'immagine dopo il calcolo|Insetto|
|CELLSNET-47308|Poche proprietà mancanti nell'HTML di output dopo l'impostazione di Cell.HtmlString|Insetto|
|CELLSNET-47343|Intestazioni mancanti durante la conversione dell'area di stampa in HTML|Insetto|
|CELLSNET-47344|L'intero foglio di lavoro esportato quando è prevista solo l'area di stampa|Insetto|
|CELLSNET-47322|Valore errato calcolato da Aspose.Cells durante l'utilizzo della funzione OFFSET|Insetto|
|CELLSNET-47333|Quando si utilizza l'API CalculateFormula su un foglio di lavoro, il valore di due celle è errato|Insetto|
|CELLSNET-46960|Formattazione e comportamento Problemi durante il caricamento del file Excel su GridWeb|Insetto|
|CELLSNET-47096|Un problema con la barra della formula di GridDesktop con SplitterPane|Insetto|
|CELLSNET-47200|Problema di sovrapposizione sui pulsanti di navigazione quando si imposta il foglio nascosto come foglio attivo|Insetto|
|CELLSNET-47221|Visualizza correttamente il numero di riga in GridDesktop|Insetto|
|CELLSNET-47228|Problema nell'apertura del file in GirdDesktop|Insetto|
|CELLSNET-47240|FormulaBar.VerticalScroll in GridDesktop non funzionante|Insetto|
|CELLSNET-47294|Allineamento verticale non efficace in GridWeb|Insetto|
|CELLSNET-47302|GridWeb mostra i commenti parziali nelle celle|Insetto|
|CELLSNET-47311|Commenti ritagliati a causa del blocco del riquadro|Insetto|
|CELLSNET-47323|L'immagine posteriore della cella chiara di Gridweb provoca il caricamento della pagina con IsPostBack falso|Insetto|
|CELLSNET-47346|GridDesktop mostra caratteri semplici invece di '*' durante l'inserimento della password da modificare|Insetto|
|CELLSNET-47349|Errore JS|Insetto|
|CELLSNET-47281|Interruzioni di riga involontarie nelle celle durante la conversione di file Excel in PDF|Insetto|
|CELLSNET-47298|Carattere esistente sostituito da Aspose.Cells|Insetto|
|CELLSNET-47299|CellsException durante la conversione da Excel a PDF|Insetto|
|CELLSNET-47320|L'importazione di XML nella cella ottiene il valore errato|Insetto|
|CELLSNET-47321|L'importazione di XML danneggia il file di output|Insetto|
|CELLSNET-47324|Errore icona nella conversione da Excel a PDF|Insetto|
|CELLSNET-46149|Problema di allineamento del testo nell'immagine del grafico|Insetto|
|CELLSNET-47231|Un'etichetta mancante sull'immagine del grafico durante il rendering con la versione più recente|Insetto|
|CELLSNET-47116|I dati vengono persi durante la conversione di sample.xlsx in .xls|Insetto|
|CELLSNET-47325|La chiamata a TextBox.Characters() provoca tag aggiuntivi in HtmlText|Insetto|
|CELLSNET-47326|Lo stile dei collegamenti ipertestuali viene perso quando si salva la cartella di lavoro ODS come PDF o HTML|Insetto|
|CELLSNET-47327|Il testo dei collegamenti ipertestuali viene perso durante il nuovo salvataggio o il rendering di un file ODS|Insetto|
|CELLSNET-47332|L'impostazione delle proprietà TextParagraph genera più righe di testo sovrapposte|Insetto|
|CELLSNET-47339|Cell il formato è perso/manca il contenuto dopo il salvataggio|Insetto|
|CELLSNET-47348|Formato della data modificato nel file ODS dopo averlo caricato e salvato|Insetto|
|CELLSNET-47290|Eccezione quando si tenta di aprire un particolare file HTML|Eccezione|
|CELLSNET-47305|RANDBETWEEN() solleva l'eccezione ArgumentOutOfRangeException|Eccezione|
|CELLSNET-47351|Formattazione condizionale che causa StackOverflowException durante il salvataggio in PDF|Eccezione|
|CELLSNET-47319|NullReferenceException su file Excel con immagine SVG collegata|Eccezione|
|CELLSNET-47359|Eccezione durante il caricamento di un file XLSX|Eccezione|
### **API pubblica e modifiche non compatibili con le versioni precedenti**
Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.
#### **Aggiunge il metodo WorkbookSettings.GetThemeFont().**
Ottiene il carattere del tema.
#### **Aggiunge la proprietà DataLabels.LinkedSource.**
Ottiene e imposta l'origine collegata.
#### **Aggiunge l'enumerazione DefaultEditLanguage.**
Rappresenta la lingua di modifica predefinita.
#### **Aggiunge la proprietà ImageOrPrintOptions.DefaultEditLanguage.**
Ottiene o imposta la lingua di modifica predefinita.
Può visualizzare/renderizzare diversi layout per i paragrafi di testo quando sono impostate diverse lingue di modifica.
#### **Aggiunge la proprietà PdfSaveOptions.DefaultEditLanguage.**
Ottiene o imposta la lingua di modifica predefinita.
Può visualizzare/renderizzare diversi layout per i paragrafi di testo quando sono impostate diverse lingue di modifica.
