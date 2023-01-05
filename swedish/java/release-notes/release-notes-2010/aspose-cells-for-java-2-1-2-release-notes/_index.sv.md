---
title: Aspose.Cells for Java 2.1.2 Release Notes
type: docs
weight: 90
url: /sv/java/aspose-cells-for-java-2-1-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 2.1.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-2.1.2/)

{{% /alert %}} 

 Vi är glada att meddela Aspose.Cells för Java!

 Vad har ändrats:

- Ger diagram-till-bild-funktion.
 Importerar RichText från SpreadSheetML mallfil.
 Stöder export av namnobjekt med externa referenser för SpreadSheetML-fil.
Exporterar bilder i PageSetup för Excel 2007-filer.
 Importerar TextBox-kontroller från Excel 2007-filer.
 Ger stöd för att ställa in postgräns vid import av data från ResultSet for Smart Markers.
 Ställer in positionen för en form till mitten av ett givet område.
 Stöder för att lägga till beräknat fält för en pivottabell.
 Stöder för att få/ställa in VeryHidden-egenskapen för ett kalkylblad.
 Lägger till ny formel till listan med formler som stöds: FREKVENS
 Känner igen filformatet automatiskt för LightCells API.
 Förbättrar stilens modell för prestationsövervägande.
 Förbättrar API angående Kommentar för prestationsövervägande.
 Förbättrar prestandan för att läsa stora Excel 2007-filer.
 Ökar prestanda för LightCells API för stora Excel 2007-filer.
 Läsoperationen för ett dokuments egenskaper förbättras.
 Operationen för att importera CSV-filer förbättras.
 67 korrigeringar och förbättringar.

Problem lösta i Aspose.Cells for Java 2.1.2



|**Utfärdande ID** |**Komponent** |**Sammanfattning** |
|:- |:- |:- |
|6245 | xls| Samla stilar|
|6362 | xls| Kopiera stil när du infogar rader/kolumner|
|11871 | xls| Kopiera cellintervall|
|11890 | html| Läs Villkorlig formatering|
|11891 | Diagram| LogarithmicBase-egenskapen för ValueAxis|
|11911 | SpreadSheetML| Spara stil|
|11928 | xls| Läs mallfilen|
|11943 | SpreadSheetML| Läs specialfil genererad av OWC|
|11973 | SpreadSheetML| Läs specialfil genererad av OWC|
|12006 |CSV | Läs csv-fil|
|12032 | FormulaEngine| COUNTIF formel|
|12034 | xls| Autopassa kolumner|
|12056 | FormulaEngine| IF formel|
|12080 | Diagram| Formaterat värde för ChartFrame|
|12105 | xls| Läs radhöjd|
|12128 | Diagram| Skaffa markör|
|12138 | Diagram| Läs markör|
|12184 | xls| Kopiera formler|
|12229 | SpreadSheetML| Läs rik text|
|12238 | xlsx| Prestanda för att läsa mallfil|
|12238 | xlsx| Prestanda för att läsa mallfil|
|12243 | Diagram| ASeries typ|
|12253 | xls| Hyperlänkens länktyp|
|12271 | Diagram| Dataetiketter|
|12275 | xls| LightCells|
|12317 | Diagram| Titelns text|
|12324 | Chart2Image| ImageOption|
|12347 | SpreadSheetML| Hyperlänk|
|12434 | Diagram| GradientFill|
|12477 | xlsx| LightCells|
|12493 | xlsx| Läs Villkorlig formatering|
|12498 | Diagram| ChartPoints och LegendEntries-samling|
|12575 | Diagram| PlotAreas storlek|
|12576 | Diagram| ErrorBar|
|12622 | xlsx| Läs delad formel|
|12625 | xlsx| Läs diagrammet|
|12667 | xls| Datum och tid värde|
|12684 |CSV |Läs nummer|
|12717 | xls| Bild med Mac OS|
|12727 | xls| Läs dokumentegenskaper|
|12750 | xls| Få hyperlänk av form|
|12870 | xlsx| Läs ritobjekt|
|12880 | Chart2Image| Rita diagram|
|12894 | Pivottabell| addCalculateField() metod|
|12915 | xlsx| Spara strängvärde|
|12957 | SpreadSheetML| Spara dokumentegenskaper|
|12971 | xls| VeryHidden egenskap hos kalkylbladet|
|13012 | Chart2Image| Ej stödd teckensnitt i speciell miljö|
|13101 | xlsx| Läs PageSetup och stil|
|13270 | xls| Positionsform|
|13385 | xls| Kopiera AutoFilter|
|13386 | xlsx| Spara xlsx-filen|
|13403 | xls| Spara stil|
|13418 | xls| Läs AutoFilter|
|13448 | Smart markör| Rekordgräns för ResultSet-datakälla|
|13614 | xlsx| Bild i PageSetup|
|13639 | xls| Skapa textruta|
|13679 | xlsx| Läs xlsx-fil med Apache zip-verktyg|
|13725 | Diagram| Kopiera Axis|
|13735 | xls| Formler för formatvillkor/valideringar|
|13736 | xls| Datumformat|
|13821 | xls| Prestanda för att skapa kommentar|
|14056 | Diagram| Gradientfyllning|
|14108 | xls| Kopiera PageBreaks|
|14116 | xls| Ta bort data|
|14146 | Chart2Image| Chart2Image|
|14246 | xls| Kopiera PageSetup|


 Anmärkningsvärda förändringar för användare:



 gamla versioner kan metoderna Cell.getStyle()/Row.getStyle()/Column.getStyle() orsaka att Cell/Row/Column behåller sitt eget Style-objekt. Ändring av det returnerade Style-objektet för getStyle() senare kommer att ändra Cell/Row/Columns stil direkt.

 Från den här versionen kommer alla Style-objekt som är inställda på Cell/Row/Column att samlas in för prestandaöverväganden och Cell/Row/Column kommer endast att behålla en stilreferens. Ändring av det returnerade Style-objektet för getStyle() senare kommer inte att ändra stilen för Cell/Row/Column. För att ändringen ska träda i kraft måste användare anropa setStyle() för Cell/Row/Column efter att stilen har ändrats.

Den här regeln krävs också för metoderna Style.getFont()/getColor()/getPatternColor()/getBorderColor(). I gamla versioner kan modifiering av det returnerade Font/Color-objektet orsaka att stilen ändras direkt. I den nya versionen, efter att ha gjort ändringar för Font/Color-objektet, måste användare anropa Style.setFont()/setColor()/setPatternColor()/setBorderColor() för att ändringen ska träda i kraft.
