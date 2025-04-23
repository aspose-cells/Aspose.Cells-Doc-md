---
title: Hantera dokumentegenskaper
linktitle: Dokumentegenskaper
type: docs
weight: 80
url: /sv/python-net/managing-document-properties/
description: Lär dig Hur man hanterar dokumentegenskaper via Aspose.Cells för Python via .NET API er.
keywords: Hur man hanterar dokumentegenskaper i C#, Hämta eller Sätt dokumentegenskaper med C#, Lägg till eller ta bort dokumentegenskaper via C#, Infoga eller ta bort dokumentegenskaper med C#, Hur man får tillgång till dokumentegenskaper med Aspose.Cells för Python via .NET API er.
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

Utvecklare kan dynamiskt hantera dokumentegenskaper med Aspose.Cells för Python via .NET API:er. Denna funktion hjälper utvecklarna att lagra användbar information tillsammans med filen, såsom när filen mottogs, bearbetades, tidsstämplades med mera.

{{% alert color="primary" %}}

Aspose.Cells för Python via .NET skriver direkt information om API och versionsnummer i utdatafiler. Till exempel, när dokumentet renderas till PDF, fyller Aspose.Cells för Python via .NET i fältet **Application** med värdet 'Aspose.Cells' och fältet **PDF Producer** med värdet, t.ex. 'Aspose.Cells for Python via .NET v17.9'.

Observera att du inte kan instruera Aspose.Cells för Python via .NET att ändra eller ta bort denna information från utdatafiler.

{{% /alert %}}


### **Hur man lägger till eller tar bort anpassade dokumentegenskaper**

Som vi tidigare har beskrivit i början av detta ämne kan utvecklare inte lägga till eller ta bort inbyggda egenskaper eftersom dessa egenskaper är systemdefinierade men det är möjligt att lägga till eller ta bort anpassade egenskaper eftersom dessa är användardefinierade.

### **Hur man lägger till anpassade egenskaper**

Aspose.Cells för Python via .NET API:er har exponerat metoden [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) för klass [**CustomDocumentPropertyCollection**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection) för att lägga till anpassade egenskaper till samlingen. Metoden [**add**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/customdocumentpropertycollection/add) tillägger egenskapen till Excel-filen och returnerar en referens till den nya dokumentegenskapen som ett [**Aspose.Cells.Properties.DocumentProperty**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/documentproperty) objekt.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingDocumentProperties.py" >}}


## **Fortsatta ämnen**
- [Lägga till anpassade egenskaper synliga inuti dokumentinformationspanelen](/cells/sv/python-net/adding-custom-properties-visible-inside-document-information-panel/)
- [Inställning av ScaleCrop och LinksUpToDate egenskaper för inbyggda dokumentegenskaper](/cells/sv/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/)
- [Ange dokumentversionen för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/python-net/specify-document-version-of-the-excel-file-using-builtin-document-properties/)
- [Ange språket för Excel-filen med hjälp av inbyggda dokumentegenskaper](/cells/sv/python-net/specify-the-language-of-the-excel-file-using-builtin-document-properties/)

