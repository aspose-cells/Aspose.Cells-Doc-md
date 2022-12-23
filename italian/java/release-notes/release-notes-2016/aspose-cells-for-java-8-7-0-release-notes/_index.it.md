---
title: Aspose.Cells for Java 8.7.0 Note di rilascio
type: docs
weight: 140
url: /it/java/aspose-cells-for-java-8-7-0-release-notes/
---
{{% alert color="primary" %}} 

 Questa pagina contiene le note di rilascio per[Aspose.Cells for Java 8.7.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.7.0/)

{{% /alert %}} 

 Di seguito è riportato un elenco di miglioramenti e modifiche in questa versione di Aspose.Cells



\1) Aspose.Cells 


## **Altri miglioramenti e modifiche**

## **Nuove caratteristiche**


 (CELLSJAVA-41672) - Esponi API per la proprietà "Ridimensiona forma per adattare il testo" per le etichette dati del grafico

 (CELLSJAVA-41655) - Il metodo Cells.importCSV() non riconosce le formule


## **Miglioramenti**


 (CELLSJAVA-41680) - API esegue il rendering del nome del mese russo in modo diverso prima e dopo aver chiamato il metodocalcFormula

(CELLSJAVA-41673) - Aspose.Cells non sta leggendo nulla dal foglio Excel nel file modello


## **Insetti**


 (CELLSJAVA-41685) - Le immagini del grafico hanno una dimensione di 0 KB durante la conversione del foglio di calcolo in HTML

 (CELLSJAVA-41684) - Manca l'immagine del grafico in HTML

 (CELLSJAVA-41676) - HTML L'output produce risultati imprevedibili

 (CELLSJAVA-41665) - L'immagine nel foglio di calcolo non viene esportata in HTML

 (CELLSJAVA-41632) - Problema di allineamento della data durante la conversione da EXCEL a HTML e ritorno a EXCEL

 (CELLSJAVA-41603) - Viene visualizzato un colore di sfondo errato per le celle durante l'esportazione di un intervallo di celle in html

 (CELLSJAVA-41337) - La conversione in HTML genera un file HTML molto grande

 (CELLSJAVA-41705) - Il colore del testo non viene visualizzato correttamente in HTML delle tabelle di Excel

 (CELLSJAVA-41647) - Il collegamento ipertestuale in un ListObject che punta a un intervallo si interrompe quando il foglio di calcolo viene convertito in HTML

(CELLSJAVA-41659) - L'applicazione di uno stile con nome su una cella non si riflette nella sezione Stili dell'interfaccia di Excel

 (CELLSJAVA-41602) - Il metodo Cell.calculate() non funziona correttamente per una cella specifica

 (CELLSJAVA-41645) - Il colore del carattere dell'intestazione di ListObject viene perso durante la copia degli intervalli

 (CELLSJAVA-41707) - Il colore del testo non viene visualizzato correttamente nell'immagine delle tabelle di Excel

 (CELLSJAVA-41688) - Problema con il carattere ebraico nell'intestazione

 (CELLSJAVA-41666) - Il bordo di DataBar non è uguale a quello di Excel durante il rendering in Immagine

 (CELLSJAVA-41662) - Bordo mancante durante il rendering di DataBar nell'immagine

 (CELLSJAVA-41548) - Da DataBar a immagine: la dimensione di DataBar nell'immagine non corrisponde a Excel

 (CELLSJAVA-41250) - Il foglio non viene visualizzato correttamente utilizzando SheetRender.toImage()

 (CELLSJAVA-41701) - I valori dell'altezza dell'area del grafico e dell'area Y del grafico sono diversi dopo aver ricaricato il grafico dal foglio di calcolo

(CELLSJAVA-41699) - Conversione da grafico a immagine - L'immagine del grafico non viene visualizzata correttamente poiché le dimensioni della barra vengono visualizzate in modo diverso

 (CELLSJAVA-41689) - L'antialiasing non sembra avere effetto per il riempimento della serie del grafico durante l'esportazione in HTML

