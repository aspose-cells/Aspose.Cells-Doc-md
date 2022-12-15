---
title: Aspose.Cells for Java 18.11 Release Notes
type: docs
weight: 20
url: /sv/java/aspose-cells-for-java-18-11-release-notes/
---
{{% alert color="primary" %}} 

Den här sidan innehåller utgåvor för Aspose.Cells for Java 18.11.

{{% /alert %}} 

|**Nyckel**|**Sammanfattning**|**Kategori**|
|:- |:- |:- |
|CELLSJAVA-42738|Fel räkning av valideringsvärden läses från XLSX|Förbättring|
|CELLSJAVA-42734|Problem samtidigt som på varandra följande avgränsare behandlas som distinkta|Förbättring|
|CELLSJAVA-42739|Aspose.Cells.GridWeb (Java) kraschar när den används samtidigt i en miljö med flera användare|Insekt|
|CELLSJAVA-42737|Diagramlinje saknas i XLSX->PNG-konvertering|Insekt|
|CELLSJAVA-42735|Problem med metoden getActualChartSize|Insekt|
|CELLSJAVA-40861|SmartArt kopierar inte när arbetsboken kopieras|Insekt|
## **Offentlig API och bakåtinkompatibla ändringar**
Följande är en lista över alla ändringar som gjorts för allmänheten API, såsom tillagda, bytt namn, borttagna eller utfasade medlemmar samt alla icke-bakåtkompatibla ändringar som gjorts till Aspose.Cells for Java. Om du har frågor om någon ändring som anges, vänligen ta upp den på supportforumet Aspose.Cells.
### **Lägger till egenskapen PivotTable.RefreshedByWho**
Hämtar namnet på användaren som uppdaterade pivottabellen förra gången.
### **Lägger till egenskapen PivotTable.RefreshDate**
Hämtar datumet då pivottabellen uppdaterades förra gången.
### **Lägger till egenskaper för CalculationData.CellRow/CellColumn**
Ger ett effektivt sätt för användaren att hämta cellens rad- och kolumnindex istället för att hämta objektet Cell.
### **Lägger till CalculationCell-klass**
Representerar beräkningsdata för en cell som beräknas.
### **Lägger till metoden AbstractCalculationMonitor.OnCircular(IEnumerator circularCellsData)**
Ger en metod för användare att samla in och bearbeta cirkulära referenser.
### **Lägger till egenskapen TxtLoadOptions.TreatConsecutiveDelimitersAsOne**
Tillåter användaren att välja om konsekutiva avgränsare ska tas som en när CSV-fil importeras.
### **Lägger till metoden FormatCondition.SetFormulas(strängformel1, strängformel2, bool ärR1C1, bool ärLokal)**
Ger ett effektivt och bekvämt sätt för användaren att ställa in formler för FormatCondition.
### **Lägger till metoden Validation.GetListValue(int row, int column).**
Tillåter användaren att få värdet för att skapa listan för validering av specifik cell.
### **Föråldrad ValidationCollection.Add(Validation validation) metod**
Använd metoden ValidationCollection.Add(CellArea) istället.
### **Lägger till metoden Validation.Copy(Aspose.Cells.Validation,Aspose.Cells.CopyOptions)**
Kopior validering.
### **Lägger till egenskaperna CreatedUniversalTime,LastPrintedUniversalTime och LastSavedUniversalTime för BuiltInDocumentPropertyCollection**
Returnerar UTC-tid om de inbyggda egenskaperna.
### **Lägger till egenskapen OoxmlSaveOptions.UpdateSmartArt**
Indikerar om den smarta konsten uppdateras.
### **Lägger till SmartArtShape-klass**
Representerar den smarta konstformen.
