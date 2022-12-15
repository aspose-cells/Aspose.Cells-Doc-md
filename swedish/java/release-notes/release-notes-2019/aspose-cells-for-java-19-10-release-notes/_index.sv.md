---
title: Aspose.Cells for Java 19.10 Release Notes
type: docs
weight: 30
url: /sv/java/aspose-cells-for-java-19-10-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 19.10.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-41814|Stöd anpassad datasortering för det specifika området i pivottabellrapporten|Ny funktion|
|CELLSJAVA-42988|Prestandaproblem med calculateFormula()|Förbättring|
|CELLSJAVA-41103|Pivottabellens datafärgning och formatering återges inte korrekt|Insekt|
|CELLSJAVA-43007|PDF genereras inte som förväntat|Insekt|
|CELLSJAVA-43025|Cell.getStyle.getCustom returnerar fel format för tysk språkversion|Insekt|
|CELLSJAVA-43013|ArrayIndexOutOfBoundsException när Excel-filen laddas|Undantag|

## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till metoden Cells.RemoveDuplicates().**
Tar bort dubbletter av data från intervallet.
### **Lägger till egenskapen OleObject.FullObjectBin**
Hämtar den fullständiga inbäddade ole-objektets binära data i mallfilen.
### **Lägger till egenskapen ContentTypeProperty.IsNillable**
Anger om egenskapen kan vara null.
### **Lägg till metoden WorkbookDesigner.SetDataSource(String,ICellsDataTable).**
Ställer in datakällan för smart markördesigner.
### **Lägger till egenskapen ImageOrPrintOptions.PageSavingCallback**
Kontrollera/indikera framsteg för sidsparprocessen.
### **Lägger till egenskapen ImageOrPrintOptions.IsFontSubstitutionCharGranularity**
Anger om teckensnittet endast byts ut när cellteckensnittet inte är kompatibelt med det.
### **Tar bort föråldrad klass HTMLLoadOptions**
Använd klassen HtmlLoadOptions istället.
### **Tar bort föråldrad klass ODSLoadOptions**
Använd klassen OdsLoadOptions istället.
### **Tar bort föråldrad klass JSONUtility**
Använd klassen JsonUtility istället.
