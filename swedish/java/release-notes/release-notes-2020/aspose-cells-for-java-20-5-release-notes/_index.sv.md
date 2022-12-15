---
title: Aspose.Cells for Java 20.5 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-20-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 20.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.5/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43173|När gruppfältet har ett nollvärde förlorar resultatet av delsummanN delsumman för nollgruppen|Förbättring|
|CELLSJAVA-43162|Excel till HTML-rendering - konverteringsprocessen tar lång tid|Insekt|
|CELLSJAVA-43164|HTML till Excel-konvertering som inte behåller de rika textformaten i utdata|Insekt|
|CELLSJAVA-43166|Roterad text renderas inte bra i XLSX till HTML-konvertering|Insekt|
|CELLSJAVA-43178|RichText-formatering går förlorad när filen exporteras till HTML|Insekt|
|CELLSJAVA-43165|Strängen "20TT1" ersattes med nummer 43850 under konvertering av CSV till XLSB|Insekt|
|CELLSJAVA-43026|Efter att ha renderat diagram till bild ändrar dataetiketter stil, och värdena är inte desamma|Insekt|
|CELLSJAVA-43154|Vissa diagrampunkter överlappar med etikett|Insekt|
|CELLSJAVA-43089|Radardiagrammet vänds och axelvärdena är inte identiska med originaldiagrammet i XLS till PDF-konvertering|Insekt|
|CELLSJAVA-43171|Dokumentet är trasigt efter kopiering av arken|Insekt|
|CELLSJAVA-43172|Ett problem med smarta markörer i sammanslagna celler|Insekt|
|CELLSJAVA-43183|Undantag "ClassCastException: ...." vid beräkning av pivottabell|Undantag|
|CELLSJAVA-43177|Ny arbetsbok med CSV-fil resulterar i "java.lang.IndexOutOfBoundsException: millisecond"|Undantag|
|CELLSJAVA-43168|Undantag "IllegalStateException: Detta är inte en strukturerad lagringsfil" vid sammanslagning av Excel-filer|Undantag|
|CELLSJAVA-43179|Undantag NumberFormatException: För inmatningssträng: "bevara"|Undantag|
|CELLSJAVA-43182|Undantag 'lang.IllegalStateException: Ogiltig kodning: null' vid laddning av XLS-fil|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till WorkbookSettings.GetThemeFont()-metoden.**
Får tematypsnitt.
### **Lägger till egenskapen DataLabels.LinkedSource.**
Hämtar och ställer in den länkade källan.
### **Lägger till DefaultEditLanguage enum.**
Representerar standardspråket för redigering.
### **Lägger till egenskapen ImageOrPrintOptions.DefaultEditLanguage.**
Hämtar eller ställer in standardspråk för redigering.
Det kan visa/rendera olika layouter för textstycken när olika redigeringsspråk är inställda.
### **Lägger till egenskapen PdfSaveOptions.DefaultEditLanguage.**
Hämtar eller ställer in standardspråk för redigering.
Det kan visa/rendera olika layouter för textstycken när olika redigeringsspråk är inställda.
