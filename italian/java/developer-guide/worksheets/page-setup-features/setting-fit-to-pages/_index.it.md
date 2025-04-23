---
title: Come stampare Excel in pagine larghe e alte adattate
type: docs
weight: 200
url: /it/java/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: Questo articolo mostra il codice che spiega come impostare FitToPagesWide e FitToPagesTall usando la libreria Aspose.Cells.
keywords: Java Come impostare FitToPagesWide e FitToPagesTall, come aggiungere FitToPagesWide e FitToPagesTall in Java, come impostare FitToPagesWide e FitToPagesTall in Excel, come cancellare FitToPagesWide e FitToPagesTall in Excel, come stampare Excel in pagine larghe e alte, come stampare il foglio di lavoro come una pagina, come stampare tutte le colonne del foglio di lavoro in una pagina.
---

## **Introduzione**

Le impostazioni FitToPagesWide e FitToPagesTall sono usate nelle applicazioni di fogli di calcolo (come Microsoft Excel) per controllare come viene scalato un foglio di calcolo durante la stampa. Queste impostazioni aiutano a garantire che il risultato stampato si adatti a un numero specificato di pagine, sia orizzontalmente che verticalmente. Ecco una spiegazione di ogni impostazione:

1. FitToPagesWide: questa impostazione specifica il numero di pagine di larghezza in cui il risultato stampato deve adattarsi. Ad esempio, impostando FitToPagesWide su 1 significa che il contenuto sarà ridimensionato per adattarsi a una singola pagina di larghezza, indipendentemente dalla larghezza del foglio di calcolo.
1. FitToPagesTall: questa impostazione specifica il numero di pagine di altezza in cui il risultato stampato deve adattarsi. Ad esempio, impostando FitToPagesTall su 1 significa che il contenuto sarà ridimensionato per adattarsi a una singola pagina di altezza, indipendentemente dal numero di righe.

## **Perché usare FitToPagesWide e FitToPagesTall**
Ecco alcuni motivi per impostare FitToPagesWide e FitToPagesTall:
1. Controllo del Layout di Stampa: specificando il numero di pagine di larghezza e altezza, puoi garantire che il tuo documento stampato sia facile da leggere e ben organizzato, senza che colonne o righe siano divise in modo inappropriato tra le pagine.
1. Coerenza: se stampi più fogli o report, usare queste impostazioni aiuta a mantenere un formato coerente, facilitando il confronto e l'analisi dei documenti stampati.
1. Presentazione Professionale: ridimensionare e adattare correttamente il contenuto a un numero specificato di pagine può dare una presentazione più professionale e curata dei tuoi dati.

## **Come stampare il file come pagine adattate in larghezza e altezza in Excel**

Per impostare le impostazioni FitToPagesWide e FitToPagesTall in Microsoft Excel, segui questi passaggi:

1. Apri il tuo file Excel e vai sul foglio che desideri stampare.
1. Vai alla scheda Layout di pagina sulla barra multifunzione.
1. Nel gruppo Imposta pagina, clicca sulla piccola freccia in basso a destra per aprire la finestra di dialogo Imposta pagina.
1. Nella finestra di dialogo Imposta pagina, vai alla scheda Pagina.
1. Sotto Scala, seleziona l'opzione "Adatta a" e specifica quindi il numero di pagine in larghezza e altezza desiderato: Inserisci il numero di pagine in larghezza nel primo campo (Adatta a x pagine in larghezza). Inserisci il numero di pagine in altezza nel secondo campo (Adatta a y pagine in altezza).
<br>
<img src="2.png" width=60% />

1. Clicca OK per applicare le impostazioni.


## **Come stampare Excel come pagine adattate in larghezza e altezza usando Aspose.Cells**

Per impostare FitToPagesWide e FitToPagesTall in un foglio di lavoro specifico: Innanzitutto, carica il [file di esempio](input.xlsx), quindi chiama i metodi [**Worksheet.PageSetup.setFitToPagesTall(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesTall-int-) e [**Worksheet.PageSetup.setFitToPagesWide(int value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/#setFitToPagesWide-int-) dell'oggetto [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/pagesetup/) per il foglio desiderato. Ecco un esempio in Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.java" >}}

Il risultato dell'output:
<br>
<img src="1.png" width=60% />

## **Come stampare il foglio di lavoro come una pagina usando Aspose.Cells**

Per stampare il foglio di lavoro come una pagina: innanzitutto, carica il [file di esempio](sample.xlsx), quindi chiama il metodo [**PdfSaveOptions.setOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setOnePagePerSheet-boolean-) dell'oggetto [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/). Ecco un esempio in Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-OnePagePerSheet.java" >}}

Il risultato dell'output:
<br>
<img src="3.png" width=60% />


## **Come stampare tutte le colonne del foglio di lavoro in una pagina usando Aspose.Cells**

Per stampare tutte le colonne del foglio di lavoro in una pagina: innanzitutto, carica il [file di esempio](sample.xlsx), quindi chiama il metodo [**PdfSaveOptions.setAllColumnsInOnePagePerSheet(boolean value)**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/#setAllColumnsInOnePagePerSheet-boolean-) dell'oggetto [**PdfSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions/). Ecco un esempio in Java:

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.java" >}}

Il risultato dell'output:
<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="java" >}}
