---
title: SmartMarker-rendering av array i en enda cell | Aspose.Cells for Java
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av Smart Marker-attributen `arrayassingle` och `arraydelimiter` i Aspose.Cells for Java.
linktitle: SmartMarker-rendering i en enda cell | Aspose.Cells
url: /sv/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, Smart Markers, arrayassingle, arraydelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kan rendera en arraydatakälla till en enda cell via Smart Markers. Attributet `arrayassingle` stänger av standardspridningen element för element, och attributet `arraydelimiter` väljer den separator som placeras mellan de sammanfogade elementen – komma som standard, eller valfritt enskilt tecken eller en citerad sträng med flera tecken som du anger.
{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en mallbaserad funktion som dynamiskt fyller kalkylblad med data med hjälp av marköruttryck som `&=DataSource.Field`. Markören placeras i en designarbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard expanderar motorn arrayen och placerar varje element i en egen cell när en Smart Marker refererar till en arrayegenskap, till exempel `&=Product.Tags`, som är bunden till en `String[]` med fyra värden. Värdena sprids då lodrätt nedåt i kolumnen under markören. Det här beteendet är bekvämt i många scenarier, men det finns situationer där du hellre vill rendera hela arrayen till en enda cell, med elementen sammanfogade och åtskilda av en valfri separator.
Attributen `arrayassingle` och `arraydelimiter`, som skrivs inom en Smart Markers parenteser i formen `name:value`, tar itu med just detta behov. De gör att du kan hålla rapportupplägg kompakta och förutsågbara samtidigt som du arbetar direkt med arraydatakällor.

## **Varför funktionen behövs**

### **Standardbeteende för arrayspridning**

När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells arrayen över flera celler som standard. En markör som `&=Product.Tags` med en `String[]` som innehåller fyra värden placerar till exempel varje värde i en egen cell under markören, vilket flyttar annat innehåll i mallen och kan bryta noggrant utformade rapportupplägg.

### **Begränsningar i användningsfall**

Det finns många praktiska situationer där standardspridningen är olämplig:
- **Sammanfattande rapporter** som behöver ett kompakt upplägg med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas med komma eller vertikalstreck som separator i en enda cell.
- **Filteretiketter eller statusindikatorer** som grupperar flera värden på samma ställe för att underlätta läsning.
- **Nedströmsflöden** (CSV-export, PDF-rendering och sammanslagning av utskick) som förväntar ett enda konsoliderat värde per cell i stället för ett expanderat intervall.
- **Plattformsoberoende kompatibilitet**, där vissa konsumenter inte kan hantera arrays som sprids över flera celler.

### **Problemet som löses**

Utan en inbyggd mekanism skulle utvecklare tvingas att förbehandla data i Java – sammanfoga arrayer till avgränsade strängar innan de kopplas till `WorkbookDesigner`. Det duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `arrayassingle` och `arraydelimiter` eliminerar denna omvägning genom att hantera formateringen deklarativt i själva Smart Markern.

## **Funktionens fördelar**

Att använda attributen `arrayassingle` och `arraydelimiter` i dina Smart Markers ger flera fördelar:
- **Sammanhållning i en cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouten kompakt och förutsägbar.
- **Kontroll över separator**: Ange den separator du vill – standardskomma, semikolon, bindestreck, vertikalstreck eller en citerad sträng med flera tecken som `" | "`.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna finns i Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande innehåll i mallen till andra rader eller kolumner.
- **Flexibla datatyper**: Fungerar med strängarrayer och numeriska värden som återges som strängar från JavaBean-datakällor.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras den ursprungliga spridningen, så befintliga mallar fortsätter att fungera oförändrat.

## **Så använder du funktionen**

### **Syntax för Smart Marker**

Attributen `arrayassingle` och `arraydelimiter` använder grammatiken `name:value` från Aspose.Cells inom parenteserna i en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Markören består av följande delar:
- `&=DataSource.ArrayProperty` – den vanliga Smart Marker som refererar till arrayegenskapen i den bundna datakällan.
- `arrayassingle:true` – instruerar motorn att rendera hela arrayen till en enda cell i stället för att sprida elementen.
- `arraydelimiter:;` – valfritt; definierar separatorn mellan arrayelementen. När det utelämnas används ett komma.

{{% alert color="warning" %}}
Skriv attribut i formen `name:value` (ett kolon, inte ett likhetstecken) och separera flera attribut med ett komma **utan mellanslag**. Ett mellanslag efter kommat förskjuter det parsade värdet med en teckenposition – `(arrayassingle:true, arraydelimiter:;)` skulle sammanfoga med den felaktiga separatorn `:;` i stället för `;`.
{{% /alert %}}

### **Former för separatorer**

- Ett enskilt tecken skrivs direkt efter kolonet: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- En separator med flera tecken skrivs inom dubbla citattecken: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Arbetsflöde steg för steg**

Följande arbetsflöde beskriver hur du renderar en array till en enda cell med hjälp av Smart Markers.
1. **Förbered datakällan**: Skapa en `public` JavaBean-klass med en gettermetod som returnerar arrayen, till exempel `String[] getTags()`, och bind en `java.util.List` med JavaBean-objekt så att motorn läser en post per rad. Enbart offentliga fält räcker inte – motorn läser JavaBean-gettermetoder.
2. **Skapa en designarbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayegenskapen, med attributet `arrayassingle` och `arraydelimiter` när en anpassad separator behövs.
3. **Instantiera `WorkbookDesigner`**: Skapa en `WorkbookDesigner` för arbetsboken och bind listan med `setDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera markörerna och fylla arbetsboken med verkliga data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller något annat filformat som stöds.

### **Kodexempel 1 – Grundläggande rendering av strängarray**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    // The bean must be public and expose a getter; public fields bind nothing
    public static class Product {
        private String[] tags;
        public String[] getTags() { return tags; }
        public void setTags(String[] tags) { this.tags = tags; }
    }

    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.setTags(new String[] { "C#", "Aspose", "SmartMarker", "Excel" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Product", Arrays.asList(product));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-single.xlsx");
    }
}
```

Exemplet skriver ut det sammanfogade värdet av hela arrayen. De fyra taggarna hamnar i en cell, åtskilda av standardskommatecken:

```
C#,Aspose,SmartMarker,Excel
```

### **Kodexempel 2 – Numeriska värden med en anpassad separator**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Student {
        private String[] scores;
        public String[] getScores() { return scores; }
        public void setScores(String[] scores) { this.scores = scores; }
    }

    public static void main(String[] args) throws Exception {
        Student student = new Student();
        student.setScores(new String[] { "95", "88", "76", "100", "67" });
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);
        worksheet.getCells().get("A1").putValue("Scores");
        // arraydelimiter:- joins the values with a hyphen
        worksheet.getCells().get("A2").putValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Student", Arrays.asList(student));
        designer.process();
        System.out.println(worksheet.getCells().get("A2").getStringValue());
        workbook.save("output-array-numeric.xlsx");
    }
}
```

Numeriska värden sammanfogas på samma sätt som strängar när arrayegenskapen returnerar `String[]`:

```
95-88-76-100-67
```

{{% alert color="note" %}}
Behåll arrayegenskapen som `String[]` i Java. En egenskap med en primitiv `int[]` som sammanfogas till en enda cell renderar arrayobjektets `toString`-text, till exempel `[I@1a2b3c4d`, i stället för siffrorna, eftersom sammanfogningen använder varje elements strängform och en primitiv array är ett enda opak element.
{{% /alert %}}

### **Kodexempel 3 – Jämförelse av standardspridning och rendering i en enda cell**

```java
import com.aspose.cells.*;
import java.util.*;

public class CodeRunner {
    public static class Order {
        private String[] items;
        public String[] getItems() { return items; }
        public void setItems(String[] items) { this.items = items; }
    }

    public static void main(String[] args) throws Exception {
        Order order = new Order();
        order.setItems(new String[] { "Apple", "Banana", "Cherry", "Date" });
        Workbook workbook = new Workbook();
        Cells cells = workbook.getWorksheets().get(0).getCells();
        // Column B: default marker — values spread vertically down the column
        cells.get("B1").putValue("Default");
        cells.get("B2").putValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells.get("C1").putValue("Single cell");
        cells.get("C2").putValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.setDataSource("Order", Arrays.asList(order));
        designer.process();
        for (int row = 1; row <= 5; row++) {
            String b = cells.get(row, 1).getStringValue();
            String c = cells.get(row, 2).getStringValue();
            if (b != null && !b.isEmpty() || c != null && !c.isEmpty())
                System.out.println("B" + (row + 1) + "=[" + b + "]  C" + (row + 1) + "=[" + c + "]");
        }
        workbook.save("output-array-comparison.xlsx");
    }
}
```

Standardmarkören fyller en cell per element nedåt i kolumn B, medan markören med `arrayassingle` sammanfogar samma array till en enda cell i kolumn C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Anteckningar och bästa praxis**

Ha följande punkter i åtanke när du arbetar med attributen `arrayassingle` och `arraydelimiter`:
- Attributvärden använder formen `name:value`. En form med likhetstecken, såsom `arrayassingle=true`, känns inte igen och återgår tyst till standardspridningen.
- Separera attribut med ett komma och inga mellanslag; ett mellanslag efter kommat förskjuter separatorvärdet med en teckenposition, se varningen ovan.
- Värdet för `arraydelimiter` kan vara ett enskilt tecken som skrivs direkt efter kolonet, eller en sträng med flera tecken omsluten av dubbla citattecken.
- När `arraydelimiter` utelämnas sammanfogas elementen med ett komma.
- Bind en `java.util.List` med offentliga JavaBeans som har gettermetoder som returnerar arrayer. Ett enda JavaBean-objekt eller enbart offentliga fält lämnar markörerna olösta.
- Behåll arrayegenskaperna som `String[]`; en primitiv `int[]` renderar sin `toString`-text när den sammanfogas, se anteckningen ovan.
- Placera Smart Markern i en cell med tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spillas över i angränsande celler, beroende på formatet.

## **Relaterade artiklar**
- [Lägga till filterfält i en pivottabell i Aspose.Cells for Java](/cells/sv/java/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for Java](/cells/sv/java/apply-style-to-pivot-table/)
- [Ändra layouten för sidfältet i en pivottabell](/cells/sv/java/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for Java](/cells/sv/java/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/java/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="java" >}}