---
title: Få en lista över de typsnitt som används i ett kalkylblad eller arbetsbok
type: docs
weight: 20
url: /sv/java/get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook/
---

## **Möjliga användningsscenario**

Det är ofta nödvändigt att veta vilka fonter som används i din arbetsbok för rendering. När du konverterar din arbetsbok till PDF eller bild, kräver Aspose.Cells att alla nödvändiga fonter är installerade på ditt system eller finns i din **fontkatalog**. Om Aspose.Cells inte hittar den nödvändiga fonten försöker den ersätta den med någon annan lämplig font som finns på ditt system eller i din fontkatalog och kan ersätta din faktiska font. Detta resulterar inte bara i oönskad rendering av PDF eller bilder utan tar också tid för att hitta lämpliga fonter.

För att hantera sådana fall bör du veta vilka fonter som används av din arbetsbok, sedan antingen installera dessa fonter på ditt system i fall av Windows miljö eller placera dem i din fontkatalog i fall av Windows- eller Linuxmiljö.

Aspose.Cells tillhandahåller [Workbook.getFonts()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#getFonts--) metoden som returnerar listan över alla fonter som används i din arbetsbok eller kalkylblad.

## **Få en lista över typsnitt som används i en kalkylblad eller arbetsbok**

Följande kodexempel laddar käll-excelfilen och hämtar listan över använda fonter i den. Den har ett dummy-ark som har några dummyfonter tillagda för illustrationssyfte. När koden skriver ut alla fonter i arbetsboken skrivs även dessa dummyfonter ut. Följande skärmbild visar [provexelfilen](sampleGetFonts.xlsx) och hur de dummyfonterna listas.

![todo:image_alt_text](get-a-list-of-fonts-used-in-a-spreadsheet-or-workbook_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetFontsUsedinWorkbook-GetFontsUsedinWorkbook.java" >}}

## **Konsoloutput**

Här är konsoloutputen av ovanstående provkod vid körning med den givna [provexelfilen](sampleGetFonts.xlsx).

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
