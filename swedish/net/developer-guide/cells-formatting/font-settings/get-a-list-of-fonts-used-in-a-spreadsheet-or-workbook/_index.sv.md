---
title: Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok
type: docs
weight: 20
url: /sv/net/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---
## **Möjliga användningsscenarier**

Det är ofta nödvändigt att känna till de typsnitt som används i din arbetsbok för renderingsändamål. När du konverterar din arbetsbok till PDF eller bild, kräver Aspose.Cells att alla nödvändiga teckensnitt är installerade på ditt system eller finns i din**teckensnittskatalog**Om Aspose.Cells inte kan hitta det önskade teckensnittet, försöker den ersätta det med något annat lämpligt teckensnitt som finns på ditt system eller i din teckensnittskatalog och kan ersätta ditt faktiska teckensnitt. Detta resulterar inte bara i oönskad rendering av PDF eller bilder utan tar också bearbetningstid för att hitta lämpliga typsnitt.

För att hantera sådana fall bör du veta vilka typsnitt som används av din arbetsbok och sedan antingen installera dessa typsnitt på ditt system i fallet med Windows-miljön eller placera det i din typsnittskatalog i fall av Windows- eller Linux-miljö.

 Aspose.Cells tillhandahåller**[Workbook.GetFonts](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/getfonts)**metod som returnerar listan över alla teckensnitt som används i din arbetsbok eller kalkylblad.

## **Få en lista över teckensnitt som används i ett kalkylblad eller en arbetsbok**

 Följande exempelkod laddar källexcelfilen och hämtar listan över teckensnitt som används i den. Den har ett dummy-arbetsblad som har några dummy-teckensnitt som lagts till för illustrationsändamål. När koden skriver ut alla teckensnitt i arbetsboken, skriver den också ut dessa dummy-teckensnitt. Följande skärmdump visar[exempel på excel-fil](25395211.xlsx)och hur dummy-teckensnitten är listade.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Fonts-GetListOfFontsUsedInSpreadsheetOrWorkbook.cs" >}}

## **Konsolutgång**

 Här är konsolutgången för ovanstående exempelkod när den körs med den givna[exempel på excel-fil](25395211.xlsx).

{{< highlight "java" >}}

Aspose.Cells.Font [ Calibri; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Arial; 10; Regular; Color [A=255, R=0, G=0, B=0]]

Aspose.Cells.Font [ Calibri; 10; Bold; Color [Black]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=128, G=128, B=128]]

Aspose.Cells.Font [ Calibri; 10; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 36; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Calibri; 11; Italic; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Bold; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 16; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 12; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=41, G=74, B=78]]

Aspose.Cells.Font [ Calibri; 11; Bold; Color [A=255, R=255, G=255, B=255]]

Aspose.Cells.Font [ Dummy-Arial-X; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Y; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Arial-Z; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-I; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-II; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Dummy-Times-III; 11; Regular; Color [Black]]

Aspose.Cells.Font [ Calibri; 10.5; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 20; Regular; Color [A=255, R=55, G=98, B=104]]

Aspose.Cells.Font [ Calibri; 11; Regular; Color [A=255, R=55, G=98, B=104]]

{{< /highlight >}}
