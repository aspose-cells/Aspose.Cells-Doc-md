---
title: Skapa pivottabell
linktitle: Skapa pivottabell
description: Skapa och formatera pivottabeller med Aspose.Cells for Java.
keywords: Skapa pivottabell, Infoga pivottabell, Formatera pivottabell.
type: docs
weight: 160
url: /sv/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Vad är en pivottabell?**
En pivottabell är en interaktiv sammanfattningsrapport: den komprimerar en stor mängd rådata, ordnad rad för rad, till en kompakt matris utan en enda formel. Du bestämmer vilka kolumner som blir radetiketter, vilka som blir kolumnetiketter och vilka som aggregeras som värden – pivottabellen sköter grupperingen och beräkningen:
- **Sammanfatta** – den totala försäljningen per produkt, region eller kvartal i stället för långa formelkedjor.
- **Jämför** – kategorier på raderna och perioder i kolumnerna omvandlar en platt lista till en korsrapport där trender syns med en blick.
- **Granska detaljer** – dubbelklicka på ett valfritt sammanfattningsvärde för att granska källraderna bakom det.
- **Uppdatera** – när källdatan ändras räknar en uppdatering om hela rapporten.
Typiska användningsfall är säljinstrumentpaneler, kostnadsfördelningar och lageranalyser – i praktiken frågor av formen ”hur fördelas dessa siffror efter kategori och tid?”. Aspose.Cells for Java bygger samma slags pivottabeller programmatiskt, så att de arbetsböcker som ditt program genererar kan innehålla färdiga rapporter i stället för enbart rådata.

### **Skapa pivottabell med Aspose.Cells**

{{% alert color="primary" %}}
Med Aspose.Cells kan du lägga till pivottabeller i kalkylblad. Aspose.Cells har ett antal särskilda klasser som används specifikt för att skapa och styra pivottabeller. Dessa klasser används för att skapa och ange egenskaperna för ett [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-objekt, som utgör byggblocken i pivottabellen.
Pivottabellobjekten är:
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField): representerar ett fält i en pivottabell.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection): representerar en samling av alla [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField)-objekt i pivottabellen.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable): representerar en pivottabell.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): representerar samlingen av alla pivottabellobjekt på kalkylbladet.
{{% /alert %}}

### **Skapa en enkel pivottabell**
Att skapa en pivottabell är en process i tre steg: skriv källdatan till celler i kalkylbladet, lägg till pivottabellen på den avsedda platsen och placera pivotfälten i rad-, kolumn- och dataområdena.
1. Lägg till data i kalkylbladets celler med hjälp av [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell)-objektets [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-)-metod (`putValue` i de flesta exempel). Denna data används som pivottabellens datakälla.
2. Lägg till en pivottabell i kalkylbladet genom att anropa metoden [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) i klassen [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection): `add(sourceData, row, column)`. `sourceData` är källintervallet (till exempel "A1:C8"); `row` och `column` är de nollbaserade koordinaterna för destinationscellen i pivottabellens övre vänstra hörn (cell E3 innebär rad 2, kolumn 4). Metoden returnerar det nya [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-objektet direkt.
3. Placera pivotfälten med hjälp av [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable)-objektets `addFieldToArea`-metod: ett fältnamn placeras i radområdet (`PivotFieldType.ROW`), kolumnområdet (`PivotFieldType.COLUMN`) eller dataområdet (`PivotFieldType.DATA`).
4. Spara arbetsboken – pivottabellen skrivs till den sparade filen.
Exempelkoden nedan skapar en enkel pivottabell enligt dessa steg. När koden körs läggs en pivottabell baserad på källdatan till i kalkylbladet:
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Skapa en ny arbetsbok och hämta det första kalkylbladet
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Skriv källdatan: försäljning per sport och kvartal
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// Lägg till en pivottabell vid destinationscellen E3, med data från A1:C8
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Tilldela pivotfält: Sport till Rader, Quarter till Kolumner, Sales till Data
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Spara arbetsboken
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
När ett cellintervall används som datakälla måste det anges från den övre vänstra till den nedre högra hörnet. För exempel är "A1:C3" ett giltigt intervall, medan "C3:A1" är ogiltigt.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}