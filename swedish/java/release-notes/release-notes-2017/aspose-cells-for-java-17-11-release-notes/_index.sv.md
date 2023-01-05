---
title: Aspose.Cells for Java 17.11 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-17-11-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 17.11.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42433|ImageOrPrintOptions.PageIndex och ImageOrPrintOptions.Count egenskaper som behövs för att få bilden av önskade sidor|Ny funktion|
|CELLSJAVA-42427|Exportera rutnät med kanter visar inte rutnät innanför gränsen i Excel till HTML-rendering|Insekt|
|CELLSJAVA-42438|LightCellsDataProvider tar bort ledande och efterföljande utrymmen|Insekt|
|CELLSJAVA-42422|Felaktigt teckensnitt används i PDF-utgången i MS Excel-diagrammet|Insekt|
|CELLSJAVA-42353|Några pilar eller anrop saknas i utgången HTML|Insekt|
|CELLSJAVA-42455|Den andra kommentaren saknas i kalkylbladets kommentarsamling|Insekt|
|CELLSJAVA-42454|Skapandet av arbetsbok verkar hänga sig när man läser från en XLSM-fil|Insekt|
|CELLSJAVA-42450|Style.QuotePrefix-egenskapen fungerar inte för filen XLSB|Insekt|
|CELLSJAVA-42445|Inställning av bilddata påverkar det andra diagrammet och det visas fel|Insekt|
|CELLSJAVA-42444|CheckBox.setName()-metoden fungerar i MS Excel 2016 men fungerar inte i MS Excel 2007|Insekt|
|CELLSJAVA-42443|MS Excel-filter konverteras inte korrekt - XLSB till XLSM konvertering|Insekt|
|CELLSJAVA-42442|Att ändra värdet på ComboBoxActiveXControl ändrar inte värdet på den länkade cellen|Insekt|
|CELLSJAVA-42435|Cells.setColumnWidthPixel och Cells.setRowHeightPixel har olika beteenden|Insekt|
|CELLSJAVA-42431|Om du utökar tabellintervallet muteras cellinnehållet oväntat|Insekt|
|CELLSJAVA-42434|Undantag: "java.lang.NumberFormatException" vid inläsning av ett HTML filformat|Undantag|
|CELLSJAVA-42448|Cells.deleteBlankRows orsakar undantaget "java.lang.ArrayIndexOutOfBoundsException: 1937"|Undantag|
|CELLSJAVA-42426|Undantag i tråden "huvud" java.lang.OutOfMemoryError: GC overhead-gränsen har överskridits - fil III|Undantag|
|CELLSJAVA-42425|Undantag i tråden "huvud" java.lang.OutOfMemoryError: GC overhead-gränsen har överskridits - Fil II|Undantag|
|CELLSJAVA-42424|Undantag i tråden "huvud" java.lang.OutOfMemoryError: GC overheadgränsen överskrids - Fil I|Undantag|
|CELLSJAVA-42428|Chart.toImage resulterar i java.lang.ArrayIndexOutOfBoundsException|Undantag|
|CELLSJAVA-42452|Att spara en arbetsbok som PDF efter RemoveUusedStyles API producerar ett CellsException|Undantag|
|CELLSJAVA-42440|"java.lang.IllegalArgumentException: Ogiltigt radindex" inträffade|Undantag|
|CELLSJAVA-42439|Undantag: "java.lang.IllegalArgumentException: Ogiltigt radindex" för att spara ett XLSX filformat|Undantag|
|CELLSJAVA-42437|Undantag: java.lang.NumberFormatUndantag när ett XLSB filformat sparas på nytt|Undantag|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till metoden Shape.GetResultOfSmartArt().**
Konvertera den smarta konsten till en gruppform.
### **Lägger till egenskapen Shape.IsSmartArt**
Indikerar om formen är smart konst.
### **Lägger till metoderna Workbook.ProtectSharedWorkbook() och Workbook.UnprotectSharedWorkbook()**
Skyddar och tar bort skyddet för den delade arbetsboken.
### **Lägger till enum StyleModifyFlag.Spacing**
Anger avståndet mellan tecken i en textkörning.
### **Lägger till egenskapen PdfSaveOptions.IgnoreError**
Indikerar om du behöver dölja felet under renderingen.
### **Lägger till egenskapen ImageOrPrintOptions.PageIndex**
Hämtar eller ställer in det 0-baserade indexet för den första sidan som ska sparas.
### **Lägger till egenskapen ImageOrPrintOptions.PageCount**
Hämtar eller ställer in antalet sidor som ska sparas.
### **Lägger till egenskapen XmlMap.RootElementName**
Hämtar namnet på rotelementet.
### **Lägger till metoden Worksheet.XmlMapQuery(strängsökväg, XmlMap xmlMap).**
Fråga cellområden som mappade/länkade till den specifika sökvägen för xml-kartan.
### **Lägger till egenskapen LoadOptions.AutoFitterOptions**
Hämtar och ställer in alternativen för automatisk montering.


### **Användningsexempel**
Kontrollera listan med hjälpämnen som lagts till i Aspose.Cells Wiki-dokument:

- [Konvertera den smarta konsten till gruppform](/cells/sv/java/convert-the-smart-art-to-group-shape/)
- [Skapa delad arbetsbok med Aspose.Cells](/cells/sv/java/create-shared-workbook-with-aspose-cells/)
- [Bestäm om Shape är Smart Art Shape](/cells/sv/java/determine-if-shape-is-smart-art-shape/)
- [Hitta rotelementets namn på XML-karta](/cells/sv/java/find-the-root-element-name-of-xml-map/)
- [Ignorera fel när du renderar Excel till Pdf](/cells/sv/java/ignore-errors-while-rendering-excel-to-pdf/)
- [Lösenordsskydda eller avskydda den delade arbetsboken](/cells/sv/java/password-protect-or-unprotect-the-shared-workbook/)
- [Fråga Cell Områden mappade till Xml Map Path med metoden Worksheet.XmlMapQuery](/cells/sv/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)
- [Rendera sekvens av sidor med hjälp av PageIndex och PageCount Properties för ImageOrPrintOptions](/cells/sv/java/render-sequence-of-pages-using-pageindex-and-pagecount-properties-of-imageorprintoptions/)
