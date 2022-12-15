---
title: Aspose.Cells for .NET 8.5.2 Release Notes
type: docs
weight: 50
url: /sv/net/aspose-cells-for-net-8-5-2-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 8.5.2](https://downloads.aspose.com/cells/net/new-releases/aspose.cells-for-.net-8.5.2/)

{{% /alert %}} 

 Följande är en lista över förbättringar och ändringar i denna version av Aspose.Cells



\1) Aspose.Cells 


## **Andra förbättringar och förändringar**

## **Nya egenskaper**


 (CELLSNET-43758) - Återge till grafisk kontext


## **Buggar**


 (CELLSNET-43786) - Filen är skadad efter att ha uppdaterat pivottabellen i mallfilen

 (CELLSNET-43594) - PivotField.IsRepeatItemLabels fungerar inte i pivottabellen

 (CELLSNET-43367) - Problem med PivotTable.Format() för att formatera PivotField-huvudet

 (CELLSNET-41618) - Visar inte vissa bilder och former efter konvertering av Xls till HTML

(CELLSNET-43817) - CalculateFormula() slutar aldrig för vissa SUMIF Excel-formler

 (CELLSNET-43675) - Problem med att beräkna NORM.S.DIST-funktionen

 (CELLSNET-43741) - Antalet ökar inte när Workbook.Settings.CreateCalcChain är satt till true

 (CELLSNET-43818) - Aspose.Cells genererar 2 sidor medan Excel Print Preview visar 1 sida

 (CELLSNET-43780) - Fel Executive-pappersstorlek vid konvertering till PDF

 (CELLSNET-43776) - Bilden konverteras till svart medan kalkylblad konverteras till PdfA1b

 (CELLSNET-43769) - Cell innehåll beskärs lite överst i utdatabilden

 (CELLSNET-43806) - Plotten/kurvan är inte densamma för XY Scatter-diagram.

 (CELLSNET-43805) - Konvertering av kalkylark till PDF: fet stil är förlorad

 (CELLSNET-43804) - Konvertering av kalkylark till PDF: Innehåll i textruta-renderingar med indrag

 (CELLSNET-43779) - Diagram till bild inkonsekvens för EMF-filformat

(CELLSNET-43772) - Texten i ritningsformen slås inte in korrekt

 (CELLSNET-43771) - Bilden har förskjutits efter att kalkylarket har renderats till PDF

 (CELLSNET-43748) - TextBox-text överlappas i Excel till PDF-rendering

 (CELLSNET-43820) - Kalkylark som innehåller Slicers blir korrupt efter att ha sparats om

 (CELLSNET-43812) - Diagrammet blir tomt i excel-filen och visas inte i Excel 2013

 (CELLSNET-43810) - Det gick inte att öppna den sparade XLSX-filen via Aspose.Cells API:er

 (CELLSNET-43807) - Kalkylark som innehåller pivottabellen är skadad efter att ha sparats på nytt

 (CELLSNET-43802) - Excel-fil korrumperar vid öppning och omspara och öppnas inte i Excel 2013

 (CELLSNET-43799) - Om du sparar om kalkylarket blir resultaten korrupta och skivorna tas bort

 (CELLSNET-43792) - Arbetsboksdataanslutningen tas bort efter att kalkylarket har sparats på nytt


## **Undantag**


 (CELLSNET-43629) - PivotTable.RefreshData() - Det går inte att casta objekt av typen

(CELLSNET-43778) - System.FormatException vid Chart.ToImage när systemspråket är Ryssland

 (CELLSNET-43822) - Arbetsbok som innehåller diagram kan inte sparas och ger undantag

 (CELLSNET-43814) - Att ladda excel i xlsm-format ger nollreferensfel

 (CELLSNET-43793) - Aspose.Cells.CellsException: Åsidosätt elementfel vid inläsning av en XLSX-fil

 (CELLSNET-43784) - System.ArgumentException vid Workbook.Combine

 (CELLSNET-43783) - Undantag vid rendering av ett kalkylblad till tabbavgränsat filformat

 (CELLSNET-43828) - System.InvalidCastException när en mall XLSX-fil sparas på nytt



\2) Aspose.Cells Grid Suite


## **Nya egenskaper**


 (CELLSNET-43809) - Lägger till asynkron återuppringningshändelse för gridesktop

 (CELLSNET-42316) - Kortkommandon Ctrl + Shift + piltangenter fungerar inte.

 (CELLSNET-42174) - Kontroll + piltangenter hoppar inte till cell med data


## **Andra förbättringar och förändringar**

## **Buggar**


 (CELLSNET-43782) - GridCell.Protected-egenskapen har tagits bort

 (CELLSNET-43688) - Radhöjden för vissa sammanslagna celler är inte korrekt.


## **Offentlig API och bakåtinkompatibla ändringar**


 Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.



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



Lägger till GridDesktop.BeforeLoadFile/FinishLoadFile/BeforeCalculate/FinishCalculate-händelser.

 Uppstår i det andra tillståndet för att ladda arbetsboksfilen i GridDesktop.


