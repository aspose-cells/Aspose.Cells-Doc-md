---
title: Hantera dokumentegenskaper
type: docs
weight: 10
url: /sv/java/managing-document-properties/
---

## **Introduktion**

Microsoft Excel ger möjligheten att lägga till egenskaper i kalkylbladfiler. Dessa dokumentegenskaper förser användbar information och är uppdelade i 2 kategorier enligt detaljerna nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarnamn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper som definieras av användaren i form av namn-värdepar.

{{% alert color="primary" %}}

Det viktigaste att veta om inbyggda och anpassade egenskaper är att inbyggda egenskaper kan kommas åt och ändras, men kan inte skapas eller tas bort, emellertid kan anpassade dokumentegenskaper skapas och hanteras.

{{% /alert %}}

## **Hantera dokumentegenskaper med hjälp av Microsoft Excel**

Microsoft Excel tillåter hantering av dokumentegenskaper för Excel-filerna på ett WYSIWYG-sätt. Följ nedanstående steg för att öppna dialogrutan **Egenskaper** i Excel 2016.

1. Välj **Info** i **Fil**-menyn.

|**Val av Info-meny**|
| :- |
|![todo:image_alt_text](managing-document-properties_1.png)|
2. Klicka på **Egenskaper** och välj "Avancerade egenskaper".

|**Klicka på Avancerad Val av egenskaper**|
| :- |
|![todo:image_alt_text](managing-document-properties_2.png)|
3. Hantera filens dokumentegenskaper.

|**Dialogruta Egenskaper**|
| :- |
|![todo:image_alt_text](managing-document-properties_3.png)|
I dialogrutan Egenskaper finns olika flikar, som Allmänt, Sammanfattning, Statistik, Innehåll och Anpassade. Varje flik hjälper till att konfigurera olika typer av information relaterad till filen. Anpassad flik används för att hantera anpassade egenskaper.

## **Arbeta med dokumentegenskaper med hjälp av Aspose.Cells**

Utvecklare kan dynamiskt hantera dokumentegenskaper med hjälp av Aspose.Cells API:er. Denna funktion hjälper utvecklarna att lagra användbar information tillsammans med filen, som när filen mottogs, bearbetades, tidsstämplades och så vidare.

{{% alert color="primary" %}}

Aspose.Cells for Java skriver direkt in information om API och versionsnummer i utdatafiler. Till exempel, vid rendering av dokument till PDF fyller Aspose.Cells for Java fältet **Applikation** med värdet 'Aspose.Cells' och fältet **PDF-producent** med värdet, t.ex. 'Aspose.Cells for Java v17.9'.

Observera att du inte kan instruera Aspose.Cells for Java att ändra eller ta bort denna information från utdatafiler.

{{% /alert %}}

### **Åtkomst till dokumentegenskaper**

Aspose.Cells API:er stödjer både inbyggda och anpassade dokumentegenskaper. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass representerar en Excel-fil och, precis som en Excel-fil, kan [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klassen innehålla flera kalkylblad, där varje representeras av [**Worksheet**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klassen medan samlingen av kalkylblad representeras av [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) klassen.

Använd [**WorksheetCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection) för att komma åt filens dokumentegenskaper enligt nedan.

- För att komma åt inbyggda dokumentegenskaper, använd [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
- För att komma åt anpassade dokumentegenskaper, använd [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

Både [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) och [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) returnerar en instans av [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection). Denna samling innehåller [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) objekt, där vardera representerar en enskild inbyggd eller anpassad dokumentegenskap.

Det är upp till tillämpningskravet hur man kommer åt en egenskap, det vill säga; genom att använda indexet eller namnet på egenskapen från [**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) som demonstreras i exemplet nedan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty) klassen tillåter att hämta namn, värde och typ av dokumentegenskap:

- För att få egenskapens namn, använd [**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
- För att få egenskapens värde, använd [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value) returnerar värdet som en Objekt.
- För att få egenskapens typ, använd [**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type). Detta returnerar en av [**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType) uppräkningens värden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Lägga till eller ta bort anpassade dokumentegenskaper**

Som vi tidigare har beskrivit i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Lägga till anpassade egenskaper**

Aspose.Cells API:er har exponerat [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-)-metoden för [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection)-klassen för att lägga till anpassade egenskaper i samlingen. [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add-java.lang.String-boolean-)-metoden lägger till egenskapen i Excel-filen och returnerar en referens för den nya dokumentegenskapen som en [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)-objekt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Konfigurera anpassad egenskap "Länk till innehåll"**

För att skapa en anpassad egenskap kopplad till innehållet i ett visst område, ring [**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent-java.lang.String-java.lang.String-)-metoden och ange egenskapens namn och källa. Du kan kontrollera om en egenskap är konfigurerad som kopplad till innehåll genom att använda [**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent)-egenskapen. Dessutom är det också möjligt att få källområdet med hjälp av [**Source**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source)-egenskapen i [**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)-klassen.

Vi använder en enkel mall Microsoft Excel-fil i exemplet. Arbetsboken har en definierad namngiven område märkt **MyRange** som hänvisar till en cellvärde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Ta bort anpassade egenskaper**

För att ta bort anpassade egenskaper med hjälp av Aspose.Cells, ring [**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove-java.lang.String-)-metoden och ange namnet på dokumentegenskapen som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
{{< app/cells/assistant language="java" >}}
