---
title: Aspose.Cells för .NET 8.6.2 Release Notes
type: docs
weight: 20
url: /sv/net/aspose-cells-for-net-8-6-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för .NET 8.6.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.6.2/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-43934) - Stöd smarta markörer för att acceptera en generisk lista som ett kapslat objekt


## **Buggar**


 (CELLSNET-44044) - PivotTable.ShowValuesRow har ingen effekt efter att ha flyttat DataField till kolumner

 (CELLSNET-44043) - Att öppna och spara en stor Excel-fil förstör dokumentet

 (CELLSNET-44031) - XLSB skadad i Excel 2010 efter att ha sparats i v8.6.1

 (CELLSNET-43990) - Felplacerad AutoShape när kalkylblad renderades till PDF

 (CELLSNET-43989) - Utrymmet mellan raderna med i en textruta minskas

 (CELLSNET-43901) - PivotTable WrapText inte vid uppdatering

 (CELLSNET-43808) - Pivottabellstilen går förlorad när kalkylblad kopieras till en annan arbetsbok och renderas till PDF

 (CELLSNET-43786) - Filen är skadad efter att ha uppdaterat pivottabellen i mallfilen

 (CELLSNET-43421) - Pilen återges inte korrekt när kalkylark konverteras till PDF

(CELLSNET-43391) - Problem med HTML-rendering för en tabell med en dold kolumn

 (CELLSNET-44045) - Arbetsbok.CalculateFormula-metoder fastnar på obestämd tid

 (CELLSNET-44051) - Ikoner för villkorlig formatering saknas i PDF

 (CELLSNET-44047) - Sidorna zoomas ut i den utgående PDF-filen

 (CELLSNET-44025) - Kanttjockleken bevaras inte enligt utskriftsområdet

 (CELLSNET-44002) - Bilden skalas på grund av något problem i koden

 (CELLSNET-43960) - Kan inte läsa någon lösenordsskyddad fil

 (CELLSNET-44062) - Diagrammets förklaringspost tas inte bort när datakällans kolumn är dold

 (CELLSNET-44026) - Alla ledarlinjer visas i utdatabilden för ett anpassat diagram

 (CELLSNET-44020) - Några av dataetiketterna saknas vid export av diagram till bild

 (CELLSNET-44010) - DiagramkategoriAxis lutande TickLabel-text avskuren när den konverterades till bild

 (CELLSNET-44000) - DataLabel saknas när diagrammet återges till bild

(CELLSNET-43978) - Diagram till bild genereras med extra värden

 (CELLSNET-43874) - Chart.NSeries.DataLabels nummerformat bibehålls inte vid omslagning

 (CELLSNET-44038) - Chart.ToImage() ändrar etikettens textjustering

 (CELLSNET-44009) - Diagramseriens namn ändras om data kommer från en sammanfogad cell

 (CELLSNET-44060) - Fel teckensnittsfärg efter kopiering av ark

 (CELLSNET-44056) - Spara till PDF tappar vertikala ramar

 (CELLSNET-44049) - Dolda kolumner tappar sin bredd

 (CELLSNET-44039) - Kunde inte beräkna formeln baserat på filtrerade värden i kalkylbladet

 (CELLSNET-44037) - Sammanlagd funktion resulterar i #NAME-fel tills användaren anger formelfältet

 (CELLSNET-44034) - Valideringar fungerar inte i XLSB-format

 (CELLSNET-44030) - SUMIFS Excel-funktionen fungerar inte i XLSB-format

 (CELLSNET-44007) - Duplicering av kameraobjekt i resulterande kalkylblad samtidigt som XLSB sparas på nytt

(CELLSNET-44006) - Skyddat visningsfel vid öppning av återsparad XLS

 (CELLSNET-44001) - NOW()-formeln visas inte korrekt i SpreadsheetML(XML) till PDF-konvertering

 (CELLSNET-43894) - OLE-länk ObjectSourceFullName kunde inte uppdateras

 (CELLSNET-43845) - Två fält till vänster från diagrammet gömdes som dyker upp igen efteråt


## **Undantag**


 (CELLSNET-44008) - CellsException på SheetRender.ToImage

(CELLSNET-43926) - CellsException at Workbook.CalculateFormula

 (CELLSNET-44052) - Undantag inträffade på Workbook.Save() i Excel till PDF-konvertering

 (CELLSNET-44050) - System.FormatException vid Workbook ctor



\2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-44036) - Teckensnittsfärgen är densamma för hela texten även om cellen har texter med olika färger

 (CELLSNET-44033) - Få modifierade celler i Ajax-läge på serversidan

 (CELLSNET-44014) - GridWorkSheet.SetEditableRange-metoden är inte tillgänglig i 8.6.1


## **Buggar**


 (CELLSNET-43955) - GridWeb.SaveCustomStyleFile-metoden saknas i 8.6.0

 (CELLSNET-44017) - Serialiseringsfel vid användning av SessionState Mode till "StateServer" i web.config-filen - GridWeb


## **Undantag**


(CELLSNET-43185) - SerializationException när Session-State Mode växlas till StateServer


## **Public API och bakåtinkompatibla ändringar**


Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för .NET. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.



 Lägger till WorkbookDesigner.CallBack-egenskapen och ISmartMarkerCallBack-gränssnittet.

 Representerar callback-gränssnitt för bearbetning av smart markör..



 Lägger till Cells.Stylefastighet.

 Hämtar och ställer in standardstilen för kalkylbladet.



 Lägger till metoden Chart.ToPdf(sträng filnamn).

 Sparar diagrammet till en pdf-fil.



 Lägger till metoden Workbook.RemoveUnusedStyles().

 Tar bort alla oanvända stilar från arbetsbokens stilpool.



 Lägger till AjaxCallFinished-evenemang i GridWeb

 Avfyras när ajax-uppdateringen av kontrollen är klar. (EnableAJAX ska ställas in på sant).



 Lägger till CellModifiedOnAjax-händelse i GridWeb

 Avfyras när cellen modifieras i ajaxcall.


