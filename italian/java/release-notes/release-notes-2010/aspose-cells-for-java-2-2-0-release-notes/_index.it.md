---
title: Aspose.Cells for Java 2.2.0 Note di rilascio
type: docs
weight: 80
url: /it/java/aspose-cells-for-java-2-2-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 2.2.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.2.0/)

{{% /alert %}} 

 Siamo felici di annunciare Aspose.Cells for Java 2.2.0!

 Cosa è cambiato:

- Imposta le formule con righe/colonne/parametri che superano il limite di MS Excel 2003
 Supporta la conservazione dei dati originali letti dal file modello MS Excel 2010
 Manipola gli sparkline di MS Excel 2010
 Fornisce stili estesi salvati da MS Excel 2007 per i file XLS
 Supporta il rilevamento automatico del tipo di formato di file durante l'apertura del file modello senza specificare il formato per i file Html e SpreadSheeML
 Rimuove un grafico dalla raccolta Grafici
 Consente di eliminare righe/colonne vuote nel foglio di lavoro
Supporta il salvataggio del colore nel colore corrispondente più vicino nella tavolozza quando il colore specificato dall'utente non è nella tavolozza standard.
 Esporta l'attributo di rotazione del testo per la funzione Excel in Pdf
 Esporta i grafici come immagini per la funzione Excel in Pdf
 Rimuove l'area di stampa esistente
 Include miglioramenti per il salvataggio delle aree unite: controlla e rimuovi o combina quelle aree duplicate/sovrapposte che potrebbero far sì che il file generato mostri un messaggio di avviso quando viene aperto in MS Excel
 Include miglioramenti per l'aggiunta di interruzioni di pagina: controlla e rimuovi le interruzioni di pagina duplicate prima di salvare
 Include miglioramenti per la funzione da grafico a immagine
 65 correzioni e altri miglioramenti.

 Problemi risolti in Aspose.Cells per Jav

 Cambiamenti notevoli per gli utenti:



 Nelle versioni precedenti, i metodi Workbook.save(String) e Workbook.save(InputStream) salveranno sempre il file risultante come formato di file Excel97TO2003.

Da questa versione, se è stato specificato il tipo di formato della cartella di lavoro, i metodi Workbook.save(String) e Workbook.save(InputStream) salveranno il file risultante nel formato specificato dalla cartella di lavoro. Il tipo di formato della cartella di lavoro può essere impostato dal metodo Workbook.setFileFormatType(int). Oppure può essere impostato automaticamente come formato del file modello di input all'apertura di un file modello esistente.

 Inoltre, il limite di riga/colonna delle formule e il limite di conteggio dei parametri delle formule dipendono anche dal tipo di formato della cartella di lavoro. Prima di superare il limite di riga/colonna/parametro delle formule per MS Excel 2003, è necessario impostare esplicitamente il formato della cartella di lavoro su altri tipi, ad esempio EXCEL2007.
