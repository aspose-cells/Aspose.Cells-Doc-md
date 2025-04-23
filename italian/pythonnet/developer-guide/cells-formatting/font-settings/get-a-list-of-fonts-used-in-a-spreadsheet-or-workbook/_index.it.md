---
title: Ottieni un elenco di font utilizzati in un foglio di calcolo o in un workbook
description: Aspose.Cells è una libreria Python per lavorare con file di fogli di calcolo. Supporta l ottenimento di una lista di caratteri utilizzati in un foglio di calcolo o in un libro, permettendo agli utenti di ottenere informazioni sui caratteri utilizzati in un documento. Questo articolo mostrerà come usare la libreria Aspose.Cells per Python via .NET per ottenere una lista di caratteri.
keywords: Aspose.Cells per Python via .NET, Foglio di calcolo, Cartella di lavoro, Carattere, Elenco
type: docs
weight: 20
url: /it/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Possibili Scenari di Utilizzo**

Spesso è necessario conoscere i caratteri usati nel tuo foglio di lavoro per scopi di rendering. Quando converti il foglio di lavoro in PDF o immagine, Aspose.Cells per Python via .NET richiede che tutti i caratteri necessari siano installati sul sistema o presenti nella tua **directory dei caratteri**. Se Aspose.Cells per Python via .NET non riesce a trovare il carattere necessario, tenta di sostituirlo con un altro carattere adatto presente sul sistema o nella directory dei caratteri, che può sostituire il carattere reale. Questo può causare rendering indesiderato di PDF o immagini e richiede tempo di elaborazione per trovare i caratteri adatti.

Per affrontare tali casi, dovresti sapere quali font vengono utilizzati nel tuo workbook, quindi installare quei font sul tuo sistema in caso di ambiente Windows o collocarli nella tua directory dei font in caso di ambiente Windows o Linux.

Aspose.Cells per Python via .NET fornisce il metodo [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts) che restituisce la lista di tutti i caratteri usati nel tuo libro di lavoro o foglio di calcolo.

## **Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro**

Il codice di esempio seguente carica il file excel di origine e recupera l'elenco di font utilizzati al suo interno. Ha un foglio di lavoro fittizio al quale sono stati aggiunti alcuni font fittizi a scopo illustrativo. Quando il codice stampa tutti i font all'interno del workbook, stampa anche quei font fittizi. La schermata seguente mostra il [file excel di esempio](25395211.xlsx) e come sono elencati i font fittizi.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

## **Output della console**

Ecco l'output della console del codice di esempio sopra quando eseguito con il [file excel di esempio](25395211.xlsx) fornito.

{{< highlight java >}}

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

