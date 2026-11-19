---
title: Rendering av SmartMarker-array till en enda cell | Aspose.Cells for .Net
description: Lär dig hur du renderar arraydata till en enda cell med hjälp av Smart Marker-attributen arrayassingle och arraydelimiter i Aspose.Cells for .Net.
linktitle: SmartMarker-array till en enda cell | Aspose.Cells
url: /sv/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, Smart Markers, arrayassingle, arraydelimiter, array i en enda cell, arrayrendering, mall
type: docs
weight: 195
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells kan med hjälp av Smart Markers rendera en arraydatakälla till en enda cell. Attributet `arrayassingle` inaktiverar standardspridningen element för element, och attributet `arraydelimiter` väljer den avgränsare som placeras mellan de sammanfogade elementen – kommatecken som standard, eller valfritt tecken eller en flerteckenssträng i citattecken som du anger.
{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en mallbaserad funktion som dynamiskt fyller kalkylblad med data via markörexpressioner som `&=DataSource.Field`. Markören placeras i en arbetsbok i designverktyget, och när mallen behandlas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard expanderar motorn arrayen när en Smart Marker refererar till en arrayegenskap (t.ex. `&=Product.Tags` kopplad till en `string[]` med fyra värden), och den placerar varje element i en egen cell, så att värdena sprids lodrätt nedåt i kolumnen under markören. Det här beteendet är bekvämt i många scenarier, men det finns situationer där du hellre vill rendera hela arrayen till en enda cell, med elementen sammanfogade och åtskilda av en avgränsare som du väljer.
Attributen `arrayassingle` och `arraydelimiter`, som skrivs inuti en Smart Markers parenteser i formatet `name:value`, tillgodoser direkt det här behovet. De gör att du kan hålla rapportlayouten kompakt och förutsägbar samtidigt som du arbetar direkt med arraydatakällor.

## **Varför den här funktionen behövs**

### **Standardspridning av arrayer**

När en Smart Marker refererar till en arrayegenskap expanderar Aspose.Cells som standard arrayen över flera celler. En markör som `&=Product.Tags` kopplad till en `string[]` med fyra värden placerar till exempel varje värde i en egen cell under markören, vilket förskjuter annat mallinnehåll utåt och potentiellt bryter noggrant utformade rapportlayouter.

### **Begränsningar för användningsfall**

Det finns många praktiska scenarier där standardspridningen är olämplig:
- **Sammanfattande rapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som värden med kommatecken eller lodstreck som avgränsare i en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på samma plats för att förbättra läsbarheten.
- **Nedströmsflöden** (CSV-export, PDF-rendering, sammanslagning av utskrifter) som förväntar sig ett enda samlat värde per cell i stället för ett expanderat intervall.
- **Kompatibilitet mellan plattformar**, där vissa konsumenter inte tolererar arrayer som sprids över flera celler.

### **Luckan som den fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas att förbehandla data i C# eller VB.NET – sammanfoga arrayer till avgränsade strängar innan de bindes till `WorkbookDesigner`. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `arrayassingle` och `arraydelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inuti själva Smart Marker-taggen.

## **Fördelar med funktionen**

Attributen `arrayassingle` och `arraydelimiter` i dina Smart Markers ger flera fördelar:
- **Inneslutning i en enda cell**: Alla arrayelement renderas till exakt en cell, vilket håller layouterna kompakta och förutsägbara.
- **Kontroll över avgränsare**: Ange den avgränsare du vill använda – kommatecken som standard, ett semikolon, en bindestreck, ett lodstreck eller en flerteckenssträng i citattecken som `" | "`.
- **Mallstyrd formatering**: Ingen ytterligare kod krävs för att förbehandla data; formateringsreglerna ligger inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata förskjuter inte längre intilliggande mallinnehåll till andra rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängarrayer och numeriska arrayer från objektdatakällor.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så att befintliga mallar fortsätter att fungera oförändrade.

## **Så använder du funktionen**

### **Smart Marker-syntax**

Attributen `arrayassingle` och `arraydelimiter` använder Aspose.Cells syntax för attribut i formatet `name:value`, inuti parenteserna i en vanlig Smart Marker. Den generella syntaxen är:

```
&=DataSource.ArrayProperty(arrayassingle:true,arraydelimiter:;)
```

Markören består av följande delar:
- `&=DataSource.ArrayProperty` – standard-Smart Marker som refererar till arrayegenskapen i den bundna datakällan.
- `arrayassingle:true` – instruerar motorn att rendera hela arrayen till en enda cell i stället för att sprida elementen.
- `arraydelimiter:;` – valfritt; definierar avgränsaren som placeras mellan arrayelementen. Om det utelämnas används ett kommatecken.

{{% alert color="warning" %}}
Skriv attribut i formatet `name:value` (ett kolon, inte ett likhetstecken) och skilj åt flera attribut med ett kommatecken **utan mellanslag**. Ett mellanslag efter kommatecknet förskjuter det parsade värdet med ett tecken – `(arrayassingle:true, arraydelimiter:;)` skulle sammanfoga med den felaktiga avgränsaren `:;` i stället för `;`.
{{% /alert %}}

### **Avgränsarformer**

- Ett enda tecken skrivs direkt efter kolonet: `arraydelimiter:;`, `arraydelimiter:-`, `arraydelimiter:*`.
- En avgränsare med flera tecken skrivs i dubbla citattecken: `arraydelimiter:" | "`, `arraydelimiter:" - "`.

### **Arbetsflöde steg för steg**

Det följande arbetsflödet beskriver hur du renderar en array till en enda cell med hjälp av Smart Markers.
1. **Förbered datakällan**: Skapa en klass som exponerar en egenskap som returnerar en array, till exempel `string[]` eller `int[]`, och bind en `List<T>` av den klassen så att motorn läser en post per rad.
2. **Skapa en arbetsbok i designverktyget**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en cell med en Smart Marker som refererar till arrayegenskapen med attributet `arrayassingle` (och `arraydelimiter` när en anpassad avgränsare behövs).
3. **Instantiera `WorkbookDesigner`**: Skapa en `WorkbookDesigner` runt arbetsboken och bind datakällan med `SetDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.Process()` för att expandera Smart Markers och fylla arbetsboken med verkliga data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller något annat filformat som stöds.

### **Kodexempel 1 – grundläggande rendering av strängarray**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Product
    {
        public string[] Tags { get; set; }
    }

    static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Tags");
        // No spaces inside the parentheses: attributes are name:value pairs
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Product", new List<Product> { product });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-single.xlsx");
    }
}
```

Exemplet skriver ut det sammanfogade värdet för hela arrayen. De fyra taggarna hamnar i en cell, där standardavgränsaren är ett kommatecken:

```
C#,Aspose,SmartMarker,Excel
```

### **Kodexempel 2 – numerisk array med anpassad avgränsare**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Student
    {
        public int[] Scores { get; set; }
    }

    static void Main()
    {
        Student student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };
        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];
        worksheet.Cells["A1"].PutValue("Scores");
        // arraydelimiter:- joins the numbers with a hyphen
        worksheet.Cells["A2"].PutValue("&=Student.Scores(arrayassingle:true,arraydelimiter:-)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Student", new List<Student> { student });
        designer.Process();
        Console.WriteLine(worksheet.Cells["A2"].StringValue);
        workbook.Save("output-array-numeric.xlsx");
    }
}
```

