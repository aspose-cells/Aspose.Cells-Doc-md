---
title: Aspose.Cells for .NET 5.1.0 Note di rilascio
type: docs
weight: 60
url: /it/net/aspose-cells-for-net-5-1-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 5.1.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-5.1.0/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells for .NET v!

 Cosa è cambiato in Aspose.Cells:

- Include il supporto degli smart tag per i file XLSX.
 Converte gli sparkline in immagini.
 Fornisce il supporto per gli Smart Marker immagine.
 Supporta i riempimenti sfumati di Cell e il tema del file XLS.
 Renders Il motivo di Cell riempie il file PDF generato.
 Aggiunge il supporto per la conformità Pdf/A-1b.
 Migliora le prestazioni e la qualità dei file PDF generati.
 46 miglioramenti e correzioni.

 Cosa è cambiato in Aspose.Cells.GridWeb:

- Converte raccolte personalizzate gerarchiche in set di dati che contengono relazioni.

 1 correzione.



 Cosa è cambiato in Aspose.Cells.GridDesktop:

- Include l'evento Scroll.

Fornisce una versione di overload per il metodo SumSelectedRanges per escludere le celle nascoste.

 1 correzione.

 Problemi risolti in Aspose.Cells for .NET v

|**ID problema** |**Componente** |**Riepilogo** |
|:- |:- |:- |
|17474 | GrigliaWeb| I bordi non vengono visualizzati per le celle unite|
|15467 | GrigliaDesktop| Modifica il nome del foglio di lavoro duplicato nel metodo ImportExcelFile|
|17581 | Grafico2Immagine| Converte il grafico in immagine|
|17762 | Grafico2Immagine| Le tabelle dati, i valori e la categoria vengono persi per i grafici a dispersione XY|
|17900 | Grafico2Immagine| Grafico di Excel per problema di immagine|
|18023 | Grafico2Immagine|Grafici a bolle|
|18190 | Grafico2Immagine| Aspose.Cells lancio di eccezioni di memoria in Azure|
|18012 | CSV| Esporta diverso da Excel|
|16207 | PDF| Trova errore durante il salvataggio del file PDF|
|17535 | PDF| Un carattere in XLSX risulta in due caratteri in PDF|
|17537 | PDF| Celle vuote in formato valuta|
|17776 | PDF| Problema di conversione di Excel in PDF|
|17804 | PDF| I valori decimali non vengono visualizzati se sono presenti solo zeri|
|17821 | PDF| Proprietà integrate|
|17981 | PDF| Problema di conversione da Excel a PDF|
|18021 | PDF| Salvataggio in PDF - Problemi con il carattere|
|18038 | PDF| Il documento PDF sembra essere danneggiato|
|18136 | PDF| Problema di salvataggio PDF|
|18258 | PDF| Le formule calcolate non si aggiornano alla conversione da Cells a PDF|
|18316 | PDF| Problema di conversione con i dati visualizzati come segni numerici|
|18258 | PDF| Le formule calcolate non si aggiornano alla conversione da Cells a PDF|
|18316 | PDF| Problema di conversione con i dati visualizzati come segni numerici|
|18239 | Foglio di calcoloML| Eccezione indice colonna finale non valida|
|17111 | Foglio di lavoro2Immagine| Formattazione non corretta dei dati numerici|
|17633 | Foglio di lavoro2Immagine| Linea nella grafica non convertita|
|17903 | Foglio di lavoro2Immagine| Le prestazioni di worksheet2image|
|18310 | Foglio di lavoro2Immagine| Nessuna risposta da SheetRender|
|17656 | xls| Come trovare righe e colonne raggruppate|
|17761 | XL| Calcola formule esterne|
|17789 | XL| Formula di formattazione condizionale|
|17810 | XL| L'intervallo mobile si comporta in modo errato|
|17820 | XL| Questo file è stato creato utilizzando una versione successiva|
|17907 | XL|L'ordinamento all'interno dei gruppi non funziona|
|17954 | XL| Shape.AlternativeText|
|17999 | XL| Supporta l'aggiunta di immagini Tif con il metodo Pictures.Add()|
|18054 | XL| Worsheet.Copy sta ancorando la CPU al 100%|
|18135 | XL| Supporta PageLayoutView|
|18160 | XL| Problema di compatibilità con MS Excel|
|18297 | XL| Formula errata (Cell.formula e collegamento esterno)|
|18366 | XL| Supporta la copia del collegamento ipertestuale nell'intervallo di copia.|
|16656 | Xlsx| Macro perse durante il salvataggio in formato XLSM|
|17041 | Xlsx| Come impostare il colore trasparente su un'immagine|
|17652 | Xlsx| Come spostare il pulsante di comando|
|17664 | Xlsx| Modifiche di formattazione condizionale esistenti|
|17719 | Xlsx| Il valore era troppo grande o troppo piccolo per un Int16|
|17982 | Xlsx| I campi della pagina della tabella pivot non funzionano in Excel 2007|
|18004 | Xlsx| Problema di subtotali|
|18036 | Xlsx| Il problema dell'apertura del file XLSM.|
|18161 | Xlsx| Eccezione indice colonna finale non valida con file XLSX|
|18356 | Xlsx| Titolo del grafico con problema di formula|
 Notevoli modifiche per gli utenti esistenti

In questa versione (Aspose.Cells for .NET v5.1.0), abbiamo rinominato alcune classi del componente Aspose.Cells per pulire la struttura dell'API. Abbiamo alcune classi di raccolta ma i loro nomi non le giustificano secondo gli standard .NET. Quindi, dopo approfondite analisi e revisioni, abbiamo deciso di cambiare i nomi di alcune classi. Questo cambiamento ha alcuni aspetti importanti che dobbiamo seguire. Di seguito è riportato l'elenco delle classi ora rinominate.
