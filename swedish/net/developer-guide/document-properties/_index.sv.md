---
title: Hantera dokumentegenskaper
linktitle: Dokument egenskaper
type: docs
weight: 80
url: /sv/net/managing-document-properties/
description: Hantera dokumentegenskaper för kalkylbladsfiler.
---
## **Introduktion**

Microsoft Excel ger möjlighet att lägga till egenskaper till kalkylarksfiler. Dessa dokumentegenskaper ger användbar information och är indelade i två kategorier enligt beskrivningen nedan.

- Systemdefinierade (inbyggda) egenskaper: Inbyggda egenskaper innehåller allmän information om dokumentet som dokumenttitel, författarens namn, dokumentstatistik och så vidare.
- Användardefinierade (anpassade) egenskaper: Anpassade egenskaper definierade av slutanvändaren i form av namn-värdepar.

{{% alert color="primary" %}}

Den viktigaste punkten att veta om inbyggda och anpassade egenskaper är att inbyggda egenskaper kan nås och ändras, men inte skapas eller tas bort. Däremot kan anpassade egenskaper skapas och hanteras.

{{% /alert %}}

## **Hantera dokumentegenskaper med Microsoft Excel**

 Microsoft Excel låter dig hantera dokumentegenskaperna för Excel-filerna på ett WYSIWYG-sätt. Följ stegen nedan för att öppna**Egenskaper** dialogrutan i Excel 2016.

1.  Från**Fil** menyn, välj**Info**.

|**Välj infomeny**|
|:- |
|![todo:image_alt_text](managing-document-properties_1.png)|
1.  Klicka på**Egenskaper**rubrik och välj "Avancerade egenskaper".

|**Klicka på Avancerat val av egenskaper**|
|:- |
|![todo:image_alt_text](managing-document-properties_2.png)|
1. Hantera filens dokumentegenskaper.

|**Egenskapsdialog**|
|:- |
|![todo:image_alt_text](managing-document-properties_3.png)|
I dialogrutan Egenskaper finns det olika flikar, som Allmänt, Sammanfattning, Statistik, Innehåll och Tull. Varje flik hjälper till att konfigurera olika typer av information relaterad till filen. Fliken Anpassad används för att hantera anpassade egenskaper.

## **Arbeta med dokumentegenskaper med Aspose.Cells**

Utvecklare kan hantera dokumentegenskaperna dynamiskt med hjälp av Aspose.Cells API:er. Den här funktionen hjälper utvecklarna att lagra användbar information tillsammans med filen, som när filen togs emot, bearbetades, tidsstämplad och så vidare.

{{% alert color="primary" %}}

 Aspose.Cells for .NET skriver direkt informationen om API och versionsnummer i utdatadokument. Till exempel, när dokument återges till PDF, fylls Aspose.Cells for .NET i**Ansökan** fält med värdet 'Aspose.Cells' och**PDF Producent** fält med värdet, t.ex. 'Aspose.Cells v17.9'.

Observera att du inte kan instruera Aspose.Cells for .NET att ändra eller ta bort denna information från utdatadokument.

{{% /alert %}}

### **Åtkomst till dokumentegenskaper**

Aspose.Cells API:er stöder båda typerna av dokumentegenskaper, inbyggda och anpassade. Aspose.Cells'[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass representerar en Excel-fil och, liksom en Excel-fil, den[**Arbetsbok**](https://reference.aspose.com/cells/net/aspose.cells/workbook) klass kan innehålla flera kalkylblad, var och en representerad av[**Arbetsblad**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) klass medan samlingen av kalkylblad representeras av[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)klass.

 Använd[**Arbetsbladssamling**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection)för att komma åt filens dokumentegenskaper enligt beskrivningen nedan.

