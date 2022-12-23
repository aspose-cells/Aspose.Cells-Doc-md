---
title: Aspose.Cells for Node.js via Java 21.6 Release Notes
type: docs
weight: 7
url: /sv/nodejs-java/aspose-cells-for-node-js-via-java-21-6-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Node.js via Java 21.6](https://downloads.aspose.com/cells/nodejs/new-releases/aspose.cells-for-node.js-via-java-21.6/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43466|CellsException: Fel för ZipFile vid import av ods|
|CELLSJAVA-43463|Tidslinjen är bruten efter att filen har sparats|
|CELLSJAVA-43464|PivotField.hideItem() träder inte i kraft i utdatafilen|
|CELLSJAVA-43470|Text efter en "br"-tagg inom en "th"-tagg trunkeras vid import av ett HTML-dokument|
|CELLSJAVA-43481|Får fel formel från en cell|
|CELLSJAVA-43490|Dokumentegenskaper kan inte extraheras|
|CELLSJAVA-43491|Värdet på formeln som använder datatabellen kan inte extraheras korrekt|
|CELLSJAVA-43498|Formaterat resultat av numeriskt värde är felaktigt för zh_CN-språk|
|CELLSJAVA-43451|Innehållet i Excel-filen visas felaktigt och ChangeStyle (vår) demo fungerar inte korrekt|
|CELLSJAVA-43484|Innehållslayouten är inkonsekvent i Excel med PDF-rendering|
|CELLSJAVA-43465|Saknar några serier av grafer vid konvertering av Excel till PDF|
|CELLSJAVA-43468|Problem med ekvationen av rät linje i Excel till PDF-rendering|
|CELLSJAVA-43432|Diagraminnehåll matchade inte när ett XLS-filformat sparades på nytt|
|CELLSJAVA-43475|Regression: Linjelindade celler skärs av|
|CELLSJAVA-43478|Regression: NUMBERS till PDF, mycket data saknas|
|CELLSJAVA-43485|Regression: Extra innehåll vid rendering PDF från ODS|
|CELLSJAVA-43492| Konvertering av en XML-fil (SpreadsheetML) tar bort den dolda inställningen i "Namndefinition" i utdata XLS och XLSX|
|CELLSJAVA-43486|NullPointerException vid konvertering av ett HTML-dokument till en arbetsbok|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts för allmänheten API, t.ex. tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Node.js via Java. Om du har frågor om någon ändring i listan, vänligen ta upp det på supportforumet Aspose.Cells.

### **Ändrar beteendet för egenskapen Cell.IsErrorValue.**

I gamla versioner gäller den här egenskapen endast formelceller. För att det ska överensstämma med andra egenskaper kontrollerar vi från 21.6 även icke-formelceller och om dess värde är felvärde returnerar vi också sant. Användaren kan kontrollera Cell.IsFormula-egenskapen först om han bara behöver kontrollera felvärdet för formelceller.

### **Ändrar beteendet för Cell.Value-egenskapen.**

gamla versioner returnerar den här egenskapen alltid DateTime-objekt om cellen är formaterad som datumtid och dess värde är numeriskt. Från 21.6 returnerar den här egenskapen själva det numeriska värdet om det överskrider det maximala giltiga DateTime-värdet. Med denna ändring överensstämmer det returnerade objektet med det som visas i formelfältet i ms excel.

### **Lägger till egenskapen Cell.IsNumericValue.**

Ger ett bekvämt och effektivt sätt för användaren att kontrollera om en cells värde är numeriskt värde (int, double, datetime).

### **Lägger till överbelastade metoder för Cell.SetSharedFormula()/SetArrayFormula()/SetDynamicArrayFormula().**

Stöd för att ställa in matrisformler och delade formler med fördefinierade värden.

### **Lägger till enum PdfFontEncoding.**

Representerar pdf-inbäddad teckensnittskodning.

### **Lägger till egenskapen PdfSaveOptions.FontEncoding.**

Hämtar eller ställer in inbäddad teckensnittskodning i pdf.

### **Lägger till egenskapen SlicerCacheItem.Value.**

Returnerar etiketttexten för utsnittsobjektet. Skrivskyddad.

### **Lägger till metoden GlobalizationSettings.GetProtectionNameOfPivotTable().**

Hämtar skyddsnamnet i pivottabellen.

### **Lägger till metoden FileFormatUtil.FileFormatToSaveFormat.**

Konverterar filformat till sparformat.

