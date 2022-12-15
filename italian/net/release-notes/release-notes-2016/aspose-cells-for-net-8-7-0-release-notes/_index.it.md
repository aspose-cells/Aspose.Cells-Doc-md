---
title: Aspose.Cells for .NET 8.7.0 Note di rilascio
type: docs
weight: 140
url: /it/net/aspose-cells-for-net-8-7-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for .NET 8.7.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.7.0/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSNET-43938) - Supporta l'esportazione del certificato VBA su file o stream

 (CELLSNET-43920) - Supporta un'API per verificare se VBAcode è firmato

 (CELLSNET-43867) - Firma digitalmente progetti/macro VBA

 (CELLSNET-44150) - Capacità di lavorare con mappe XML

 (CELLSNET-43992) - Supporta la funzionalità di importazione della mappatura XML come avviene dalla scheda Sviluppatore di Excel


## **Miglioramenti**


 (CELLSNET-43878) - Il segno digitale VBA viene perso durante la conversione (da XLSM a XLS)

 (CELLSNET-43160) - Il progetto VBA perde la firma digitale durante il salvataggio di xls come formato di file xlsm

 (CELLSNET-44169) - L'ordine dell'array Validation.Value1 è diverso da quanto mostrato in Excel

 (CELLSNET-44168) - Impossibile creare la formattazione condizionale della scala a 2 colori

 (CELLSNET-44167) - Supporta la funzione ISOWEEKNUM MS Excel 2013

(CELLSNET-44166) - Il segno digitale VBA viene perso durante la conversione (da XLSB a XLSM)


## **Prestazione**


 (CELLSNET-44156) - L'applicazione console si arresta in modo anomalo su Workbook.CalculateFormula

 (CELLSNET-44120) - Workbook.CalculateFormula richiede più tempo per calcolare le formule nella cartella di lavoro.

 (CELLSNET-43896) - Processo terminato durante la chiamata a Workbook.CalculateFormula


## **Insetti**


 (CELLSNET-44164) - Struttura HTML incompleta durante il salvataggio in un flusso

 (CELLSNET-44147) - L'aggiornamento della tabella pivot genera un file excel corrotto

 (CELLSNET-44022) - Workbook.Copy non conserva la formattazione per le tabelle pivot

 (CELLSNET-44139) - Valori diversi per la stessa cella prima e dopo la chiamata al metodo CalculateFormula()

 (CELLSNET-44135) - Il file Excel non viene calcolato correttamente (completamente) (per quanto riguarda i grafici) prima della generazione del PDF

 (CELLSNET-44138) - Cell l'ombreggiatura si sovrappone al bordo causandone l'assottigliamento

 (CELLSNET-44136) - Excel mostra una pagina nell'anteprima di stampa in cui Aspose.Cells esegue il rendering delle pagine PDF

(CELLSNET-44122) - Il rendering delle immagini nei fogli non è uguale a quello del file Excel modello originale

 (CELLSNET-43587) - Cell L'area si sovrappone al bordo Cell durante la conversione del foglio di calcolo in PDF

 (CELLSNET-44171) - CopyData tra intervalli non funziona in orizzontale ma funziona correttamente in verticale

 (CELLSNET-44153) - Da XLSB a XLSM non funziona correttamente e produce file danneggiati

 (CELLSNET-44149) - OleObjects viene rimosso dopo la conversione da XLSB a XLSM

 (CELLSNET-44146) - I risultati della formattazione condizionale non vengono visualizzati correttamente in PDF

 (CELLSNET-44144) - L'aggiunta di proprietà personalizzate rimuove il contenuto del foglio di lavoro

 (CELLSNET-44141) - L'asse delle categorie primarie del grafico si sbaglia quando si salva nuovamente il file excel di origine

 (CELLSNET-44160) - L'asse orizzontale è stato modificato con etichette diverse rispetto al file iniziale

 (CELLSNET-44157) - L'asse x principale del grafico personalizzato è stato modificato dopo l'apertura e il nuovo salvataggio del file XLSX del modello

(CELLSNET-43910) - L'estrazione dell'immagine dal foglio di lavoro e l'inserimento nel file del documento la rende incompleta


## **Eccezioni**


 (CELLSNET-44119) - Errore nel calcolo in Workbook.CalculateFormula

 (CELLSNET-44089) - System.IndexOutOfRangeException in PivotTable.CalculateData

 (CELLSNET-44064) - CalculateFormula genera un'eccezione sull'xlsm di origine

 (CELLSNET-44055) - Aspose.Cell. Eccezione causata dalla conversione pdf a causa dell'impostazione della preferenza di memoria

 (CELLSNET-44179) - Eccezione durante il caricamento di un file HTML (creato da XSLT)

 (CELLSNET-44145) - System.NullReferenceException in WorkbookMetadata ctor

 (CELLSNET-44143) - Eccezione nella cartella di lavoro ctor durante il caricamento di XLSX

 (CELLSNET-44142) - IndexOutOfBoundsException durante la creazione di un'istanza della cartella di lavoro con XLS



\2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSNET-44151) - JavaScript non viene attivato durante l'eliminazione dei contenuti dalla cella GridWeb

 (CELLSNET-44113) - Il testo della riga di intestazione viene visualizzato anche all'interno dei valori del filtro


## **API pubblica e modifiche non compatibili con le versioni precedenti**


 Di seguito è riportato un elenco di tutte le modifiche apportate all'API pubblica come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for .NET. il forum di supporto Aspose.Cells.



 Aggiunge la proprietà TxtLoadOptions.HasFormula.

 Indica se il file csv contiene una formula.



 Aggiunge la proprietà ColorScale.Is3ColorScale.

 Indica se la formattazione condizionale è una scala di 3 colori.



Elimina la proprietà Workbook.SaveOptions obsoleta.

 Usare invece il metodo Workbook.Save(Stream,SaveOptions) o Workbook.Save(string,SaveOptions).



 Aggiunge il metodo Protection.VerifyPassword.

 Verifica la password di protezione del foglio di lavoro.



 Aggiunge la proprietà Proptection.IsProtectedWithPassword.

 Indica se il foglio di lavoro è protetto da password.



 Aggiunge il metodo VbaProject.Sign.

Firma il progetto VBA con una firma digitale.



 Aggiunge la proprietà VbaProject.IsValidSigned.

 Indica se la firma del progetto VBA è valida o meno.



 Aggiunge la proprietà VbaProject.CertRawData.

 Ottiene i dati non elaborati del certificato se il progetto VBA è firmato.



 Aggiunge la proprietà PdfSaveOptions.OptimizationType.

 Ottiene e imposta il tipo di ottimizzazione pdf.


