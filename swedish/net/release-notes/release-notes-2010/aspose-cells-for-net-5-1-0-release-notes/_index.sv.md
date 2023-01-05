---
title: Aspose.Cells for .NET 5.1.0 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-5-1-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 5.1.0](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-5.1.0/)

{{% /alert %}} 

 Vi är glada att meddela Aspose.Cells for .NET v!

 Vad har ändrats i Aspose.Cells:

- Inkluderar stöd för Smart Tags för XLSX-filer.
 Konverterar Sparklines till bilder.
 Ger stöd för smarta bildmarkörer.
 Stöder Cells gradientfyllningar och tema för XLS-filen.
 Render Cells mönster fyller i den genererade PDF-filen.
 Lägger till stöd för Pdf/A-1b-kompatibilitet.
 Förbättrar prestanda och kvalitet på de genererade PDF-filerna.
 46 förbättringar och korrigeringar.

 Vad har ändrats i Aspose.Cells.GridWeb:

- Konverterar hierarkiska anpassade samlingar till Dataset som innehåller relationer.

 1 fix.



 Vad har ändrats i Aspose.Cells.GridDesktop:

- Inkluderar Scroll-händelse.

Tillhandahåller en överbelastad version för metoden SumSelectedRanges för att utesluta dolda celler.

 1 fix.

 Problem lösta i Aspose.Cells for .NET v

|**Utfärdande ID** |**Komponent** |**Sammanfattning** |
|:- |:- |:- |
|17474 | GridWeb| Kanter återges inte för de sammanslagna cellerna|
|15467 | GridDesktop| Ändrar dubblettkalkylbladets namn i metoden ImportExcelFile|
|17581 | Chart2Image| Konverterar diagram till bild|
|17762 | Chart2Image| Datatabeller, värden och kategori går förlorade för XY-spridningsgrafer|
|17900 | Chart2Image|Excel diagram till bild problem|
|18023 | Chart2Image| Bubbeldiagram|
|18190 | Chart2Image| Aspose.Cells kastar ut minnesundantag i Azure|
|18012 |CSV | Exportera annorlunda till Excel|
|16207 | Pdf| Hitta fel när PDF-filen sparades|
|17535 | Pdf| Ett teckensnitt i XLSX resulterar i två teckensnitt i PDF|
|17537 | Pdf| Valutaformaterade tomma celler|
|17776 | Pdf| Problem med att konvertera Excel till PDF|
|17804 | Pdf| Decimalvärden visas inte om endast nollor finns där|
|17821 | Pdf| Inbyggda fastigheter|
|17981 | Pdf| Excel till PDF Konverteringsproblem|
|18021 | Pdf| Sparar till PDF - Problem med teckensnitt|
|18038 | Pdf| PDF dokument verkar vara skadat|
|18136 | Pdf| Fråga om att spara PDF|
|18258 | Pdf| Beräknade formler uppdateras inte vid konvertering från Cells till PDF|
|18316 | Pdf| Konverteringsproblem med data som visas som nummertecken|
|18258 | Pdf| Beräknade formler uppdateras inte vid konvertering från Cells till PDF|
|18316 | Pdf| Konverteringsproblem med data som visas som nummertecken|
|18239 |SpreadsheetML | Ogiltigt undantag för slutkolumnindex|
|17111 | Arbetsblad 2 Bild| Formaterar inte numeriska data korrekt|
|17633 | Arbetsblad 2 Bild| Rad i grafik inte konverterad|
|17903 | Arbetsblad 2 Bild| Prestanda för kalkylblad2bild|
|18310 | Arbetsblad 2 Bild| Inget svar från SheetRender|
|17656 | xls| Hur man hittar grupperade rader och kolumner|
|17761 | Xls| Beräkna externa formler|
|17789 | Xls| Formel för villkorlig formatering|
|17810 | Xls|Räckvidden fungerar felaktigt|
|17820 | Xls| Den här filen skapades med en senare version|
|17907 | Xls| Att sortera inom grupper fungerar inte|
|17954 | Xls| Shape.AlternativeText|
|17999 | Xls| Stöder tillägg av Tif-bild med metoden Pictures.Add().|
|18054 | Xls| Worsheet.Copy kopplar CPU till 100 %|
|18135 | Xls| Stöder PageLayoutView|
|18160 | Xls| Kompatibilitetsproblem med MS Excel|
|18297 | Xls| Felaktig formel(Cell.formula och ExternalLink)|
|18366 | Xls| Stöder kopiering av hyperlänk inom kopieringsområdet.|
|16656 | Xlsx| Förlorade makron när du sparade i XLSM-format|
|17041 | Xlsx| Hur man ställer in transparent färg på en bild|
|17652 | Xlsx| Hur man flyttar kommandoknappen|
|17664 | Xlsx| Befintliga ändringar av villkorlig formatering|
|17719 | Xlsx| Värdet var antingen för stort eller för litet för en Int16|
|17982 | Xlsx| Pivottabellsidfält fungerar inte i Excel 2007|
|18004 | Xlsx| Delsummor ärende|
|18036 | Xlsx| Frågan om att öppna filen XLSM.|
|18161 | Xlsx| Ogiltigt undantag för slutkolumnindex med XLSX-fil|
|18356 | Xlsx| Diagramtitel med formelproblem|
 Anmärkningsvärda förändringar för befintliga användare

 den här versionen (Aspose.Cells for .NET v5.1.0) har vi bytt namn på vissa klasser av Aspose.Cells-komponenten för att rengöra API-strukturen. Vi har några insamlingsklasser men deras namn motiverar dem inte enligt .NET standarder. Så efter djupgående analyser och granskningar har vi beslutat att byta namn på några klasser. Denna förändring har några viktiga aspekter som vi måste följa. Följande är listan över klasser som har bytt namn nu.
