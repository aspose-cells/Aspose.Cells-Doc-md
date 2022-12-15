---
title: Hantera dokumentegenskaper
type: docs
weight: 10
url: /sv/java/managing-document-properties/
---
## **Introduktion**

Microsoft Excel ger möjlighet att lägga till egenskaper till kalkylarksfiler. Dessa dokumentegenskaper ger användbar information och är indelade i två kategorier enligt beskrivningen nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarens namn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper definierade av slutanvändaren i form av namn-värdepar.

{{% alert color="primary" %}}

Den viktigaste punkten att veta om inbyggda och anpassade egenskaper är att inbyggda egenskaper kan nås och ändras, men inte kan skapas eller tas bort, men anpassade dokumentegenskaper kan skapas och hanteras.

{{% /alert %}}

## **Hantera dokumentegenskaper med Microsoft Excel**

 Microsoft Excel tillåter hantering av dokumentegenskaper för Excel-filer på ett WYSIWYG-sätt. Följ stegen nedan för att öppna**Egenskaper** dialogrutan i Excel 2016.

1.  Från**Fil** menyn, välj**Info**.

|**Välj infomeny**|
|:- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1.  Klicka på**Egenskaper** rubrik och välj "Avancerade egenskaper".

|**Klicka på Avancerat val av egenskaper**|
|:- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Hantera filens dokumentegenskaper.

|**Egenskapsdialog**|
|:- |
|![todo:image_alt_text](managing-document-properties_3.png)|
dialogrutan Egenskaper finns det olika flikar, som Allmänt, Sammanfattning, Statistik, Innehåll och Tull. Varje flik hjälper till att konfigurera olika typer av information relaterad till filen. Fliken Anpassad används för att hantera anpassade egenskaper.

## **Arbeta med dokumentegenskaper med Aspose.Cells**

Utvecklare kan hantera dokumentegenskaperna dynamiskt med hjälp av Aspose.Cells API:er. Den här funktionen hjälper utvecklarna att lagra användbar information tillsammans med filen, som när filen togs emot, bearbetades, tidsstämplad och så vidare.

{{% alert color="primary" %}}

 Aspose.Cells for Java skriver direkt informationen om API och versionsnummer i utdatadokument. Till exempel, vid rendering av dokument till PDF, fylls Aspose.Cells for Java**Ansökan** fält med värdet 'Aspose.Cells' och**PDF-producent** fält med värdet, t.ex. 'Aspose.Cells for Java v17.9'.

Observera att du inte kan instruera Aspose.Cells for Java att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}}

### **Åtkomst till dokumentegenskaper**

 Aspose.Cells API:er stöder båda typerna av dokumentegenskaper, inbyggda och anpassade. Aspose.Cells'[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook) klass representerar en Excel-fil och, liksom en Excel-fil, den[**Arbetsbok**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook)klass kan innehålla flera kalkylblad, var och en representerad av[**Arbetsblad**](https://reference.aspose.com/cells/java/com.aspose.cells/Worksheet) klass medan samlingen av kalkylblad representeras av[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)klass.

 Använd[**Arbetsbladssamling**](https://reference.aspose.com/cells/java/com.aspose.cells/WorksheetCollection)för att komma åt filens dokumentegenskaper enligt beskrivningen nedan.

-  För att komma åt inbyggda dokumentegenskaper, använd[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties).
-  För att komma åt anpassade dokumentegenskaper, använd[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties).

 Både[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#BuiltInDocumentProperties) och[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheetcollection#CustomDocumentProperties) returnera en instans av[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection) . Denna samling innehåller[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)objekt, som vart och ett representerar en enskild inbyggd eller anpassad dokumentegenskap.

 Det är upp till applikationskravet hur man kommer åt en fastighet, det vill säga; genom att använda index eller namn på fastigheten från[**DocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentPropertyCollection)som visas i exemplet nedan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentProperties.java" >}}

 De[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)klass tillåter att hämta namn, värde och typ av dokumentegenskapen:

-  För att få fastighetsnamnet, använd[**DocumentProperty.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Name).
-  För att få fastighetsvärdet, använd[**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Value)returnerar värdet som ett objekt.
-  För att få egenskapstypen, använd[**DocumentProperty.Type**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Type) . Detta returnerar en av[**PropertyType**](https://reference.aspose.com/cells/java/com.aspose.cells/PropertyType)uppräkningsvärden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AccessingDocumentPropertyValue.java" >}}

### **Lägga till eller ta bort anpassade dokumentegenskaper**

Som vi har beskrivit tidigare i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Lägga till anpassade egenskaper**

 Aspose.Cells API:er har avslöjat[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) ) metod för[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/CustomDocumentPropertyCollection) klass för att lägga till anpassade egenskaper till samlingen. De[**Lägg till**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#add(java.lang.String,%20boolean) )-metoden lägger till egenskapen i Excel-filen och returnerar en referens för den nya dokumentegenskapen som en[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)objekt.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AddingCustomProperty.java" >}}

### **Konfigurera "Länk till innehåll" anpassad egendom**

 För att skapa en anpassad egenskap kopplad till innehållet i ett givet intervall, anropa[**CustomDocumentPropertyCollection.addLinkToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/customdocumentpropertycollection#addLinkToContent(java.lang.String,%20java.lang.String) metod och pass egenskapens namn och källa. Du kan kontrollera om en egenskap är konfigurerad som länkad till innehåll med hjälp av[**DocumentProperty.isLinkedToContent**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#IsLinkedToContent) fast egendom. Dessutom är det också möjligt att få källomfånget med hjälp av[**Källa**](https://reference.aspose.com/cells/java/com.aspose.cells/documentproperty#Source) egendom av[**DocumentProperty**](https://reference.aspose.com/cells/java/com.aspose.cells/DocumentProperty)klass.

 Vi använder en enkel mall Microsoft Excel-fil i exemplet. Arbetsboken har ett definierat namngivet intervall märkt**MyRange** som hänvisar till ett cellvärde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConfiguringLinkToContentCustomProperty.java" >}}

### **Ta bort anpassade egenskaper**

 För att ta bort anpassade egenskaper med Aspose.Cells, ring[**DocumentPropertyCollection.remove**](https://reference.aspose.com/cells/java/com.aspose.cells/documentpropertycollection#remove(java.lang.String)) och skicka namnet på dokumentegenskapen som ska tas bort.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-RemovingCustomProperty.java" >}}
