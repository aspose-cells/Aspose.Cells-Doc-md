---
title: Aspose.Cells for Java 17.6 Release Notes
type: docs
weight: 70
url: /sv/java/aspose-cells-for-java-17-6-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 17.6](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.6/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42315|Lägg till JS Client API för AjaxCallFinished event - GridWeb (JAVA)|Ny funktion|
|CELLSJAVA-42194|Gruppera rader i kalkylbladet - GridWeb (JAVA)|Ny funktion|
|CELLSJAVA-42308|Pivottabell är fel (saknade rader, pivotfältsrubriker utskrivna två gånger, datum konverterat till numeriska värden, etc.) i Excel till HTML-rendering|Insekt|
|CELLSJAVA-42298|Extra tecken som finns i HTML utdata från Excel-fil|Insekt|
|CELLSJAVA-42277|Bilden visas inte i utgången HTML när HtmlSaveOptions.setExportHiddenWorksheet är inställt på false|Insekt|
|CELLSJAVA-42259|HTML kunde inte konverteras till Excel-fil korrekt|Insekt|
|CELLSJAVA-42256|Problem med HTML-tabell till Excel-rendering|Insekt|
|CELLSJAVA-42319|Problem med att beräkna Print Area när du anger formler|Insekt|
|CELLSJAVA-42273|Funktionen Set Column Header Tips fungerar inte i GridWeb (JAVA)|Insekt|
|CELLSJAVA-42269|GridWorksheet.setColumnHeaderToolTip() fungerar inte i GridWeb (JAVA)|Insekt|
|CELLSJAVA-42320|Diagrammet uppdateras inte om det finns i ett separat ark|Insekt|
|CELLSJAVA-42295|Cell-värdet läggs till i början när vi klickar på en befintlig cell (har något värde)|Insekt|
|CELLSJAVA-42325|När XLSX sparas som PDF speglas orden|Insekt|
|CELLSJAVA-42299|Extra tecken finns i utdata PDF/bild av Excel-fil|Insekt|
|CELLSJAVA-42301|Staplar saknas i stapeldiagrammets PDF-utgång|Insekt|
|CELLSJAVA-42293|Diagrambilden är fel i utgången HTML|Insekt|
|CELLSJAVA-42292|Bilden av diagrammet är felaktig i utdata HTML|Insekt|
|CELLSJAVA-42270|Innehåll saknas när Excel-diagram konverteras till PDF|Insekt|
|CELLSJAVA-42258|Diagrammets PDF har fel datumformat för x-axeletiketter|Insekt|
|CELLSJAVA-42252|Felaktig Y-axelskalning i utgången PDF|Insekt|
|CELLSJAVA-42245|Stil/formatering är fel när du sparar till HTML|Insekt|
|CELLSJAVA-42316|Möjligheten att komprimera bilder bevaras inte när Excel-filen öppnas och sparas|Insekt|
|CELLSJAVA-42306|Bakgrundsfärgen på cellerna i File2 ändras när arbetsboken öppnas och sparas|Insekt|
|CELLSJAVA-42305|Bakgrundsfärgen på cellerna i File1 ändras när arbetsboken öppnas och sparas|Insekt|
|CELLSJAVA-42303|Excel-formelcell blir icke-formelcell när du anger text för formen|Insekt|
|CELLSJAVA-42284|Workbook.getFonts() visar ytterligare teckensnitt efter att samma kalkylblad har laddats om|Insekt|
|CELLSJAVA-42307|Undantag: "Radindexet ska inte finnas i den pivotbara rapporten" inträffade vid rendering till filformatet HTML|Undantag|
|CELLSJAVA-42285|Undantag: "Radindex kan inte vara negativt" inträffade om det finns en pivottabell i kalkylbladet som ska konverteras till filformatet HTML|Undantag|
|CELLSJAVA-42318|Ett undantag skapas när du försöker öppna Workbook|Undantag|
|CELLSJAVA-42311|Undantag: "java.lang.NullPointerException" när du öppnar en ODS-fil via Aspose.Cells API:er|Undantag|
|CELLSJAVA-42302|NullPointerException om att skapa arbetsboksinstans från källexcelfil|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskapen Gridweb.OnAjaxCallFinishedClientFunction**
Hämtar eller ställer in klientsidans funktionsnamn som ska anropas när ajaxcall avslutats.
### **Lägger till enum StyleModifyFlag.RelativeIndent**
Representerar relativ indrag.
### **Lägger till egenskapen TextureFill.IsTiling**
Indikerar om kakelbild som struktur.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Kakelbild som en textur inuti formen](/cells/sv/java/tile-picture-as-a-texture-inside-the-shape/)
- [Använda OnAjaxCallFinishedClientFunction av GridWeb](/cells/sv/java/using-onajaxcallfinishedclientfunction-of-gridweb/)
- [Använder formelparametern i Smart Marker-fältet](/cells/sv/java/using-formula-parameter-in-smart-marker-field/)