(CELLSJAVA-41686) - RenderingHints.VALUE_TESTO_ ANTIALIAS_GASP non ha effetto durante la conversione del foglio di calcolo in HTML

 (CELLSJAVA-41678) - Vengono visualizzati colori errati nel grafico PDF

 (CELLSJAVA-41669) - Tutte le barre vengono visualizzate sotto la regola del valore 0 nel grafico PDF

 (CELLSJAVA-41667) - I grafici a barre raggruppati non vengono visualizzati nel formato di file di output PDF

 (CELLSJAVA-41660) - Lo spessore dell'asse X e dell'asse Y è aumentato nel grafico PDF

 (CELLSJAVA-41657) - Il grafico a bolle non viene visualizzato correttamente durante la conversione in immagine

 (CELLSJAVA-41656) - Il valore della serie di grafici viene visualizzato ad angolo

(CELLSJAVA-41646) - la sezione inferiore dell'asse X nel grafico PDF viene tagliata

 (CELLSJAVA-41644) - Le etichette degli assi vengono mostrate inclinate durante il rendering del grafico su PDF

 (CELLSJAVA-41628) - Allineamento dell'intestazione non accurato nel grafico a PDF

 (CELLSJAVA-41623) - Mancano alcune barre della serie di dati nel grafico PDF utilizzando Chart.toPdf

 (CELLSJAVA-41468) - Problema di qualità del grafico: l'anti-aliasing non ha effetto senza ombra

 (CELLSJAVA-41445) - Il grafico a bolle non ha effetto anti-aliasing nel formato file HTML sottoposto a rendering

 (CELLSJAVA-41306) - Problema di conversione da Excel a PDF - lato destro tagliato

 (CELLSJAVA-41697) - Viene visualizzato un colore del carattere errato per tabelle e intervalli nel formato HTML/Image/PDF generato

 (CELLSJAVA-41679) - Worksheet.getProtection().getPasswordHash() restituisce 0 dopo la riprotezione tramite codice macro

 (CELLSJAVA-41675) - L'immagine non è trasparente nel pdf di output

 (CELLSJAVA-41671) - Rendering errato dei colori Cell con formattazione condizionale nella risultante PDF

(CELLSJAVA-41663) - Il salvataggio dei dati dell'immagine dell'icona della formattazione condizionale nel file risulta in un'immagine vuota

 (CELLSJAVA-41661) - Il processo si blocca durante il caricamento e la conversione in file xlsx da xml

 (CELLSJAVA-41597) - Contenuto illeggibile in Excel 2007 dopo il nuovo salvataggio XLSB


## **Eccezioni**


 (CELLSJAVA-41592) - Nullpointer quando si tenta di salvare il foglio Excel come html



 \2) Aspose.Cells Griglia Suite


## **Altri miglioramenti e modifiche**

## **Insetti**


 (CELLSJAVA-41598) - Dopo aver caricato il file modello in GridWeb e aver fatto clic più volte sul pulsante Ricarica, la memoria aumenta


## **Pubblico API e modifiche incompatibili con le versioni precedenti**


 Di seguito è riportato un elenco di eventuali modifiche apportate al pubblico API come membri aggiunti, rinominati, rimossi o deprecati, nonché qualsiasi modifica non compatibile con le versioni precedenti apportata a Aspose.Cells for Java. In caso di dubbi su qualsiasi modifica elencata, si prega di segnalarlo su il forum di supporto Aspose.Cells.



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



 Aggiunge la proprietà PdfSaveOptions.OptimizationType.

 Ottiene e imposta il tipo di ottimizzazione pdf.





 Nota

 Poiché la base di codice di Aspose.Cells for Java corrisponde al codice della versione .NET pertinente, la maggior parte delle modifiche, miglioramenti e correzioni inclusi in Aspose.Cells for .NET v8.7.0 sono inclusi anche in questo Aspose.Cells for Java v8.7.0.
