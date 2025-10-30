---
title: Ottieni un elenco di font utilizzati in un foglio di calcolo o in un workbook
linktitle: Ottieni un elenco di font utilizzati in un foglio di calcolo o in un workbook
description: Impara come ottenere una lista dei caratteri usati in un foglio di calcolo o in un workbook usando Aspose.Cells for Node.js via C++. Questo articolo mostrerà come recuperare informazioni sui caratteri da un documento.
keywords: Aspose.Cells, Node.js tramite C++, Foglio di calcolo, Workbook, Carattere, Elenco
type: docs
weight: 20
url: /it/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Possibili Scenari di Utilizzo**

È spesso necessario conoscere i font utilizzati nel tuo workbook per scopi di rendering. Quando converti il tuo workbook in PDF o immagine, allora Aspose.Cells richiede che tutti i font necessari siano installati sul tuo sistema o presenti nella tua **directory dei font**. Se Aspose.Cells non è in grado di trovare il font necessario, cerca di sostituirlo con qualche altro font adatto presente sul tuo sistema o nella tua directory dei font e può sostituire il tuo font effettivo. Questo non solo comporta il rendering indesiderato di PDF o immagini ma richiede anche tempo di elaborazione per trovare font adatti.

Per gestire tali casi, dovresti sapere quali caratteri sono usati dal tuo workbook, poi installarli sul sistema in caso di ambiente Windows o collocarli nella directory dei caratteri in caso di ambiente Windows o Linux.

Aspose.Cells for Node.js via C++ fornisce il metodo [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--) che restituisce l'elenco di tutti i caratteri usati nel tuo workbook o foglio di calcolo.

## **Ottieni un elenco di font utilizzati in un foglio di calcolo o di lavoro**

Il codice di esempio seguente carica il file excel di origine e recupera l'elenco di font utilizzati al suo interno. Ha un foglio di lavoro fittizio al quale sono stati aggiunti alcuni font fittizi a scopo illustrativo. Quando il codice stampa tutti i font all'interno del workbook, stampa anche quei font fittizi. La schermata seguente mostra il [file excel di esempio](25395211.xlsx) e come sono elencati i font fittizi.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


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
{{< app/cells/assistant language="nodejs-cpp" >}}
