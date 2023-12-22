---
title: Ottieni un elenco di caratteri utilizzati in un foglio di calcolo o in una cartella di lavoro
description: Aspose.Cells è una libreria .NET per lavorare con file di fogli di calcolo. Supporta l'ottenimento di un elenco di caratteri utilizzati in un foglio di calcolo o in una cartella di lavoro, consentendo agli utenti di ottenere informazioni sui caratteri utilizzati in un documento. Questo articolo ti mostrerà come utilizzare la libreria Aspose.Cells per ottenere un elenco di caratteri.
keywords: Aspose.Cells, Spreadsheet, Workbook, Font, List
type: docs
weight: 20
url: /it/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
##  **Possibili scenari di utilizzo**

Spesso è necessario conoscere i caratteri utilizzati nella cartella di lavoro per scopi di rendering. Quando converti la cartella di lavoro in PDF o immagine, Aspose.Cells richiede che tutti i caratteri necessari siano installati sul tuo sistema o presenti nella *directory dei caratteri**. Se Aspose.Cells non riesce a trovare il carattere necessario, tenta di sostituirlo con un altro carattere adatto presente nel tuo sistema o nella directory dei caratteri e può sostituire il carattere attuale. Ciò non solo provoca la resa indesiderata di PDF o immagini, ma richiede anche tempo di elaborazione per trovare i caratteri adatti.

Per gestire questi casi, dovresti sapere quali caratteri vengono utilizzati dalla tua cartella di lavoro, quindi installare tali caratteri sul tuo sistema in caso di ambiente Windows o inserirli nella directory dei caratteri in caso di ambiente Windows o Linux.

 Aspose.Cells fornisce il**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**metodo che restituisce l'elenco di tutti i caratteri utilizzati nella cartella di lavoro o nel foglio di calcolo.

##  **Ottieni un elenco di caratteri utilizzati in un foglio di calcolo o in una cartella di lavoro**

 Il seguente codice di esempio carica il file Excel di origine e recupera l'elenco dei caratteri utilizzati al suo interno. Ha un foglio di lavoro fittizio a cui sono stati aggiunti alcuni caratteri fittizi a scopo illustrativo. Quando il codice stampa tutti i caratteri all'interno della cartella di lavoro, stampa anche i caratteri fittizi. La seguente schermata mostra il[file Excel di esempio](25395211.xlsx) e come sono elencati i caratteri fittizi.

![cose da fare:immagine_alt_testo](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

##  **Uscita della console**

 Ecco l'output della console del codice di esempio precedente quando eseguito con il comando dato[file Excel di esempio](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0] ]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128] ]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78] ]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255] ]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black] ]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104] ]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104] ]

{{< /highlight >}}
