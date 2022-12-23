---
title: Aspose.Cells for Java 8.3.0 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-8-3-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.3.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.3.0/)

{{% /alert %}} 

\1) Aspose.Cells 


Andra förbättringar och förändringar

Förbättringar

(CELLSJAVA-41052) - Öka prestandan genom att cachelagra det förberedda MessageFormat-objektet
(CELLSJAVA-41050) - Ta bort eller cachelagra MessageFormat/DecimalFormat.format() för att förbättra prestandan
(CELLSJAVA-41069) - Ta bort XLA-referenser

Buggar

(CELLSJAVA-41084) - Diagramstaplar för de negativa värdena tappar färg när kalkylbladet sparas av Aspose.Cells
(CELLSJAVA-41082) - Fel vid beräkning av celler - undantag för beräkningsformel
(CELLSJAVA-41070) - HTML till XLS nummer - formaterat nummer återges som tomt
(CELLSJAVA-41034) - Textrutatext ingår inte i diagrambilden
(CELLSJAVA-41083) - Excel-funktionen NOW() fungerar inte i ryska inställningar
(CELLSJAVA-41062) - Color.getBlack().equals(Color.getEmpty()) returnerar true. Det bör returnera falskt
(CELLSJAVA-41014) - DateTime-värdet läses inte i korrekt format
(CELLSJAVA-41076) - XLA-referens togs inte bort korrekt av ExternalLink.setDataSource
(CELLSJAVA-41068) - XLSX-filen är skadad efter att ha sparat filen på nytt via Aspose.Cells API:er
(CELLSJAVA-41066) - Sjökortsaxelsteg gick sönder efter kopiering av kalkylblad
(CELLSJAVA-41060) - Om du ändrar arbetsbokens färgpalett samtidigt som du sparar XLSX till XLS får MS Excel att öppna det resulterande kalkylbladet i skyddad vy
(CELLSJAVA-41059) - Ändra i ordningen för regler för villkorlig formatering samtidigt som du sparar XLSX till XLS med Palettändring
(CELLSJAVA-41057) - Förlorade noteringar för vissa namngivna intervall
(CELLSJAVA-41056) - Cells.copyRows() metoden kopierar inte sparklines i filformatet XLSX
(CELLSJAVA-41055) - Problem med textformatering vid läsning av cellernas stilar
(CELLSJAVA-41049) - Får #VALUE! fel när RATE-funktionen används
(CELLSJAVA-41038) - Dolda serier inuti förklaringen visas igen efter att arbetsbladet har kopierats.
(CELLSJAVA-41036) - Diagramaxelsteg gick sönder när arbetsboken sparades på nytt
(CELLSJAVA-41054) - Kopiera inklistrad bild återges inte i PDF
(CELLSJAVA-41044) - Aspose.Cells genererad PDF klarar inte PDF/A-1b efterlevnadstestet
(CELLSJAVA-41015) - Aspose.Cells Genererat PD/A-1b-dokument misslyckas med preflight-valideringen
(CELLSJAVA-40951) - PDF dokumentet är trasigt och kan inte öppnas i Acrobat Reader efter konvertering från Excel-mallfil
(CELLSJAVA-40725) - Clipart visas inte i pdf
(CELLSJAVA-40692) - Överensstämmelse PDF/A-1b misslyckades med Adobe Preflight
(CELLSJAVA-41086) - Användardefinierade diagramserienamn är tomma
(CELLSJAVA-41065) - Listornas titlar är förstörda
(CELLSJAVA-41047) - Dataseparator för staplade kolumndiagram har olika tjocklek samtidigt som den renderar kalkylark till formatet PDF
(CELLSJAVA-41045) - Kolumner i diagrammet överlappar den nedre axeln medan kalkylbladet renderas till formatet PDF
(CELLSJAVA-40989) - Stapeldiagram har extra vertikala linjer till höger om staplarna när det återges som PDF
(CELLSJAVA-40988) - Diagrammets dataetikett trimmas av i den renderade PDF
(CELLSJAVA-40987) - Diagrammets axeletiketter och -förklaring överlappar i den renderade PDF
(CELLSJAVA-40945) - Textrutor försvinner från diagrammet

Undantag

(CELLSJAVA-41067) - Random CellsException: Okänt bildformat, i Workbook ctor

\2) Aspose.Cells Grid Suite

Andra förbättringar och förändringar

Nya egenskaper

(CELLSJAVA-41074) - Exportera data från GridWeb till Excel-fil eller XML-fil - GridWeb för JAVA
(CELLSJAVA-41078) - Stöd för att exportera SpreadsheetML (.xml) fil - GridWeb (JAVA)

Buggar

(CELLSJAVA-41063) - Fokuseringscell med ett enda klick och inmatning av data fungerar inte i IE8
(CELLSJAVA-41081) - Taggen för cellen visar cellvärdefel i GridWeb Logical demo
(CELLSJAVA-41073) - Bredden på rubriker för kolumner skiljer sig från bredden på celler i Chrome/Opera (GridWeb för JAVA)
(CELLSJAVA-41077) - Det reguljära uttrycket är ogiltigt i GridWeb-demo
(CELLSJAVA-41071) - Fel nummerformat i customformat.jsp
(CELLSJAVA-41079) - DateAndTime och CustomFormat-demos ger oformaterade resultat när man anger anpassat datum

Offentlig API och bakåtinkompatibla ändringar

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

 Lägger till egenskapen TxtLoadOptions.KeepExactFormat
Anger om den exakta formateringen ska behållas för cellen vid konvertering av strängvärde till nummer eller datumtid.

Uppdateringar Aspose.Cells.Pivot.PivotItemPosition enum
Uppdateringar som: Föregående, Nästa och Anpassad.

Lägger till metoden SetPositionAuto() för PlotArea.
Ställer in positionen för plotområdet som automatiskt.

Lägger till egenskapen Shape.Id
Den används för att få formens id.

Lägger till egenskapen GridDesktop.SheetTabWidth
Ställer in /får bredd på arkfliken.


Notera
Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.3.0 också inkluderade i denna 076157316.0.481.0.481.
