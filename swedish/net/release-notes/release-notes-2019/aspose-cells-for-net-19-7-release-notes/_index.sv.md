---
title: Aspose.Cells for .NET 19.7 Release Notes
type: docs
weight: 60
url: /sv/net/aspose-cells-for-net-19-7-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for .NET 19.7](https://www.nuget.org/packages/Aspose.Cells/19.7.0).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSNET-42029|Stöd för att lägga till någon form av Callback-händelse/mekanism som meddelar dig om konverteringens framsteg|Ny funktion|
|CELLSNET-46791|Stöd fler vyer men inte anpassad vy|Ny funktion|
|CELLSNET-46808|Stöd lästabellen enstaka celler av XLS fil.|Ny funktion|
|CELLSNET-46775|Den grupperade formens bredd kan inte ställas in|Förbättring|
|CELLSNET-46785|Förkortningens skiftläge är annorlunda för samma ord: HtmlSaveOptions och HTMLLoadOptions, JsonLayoutOptions och JSONUtility, ODSLoadOptions och OdsSaveOptions.|Förbättring|
|CELLSNET-46811|Stöd HeadingPairs och TitlesOfParts-taggar av XLS-filen.|Förbättring|
|CELLSNET-46783|CalculateFormula är mycket långsam|Prestanda|
|CELLSNET-46746|CalculateFormula - formler påverkar inte diagram|Insekt|
|CELLSNET-46772|Felaktigt PDF skapat av att grafiken saknas|Insekt|
|CELLSNET-46802|Diagram renderas annorlunda i XLS än PDF|Insekt|
|CELLSNET-46806|Kombinationsdiagram återges till PDF felaktigt|Insekt|
|CELLSNET-41449|XLSB med komplexa pivottabellfiler|Insekt|
|CELLSNET-43921|Rendering XLSX till XLSB ger en skadad fil|Insekt|
|CELLSNET-44593|Utdata Excel-fil är inte bra när du konverterar HTML till Excel|Insekt|
|CELLSNET-46794|Cells skift när HTML konverterades till XLSX|Insekt|
|CELLSNET-46809|De villkorliga formaten har tömt alla celler i kolumnen (kolumnerna B, C och D)|Insekt|
|CELLSNET-46778|CalculateFormula() bryter UNICHAR()-bilden|Insekt|
|CELLSNET-46781|System.Globalization.CultureInfo.CurrentCulture har ändrats|Insekt|
|CELLSNET-46244|GridDesktop Kopiera och klistra in med kommentarfel ute|Insekt|
|CELLSNET-46774|Text i rader förvrängd vid konvertering av en stor fil till PDF|Insekt|
|CELLSNET-46798|Problem med att konvertera Excel till PDF|Insekt|
|CELLSNET-46797|Understruket teckensnitt ignoreras när Excel-ark renderas till BMP/Tiff|Insekt|
|CELLSNET-46664|HeadingPairs och TitlesOfParts-taggar återställs igen efter konvertering av rensat XLS tillbaka till XLSM filformat|Insekt|
|CELLSNET-46782|Smart Marker uppdaterar inte formelreferens för tvärark|Insekt|
|CELLSNET-46784|Smarta markörer - Problem med att visa JSON listobjekt med egenskaper|Insekt|
|CELLSNET-46800|Öppna/Spara tar bort CheckBox.AlternativeText|Insekt|
|CELLSNET-46807|En del av texten saknas vid konvertering av XLS till PDF|Insekt|
|CELLSNET-42168|IndexOutOfRangeException: på Workbook.SaveToStream|Undantag|
|CELLSNET-46248|Undantag görs vid läsning av filen HTML.|Undantag|
|CELLSNET-46792|Undantag när du försöker ta bort tomma kolumner på en specifik arbetsbok|Undantag|
|CELLSNET-46799|Undantag uppstod när XLSX-filen konverterades till PDF|Undantag|
|CELLSNET-46803|Undantag "Objektreferens inte satt till en instans av ett objekt" när en XLSX-fil laddas|Undantag|
### **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for .NET. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
#### **Föråldrar HTMLLoadOptions-klassen och lägger till HtmlLoadOptions-klassen**
Använd klassen HtmlLoadOptions istället.
#### **Föråldrar klassen ODSLoadOptions och lägger till klassen OdsLoadOptions**
Använd klassen OdsLoadOptions istället.
#### **Föråldrar JSONUtility-klassen och lägger till JsonUtility-klassen**
Använd klassen JsonUtility istället.
#### **Uppdatera namnområdet Aspose.Cells.ODS som Aspose.Cells.Ods och uppdatera ODS* klasser/uppräkningar/egenskaper som Ods**
Använd uppdaterade klasser/uppräkningar/egenskaper istället.
#### **Lägger till gränssnitt IPageSavingCallback**
Kontrollera/indikera framsteg för sidsparprocessen.
#### **Lägger till klass PageSavingArgs**
Info för en process för att spara sidan.
#### **Lägger till klass PageStartSavingArgs**
Information för en sida börjar sparas.
#### **Lägger till klass PageEndSavingArgs**
Information för en sida avslutar sparprocessen.
#### **Lägger till egenskapen PdfSaveOptions.PageSavingCallback**
Kontrollera/indikera framsteg för sidsparprocessen.
