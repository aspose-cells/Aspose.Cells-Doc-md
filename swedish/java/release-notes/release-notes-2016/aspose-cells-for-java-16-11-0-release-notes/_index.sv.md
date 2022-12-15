---
title: Aspose.Cells for Java 16.11.0 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-16-11-0-release-notes/
---
|**Nyckel** |**Sammanfattning** |**Kategori** |
|:- |:- |:- |
|CELLSJAVA-42042 | Stöd Subtotal/Total etiketter på andra språk| Ny funktion|
|CELLSJAVA-41994 | Cell:s text svämmar över till nästa cell| Insekt|
|CELLSJAVA-42039 | CalculateFormula har problem att räkna om celler med hänvisning till celler med formler| Insekt|
|CELLSJAVA-42050 |Hebreiska kontrolltecken återges inte korrekt i PDF| Insekt|
|CELLSJAVA-42020 | XLS till PDF-konvertering tar för mycket tid| Insekt|
|CELLSJAVA-42017 | Layoutproblem vid konvertering av kalkylblad till PDF| Insekt|
|CELLSJAVA-42023 | X-axeletiketter överlappar med Legend när de renderas till PDF| Insekt|
|CELLSJAVA-42022 | Bilden skalas inte bra och dess SVG-fil är inte korrekt| Insekt|
|CELLSJAVA-42003 | Felaktig rendering av diagram vid konvertering av kalkylblad till HTML| Insekt|
|CELLSJAVA-41986 | Mellanslag utelämnas från text i PNG-utdata i diagram| Insekt|
|CELLSJAVA-41438 | Val eller kontrollstatus sparas inte när du sparar till PDF| Insekt|
|CELLSJAVA-41339 |Text- och textjustering är förstörd i filen (01_de_gödsel_verktyg_baltiska_20131215_ incl_logo.xlsx)| Insekt|
|CELLSJAVA-42056 | Om du utökar MS Excel-tabellen/listobjektet ändras cellformateringen| Insekt|
|CELLSJAVA-42055 | Att lägga till Arc i en ny arbetsbok genererar ett potentiellt osäkert kalkylblad| Insekt|
|CELLSJAVA-42038 |Tabellkolumn löser sig bruten om den innehåller '[' ]| Insekt|
|CELLSJAVA-42021 | Problem med att utöka innehållet i Excel-tabell/listobjekt gällande formler| Insekt|
|CELLSJAVA-42019 | Felaktig formel returnerades från en kalkylbladscell| Insekt|
|CELLSJAVA-42004 |java.lang.NullPointerException, i Workbook ctor när du laddar XLSX-filen| Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till Workbook.AbsolutePath-egenskapen**
Hämtar och ställer in den absoluta sökvägen för filen. Används endast för externa länkar.
#### **Lägger till GlobalizationSettings-klassen och WorkbookSettings.GlobalizationSettings-egenskapen**
Hämtar och ställer in globaliseringsinställningarna.
#### **Tar bort föråldrad metod Cell.GetConditionalStyle()**
Använd metoden Cell.GetConditionalFormattingResult() istället.
#### **Tar bort föråldrad metod Cells.MaxDataRowInColumn(int column)**
Använd metoden Cells.GetLastDataRow(int) istället.
#### **Tar bort föråldrad PageSetup.Draft-egenskap**
Använd egenskapen PageSetup.PrintDraft istället.
#### **Tar bort föråldrad AutoFilter.FilterColumnCollection-egenskap**
Använd egenskapen AutoFilter.FilterColumns istället.
#### **Föråldrar stilkonstruktorn och lägger till klassen CellsFactory**
Använd metoden CellsFactory.CreateStyle() istället.
#### **Tar bort föråldrad TickLabels.Rotation-egenskap**
Använd egenskapen TickLabels.RotationAngle istället.
#### **Lägger till metoden GridHyperlinkCollection.GetHyperlink(GridCell cell).**
Hämtar cellens Hyperlink-objekt. Om det inte finns någon hyperlänk i cellen, returnerar den null.
#### **Lägger till metoden GridHyperlinkCollection.GetHyperlink(int row,int column).**
Hämtar cellens Hyperlink-objekt. Om det inte finns någon hyperlänk i cellen, returnerar den null.
