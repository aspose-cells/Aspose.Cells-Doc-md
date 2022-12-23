---
title: Aspose.Cells for .NET 19.9 Release Notes
type: docs
weight: 40
url: /sv/net/aspose-cells-for-net-19-9-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.9](https://www.nuget.org/packages/Aspose.Cells/19.9.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-46864|Stöd läsning och rendering Kontroll av ODS-filer|Ny funktion|
|CELLSNET-46877|Lägg till SheetRender.ToPrinter(PrinterSettings PrinterSettings) överbelastning till API:erna|Ny funktion|
|CELLSNET-46907|Konfigurera ZIP-komprimeringsnivå för XLSX/XLSB|Ny funktion|
|CELLSNET-46890|Resultat av heltalsdivision ska inte tilldelas flyttalsvariabler|Insekt|
|CELLSNET-46883|Pivottabeller behåller inte flera valalternativ efter bearbetning av smarta markörer|Insekt|
|CELLSNET-46874|Värden som inte härrör från formeln och kräver att man trycker på F2 för att få värden i celler|Insekt|
|CELLSNET-46904|Hyperlänkar går förlorade när data importeras från DataTable|Insekt|
|CELLSNET-46875|Innehållet flödar över från sidan under PDF konvertering|Insekt|
|CELLSNET-46865|Ett objekt ändras efter att ha öppnat och sparat|Insekt|
|CELLSNET-46866|Att ställa in teckensnitt och teckenstorlek för Drawing.TextBox fungerar inte i ODS|Insekt|
|CELLSNET-46867|Kryssrutor förlorade när du sparade om XLSX|Insekt|
|CELLSNET-46873|Ref! visas som formel ej tillämpad|Insekt|
|CELLSNET-46876|OLE-objektlänk är inte tillgänglig från XLS-filen|Insekt|
|CELLSNET-46881|Gruppering och avgruppering döljer inte gränser|Insekt|
|CELLSNET-46884|Arbetsblad grupperas när du använder VisibilityType.VeryHidden/Hidden|Insekt|
|CELLSNET-46886|Tabell med en rad som utökas till ytterligare en rad nedan efter att du har sparat arbetsboken|Insekt|
|CELLSNET-46887|Villkorlig formatering behålls inte efter att filen har öppnats i MS Excel och sparats.|Insekt|
|CELLSNET-46891|OleObjects gradientfyllning läses som FillType.Solid|Insekt|
|CELLSNET-46894|Visa arkfliksinställning avmarkerad när du sparar Excel-filen|Insekt|
|CELLSNET-46906|Aspose.Cells hängde på att öppna en XLSX fil|Insekt|
|CELLSNET-46909|OLE Objects formatering ändrades efter att Excel-filen öppnades och sparades|Insekt|
|CELLSNET-46857|Filteranslutningar på pivotdiagram förlorar inställningar vid spara efter att ha uppdaterat pivottabeller|Insekt|
|CELLSNET-46862|Inställningen "Dölj objekt utan data" i slicer går förlorad efter uppdatering av pivottabeller|Insekt|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Tar bort föråldrad Chart.Rotation-egenskap**
Använd egenskapen Chart.RotationAngle istället.
#### **Tar bort föråldrad Chart.IsDataTableShownproperty**
Använd Chart.ShowDataTableproperty istället.
#### **Tar bort föråldrad Chart.IsLegendShown-egenskap**
Använd egenskapen Chart.ShowLegend istället.
#### **Tar bort föråldrad Axis.Crosses-egenskap**
Använd egenskapen Axis.Crosses istället.
#### **Tar bort föråldrad klass HTMLLoadOptions**
Använd klassen HtmlLoadOptions istället.
#### **Tar bort föråldrad klass JSONUtility**
Använd klassen JsonUtility istället.
#### **Lägger till egenskaperna OoxmlCompressionType och XlsbSaveOptions.CompressionType, OoxmlSaveOptions.CompressionType.**
Representerar komprimeringstypen för OOXML-filer.
#### **Tar bort föråldrad klass ODSLoadOptions**
Använd klassen OdsLoadOptions istället.




