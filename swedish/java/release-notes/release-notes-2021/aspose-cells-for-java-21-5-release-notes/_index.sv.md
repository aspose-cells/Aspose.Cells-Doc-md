---
title: Aspose.Cells for Java 21.5 Release Notes
type: docs
weight: 8
url: /sv/java/aspose-cells-for-java-21-5-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 21.5](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.5/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43452|Japansk kalender som använder en Excel-funktion läses inte korrekt|
|CELLSJAVA-43420| Roterad text felaktigt justerad när den sparades som HTML|
|CELLSJAVA-43450|Problem med uppdatering av pivottabell|
|CELLSJAVA-43444|Regression: getLastSavedUniversalTime returnerar felaktigt datum|
|CELLSJAVA-43446|Cells Undantag för spårändringar|
|CELLSJAVA-43448|Regression: Ogiltig referens för lista|
|CELLSJAVA-43457|Oändlig slinga när kopierad arbetsbok sparas|
|CELLSJAVA-43442|Problem med datasortering när du klickar på rubriklänkar i GridWebs vårdemon|
|CELLSJAVA-43443|Problem med redigeringsläge i GridWeb Java|
|CELLSJAVA-43455|Teckensnitt är inte inbäddade i PDF för icke ASCII-tecken när EmbedStandardWindowsFonts ställs in på false|
|CELLSJAVA-43449|Det går inte att ändra teckensnittsfamiljen av diagramelement från "Calibri" till "Aktiv Grotesk"|
|CELLSJAVA-43454|X-axeletiketter är avskurna|
|CELLSJAVA-43445|Regression: saknade raddata för .numbers-filer|
|CELLSJAVA-43459|NullPointerException i getFormulaLocal() med anpassade GlobalizationSettings|
|CELLSJAVA-43447| Undantag "java.lang.NullPointerException" inträffade vid användning av anpassad stilfil i GridWeb|
|CELLSJAVA-43439|NegativeArraySizeException inträffar vid inläsning av arbetsbok|
|CELLSJAVA-43453|NullPointerException på Workbook.save-metoden|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till Slicer.AddPivotConnection(PivotTable pivot) metod.**

Lägger till PivotTable-anslutning för slicer.

### **Lägger till Slicer.RemovePivotConnection(PivotTable pivot) metod.**

Tar bort PivotTable-anslutning av slicer.

### **Lägger till egenskapen TxtSaveOptions.ExportAllSheets.**

Anger om alla kalkylblad exporteras till filen. Dafaut-värdet är falskt som MS Excel.

### **Lägger till FileFormatType.Numbers09 enum.**

Representerar filformatet .numbers 09. Och FileFormatType.Number kommer att representera den senaste.numbers filformattypen senare.

### **Lägger till metoden WorkbookSettings.SetPageOrientationType().**

Ställer in utskriftssidans orienteringstyp för hela filen.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisAutomatic enum.**

Använd DataBarAxisPosition.Automatic enum istället.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisMidpointe num.**

Använd DataBarAxisPosition.Midpoint enum istället.

### **Tar bort föråldrad DataBarAxisPosition.DataBarAxisNone enum.**

Använd DataBarAxisPosition.None enum istället.

### **Tar bort föråldrade DataBarBorderType.DataBarBorderNone enum.**

Använd DataBarBorderType.None enum istället.

### **Tar bort föråldrade DataBarBorderType.DataBarBorderSolid enum.**

Använd DataBarBorderType.Solid enum istället.

### **Tar bort föråldrad DataBarFillType.DataBarFillGradient enum.**

Använd DataBarFillType.Gradient enum istället.

### **Tar bort föråldrade DataBarFillType.DataBarFillSolid enum.**

Använd DataBarFillType.Solid enum istället.

### **Tar bort föråldrad DataBarNegativeColorType.DataBarColor enum.**

Använd DataBarNegativeColorTypeColor enum istället.

### **Tar bort föråldrad DataBarNegativeColorType.DataBarSameAsPositive enum.**

Använd DataBarNegativeColorType.SameAsPositive enum istället.

### **Tar bort föråldrad OleObject.FileFormatType enum.**

Använd OleObject.FileFormatType enum istället.

### **Tar bort föråldrad DynamicFilterType.Februray enum.**

Använd DynamicFilterType.February enum istället.

### **Lägger till metoden GridCells.MoveRange().**

Flyttar intervallet.

### **Lägger till metoden GridCells.InsertRange().**

Infogar ett område med växlingsalternativ.

### **Lägger till metoden GridCells.DeleteRange().**

Tar bort ett område med skiftalternativ.