Numeriska arrayer sammanfogas på samma sätt som strängarrayer – varje element behåller sin rena numeriska text:

```
95-88-76-100-67
```

### **Kodexempel 3 – jämförelse av standardspridning och rendering i en enda cell**

```csharp
using System;
using System.Collections.Generic;
using Aspose.Cells;

class Program
{
    class Order
    {
        public string[] Items { get; set; }
    }

    static void Main()
    {
        Order order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };
        Workbook workbook = new Workbook();
        Worksheet sheet = workbook.Worksheets[0];
        Cells cells = sheet.Cells;
        // Column B: default marker — values spread vertically down the column
        cells["B1"].PutValue("Default");
        cells["B2"].PutValue("&=Order.Items");
        // Column C: single-cell rendering — the whole array joins into one cell
        cells["C1"].PutValue("Single cell");
        cells["C2"].PutValue("&=Order.Items(arrayassingle:true)");
        WorkbookDesigner designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", new List<Order> { order });
        designer.Process();
        for (int row = 1; row <= 5; row++)
        {
            string b = cells[row, 1].StringValue;
            string c = cells[row, 2].StringValue;
            if (!string.IsNullOrEmpty(b) || !string.IsNullOrEmpty(c))
                Console.WriteLine($"B{row + 1}=[{b}]  C{row + 1}=[{c}]");
        }
        workbook.Save("output-array-comparison.xlsx");
    }
}
```

Den vanliga markören fyller en cell per element nedåt i kolumn B, medan `arrayassingle`-markören sammanför samma array till en enda cell i kolumn C:

```
B2=[Apple]  C2=[Apple,Banana,Cherry,Date]
B3=[Banana]  C3=[]
B4=[Cherry]  C4=[]
B5=[Date]  C5=[]
```

### **Anteckningar och bästa praxis**

Beakta följande punkter när du arbetar med attributen `arrayassingle` och `arraydelimiter`:
- Attributvärden har formatet `name:value`. En form med likhetstecken, så som `arrayassingle=true`, känns inte igen och återgår tyst till det vanliga spridningsbeteendet.
- Separera attribut med ett kommatecken och inga mellanslag; ett mellanslag efter kommatecknet förskjuter avgränsarvärdet med ett tecken (se varningen ovan).
- `arraydelimiter`-värdet kan vara ett enda tecken som skrivs direkt efter kolonet eller en sträng med flera tecken inom dubbla citattecken.
- När `arraydelimiter` utelämnas sammanfogas elementen med ett kommatecken.
- Datakällan måste låta motorn iterera över poster: bind en `List<T>` (eller en annan samling) vars elementtyp exponerar arrayegenskapen. Om ett enda objekt binds förblir markörerna i brödtexten olösta.
- Samma attribut fungerar för strängarrayer och numeriska arrayer; varje element renderas med sin rena värdetext.

## **Relaterade artiklar**
- [Lägg till filterfält i en pivottabell i Aspose.Cells for .NET](/cells/sv/net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for .NET](/cells/sv/net/apply-style-to-pivot-table/)
- [Ändra layouten för sidfältet i en pivottabell](/cells/sv/net/change-page-field-layout/)
- [Konvertera Sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}