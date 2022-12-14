---
title: Aspose.Cells för Java 8.7.0 Release Notes
type: docs
weight: 140
url: /sv/java/aspose-cells-for-java-8-7-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells för Java 8.7.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.7.0/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSJAVA-41672) - Exponera API för egenskapen "Ändra storlek på form för att passa text" för diagrammets dataetiketter

 (CELLSJAVA-41655) - Cells.importCSV() metod som inte känner igen formler


## **Förbättringar**


 (CELLSJAVA-41680) - API återger det ryska månadsnamnet annorlunda före och efter anropet calculateFormula-metoden

 (CELLSJAVA-41673) - Aspose.Cells läser inget från Excel-arket i mallfilen


## **Buggar**


 (CELLSJAVA-41685) - Diagrambilder har en storlek på 0 KB vid konvertering av kalkylblad till HTML

 (CELLSJAVA-41684) - Diagrambild saknas i HTML

 (CELLSJAVA-41676) - HTML-utdata ger oförutsägbara resultat

 (CELLSJAVA-41665) - Bilden i kalkylbladet exporteras inte till HTML

 (CELLSJAVA-41632) - Problem med datumjustering vid konvertering från EXCEL till HTML och tillbaka till EXCEL

(CELLSJAVA-41603) - Fel bakgrundsfärg för celler visas vid export av ett cellintervall till html

 (CELLSJAVA-41337) - Konvertering till HTML genererar en väldigt stor HTML-fil

 (CELLSJAVA-41705) - Textfärg återges inte korrekt i HTML i Excel-tabeller

 (CELLSJAVA-41647) - Hyperlänk i ett ListObject som pekar på ett område blir bruten när kalkylblad konverteras till HTML

 (CELLSJAVA-41659) - Användning av namngiven stil på en cell återspeglas inte i avsnittet Stilar i Excel-gränssnittet

 (CELLSJAVA-41602) - Cell.calculate()-metoden fungerar inte korrekt för en specifik cell

 (CELLSJAVA-41645) - ListObjects huvudteckensnittsfärg försvinner under kopiering av intervall

 (CELLSJAVA-41707) - Textfärgen återges inte korrekt i bilden av Excel-tabeller

 (CELLSJAVA-41688) - Utgåva med hebreisk karaktär i rubriken

 (CELLSJAVA-41666) - DataBars gräns är inte densamma som i Excel vid rendering till bild

 (CELLSJAVA-41662) - Kant saknas vid rendering av DataBar till bild

(CELLSJAVA-41548) - DataBar till bild: DataBar-storleken i bilden motsvarar inte Excel

 (CELLSJAVA-41250) - Arket återges inte korrekt med SheetRender.toImage()

 (CELLSJAVA-41701) - Plot Area höjd & Plot Area Y-värden är olika efter att ha laddat om diagrammet från kalkylbladet

 (CELLSJAVA-41699) - Konvertering av diagram till bild - Diagrambild är inte korrekt återgiven eftersom stapelstorlekar visar olika

 (CELLSJAVA-41689) - Kantutjämning verkar inte träda i kraft för diagrammets seriefyllning vid export till HTML

(CELLSJAVA-41686) - RenderingHints.VALUE_TEXT_ ANTIALIAS_GASP träder inte i kraft när kalkylark konverteras till HTML

 (CELLSJAVA-41678) - Felaktiga färger återges i diagrammets PDF

 (CELLSJAVA-41669) - Alla staplar visas under 0-värdesregeln i diagrammets PDF

 (CELLSJAVA-41667) - Klustrade stapeldiagram visas inte i PDF-filformatet

(CELLSJAVA-41660) - Tjockleken på X-axeln och Y-axeln ökar i diagrammets PDF

 (CELLSJAVA-41657) - Bubbeldiagram visas inte korrekt när det konverteras till bild

 (CELLSJAVA-41656) - Diagramserievärde visas i en vinkel

 (CELLSJAVA-41646) - nedre delen av X-axeln i diagrammets PDF trimmas

 (CELLSJAVA-41644) - Axeletiketter visas lutade medan diagram renderas till PDF

 (CELLSJAVA-41628) - Inriktning av rubrik inte korrekt i diagram till PDF

 (CELLSJAVA-41623) - Några dataseriestaplar saknas i diagrammets PDF med Chart.toPdf

 (CELLSJAVA-41468) - Diagrammets kvalitetsproblem - Kantutjämning träder inte i kraft utan skugga

 (CELLSJAVA-41445) - Bubbeldiagram har ingen kantutjämningseffekt i det renderade HTML-filformatet

(CELLSJAVA-41306) - Excel till PDF-konverteringsproblem - höger sida avskuren

 (CELLSJAVA-41697) - Fel teckensnittsfärg visas för tabeller och intervall i det genererade HTML/Image/PDF-formatet

(CELLSJAVA-41679) - Worksheet.getProtection().getPasswordHash() returnerar 0 efter omskydd med makrokod

 (CELLSJAVA-41675) - Bilden är inte transparent i utdata-pdf

 (CELLSJAVA-41671) - Felaktig återgivning av villkorligt formaterade Cell-färger i resulterande PDF

 (CELLSJAVA-41663) - Spara villkorlig formateringsikonbilddata till filresultat i tom bild

 (CELLSJAVA-41661) - Processen fastnar när du laddar och konverterar till xlsx-fil från xml

 (CELLSJAVA-41597) - Oläsbart innehåll i Excel 2007 efter att XLSB har sparats på nytt


## **Undantag**


 (CELLSJAVA-41592) - Nullpointer när du försöker spara excelark som html



\2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSJAVA-41598) - Efter att ha laddat mallfilen till GridWeb och klickat på Reload-knappen flera gånger, ökar minnet


## **Public API och bakåtinkompatibla ändringar**


 Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.



 Lägger till egenskapen TxtLoadOptions.HasFormula.

 Indikerar om csv-filen innehåller formel.



 Lägger till egenskapen ColorScale.Is3ColorScale.

 Anger om villkorlig formatering är 3 färgskala.



Tar bort föråldrad Workbook.SaveOptions-egenskap.

 Använd metoden Workbook.Save(Stream,SaveOptions) eller Workbook.Save(string,SaveOptions) istället.



 Lägger till metoden Protection.VerifyPassword.

 Verifierar lösenordet för kalkylbladets skydd.



 Lägger till egenskapen Proptection.IsProtectedWithPassword.

 Indikerar om kalkylbladet är skyddat med lösenord.



 Lägger till egenskapen PdfSaveOptions.OptimizationType.

 Hämtar och ställer in pdf-optimeringstyp.





 Notera

 Eftersom kodbasen för Aspose.Cells för Java matchar koden för relevant .NET-version, ingår de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells för .NET v8.7.0 också i denna Aspose.Cells för Java v8.7.0.
