---
title: Aspose.Cells for Node.js via Java 23.2 Release Notes
type: docs
weight: 11
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-23-2-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 23.2](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-23.2/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
| :- | :- | :- |
|CELLSJAVA-43438|Fyll i `<Application>`-taggen i XLSX|
|CELLSJAVA-45119|När du läser in i 03-format excel, bearbetas inte "FillType" för den raka linjen|
|CELLSJAVA-45128|Horisontell flip verkar saknas när du läser pillinjer|
|CELLSJAVA-45061|XLS till HTML: Bild sträckt|
|CELLSJAVA-45062|XLS till HTML: Pilförskjutning|
|CELLSJAVA-45085|Diagram spridda problem i Excel till PDF rendering|
|CELLSJAVA-45118|Ofullständig formvisning efter rotation när du sparar till pdf|
|CELLSJAVA-45078|SUMMEDELsberäkning `#VALUE!` |
|CELLSJAVA-45088|Det visade resultatet är felaktigt för resulterande html när cellvärdet är sträng med anpassat format|
|CELLSJAVA-45094|Globala namngivna intervall med referenser som `=!$K$23` bryter i den nya versionen|
|CELLSJAVA-45115|Metoden deleteRows orsakar felaktig formatering|
|CELLSJAVA-45077|Den sparade filen rapporterar ett fel när den laddas upp och öppnas på Onedrive-disken|
|CELLSJAVA-45109|Ett undantag görs vid konvertering av diagram till bild|
|CELLSJAVA-45112|Gör en speciell större rutnätslinje för radardiagram|
|CELLSJAVA-45103|Färgade bilder som infogas i excel blir svarta när de konverteras till pdf|
|CELLSJAVA-45155| Center Across text skärs bort om den finns i den sista kolumnen vid konvertering till pdf|
|CELLSJAVA-45160|HTML till EXCEL-konvertering misslyckades med felet Ogiltig `#`|
|CELLSJAVA-45079|Anpassat nummerformat med efterföljande punkter ignoreras vid export till HTML|
|CELLSJAVA-45084|Teckensnittet har ändrats i den återsparade xls-filen|
|CELLSJAVA-45106|Resultatfilen är onormal vid konvertering av excel till html|
|CELLSJAVA-45117|Formroteringsfel när du sparar till html|
|CELLSJAVA-45123|Bågformen ska vändas horisontellt i Excel 95|
|CELLSJAVA-45132|Stöd mönsterfyllning av form i Excel95/5.0|
|CELLSJAVA-45147|En del text i den sista kolumnen skärs bort när filen sparas till html|
|CELLSJAVA-45148|Sammanslagna områden förlorade efter att ha sparats som html|
|CELLSJAVA-45087|Ramen visas på texten för diagramtiteln i Excel till PDF-rendering|

##  **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

###  **Lägger till egenskapen ChartTextFrame.IsAutomaticRotation**

Indikerar om texten i diagrammet roteras automatiskt.

###  **Föråldrade egenskaperna JsonLayoutOptions.IgnoreObjectTitle och JsonLayoutOptions.IgnoreArrayTitle**

Använd egenskapen JsonLayoutOptions.IgnoreTitle istället.

###  **Lägger till egenskapen JsonLayoutOptions.IgnoreTitle**

Ingores titlar på Json-attribut vid konvertering av json till Excel.

###  **Lägger till metoden Style.ToJson().**

Konverterar stil av Excel-filer till json-fil

###  **Lägger till metoden Cell.ToJson().**

Konverterar en cell med celler till json-fil.
