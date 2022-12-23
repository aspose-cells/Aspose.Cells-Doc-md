---
title: Aspose.Cells for Java 19.11 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-19-11-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 19.11.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43032|Lägg till Validation.addArea (CellArea cellArea, boolean skipArea) eller Validation.setAreas() metod/överbelastningar till API:erna|Ny funktion|
|CELLSJAVA-42851|Få information om ODATA-anslutningen|Ny funktion|
|CELLSJAVA-43018|Exportera utskriftsområdesintervall till HTML utan att implicit ändra något tillstånd för samma arbetsbok|Förbättring|
|CELLSJAVA-43041|Cells.importCSV ger undantaget "strängvärde får inte överstiga 255 tecken"|Förbättring|
|CELLSJAVA-43043|Cells.removeDuplicates tar mer tid för stora datamängder|Förbättring|
|CELLSJAVA-43019|Radiellt diagram renderas inte korrekt till HTML|Insekt|
|CELLSJAVA-43027|Efter återgivning till PNG är skalningen av axeln annorlunda.|Insekt|
|CELLSJAVA-42474|Pivottabellen uppdateras inte och är skadad efter uppdatering av källdata|Insekt|
|CELLSJAVA-43033|Konverteringen till PDF slutar inte.|Insekt|
|CELLSJAVA-43034|Ogiltigt ryskt (anpassat) datumformat har hämtats|Insekt|
|CELLSJAVA-43040|LoadFilter tar inte hänsyn till det obligatoriska arket|Insekt|
|CELLSJAVA-43035|Gränser försvinner när Excel-fil konverteras till EMF|Insekt|
|CELLSJAVA-43016|Ogiltigt sidantal från SheetRender|Insekt|
|CELLSJAVA-43026|Efter att ha renderat diagram till en bild ändrar dataetiketter stil och värdena är inte desamma|Insekt|
|CELLSJAVA-43038|Hyperlänkar exporteras inte med Cell.setHtmlString()|Insekt|
|CELLSJAVA-43039|Cell.setHtmlString() renderar inte vissa HTML-taggar/skript till Excel-export|Insekt|

## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till metoder: Validation.AddArea(CellArea,bool,bool),AddAreas(CellArea[], bool, bool),RemoveAreas(CellArea[])**
Lägger till/tar bort valideringsinställningar från givna områden med hänsyn till prestanda.
### **Lägger till metoden Workbook.ImportXml (Stream stream, string sheetName, int row, int col).**
Importerar en XML-filström till arbetsboken.
### **Lägger till metoden Workbook.ExportXml (sträng mapName, Stream stream).**
Exportera XML-data till en ström.
### **Lägger till egenskapen HtmlSaveOptions.ExportArea**
Hämtar eller ställer in den exporterande CellArea för det aktuella aktiva arbetsbladet. Om du ställer in det här attributet kommer utskriftsområdet för det aktuella aktiva arbetsbladet att utelämnas. Endast det angivna området kommer att exporteras när filen sparas till HTML.
### **Lägger till klasser: DataMashup,PowerQueryFormula,PowerQueryFormulaCollection,PowerQueryFormulaItem och PowerQueryFormulaItemCollection**
Får information i DataMashup.
### **Lägger till egenskapen DBConnection.SeverCommand.**
Hämtar och ställer in en andra kommandotextsträng som kvarstår när PivotTable-serverbaserade sidfält används.
### **Lägger till metoden CellsHelper.GetTextWidth().**
Hämtar textens bredd i punktenheten.
