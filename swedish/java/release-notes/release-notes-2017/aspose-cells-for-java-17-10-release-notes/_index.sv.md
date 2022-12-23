---
title: Aspose.Cells for Java 17.10 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-17-10-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 17.10](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-17.10/).

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42423|Avbryt långvarig beräkning av Workbook.calculateFormula-metoden|Ny funktion|
|CELLSJAVA-42414|Få SheetId-fältet i MS Excel-kalkylbladet|Ny funktion|
|CELLSJAVA-42402|Bra HTML behövs för det bifogade HTML|Förbättring|
|CELLSJAVA-42372|Positionen för långa bindestreck är inte samma som Microsoft Excel|Förbättring|
|CELLSJAVA-42399|Pilpunkterna är inte tydliga i utdata-Pdf|Insekt|
|CELLSJAVA-42419|Texten trunkeras i utgången HTML|Insekt|
|CELLSJAVA-42418|Kantfärgen matchar inte som MS Excel i utdata HTML|Insekt|
|CELLSJAVA-42417|Bakgrundsfärgen matchar inte som Ms Excel i utdata HTML|Insekt|
|CELLSJAVA-42385|callback IFilePathProvider anropas aldrig och då har filen HTML 'null' i sökvägen|Insekt|
|CELLSJAVA-42412|Värdeaxeletiketter saknas vid konvertering av Excel till PDF|Insekt|
|CELLSJAVA-42408|Textöverlappning Problem efter rendering av kalkylblad till bild|Insekt|
|CELLSJAVA-42420|Problem med annullering och slut på minne på grund av stort dataområde i diagrammet|Insekt|
|CELLSJAVA-42415|Utdatadiagram är inte som originaldiagrammet i utdata HTML|Insekt|
|CELLSJAVA-42410|Diagramområdet, etiketter, förklaringar etc. återges felaktigt i utdata PDF och PNG|Insekt|
|CELLSJAVA-42409|Diagramområdet återges inte korrekt i PDF- och PNG-utgångarna i MS Excel-diagrammet|Insekt|
|CELLSJAVA-41046|Diagrammets förklaringssekvens har ändrats när kalkylbladet renderades till formatet PDF|Insekt|
|CELLSJAVA-40416|Färger och stil på diagrammet går förlorade|Insekt|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till AbstractCalculationMonitor.Interrupt(string)-metoden**
Tillåter användare att avbryta fortskridandet av formelberäkningar.
### **Lägger till HtmlCrossType.MSExport enum**
Visar strängen som MS Excel som exporterar HTML.
### **Lägger till egenskapen Worksheet.TabId**
Hämtar den interna identifieraren för arket.
### **Lägger till enum OLEDBCommandType.None**
Kommandotypen är inte specificerad.
### **Lägger till enum ConnectionDataSourceType**
Representerar datakällans typ av anslutning.
### **Föråldrade egenskapen ExternalConnection.Credentials och ExternalConnection.ReConnectionMethod**
Använd egenskapen ExternalConnection.CredentialsMethodType och ExternalConnection.ReconnectionMethodType istället.
### **Föråldrade egenskapen WebQueryConnection.EditPage**
Använd egenskapen WebQueryConnection.EditWebPage istället.
### **Lägger till egenskapen Series.ValuesFormatCode**
Representerar nummerformatets kod för serievärden.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Ställ in värdeformatets kod för diagramserien](/cells/sv/java/set-the-values-format-code-of-chart-series/)
- [Använd egenskapen Sheet.SheetId för OpenXml med Aspose.Cells](/cells/sv/java/utilize-sheet-sheetid-property-of-openxml-using-aspose-cells/)
- [Läs och skriv extern anslutning av XLSB-fil](/cells/sv/java/read-and-write-external-connection-of-xlsb-or-xls-file/)
- [Avbryt eller avbryt formelberäkningen av arbetsboken](/cells/sv/java/interrupt-or-cancel-the-formula-calculation-of-workbook/)
- [Ange hur strängen ska korsas i utdata HTML med HtmlCrossType](/cells/sv/java/specify-how-to-cross-string-in-output-html-using-htmlcrosstype/)
