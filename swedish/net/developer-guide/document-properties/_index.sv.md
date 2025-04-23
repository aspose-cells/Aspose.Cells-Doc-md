---
title: Hantera dokumentegenskaper
linktitle: Dokumentegenskaper
type: docs
weight: 80
url: /sv/net/managing-document-properties/
description: Lär dig hur du hanterar dokumentegenskaper genom Aspose.Cells for NET API er.
keywords: Hur man hanterar dokumentegenskaper i C#, Hämta eller ange dokumentegenskaper med C#, Lägg till eller ta bort dokumentegenskaper via C#, Infoga eller ta bort dokumentegenskaper med C#, Hur man får åtkomst till dokumentegenskaper med Aspose.Cells for NET API er.
---


## **Introduktion**

Microsoft Excel ger möjligheten att lägga till egenskaper i kalkylbladfiler. Dessa dokumentegenskaper förser användbar information och är uppdelade i 2 kategorier enligt detaljerna nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarnamn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper som definieras av användaren i form av namn-värdepar.

{{% alert color="primary" %}}

Det viktigaste att veta om inbyggda och anpassade egenskaper är att inbyggda egenskaper kan kommas åt och ändras, men inte skapas eller tas bort. Däremot kan anpassade egenskaper skapas och hanteras.

{{% /alert %}}

## **Hur man hanterar dokumentegenskaper med Microsoft Excel**

Microsoft Excel tillåter dig att hantera dokumentegenskaper för Excel-filer på ett WYSIWYG-sätt. Följ nedanstående steg för att öppna dialogrutan **Egenskaper** i Excel 2016.

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

## **Hur man arbetar med dokumentegenskaper med Aspose.Cells**

Utvecklare kan dynamiskt hantera dokumentegenskaper med hjälp av Aspose.Cells API:er. Denna funktion hjälper utvecklarna att lagra användbar information tillsammans med filen, som när filen mottogs, bearbetades, tidsstämplades och så vidare.

{{% alert color="primary" %}}

Aspose.Cells for .NET skriver direkt information om API och versionsnummer i utdata-dokument. Till exempel fyller Aspose.Cells for .NET vid rendering av dokument till PDF-fältet **Applikation** med värdet 'Aspose.Cells' och fältet **PDF-producent** med värdet, t.ex. 'Aspose.Cells v17.9'.

Observera att du inte kan instruera Aspose.Cells for .NET att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}}

### **Hur man får åtkomst till dokumentegenskaper**

Aspose.Cells API:er stödjer både inbyggda och anpassade dokumentegenskaper. Aspose.Cells' [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass representerar en Excel-fil och, precis som en Excel-fil, kan [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klassen innehålla flera kalkylblad, där varje representeras av [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klassen medan samlingen av kalkylblad representeras av [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) klassen.

Använd [**WorksheetCollection**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) för att komma åt filens dokumentegenskaper enligt nedan.

- För att komma åt inbyggda dokumentegenskaper, använd [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
- För att komma åt anpassade dokumentegenskaper, använd [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

Både [**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) och [**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) returnerar en instans av [**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Denna samling innehåller [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) objekt, där varje representerar en enskild inbyggd eller anpassad dokumentegenskap.

Det är upp till tillämpningskravet hur man kommer åt en egenskap, det vill säga; genom att använda indexet eller namnet på egenskapen från [**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection) som demonstreras i exemplet nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) klassen tillåter att hämta namn, värde och typ av dokumentegenskap:

- För att få egenskapens namn, använd [**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
- För att få egenskapens värde, använd [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) returnerar värdet som en Objekt.
- För att hämta egenskapstypen, använd [**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type). Detta returnerar en av [**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype)-uppräkningens värden. Efter att du har hämtat egenskapstypen, använd en av metoderna **DocumentProperty.ToXXX** för att få värdet av lämplig typ istället för att använda [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). Metoderna **DocumentProperty.ToXXX** beskrivs i tabellen nedan.

{{% alert color="primary" %}}

Klassen [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty) tillhandahåller också en uppsättning metoder som returnerar värden för andra datatyper.

{{% /alert %}}

|**Medlemsnamn**|**Beskrivning**|**ToXXX-metod**|
| :- | :- | :- |
|Boolean| Egenskapens datatyp är Boolean|ToBool|
|Date| Egenskapens datatyp är DateTime. Observera att Microsoft Excel endast lagrar <br>datumdelen, ingen tid kan lagras i en anpassad egenskap av denna typ|ToDateTime|
|Float| Egenskapens datatyp är Dubbel|ToDouble|
|Number| Egenskapens datatyp är Int32|ToInt|
|String| Egenskapens datatyp är Sträng|ToString|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Hur man lägger till eller tar bort anpassade dokumentegenskaper**

Som vi tidigare har beskrivit i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Hur man lägger till anpassade egenskaper**

Aspose.Cells API:er har exponerat [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)-metoden för [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection)-klassen för att lägga till anpassade egenskaper i samlingen. [**Add**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index)-metoden lägger till egenskapen i Excel-filen och returnerar en referens för den nya dokumentegenskapen som ett [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)-objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Hur man konfigurerar egendom med länk till innehåll**

För att skapa en anpassad egenskap kopplad till innehållet i ett visst område, ring [**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent)-metoden och ange egenskapens namn och källa. Du kan kontrollera om en egenskap är konfigurerad som kopplad till innehåll genom att använda [**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent)-egenskapen. Dessutom är det också möjligt att få källområdet med hjälp av [**Source**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source)-egenskapen i [**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)-klassen.

Vi använder en enkel mall Microsoft Excel-fil i exemplet. Arbetsboken har en definierad namngiven område märkt **MyRange** som hänvisar till en cellvärde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Hur man tar bort anpassade egenskaper**

För att ta bort anpassade egenskaper med hjälp av Aspose.Cells, ring [**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)-metoden och ange namnet på dokumentegenskapen som ska tas bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Fortsatta ämnen**
- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper](/cells/sv/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
{{< app/cells/assistant language="csharp" >}}
