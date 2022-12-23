---
title: Aspose.Cells for Java 8.6.2 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-8-6-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.6.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.6.2/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSJAVA-41144) - Möjlighet att ta bort Style från StyleCollection


## **Buggar**


 (CELLSJAVA-41554) - Bild saknas vid konvertering från HTML till EXCEL-format

(CELLSJAVA-41549) - XLSB skadad i Excel 2010 efter att ha sparats av Aspose.Cells v8.6.1

 (CELLSJAVA-41530) - Klassisk pivottabell layoutinställning förlorade när mallen XLSB sparades på nytt

 (CELLSJAVA-41558) - Genomsnittliga villkorliga format Få tillagda formler

 (CELLSJAVA-41546) - Workbook.calculateFormula-metoder fastnar på obestämd tid

 (CELLSJAVA-41544) - Problem med japanskt datumformat vid konvertering från "XML Spreadsheet 2003" till XLSX

 (CELLSJAVA-41543) - Problem med CODE()-funktionen för ryska bokstäver

 (CELLSJAVA-41541) - Teckenstorleken bevaras inte vid konvertering av XML Spreadsheet 2003 till andra format

 (CELLSJAVA-41538) - Om du sparar kalkylarket på nytt tar du bort några egenskaper från sheet1.xml för controlPr-taggen

 (CELLSJAVA-41567) - Problem med webdings-teckensnitt i Excel till PDF-renderingar

 (CELLSJAVA-41559) - Att spara till PDF genererar felaktiga färgskalafärger

 (CELLSJAVA-41556) - Att skriva ut Aspose.Cells genererade PDF ändrar den inbäddade streckkoden till viss del

(CELLSJAVA-41552) - Bredd och höjd på ett roterat textvärde verkar vara felaktigt

 (CELLSJAVA-41578) - Diagram till PDF genereras inte precis efter att metoden chart.toPdf(fileName) har körts

 (CELLSJAVA-41574) - Avståndsproblem mellan Y-axeln och Legends

 (CELLSJAVA-41557) - Skillnaden mellan axeletikettens tickmarkeringar ändras från 10 till 20 medan diagrammet renderas till PDF

 (CELLSJAVA-41553) - Diagramfärger visar stora förändringar i PDF-utgången

 (CELLSJAVA-41539) - vertikalt axelområde matchar inte källdiagrammet när kalkylbladet renderas till PDF

 (CELLSJAVA-41536) - Problem med formerna på serielinjen i diagrammet enligt MS Excel 2010/2013

 (CELLSJAVA-41533) - Avståndet mellan teckenförklaringen och axeletiketterna i diagrammet är mindre än förväntat

 (CELLSJAVA-41520) - Kartbilden skärs upp från toppen och höger sida

 (CELLSJAVA-41509) - Problem med sjökortsgränser vid rendering av diagram till PDF

(CELLSJAVA-41505) - Höger och nedre kanter trimmas när diagrammet renderas till PDF

 (CELLSJAVA-41560) - Hur man får standardfärg på kalkylbladet

 (CELLSJAVA-41542) - Problem med CheckBox-namn när CheckBoxes skapas med Aspose.Cells

 (CELLSJAVA-41469) - Stöd för kapslade smarta markörer


## **Undantag**


 (CELLSJAVA-41550) - java.lang.NullPointerException på Workbook.combine

 (CELLSJAVA-41564) - NullPointerExceptions som anropar com.aspose.cells.Row



 \2) Aspose.Cells Grid Suite


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSJAVA-41566) - Teckenstorleken är mindre än andra celler


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



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





 Notera

 Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.6.2 också inkluderade i denna 076157316.4816.4816.
