---
title: Aspose.Cells for Java 8.5.2 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-8-5-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.5.2](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.5.2/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSJAVA-41374) - Lägg till konstant "Distinct Count" till ConsolidationFunction-klassen i pivottabeller


## **Förbättringar**


 (CELLSJAVA-41373) - Felaktig överensstämmelse i justeringsinställningar efter att ha sparat Excel-fil till HTML-filformat


## **Buggar**


 (CELLSJAVA-41332) - AttachedFilesDirectory och AttachedFilesUrlPrefix fungerar inte korrekt

 (CELLSJAVA-41303) - PivotField.IsRepeatItemLabels fungerar inte i pivottabellen

 (CELLSJAVA-41430) - Alternativet Sammanfoga och centrera har valts även om det har en enda cell

 (CELLSJAVA-41429) - Lotus-kompatibilitetsinställningar för inmatning av övergångsformel ändras efter att kalkylarket har sparats på nytt

 (CELLSJAVA-41427) - För många validering Cells Korrumperar XLS-filen

(CELLSJAVA-41424) - Att använda anpassad funktion via ICustomFunction-gränssnittet beräknar inte korrekt värde

 (CELLSJAVA-41423) - Fel layout vid rendering av PDF från en ODS-fil

 (CELLSJAVA-41422) - Cells.copyRows med villkorlig formatering i celler gör att filstorleken ökar och prestandaproblem

 (CELLSJAVA-41419) - OutOfMemoryError, Aspose.Cells håller kvar miljontals celler för alltid

 (CELLSJAVA-41395) - ODS till HTML-konvertering - Textstilsproblem

 (CELLSJAVA-41426) - Cell diagram med x-axel skalas inte korrekt vid konvertering till pdf

 (CELLSJAVA-41421) - Sista ordet i diagrammets textruta hoppar till nästa rad

 (CELLSJAVA-41416) - Värdet på avdelningsproblemet medan kalkylbladet sparas på nytt med Aspose.Cells

 (CELLSJAVA-41387) - Dataetiketter åsidosätts av rubriksektionen


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.





 Lägger till egenskapen SaveOptions.MergeAreas.

 Den används för att slå samman individuella CellAreas för villkorlig formatering och validering.



 Lägger till metoden PivotTable.GetCellByDisplayName(string displayName).

 Hämtar objektet Cell med visningsnamnet för pivotfältet.



Lägger till metoden SheetRender.ToImage(int pageIndex, Graphics g, float x, float y)

 Gör en viss sida i SheetRender till en grafik.



 Lägger till metoden SheetRender.ToImage(int pageIndex, Graphics g, float x, float y, float width, float höjd).

 Gör en viss sida i SheetRender till en grafik.



 Lägger till egenskapen Shape.Geometry.ShapeAdjustValues.

 Får en samling av formjusteringsvärden.





 Notera

 Eftersom kodbasen för Aspose.Cells for Java matchar koden för den relevanta versionen .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.5.2 också inkluderade i denna 076157316.481.4816.481.
