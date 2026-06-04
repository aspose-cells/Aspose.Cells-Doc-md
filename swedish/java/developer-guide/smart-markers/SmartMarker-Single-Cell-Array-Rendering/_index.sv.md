---
title: SmartMarker-rendering av enkelcellsarray | Aspose.Cells Java
description: Lär dig hur du renderar arraydata i en enda cell med attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for Java.
keywords: Aspose.Cells, Java-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, enkelcellsarray, arrayrendering, mall
type: docs
weight: 195
url: /sv/java/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells stöder rendering av arraydata i en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelement separeras i en enda cell, vilket ger flexibel formatering för rapporter och mallar.

{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla kalkylbladsdata med hjälp av marköruttryck som `&=DataSource.Field`. Markören placeras i en designer-arbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard, när en Smart Marker refererar till en arrayegenskap (till exempel `&=DataSource.Numbers`), expanderar motorn arrayen och placerar varje element i en separat intilliggande cell – antingen horisontellt över en rad eller vertikalt nedför en kolumn. Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela arrayen i en enda cell, med elementen sammanfogade och separerade med en avgränsare du väljer.

Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans i en Smart Marker-tagg, uppfyller just detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar naturligt med arraydatakällor.

## **Varför denna funktion behövs**

### **Standardspridning av arrayer**

När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells arrayen över flera celler som standard. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, och skjuter ut annat mallinnehåll och kan potentiellt bryta noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:

- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller rörseparerade värden i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformsoberoende kompatibilitet**, där vissa konsumenter inte tolererar arrayer som sprids över flera celler.

### **Vilket gap det fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas förbearbeta data i Java – sammanfoga arrayer till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inuti Smart Markern själv.

## **Funktionsfördelar**

Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:

- **Inneslutning i en cell**: Alla arrayelement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng – komma, semikolon, bindestreck, rör, nyrad eller annan anpassad text.
- **Malldriven formatering**: Ingen ytterligare kod krävs för att förbearbeta data; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre ut närliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Hur man använder denna funktion**

### **Smart Marker-syntax**

Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en standard Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:

- `&=DataSource.ArrayProperty` – den standardmässiga Smart Marker som refererar till arrayegenskapen på den bundna datakällan.
- `arrayasSingle=true` – instruerar motorn att rendera hela arrayen i en enda cell. Endast värdet `true` utlöser enkelcellsbeteendet.
- `extraDelimiter=", "` – definierar avgränsaren som placeras mellan arrayelement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en flerteckensträng.

{{% alert color="primary" %}}

Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive flerteckenavgränsare, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om arrayen är tom lämnas den resulterande cellen tom.

{{% /alert %}}

### **Steg-för-steg-arbetsflöde**

Följande arbetsflöde beskriver hur man renderar en array i en enda cell med hjälp av Smart Markers.

1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en array. Egenskapen kan returnera `String[]`, `int[]` eller annan arraytyp som stöds.
2. **Skapa en designer-arbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till arrayegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, koppla designer-arbetsboken till det och bind din datakälla med metoden `setDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.process()` för att expandera Smart Markers och fylla arbetsboken med verklig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller annat filformat som stöds.

### **Kodexempel 1 – Grundläggande strängarrayrendering**

```java
import com.aspose.cells.*;

class Product {
    public String[] Tags;
}

public class CodeRunner {
    public static void main(String[] args) throws Exception {
        Product product = new Product();
        product.Tags = new String[] { "C#", "Aspose", "SmartMarker", "Excel" };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Tags");
        worksheet.getCells().get("A2").putValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.setWorkbook(workbook);
        designer.setDataSource("Product", product);
        designer.process();

        workbook.save("output_arraySingle.xlsx");
    }
}
```

### **Kodexempel 2 – Numerisk array med anpassad avgränsare**

```java
import com.aspose.cells.*;

class Student
{
    public int[] Scores;
}

public class CodeRunner
{
    public static void main(String[] args) throws Exception
    {
        Student student = new Student();
        student.Scores = new int[] { 95, 88, 76, 100, 67 };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.getWorksheets().get(0);

        worksheet.getCells().get("A1").putValue("Scores");

        StringBuilder joined = new StringBuilder();
        for (int i = 0; i < student.Scores.length; i++)
        {
            if (i > 0) joined.append(" - ");
            joined.append(student.Scores[i]);
        }
        worksheet.getCells().get("A2").putValue(joined.toString());

        workbook.save("output_numericArray.xlsx");
    }
}
```

### **Kodexempel 3 – Jämförelse av standard- vs. ArrayAsSingle-beteende**

```java
class Order
{
    private String[] items;

    public String[] getItems()
    {
        return items;
    }

    public void setItems(String[] items)
    {
        this.items = items;
    }
}
```

### **Anteckningar och bästa praxis**

Ha följande punkter i åtanke när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:

- Värdet `extraDelimiter` behandlas som en strängliteral; escapa alla specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`true` / `false`). Endast `true` utlöser enkelcellsbeteendet; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om arrayen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatypen).
- Funktionen fungerar med objektdatakällor samt `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i arrayer.
- För nyradsseparerad utdata kan du använda `\n` eller `System.lineSeparator()` som avgränsarvärde.
- Placera Smart Markern i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över till intilliggande celler beroende på formatet.

## **Relaterade artiklar**

- [Smart Markers](/cells/sv/java/smart-markers/)
- [Slå ihop och dela celler](/cells/sv/java/merging-and-unmerging-cells/)

{{< app/cells/assistant language="java" >}}