-  För att komma åt inbyggda dokumentegenskaper, använd[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties).
-  För att komma åt anpassade dokumentegenskaper, använd[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties).

 Både[**WorksheetCollection.BuiltInDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/builtindocumentproperties) och[**WorksheetCollection.CustomDocumentProperties**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection/properties/customdocumentproperties) returnera instansen av[**Aspose.Cells.Properties.DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection). Denna samling innehåller[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objekt, som vart och ett representerar en enskild inbyggd eller anpassad dokumentegenskap.

 Det är upp till applikationskravet hur man kommer åt en fastighet, det vill säga; genom att använda index eller namn på fastigheten från[**DocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection)som visas i exemplet nedan.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingDocumentProperties.cs" >}}

 De[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)klass tillåter att hämta namn, värde och typ av dokumentegenskapen:

-  För att få fastighetsnamnet, använd[**DocumentProperty.Name**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/name).
-  För att få fastighetsvärdet, använd[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value). [**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value)returnerar värdet som ett objekt.
-  För att få egenskapstypen, använd[**DocumentProperty.Type**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/type) . Detta returnerar en av[**PropertyType**](https://reference.aspose.com/cells/net/aspose.cells.properties/propertytype) uppräkningsvärden. När du har fått egenskapstypen, använd en av de**DocumentProperty.ToXXX** metoder för att erhålla värdet av lämplig typ istället för att använda[**DocumentProperty.Value**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/value) . De**DocumentProperty.ToXXX**metoderna beskrivs i tabellen nedan.

{{% alert color="primary" %}}

 De[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)klass tillhandahåller också en uppsättning metoder som returnerar värden för andra datatyper.

{{% /alert %}}

|**Medlemsnamn**|**Beskrivning**|**ToXXX-metoden**|
|:- |:- |:- |
|Boolean|Egenskapsdatatypen är boolesk|ToBool|
|Datum|Egenskapsdatatypen är DateTime. Observera att endast Microsoft Excel-butiker<br>datumdelen, ingen tid kan lagras i en anpassad egenskap av denna typ|ToDateTime|
|Flyta|Egenskapsdatatypen är dubbel|Att dubblera|
|siffra|Egenskapsdatatypen är Int32|ToInt|
|Sträng|Egenskapens datatyp är String|Att stränga|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AccessingValueOfDocumentProperties.cs" >}}

### **Lägga till eller ta bort anpassade dokumentegenskaper**

Som vi har beskrivit tidigare i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Lägga till anpassade egenskaper**

 Aspose.Cells API:er har avslöjat[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) metod för[**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection) klass för att lägga till anpassade egenskaper till samlingen. De[**Lägg till**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/add/index) metod lägger till egenskapen i Excel-filen och returnerar en referens för den nya dokumentegenskapen som en[**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)objekt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AddingDocumentProperties.cs" >}}

### **Konfigurera "Länk till innehåll" anpassad egendom**

 För att skapa en anpassad egenskap kopplad till innehållet i ett givet intervall, anropa[**CustomDocumentPropertyCollection.AddLinkToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/customdocumentpropertycollection/methods/addlinktocontent) metod och pass egenskapens namn och källa. Du kan kontrollera om en egenskap är konfigurerad som länkad till innehåll med hjälp av[**DocumentProperty.IsLinkedToContent**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/islinkedtocontent) fast egendom. Dessutom är det också möjligt att få källomfånget med hjälp av[**Källa**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty/properties/source) egendom av[**DocumentProperty**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentproperty)klass.

 Vi använder en enkel mall Microsoft Excel-fil i exemplet. Arbetsboken har ett definierat namngivet intervall märkt**MyRange** som hänvisar till ett cellvärde.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ConfigureLinktoContentDocumentProperty.cs" >}}

### **Ta bort anpassade egenskaper**

 För att ta bort anpassade egenskaper med Aspose.Cells, ring[**DocumentPropertyCollection.Remove**](https://reference.aspose.com/cells/net/aspose.cells.properties/documentpropertycollection/methods/remove)metod och skicka namnet på dokumentegenskapen som ska tas bort.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-RemovingCustomProperties.cs" >}}

## **Förhandsämnen**
- [Lägga till anpassade egenskaper som är synliga i dokumentinformationspanelen](/cells/sv/net/adding-custom-properties-visible-inside-document-information-panel/)
- [Ställa in egenskaperna ScaleCrop och LinksUpToDate för inbyggda dokumentegenskaper](/cells/sv/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Ange dokumentversion av Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Ange språket för Excel-filen med inbyggda dokumentegenskaper](/cells/sv/net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)
