---
title: Få en lista över de typsnitt som används i ett kalkylblad eller arbetsbok
linktitle: Få en lista över de typsnitt som används i ett kalkylblad eller arbetsbok
description: Lär dig hur du hämtar en lista över typsnitt som används i ett kalkylblad eller arbetsbok med Aspose.Cells for Node.js via C++. Den här artikeln visar dig hur du hämtar typsnittsinformation från ett dokument.
keywords: Aspose.Cells, Node.js via C++, Kalkylblad, Arbetsbok, Typsnitt, Lista
type: docs
weight: 20
url: /sv/nodejs-cpp/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Möjliga användningsscenario**

Det är ofta nödvändigt att veta vilka typsnitt som används i din arbetsbok för renderingsändamål. När du konverterar din arbetsbok till PDF eller bild kräver Aspose.Cells att alla nödvändiga typsnitt är installerade på ditt system eller finns i din **typsnittskatalog**. Om Aspose.Cells inte kan hitta det nödvändiga typsnittet, försöker den att ersätta det med något annat lämpligt typsnitt som finns på ditt system eller i din typsnittskatalog och kan ersätta ditt faktiska typsnitt. Detta resulterar inte bara i ogynnsam rendering av PDF eller bilder utan tar också bearbetningstid för att hitta lämpliga typsnitt.

För att hantera sådana fall bör du veta vilka typsnitt som används av din arbetsbok, antingen installera dessa typsnitt på ditt system om du använder Windows eller placera dem i din typsnittskatalog vid Windows eller Linux.

Aspose.Cells for Node.js via C++ tillhandahåller [**Workbook.getFonts**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getFonts--) metoden som returnerar listan över alla typsnitt som används i din arbetsbok eller kalkylblad.

## **Få en lista över typsnitt som används i en kalkylblad eller arbetsbok**

Följande kodprov laddar den ursprungliga excelfilen och hämtar listan över använda typsnitt i den. Den har ett dumt arbetsblad med några dumma typsnitt tillagda i illustrativt syfte. När koden skriver ut alla typsnitt i arbetsboken, skrivs också dessa dumma typsnitt ut. Följande skärmdump visar [provningsexcelfilen](25395211.xlsx) och hur de dumma typsnitten listas.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FontSettings-GetFontsListUsedInWorkbook.js" >}}


## **Konsoloutput**

Här är konsolens utmatning av det ovanstående kodprovet när det körs med den angivna [provningsexcelfilen](25395211.xlsx).

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
