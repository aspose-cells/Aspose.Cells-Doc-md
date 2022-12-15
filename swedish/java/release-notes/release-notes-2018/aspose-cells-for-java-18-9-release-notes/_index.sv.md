---
title: Aspose.Cells for Java 18.9 Release Notes
type: docs
weight: 40
url: /sv/java/aspose-cells-for-java-18-9-release-notes/
---
{{% alert color="primary" %}}

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.9.

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42715|Formler hämtas inte på samma sätt som i MS Excel-fil|Insekt|
|CELLSJAVA-42711|Diagram i PDF genereras inte från Excel-mallen|Insekt|
|CELLSJAVA-42710|Duplicera förklaringsobjekttext i diagrammet i Excel till PDF-konvertering|Insekt|
|CELLSJAVA-42706|PDF-utdata visar inte diagrametikett|Insekt|
|CELLSJAVA-42700|Vattenfallsdiagrammet återges inte korrekt efter att ha ändrat sjökortsdata|Insekt|
|CELLSJAVA-42717|Cells.deleteRow fungerar felaktigt|Insekt|
|CELLSJAVA-42716|Fel värde hämtat för kantstil|Insekt|
|CELLSJAVA-42709|Fel nedre kantstil returnerades för sammanslagen cell|Insekt|
|CELLSJAVA-42705|MS Excel ger upphov till ett fel när filen laddas efter inställning av autofiltret|Insekt|
|CELLSJAVA-42703|Diagrammet renderades inte vid konvertering av ODS till PDF|Insekt|
|CELLSJAVA-42702|Grå ramar visas efter att ha läst cellformat i kalkylbladet|Insekt|
|CELLSJAVA-42699|PasteType.VALUES_OCH_NUMBER_FORMATS fungerar inte bra|Insekt|
|CELLSJAVA-42646|Undantag: "FormulaBuild Unknown formula token0" på Name.getRefersTo()|Undantag|
|CELLSJAVA-42707|Chart.calculate-metoden orsakar OutOfMemoryError|Undantag|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till metoderna CellsHelper.CreateSafeSheetName(strängnamnProposal)/CreateSafeSheetName(strängnamnProposal, char replaceChar)**

Metoder för användarens bekvämlighet för att skapa ett giltigt arknamn.

### **Lägger till Row.FirstDataCell**

Får den första icke-tomma cellen i raden.

### **Lägger till MapChartLabelLayout enum**

Representerar etikettlayouttypen för kartdiagrammet.

### **Lägger till MapChartProjectionType enum**

Representerar projektionstypen för kartdiagrammet.

### **Lägger till MapChartRegionType enum**

Representerar regiontypen för kartdiagrammet.

### **Lägger till QuartileCalculationType enum**

Representerar diagrammets kvartilberäkningstyp.

### **Lägger till egenskapen Series.LayoutProperties och klassen SeriesLayoutProperties**

Representerar layoutegenskaperna för serien.

### **Lägger till egenskapen TickLabels.IsAutomaticRotation**

Indikerar om rotationen av bocketiketterna är automatisk.

### **Lägger till FilterOperatorType.BeginsWith, Contains, EndsWith och NotContains enum**

Representerar textfilteroperatortypen.

### **Lägger till metoden Cell.GetDisplayStyle(bool).**

Hämtar visningsstilen för cellen.

### **Lägger till metoden GlobalizationSettings.GetStandardHeaderFooterFontStyleName(string localFontStyleName)**

Får standardnamn på engelska typsnittsstilen (vanlig, fet, kursiv) för sidhuvud/sidfot enligt det givna språkets teckensnittsnamn.

### **Lägger till PdfCustomPropertiesExport enum**

Anger hur CustomDocumentPropertyCollection exporteras till PDF-fil.

### **Lägger till egenskapen PdfSaveOptions.CustomPropertiesExport**

Hämtar eller ställer in ett värde som bestämmer hur CustomDocumentPropertyCollection exporteras till PDF-fil. Standardvärdet är None.

### **Lägger till klass XmlDataBinding**

Representerar Xml-databindningsinformation.

### **Lägger till egenskapen ListObject.XmlMap**

Får en XmlMap som används för den här listan.

### **Lägger till egenskapen XmlDataBinding.Url**

Hämtar käll-url för denna databindning.

### **Lägger till egenskapen XmlMap.DataBinding**

Får en XmlDataBinding av denna karta.
