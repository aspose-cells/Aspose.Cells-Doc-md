---
title: Aspose.Cells for Java 8.5.0 Release Notes
type: docs
weight: 50
url: /sv/java/aspose-cells-for-java-8-5-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.5.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.0/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSJAVA-41335) - Förbättra PasteOptions/PasteType-mekanismen för att tillåta kopiering av radhöjder medan du kopierar intervall

 (CELLSJAVA-41053) - Omräkning av skalfaktorn för sidinställningar


## **Förbättringar**


 (CELLSJAVA-41334) - HYPERLINK formel/funktion - Tillåt användaren att bearbeta parametrar för hyperlänk

 (CELLSJAVA-41357) - CELLSJAVA-41225 Fel bakgrundsfärg returneras av Aspose.Cells


## **Buggar**


 (CELLSJAVA-41366) - Kalkylblad skadat efter att ha öppnat och sparat mallen XLSX-fil

(CELLSJAVA-41355) - Konvertering till HTML lägger till # sträng i slutet av värden för en kolumn

 (CELLSJAVA-41354) - Siffror i textrutorna visas inte inuti

 (CELLSJAVA-41353) - De smarta konsternas placering/justering i PDF:en matchar inte källfilen i Excel

 (CELLSJAVA-41343) - Bottom line är mycket längre än originalet i mallfilen

 (CELLSJAVA-41342) - Data flyttade till höger i mallfilen

 (CELLSJAVA-41341) - Text överlappas med vit bakgrund i mallfilen

 (CELLSJAVA-41340) - Cell justering är till vänster istället för höger i mallfil

 (CELLSJAVA-41339) - Text- och textjustering är förstörd i mallfilen

 (CELLSJAVA-41336) - JavaScript-fel vid export till HTML

 (CELLSJAVA-41327) - Förlust av text i mallfil

 (CELLSJAVA-41326) - Förlust av text i mallfil

 (CELLSJAVA-41304) - Misslyckade konverteringar från XLS till PDF med Aspose.Cells API:er

(CELLSJAVA-41206) - Konvertera Excel-fil som innehåller hyperlänkar till HTML - Cell refererade hyperlänkar fungerar inte

 (CELLSJAVA-40483) - Problem med formateringen av en pilform/-objekt - Excel till PDF-rendering

 (CELLSJAVA-41372) - Gantt-diagram renderas inte i utdata-PDF-filformatet

 (CELLSJAVA-41363) - Problem med de returnerade värdena för parametrar vid beräkning av anpassad funktion

 (CELLSJAVA-41345) - Anpassad funktion som involverar Excel-formel (INDIREKT) misslyckas

 (CELLSJAVA-41320) - Problem med värdet som tas emot i en CustomFunction

 (CELLSJAVA-40734) - Problem med RefferedArea som ett resultat av parameterns beräkning

 (CELLSJAVA-41370) - När en arbetsbok instansieras med ett skadat Excel-dokument och LoadOptions, uppstår hängning

 (CELLSJAVA-41369) - Problem med autofilter på formler

 (CELLSJAVA-41348) - Villkorsformat med nummerformat fungerar inte för XLS

 (CELLSJAVA-41347) - Style.isDateTime returnerar false för en cell formaterad som Date

(CELLSJAVA-41338) - Vänster kant som visas när den inte borde för en cell som har en intilliggande dold kolumn

 (CELLSJAVA-41331) - Formler uppdateras inte korrekt efter infogningsrader

 (CELLSJAVA-41330) - Dynamiskt utskriftsområde brutet när du sparar som / skriv ut PDF

 (CELLSJAVA-41365) - Några hebreiska tecken i textrutan saknas i utdata-PDF-filen

 (CELLSJAVA-41346) - Etiketterna för värdeaxeln och kategoriaxeln i diagrammet är svarta (Excel till PDF-konvertering)

 (CELLSJAVA-41312) - Texten är för stor och expanderar utanför marginalen

 (CELLSJAVA-41305) - Fet texttecken överlappar varandra medan kalkylblad konverteras till bild

 (CELLSJAVA-40916) - Texten utanför sidbrytningen renderas i PDF som radbruten text

 (CELLSJAVA-40791) - Problem med sidbrytning, teckensnittsrendering och marginaler i Excel till PDF-rendering

 (CELLSJAVA-40605) - Aspose.Cells: avskuren text i originalcellen visas helt när den konverteras till PDF

(CELLSJAVA-40479) - Återgivning av problem med sidlayout (RTL).

 (CELLSJAVA-40448) - Sidfoten är förstörd i den genererade PDF-filen

 (CELLSJAVA-41359) - En liten prick visas i mitten av cirkeldiagrammet medan du sparar den i bild

 (CELLSJAVA-41358) - Diagram brukade acceptera en serieformel med tomma värden men nu ger det undantag

 (CELLSJAVA-41356) - Återgivningsproblem vid konvertering av diagram till bild

 (CELLSJAVA-41351) - Problem med diagramaxeletiketternas bredd vid konvertering av Excel-kalkylblad till bild

 (CELLSJAVA-40607) - Problem med egenskaper för diagramdataetikett

 (CELLSJAVA-40613) - Cirkeldiagram procentuellt problem


## **Undantag**


 (CELLSJAVA-41377) - Undantag när cell.getPrecedents anropas

 (CELLSJAVA-41361) - java.lang.NumberFormatException: För inmatningssträng: "0,00" i Workbook ctor

 (CELLSJAVA-41344) - java.lang.NullPointerException på Cells.find


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



 Lägger till enum PasteType.RowHeights

 Den används för att kopiera höjderna på området.



Lägger till egenskapen SheetRender.PageScale.

 Det används för att få beräknad sidskala på arket.



 Lägger till metod Cell.GetStingValue(CellValueFormatStrategy).

 Det används för att få strängvärdet för cellen genom specifik formaterad strategi.



 Lägger till egenskap ExportTableOptions.FormatStrategy.

 Hämtar och ställer in formatstrategin när värdet exporteras som strängvärde.



 Lägger till klassberäkningsalternativ.

 Representerar alternativ för beräkning av formler.



Lägger till metoder för att beräkna formler med CalculationOptions: Cell.Calculate(CalculationOptions),
 Workbook.CalculateFormula(CalculationOptions), Worksheet.CalculateFormula(CalculationOptions-alternativ, bool rekursiv).

 Tillåt användaren att beräkna formler med mer flexibla och utbyggbara alternativ.



 Lägger till metoder: ReferredArea.GetValues(),ReferredArea.GetValue(int rowOffset, int colOffset)

 Tillåt användaren att hämta data från en referens.



Ändringar för parametrar för ICustomFunction.CalculateCustomFunction(strängfunktionsnamn, ArrayList paramsList, ArrayList contextObjects)

 Nu lägger vi till ReferredArea-objektet i "paramsList" istället för värdet eller värdematrisen för det refererade området när motsvarande parameter är en referens eller dess beräknade resultat är referens. Och vi tar bort ReferredAreaCollection från contextObjexts.





 Notera

 Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.5.0 också inkluderade i denna 076157316.0.481.
