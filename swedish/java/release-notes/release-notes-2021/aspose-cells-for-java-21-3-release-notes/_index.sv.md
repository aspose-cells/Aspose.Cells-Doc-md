---
title: Aspose.Cells for Java 21.3 Release Notes
type: docs
weight: 10
url: /sv/java/aspose-cells-for-java-21-3-release-notes/
---
{{% alert color="primary" %}}

 Den här sidan innehåller release notes för[Aspose.Cells for Java 21.3](https://downloads.aspose.com/cells/java/new-releases/aspose.cells-for-java-21.3/).

{{% /alert %}}

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-43400|Stöd UNIQUE() funktion|
|CELLSJAVA-42863|Hämta diagrams undertitel|
|CELLSJAVA-43401|Stöd för enhetligt formateringsresultat för japanska eran för alla JDK:er|
|CELLSJAVA-43398|Villkorlig formatering återges inte korrekt i konverteringen ODS till HTML|
|CELLSJAVA-43388|Utdatafilen är korrupt efter kopiering av arbetsbok|
|CELLSJAVA-43406|Problem vid konvertering av HTML till Excel|
|CELLSJAVA-43399|CalculateFormula() skapar många feltypvärden #VALUE|
|CELLSJAVA-43362|Procentuellt problem för etiketter vid utskrift av diagram|
|CELLSJAVA-43384|Procentproblem för vissa etiketter vid rendering till PDF och utskrift av diagram|
|CELLSJAVA-43402|Generera exakt diagrambild från Excel-fil|
|CELLSJAVA-43408|Toppen av diagrammet skärs av och den lutande linjen går upp|
|CELLSJAVA-43412|CellsException i xlsx till html-konvertering|

## **Offentlig API och bakåtinkompatibla ändringar**

Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.

### **Lägger till egenskapen SignatureLine.Id.**

Hämtar eller ställer in identifierare för denna signaturrad.

### **Lägger till egenskapen DigitalSignature.Id.**

Anger ett UUID som kan korsreferens med UUID för signaturraden som lagras i dokumentinnehållet.

### **Lägger till egenskapen DigitalSignature.ProviderId.**

Anger klass-ID för signaturleverantören.

### **Lägger till egenskapen DigitalSignature.Image.**

Anger en bild för den digitala signaturen.

### **Lägger till egenskapen DigitalSignature.Text.**

Anger texten för den faktiska signaturen i den digitala signaturen.

### **Lägger till metoden Cells.ClearMergedCells().**

Tar bort alla sammanslagna celler.

### **Lägger till metoden Workbook.RemovePersonalInformation().**

Tar bort all personlig information.

### **Lägger till egenskapen WorkbookSettings.ForceFullCalculate.**

Egenskapen instruerar ms excel att helt beräkna varje gång en beräkning utlöses.

### **Lägger till DocxSaveOptions(Boolean) konstruktor.**

Representerar alternativ för att spara .docx-filer.

### **Tar bort föråldrad WorkbookSettings.IsWriteProtected-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.IsWriteProtected istället.

### **Tar bort föråldrad WorkbookSettings.RecommendReadOnly-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.RecommendReadOnly istället.

### **Tar bort föråldrad WorkbookSettings.WriteProtectedPassword-egenskap.**

Använd egenskapen WorkbookSettings.WriteProtection.Password istället.
