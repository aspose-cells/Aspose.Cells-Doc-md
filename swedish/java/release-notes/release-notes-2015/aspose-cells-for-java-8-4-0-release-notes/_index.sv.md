---
title: Aspose.Cells for Java 8.4.0 Release Notes
type: docs
weight: 80
url: /sv/java/aspose-cells-for-java-8-4-0-release-notes/
---
{{% alert color="primary" %}} 

 Den här sidan innehåller release notes för[Aspose.Cells for Java 8.4.0](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-8.4.0/)

{{% /alert %}} 

\1) Aspose.Cells

Andra förbättringar och förändringar

Nya egenskaper

(CELLSJAVA-41198) - Extrahera temadata från Excel-filer
(CELLSJAVA-41185) - Generera datafältsbilder

Förbättringar

(CELLSJAVA-41169) - Ta bort falska nullattribut i den genererade HTML-filen
(CELLSJAVA-41179) - Japansk kalenderstöd

Buggar

(CELLSJAVA-41222) - Pivottabellens sorteringsfält är fel i XLSX-utdata
(CELLSJAVA-41173) - HtmlSaveOptions.setExportHiddenWorksheet(true) fungerar inte korrekt
(CELLSJAVA-41168) - Ändringar i beskärning av korscellstext sedan 8.3.1 till 8.3.1.5
(CELLSJAVA-41167) - Uppdatering av pivottabeller genererar korrupt arbetsbok
(CELLSJAVA-41232) - Bug - Formeln innehåller ett definierat namn som slutar med nummer+e
(CELLSJAVA-41215) - EMF genererad med Aspose.Cells återges olika i olika tittare
(CELLSJAVA-41196) - XLSB blir skadad efter att ha lagt till ett kalkylblad och ett cellvärde
(CELLSJAVA-41227) - API kan inte ersätta Arial-teckensnittet med Liberation Fonts
(CELLSJAVA-41224) - Fel vid bildkonvertering vid rendering av Excel till PDF
(CELLSJAVA-41223) - Signering av exporterade PDF-filer misslyckas
(CELLSJAVA-41208) - Rendering Hints (Anti Aliasing) fungerar inte med SheetRender
(CELLSJAVA-41193) - Wingdings-symboler återges inte korrekt när kalkylbladet renderas till bild
(CELLSJAVA-41184) - Problem med utdatabildåtergivning från diagrammet
(CELLSJAVA-41106) - Dataetiketter för cirkeldiagram överlappar varandra i diagrambilden
(CELLSJAVA-40941) - Överlappning av dataetiketter i cirkeldiagram när diagram renderas som bild
(CELLSJAVA-40813) - Cirkeldiagrammets dataetikett överlappar i den återgivna HTML-koden
(CELLSJAVA-41182) - Slät linje är inte korrekt när punktfärgen är annorlunda

Undantag

(CELLSJAVA-41201) - java.lang.IllegalArgumentException: Okänt område, vid PivotTable.refreshData
(CELLSJAVA-41192) - Undantag: "java.lang.Exception: End of stream nådd" vid öppning av en XLS-fil
(CELLSJAVA-41228) - java.lang.ArrayIndexOutOfBoundsException på Workbook ctor när en XLS laddas
(CELLSJAVA-41211) - Undantag uppstår vid lösning av formelreferens när filnamnet ställs in med Workbook.setFileName()

\2) Aspose.Cells Grid Suite

Andra förbättringar och förändringar

(CELLSJAVA-41202) - Visa Cell Kommentarer i GridWeb-komponent

Buggar

(CELLSJAVA-41214) - Att dra radhöjden till 0 gör att GridWeb inte visar värdet
(CELLSJAVA-41209) - Datavalideringslistan visas inte i GridWeb
(CELLSJAVA-41205) - När kanterna är tjocka ökar höjden när cellvärdet tas bort i GridWeb
(CELLSJAVA-41204) - När kanterna är tjocka matchar inte rubrikhöjderna i GridWeb
(CELLSJAVA-41203) - Rubrik och cellbredd matchar inte i GridWeb
(CELLSJAVA-41073) - Bredden på rubriker för kolumner skiljer sig från bredden på celler i Chrome/Opera

Offentlig API och bakåtinkompatibla ändringar

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

 Lägger till attributet HtmlSaveOptions.ExportBogusRowData
Anger om falsk data på nedre raden exporteras. standardvärdet är sant.

 Lägger till attributet HtmlSaveOptions.CellCssPrefix
Hämtar och ställer in prefixet för css-namnet, standardvärdet är "".

 Lägger till metoden PivotTable.ShowInCompactForm().
Layouter pivottabellen i kompakt form.

 Lägger till metoden PivotTable.ShowInOutlineForm().
Layouter pivottabellen i konturform.

Lägger till metoden PivotTable.ShowInTabularForm().
Layouter pivottabellen i tabellform.

 Lägger till metoden PivotTableCollection.Remove(PivotTable PivotTable).
Tar bort den angivna pivottabellen

 Lägger till metoden PivotTableCollection.RemoveAt(int index).
Tar bort pivottabellen vid det angivna indexet

 Lägger till klasserna Aspose.Cells.Vba namespace, VbaPorject, VbaModuleCollection och VbaModule.
De används för att läsa och ändra VBA-projektet i filen.

 Lägger till egenskapen Border.ThemeColor.
Hämtar och ställer in gränsens temafärg.

 Lägger till klassen TxtLoadStyleStrategy och egenskapen TxtLoadOptions.LoadStyleStrategy.
Indikerar strategin för att tillämpa stil för analyserade värden vid konvertering av strängvärde till nummer eller datum och tid.

 Föråldrade TxtLoadOptions.KeepExactFormat-metoder.
Använd egenskapen TxtLoadOptions.LoadStyleStrategy istället.

 Föråldrade metoderna Cells.GetCellByIndex() och Row.GetCellByIndex().
Använd metoden GetEnumerator() för att iterera alla celler istället.

 Obsoletes DrawObject.Image-egenskapen
Använd egenskapen DrawObject.ImageBytes för att hämta bilddata istället.

 Lägger till egenskapen DrawObject.ImageBytes
Får byte av bild som konverteras från diagram eller form.


Notera
Eftersom kodbasen för Aspose.Cells for Java matchar koden för relevant version .NET, är de flesta ändringar, förbättringar och korrigeringar som ingår i Aspose.Cells for .NET v8.4.0 också inkluderade i denna 076157316.0.481.
