---
title: Få en lista över de typsnitt som används i ett kalkylblad eller arbetsbok
description: Aspose.Cells är ett Python bibliotek för att arbeta med kalkylbladsfiler. Det stöder att få en lista över de typsnitt som används i ett kalkylblad eller arbetsbok, vilket gör det möjligt för användare att få information om typsnitt som används i ett dokument. Denna artikel visar hur du använder Aspose.Cells för Python via .NET biblioteket för att få en lista över typsnitt.
keywords: Aspose.Cells för Python via .NET, Kalkylblad, Arbetsbok, Typsnitt, Lista
type: docs
weight: 20
url: /sv/python-net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Möjliga användningsscenario**

Det är ofta nödvändigt att känna till vilka typsnitt som används i ditt arbetsblad för rendering. När du konverterar ditt arbetsblad till PDF eller bild kräver Aspose.Cells för Python via .NET att alla nödvändiga typsnitt är installerade på ditt system eller finns i din **typsnitts-mapp**. Om Aspose.Cells för Python via .NET inte kan hitta det nödvändiga typsnittet försöker den ersätta det med ett annat lämpligt typsnitt som finns på ditt system eller i din typsnitts-mapp och kan ersätta ditt faktiska typsnitt. Detta kan inte bara leda till felaktig rendering av PDF eller bilder, men också ta tid att hitta lämpliga typsnitt.

För att hantera sådana fall bör du veta vilka typsnitt som används av din arbetsbok, sedan antingen installera dessa typsnitt på ditt system vid Windows-miljö eller placera dem i din typsnittskatalog vid Windows- eller Linux-miljö.

Aspose.Cells för Python via .NET erbjuder metoden [**Workbook.get_fonts**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/get_fonts), som returnerar listan över alla typsnitt som används i din arbetsbok eller kalkylblad.

## **Få en lista över typsnitt som används i en kalkylblad eller arbetsbok**

Följande kodprov laddar den ursprungliga excelfilen och hämtar listan över använda typsnitt i den. Den har ett dumt arbetsblad med några dumma typsnitt tillagda i illustrativt syfte. När koden skriver ut alla typsnitt i arbetsboken, skrivs också dessa dumma typsnitt ut. Följande skärmdump visar [provningsexcelfilen](25395211.xlsx) och hur de dumma typsnitten listas.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-GetListOfFontsUsedInSpreadsheetOrWorkbook.py" >}}

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

