---
title: Aspose.Cells för Java 20.8 Release Notes
type: docs
weight: 8
url: /sv/java/aspose-cells-for-java-20-8-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells för Java 20.8](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-20.8/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43242|En av stiltaggen som finns utanför Head-taggen|Insekt|
|CELLSJAVA-43157|Anpassad dataseriefärg bevaras inte när du skapar ett vattenfallsdiagram|Insekt|
|CELLSJAVA-43240|Oavsiktliga radbrytningar i former/objekt vid konvertering av Excel till PDF|Insekt|
|CELLSJAVA-43255|Prestandaproblem vid konvertering av Excel till PDF|Insekt|
|CELLSJAVA-43250|Utökade etikettceller slås inte samman i SmartMarker|Insekt|
|CELLSJAVA-43253|Att spara filen med OoxmlSaveOptions efter att ha ersatt text i SmartArt konverterar XLS till XLSX|Insekt|
CELLSJAVA-43170|CellUndantag på calculateFormel-metod|Undantag|

## **Public API och bakåtinkompatibla ändringar**

Följande är en lista över eventuella ändringar som gjorts i det offentliga API:t som tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts i Aspose.Cells för Java. Om du har funderingar på någon av de listade ändringarna, vänligen ta upp det på Aspose.Cells supportforum.

### **Markerar gränssnittet ICustomFunction som föråldrat.**

 Detta gränssnitt orsakar ibland oklarheter och missförstånd för användarna. Användaren ska använda**AbstractCalculation Engine** istället som ger mer bekväma och flexibla API:er för att manipulera anpassade funktioner.

### **Markerar egenskapen CalculationOptions.CustomFunction som föråldrad.**

Snälla använd**AbstractCalculation Engine** istället för**ICustomFunction** av egenskapen CalculationOptions.CustomEngine.

### **Markerar Workbook.CalculateFormula(bool, ICustomFunction)-metoden som föråldrad.**

Snälla använd**Workbook.CalculateFormula(CalculationOptions) metod** istället.

### **Markerar Worksheet.CalculateFormula(bool, bool, ICustomFunction)-metoden som föråldrad.**

Snälla använd**Worksheet.CalculateFormula(CalculationOptions, bool)** metod istället.

### **Markerar Cell. Beräkna (bool, ICustomFunction)-metoden som föråldrad.**

Snälla använd**Cell. Beräkna (Beräkningsalternativ)** metod istället.

### **Lägger till DocxSaveOptions-klassen och SaveFormat.Docx enum**

Representerar alternativen och uppräkningen för att spara arbetsboken som .docx-filer.

### **Lägger till klass PptxSaveOptions och SaveFormat.Pptx enum**

Representerar alternativen och uppräkningen för att spara arbetsboken som .pptx-filer.

### **Lägger till klassen PowerQueryFormulaFunction**

Representerar power query formel funktion.

### **Lägger till SaveOptions.UpdateSmartArt och tar bort OoxmlSaveOptions.UpdateSmartArt-egenskapen**

Anger om texten i smarta konstformer uppdateras när filer sparas.

### **Lägger till metoden SlicerCollection.Add(ListObject table, int index, string destCellName)**

Lägg till en ny Slicer med ListObject som datakälla.

### **Lägger till metoden SlicerCollection.Add(ListObject table, ListColumn listColumn, string destCellName)**

Lägg till en ny Slicer med ListObject som datakälla.

### **Lägger till metoden SlicerCollection.Add(ListObject table, ListColumn listColumn, int rad, int kolumn)**

Lägg till en ny Slicer med ListObject som datakälla.
