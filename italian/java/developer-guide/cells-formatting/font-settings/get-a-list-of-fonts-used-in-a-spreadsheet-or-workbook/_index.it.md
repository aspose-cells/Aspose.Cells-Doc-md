---
title: Ottieni un elenco di font utilizzati in un foglio di calcolo o in un workbook
type: docs
weight: 20
url: /it/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Possibili Scenari di Utilizzo**

È spesso necessario conoscere i caratteri utilizzati nel tuo foglio di lavoro per fini di rendering. Quando converti il tuo lavoro in PDF o immagine, Aspose.Cells richiede che tutti i caratteri necessari siano installati sul tuo sistema o presenti nella tua **cartella dei caratteri**. Se Aspose.Cells non riesce a trovare il carattere necessario, cerca di sostituirlo con un altro carattere adatto presente sul tuo sistema o nella tua directory dei caratteri e può sostituire il tuo carattere effettivo. Ciò non solo comporta un rendering indesiderato di PDF o immagini, ma richiede anche tempo di elaborazione per individuare caratteri adatti.

Per gestire tali casi, è necessario conoscere i caratteri utilizzati dal tuo foglio di lavoro, quindi installa quei caratteri sul tuo sistema nel caso di ambiente Windows o inseriscili nella tua directory dei caratteri nel caso di ambiente Windows o Linux.

Aspose.Cells fornisce il metodo [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) che restituisce l'elenco di tutti i caratteri utilizzati nel tuo foglio di lavoro o foglio di calcolo.

## **Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro**

Il seguente codice di esempio carica il file excel di origine e recupera l'elenco dei caratteri utilizzati al suo interno. Ha un foglio di lavoro fittizio con alcuni caratteri fittizi aggiunti a scopo illustrativo. Quando il codice stampa tutti i caratteri all'interno del foglio di lavoro, stampa anche quei caratteri fittizi. La seguente schermata mostra il [file excel di esempio](sampleGetFonts.xlsx) e come i caratteri fittizi sono elencati.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Output della console**

Ecco l'output della console del codice di esempio precedente quando eseguito con il [file excel di esempio](sampleGetFonts.xlsx) dato.

{{< highlight java >}}

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Arial; 10.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Bold; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff808080 ]

Aspose.Cells.Font [ Calibri; 10.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 36.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Calibri; 11.0; Italic; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Bold; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 16.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 12.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff294a4e ]

Aspose.Cells.Font [ Calibri; 11.0; Bold; com.aspose.cells.Color@ffffffff ]

Aspose.Cells.Font [ Dummy-Arial-X; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-I; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-II; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Dummy-Times-III; 11.0; Regular; com.aspose.cells.Color@ff000000 ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 20.0; Regular; com.aspose.cells.Color@ff376268 ]

Aspose.Cells.Font [ Calibri; 11.0; Regular; com.aspose.cells.Color@ff376268 ]

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
