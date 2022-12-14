---
title: Aspose.Cells for .NET 18.9 Note di rilascio
type: docs
weight: 40
url: /it/net/aspose-cells-for-net-18-9-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 18.9](https://www.nuget.org/packages/Aspose.Cells/18.9.0).

{{% /alert %}} 

|**Chiave**|**Riepilogo**|**Categoria**|
|:- |:- |:- |
|CELLSNET-42992|Applicazione dell'allineamento del testo al testo parziale all'interno di TextBox|Nuova caratteristica|
|CELLSNET-46308|Esporta le proprietà del documento personalizzato in PDF|Nuova caratteristica|
|CELLSNET-46301|Ottieni il percorso XML da List Object/Table|Nuova caratteristica|
|CELLSNET-46315|Supporta il grafico azionario nel file ODS|Nuova caratteristica|
|CELLSNET-46304|Aggiungi la proprietà Row.FirstDataCell per recuperare la prima cella di dati nella riga|Aumento|
|CELLSNET-46298|Crea nomi di fogli sicuri simili a Apache POI|Aumento|
|CELLSNET-46319|FilterOperatorType.Contains mancante da API|Aumento|
|CELLSNET-46297|Recupera l'intervallo della tabella delle query|Aumento|
|CELLSNET-46294|Assegna un nome al foglio di lavoro uguale al nome del file di origine durante la conversione di CSV/TSV in foglio di calcolo|Aumento|
|CELLSNET-46289|Includi DLL non firmate di Aspose.Cells|Aumento|
|CELLSNET-46290|Colori errati resi per le forme nella conversione da Excel a PDF|Insetto|
|CELLSNET-46282|Immagini piuttosto piccole rese in PDF|Insetto|
|CELLSNET-46328|Collegamento ipertestuale interrotto in HTML|Insetto|
|CELLSNET-46322|Problemi nei valori di numero e data durante la chiamata di AutoFitColumns()|Insetto|
|CELLSNET-46312|Le tabelle pivot non funzionano dopo il caricamento e il salvataggio|Insetto|
|CELLSNET-46291|Problemi nelle tabelle pivot durante l'aggiornamento e l'occultamento degli elementi pivot|Insetto|
|CELLSNET-46279|PivotTable.RefreshData genera l'eccezione "Indice fuori intervallo".|Insetto|
|CELLSNET-46303|Formula non calcolata correttamente|Insetto|
|CELLSNET-46327|Intervalli denominati quando convertiti in SVG, non catturano i caratteri e la spaziatura esatti|Insetto|
|CELLSNET-46313|Problemi nel PDF di output quando si utilizzano parole chiave tedesche nelle intestazioni e nei piè di pagina degli script|Insetto|
|CELLSNET-46300|L'oggetto tabella/elenco ha sovrapposto i dati sotto la tabella durante l'importazione di dati xml nel foglio di calcolo|Insetto|
|CELLSNET-46318|Le griglie verticali sono apparse nel grafico dopo aver chiamato il metodo Chart.Calculate()|Insetto|
|CELLSNET-46287|L'asse orizzontale non è presente nelle immagini renderizzate dal grafico di Excel|Insetto|
|CELLSNET-46286|Problema durante l'impostazione dell'angolo di rotazione dell'asse delle categorie|Insetto|
|CELLSNET-46333|Il GUID dell'applicazione è stato modificato|Insetto|
|CELLSNET-46332|Archivi e flussi mancanti dal pacchetto OLE dopo aver salvato nuovamente un file XLSX crittografato|Insetto|
|CELLSNET-46325|Grafici persi durante la copia del foglio di lavoro da una cartella di lavoro a un'altra|Insetto|
|CELLSNET-46316|La formattazione condizionale viene applicata senza caratteri e colori di ombreggiatura durante l'unione delle cartelle di lavoro|Insetto|
|CELLSNET-46305|Area testo fuori stampa resa in PDF|Insetto|
|CELLSNET-46296|Adatta colonne o righe che disturbano le forme raggruppate|Insetto|
|CELLSNET-46292|Differenza nei file XML|Insetto|
|CELLSNET-46283|Bordo mancante nell'output ODS Excel|Insetto|
|CELLSNET-46331|Eccezione durante la conversione di un file XLSX in formato file PDF|Eccezione|
|CELLSNET-46270|ArgumentOutOfRangeException sollevata durante la chiamata a Slicer.Refresh()|Eccezione|
|CELLSNET-46323|Problema di convalida dei dati durante il tentativo di modificare il valore della cella con uno dei valori a discesa|Eccezione|
|CELLSNET-46307|Eccezione durante il recupero dell'URL della mappa di data binding xml dell'oggetto elenco|Eccezione|
|CELLSNET-46336|System.OverflowException sollevata durante la chiamata a Chart.Calculate|Eccezione|
|CELLSNET-46293|Eccezione durante il salvataggio del documento|Eccezione|
### **Pubblico API e modifiche incompatibili con le versioni precedenti**
Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.
#### **Aggiunge i metodi CellsHelper.CreateSafeSheetName(string nameProposal)/CreateSafeSheetName(string nameProposal, char replaceChar)**
Metodi per comodità dell'utente per creare un nome di foglio valido.
#### **Aggiunge Row.FirstDataCell**
Ottiene la prima cella non vuota nella riga.
#### **Aggiunge l'enumerazione MapChartLabelLayout**
Rappresenta il tipo di layout dell'etichetta del grafico a mappa.
#### **Aggiunge l'enumerazione MapChartProjectionType**
Rappresenta il tipo di proiezione del grafico a mappa.
#### **Aggiunge l'enumerazione MapChartRegionType**
Rappresenta il tipo di regione del grafico a mappa.
#### **Aggiunge l'enumerazione QuartileCalculationType**
Rappresenta il tipo di calcolo quartile del grafico.
#### **Aggiunge la proprietà Series.LayoutProperties e la classe SeriesLayoutProperties**
Rappresenta le proprietà di layout della serie.
#### **Aggiunge la proprietà TickLabels.IsAutomaticRotation**
Indica se la rotazione delle etichette di spunta è automatica.
#### **Aggiunge l'enumerazione FilterOperatorType.BeginsWith, Contains, EndsWith e NotContains**
Rappresenta il tipo di operatore del filtro di testo.
#### **Aggiunge il metodo Cell.GetDisplayStyle(bool).**
Ottiene lo stile di visualizzazione della cella.
#### **Aggiunge il metodo GlobalizationSettings.GetStandardHeaderFooterFontStyleName(string localFontStyleName)**
Ottiene il nome dello stile del carattere inglese standard (regolare, grassetto, corsivo) per intestazione/piè di pagina in base al nome dello stile del carattere locale specificato.
#### **Aggiunge l'enumerazione PdfCustomPropertiesExport**
Specifica il modo in cui le CustomDocumentPropertyCollection vengono esportate nel file PDF.
#### **Aggiunge la proprietà PdfSaveOptions.CustomPropertiesExport**
Ottiene o imposta un valore che determina il modo in cui CustomDocumentPropertyCollection viene esportato in un file PDF. Il valore predefinito è Nessuno.
#### **Aggiunge la classe XmlDataBinding**
Rappresenta le informazioni sull'associazione dati Xml.
#### **Aggiunge la proprietà ListObject.XmlMap**
Ottiene un oggetto XmlMap usato per questo elenco.
#### **Aggiunge la proprietà XmlDataBinding.Url**
Ottiene l'URL di origine di questo data binding.
#### **Aggiunge la proprietà XmlMap.DataBinding**
Ottiene un XmlDataBinding di questa mappa.
