---
title: Aspose.Cells for Python via Java 21.12 Release Notes
type: docs
weight: 1
url: /sv/python-java/aspose-cells-for-python-via-java-21-12-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Python via Java 21.12](https://downloads.aspose.com/cells/python-java/new-releases/aspose.cells-for-python-via-java-21.12/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43994|Stöd för att avbryta exekveringen av WorkbookDesigner.process i SmarkMarker|
|CELLSJAVA-44039|Ändra PDF Producer-attribut från den genererade PDF-filen|
|CELLSJAVA-43469|Möjlig regression: Prestandaförsämring av FormatConditionCollection.addArea()|
|CELLSJAVA-43983|Regression: Oändlig loop vid konvertering av XLSX till PDF|
|CELLSJAVA-44029|XLSX till PDF: Bilden konverteras inte|
|CELLSJAVA-44093| Problem med textavkortning med rektangelformer vid rendering till bild i nyare Aspose.Cells for Java versioner|
|CELLSJAVA-44089|DataLabels.setShadow() är inte tillgänglig och den är inte lika med metoden Series.setShadow()|
|CELLSJAVA-44000|Cells stil är felaktig i HTML när man använder ikonuppsättning och annan villkorlig formatering samtidigt|
|CELLSJAVA-43932|Problem med att ställa in dataetiketternas position för exploderade munkdiagram i utdatabilden|
|CELLSJAVA-43934|Cirkeldiagrametiketterna matchade inte med Excel efter manipulering eller uppdatering av diagram|
|CELLSJAVA-44094|Diagramtitel trunkeras vid export till PDF|
|CELLSJAVA-43533|Problem med att skapa XLSX till HTML i Ubuntu|
|CELLSJAVA-43987|Den högra kanten av sammanslagna celler går förlorad i html|
|CELLSJAVA-44016|Problem vid konvertering av Excel-filen som innehåller bildens URL till HTML|
|CELLSJAVA-44071|com.aspose.cells.CellsException: Du har angett för få parametrar för funktionen IF när du anropar Workbook.calculateFormula()|
|CELLSJAVA-44104|NullPointerException vid import av SpreadSheetML|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Fler begränsningar för att lägga till områden för validering.**

Vi har ändrat områdesmodellen för validering och villkorlig formatering för prestandaövervägande. Den nya modellen kräver fler begränsningar för sekvensen av tillagda områden. För Validation.AddArea(CellArea cellArea, bool checkIntersection, bool checkEdge) och Validation.AddAreas(CellArea[]areas, bool checkIntersection, bool checkEdge), om de två "check"-parametrarna är falska, måste användaren se till att de tillagda områdena sorteras i stigande ordning efter de övre vänstra hörnen. Annars kan oväntade resultat fås för andra operationer. I den nya versionen, eftersom prestandan för att lägga till stora mängder områden har förbättrats avsevärt, tror vi inte att Validation.AddArea(CellArea cellArea) kommer att vara en flaskhals längre. Så vi tror att användare bara kan ringa AddArea(CellArea cellArea) direkt, utan att behöva använda dessa två speciella metoder.

### **Ändrat beteende för att ändra områden av Validation/ConditionalFormatting.**

För validering och villkorlig formatering, i gamla versioner kan deras områden backas upp av CellArea-objektet som hämtats från eller ställts in på dem. Så om användaren ändrar fältvärdet för CellArea-objektet kan områdena också ändras, och vice versa. I själva verket är detta ett oväntat resultat från synen på API design. Från denna version har denna bieffekt tagits bort och användaren kan inte ändra områdena genom att ändra CellArea-objektet längre.

### **Ändrade beteende för att lägga till formatvillkor i FormatConditionCollection.**

För FormatConditionCollection.AddCondition(...)-metoder, gör gamla versioner prioritet för en nyligen tillagd som den lägsta. Det skiljer sig från ms excels beteende. Från den här versionen, precis som vad du får för operationen i ms excel, gör vi det nyligen tillagda formatvillkorets prioritet som den högsta.

### **Lägger till egenskapen AbstractInterruptMonitor.TerminateWithoutException.**

Den här egenskapen anger när ett avbrott har krävts för en process, om processen ska avslutas med ett undantag eller bara avslutas tyst. Som standard är den här egenskapen falsk, det vill säga att processen avslutas av ett undantag när den avbryts.

### **Lägger till WorkbookSettings.ResourceProvider-egenskapen.**

Omdöpt egenskap för WorkbookSettings.StreamProvider för att göra den mer lämpad för sin funktion och lättare för användare att förstå.

### **Lägger till alternativet LoadDataFilterOptions.Revision.**

Vissa mallfiler kan innehålla stora mängder revisionsloggar och som orsakar dålig prestanda för att ladda arbetsboken. Användaren kan använda detta alternativ för att kontrollera om dessa revisionsloggar ska laddas eller inte.

### **Föråldrad WorkbookSettings.StreamProvider-egenskap.**

Använd egenskapen WorkbookSettings.ResourceProvider istället.

### **Tar bort den föråldrade egenskapen PdfSaveOptions.StreamProvider.**

Använd egenskapen WorkbookSettings.ResourceProvider istället.

### **Lägger till egenskapen JsonLoadOptions.MultipleWorksheets.**

Anger om varje attribut för JsonObject-objekt importeras som ett kalkylblad när alla underordnade noder är matrisnoder.

### **Lägger till FileFormatType.SqlScript, SaveFormat.SqlScript och SqlScriptSaveOptions**

Representerar alternativen för att spara sql-skript.

### **Lägger till SaveFormat.Xml, LoadFormat.Xml, XmlSaveOptions och XmlLoadOptions**

Representerar alternativen för R/W xml-filer.

### **Lägger till egenskapen HtmlSaveOptions.SaveAsSingleFile.**

 Anger om excel sparas som en enda fil.

### **Lägger till egenskapen JsonLoadOptions.MultipleWorksheets.**

 Anger om data från Json-filen laddas till flera kalkylblad

### **Lägger till egenskapen PdfSaveOptions.Producer.**

 Hämtar och ställer in producent av genererade pdf-dokument.

### **Lägger till metoderna ListColumn.GetCustomTotalsRowFormula() och ListColumn.SetCustomTotalsRowFormula()**

 Hämtar och ställer in den anpassade formeln för totalraden i tabellen.
