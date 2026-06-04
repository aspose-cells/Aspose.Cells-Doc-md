---
title: SmartMarker Enkelcellsmatrisrendering | Aspose.Cells .NET
description: Lär dig hur du renderar matrisdata till en enskild cell med hjälp av attributen ArrayAsSingle och ExtraDelimiter i Smartmarkörer med Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, Smartmarkörer, ArrayAsSingle, ExtraDelimiter, enstaka cellmatris, matrisrendering, mall
type: docs
weight: 195
url: /sv/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
---

{{% alert color="primary" %}}

Aspose.Cells stöder rendering av matrisdata till en enskild cell via Smartmarkörer. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur matriselement separeras inom en enskild cell, vilket ger flexibel formatering för rapporter och mallar.

{{% /alert %}}

## **Introduktion**

Smartmarkörer i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla i kalkylbladsdata med hjälp av markörexpressioner som `&=DataSource.Field`. Markören placeras i en designarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard, när en Smartmarkör refererar till en matrisegenskap (till exempel `&=DataSource.Numbers`), expanderar motorn matrisen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt nedåt i en kolumn. Även om detta beteende är bekvämt i många scenarier, finns det situationer där du skulle föredra att rendera hela matrisen i en enda cell, med elementen sammanfogade och åtskilda av en avgränsare som du själv väljer.

Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inuti en Smartmarkör-tagg, uppfyller just detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar direkt med matriskällor.

## **Varför denna funktion behövs**

### **Standardbeteende för matrisspridning**

När en Smartmarkör refererar till en matrisegenskap expanderar Aspose.Cells som standard matrisen över flera celler. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, vilket trycker ut annat mallinnehåll och potentiellt bryter noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:

- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller röravgränsade värden inom en enskild cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformsoberoende kompatibilitet**, där vissa konsumenter inte tolererar matriser som spiller över flera celler.

### **Vilket glapp det fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas förbehandla data i C# eller VB.NET — sammanfoga matriser till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inuti Smartmarkören själv.

## **Fördelar med funktionen**

Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smartmarkörer ger flera fördelar:

- **Inneslutning i en cell**: Alla matriselement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng du vill — komma, semikolon, bindestreck, rör, nyrad eller annan anpassad text.
- **Maldriven formatering**: Ingen ytterligare kod krävs för att förbehandla datan; formateringsregler finns inuti Smartmarkör-taggen.
- **Renare rapporter**: Matrisdata trycker inte längre ut intilliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Hur man använder denna funktion**

### **Syntax för Smartmarkörer**

Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en standard-Smartmarkör. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören är uppbyggd av följande delar:

- `&=DataSource.ArrayProperty` — standard-Smartmarkören som refererar till matrisegenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela matrisen i en enda cell. Endast värdet `true` aktiverar enkelcellsbeteendet.
- `extraDelimiter=", "` — definierar avgränsaren som placeras mellan matriselement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en flerteckensträng.

{{% alert color="primary" %}}

Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive flerteckensavgränsare, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om matrisen är tom lämnas den resulterande cellen tom.

{{% /alert %}}

### **Steg-för-steg-arbetsflöde**

Följande arbetsflöde beskriver hur man renderar en matris till en enskild cell med hjälp av Smartmarkörer.

1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en matris. Egenskapen kan returnera `string[]`, `int[]` eller annan matristyp som stöds.
2. **Skapa en designarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smartmarkör-cell som refererar till matrisegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, koppla designarbetsboken till det och bind din datakälla med metoden `SetDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.Process()` för att expandera Smartmarkörerna och fylla arbetsboken med riktig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller annat filformat som stöds.

### **Kodexempel 1 — Grundläggande strängmatrisrendering**

```csharp
using System;
using Aspose.Cells;

class Program
{
    public class Product
    {
        public string[] Tags { get; set; }
    }

    public static void Main()
    {
        Product product = new Product
        {
            Tags = new string[] { "C#", "Aspose", "SmartMarker", "Excel" }
        };

        Workbook workbook = new Workbook();
        Worksheet worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Tags");
        worksheet.Cells["A2"].PutValue("&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

        WorkbookDesigner designer = new WorkbookDesigner();
        designer.Workbook = workbook;
        designer.SetDataSource("Product", product);
        designer.Process();

        workbook.Save("output_arraySingle.xlsx");
    }
}
```

### **Kodexempel 2 — Numerisk matris med anpassad avgränsare**

```csharp
public class Student
{
    public int[] Scores { get; set; }
}

public class Program
{
    public static void Main()
    {
        var student = new Student
        {
            Scores = new int[] { 95, 88, 76, 100, 67 }
        };

        var workbook = new Workbook();
        var worksheet = workbook.Worksheets[0];

        worksheet.Cells["A1"].PutValue("Scores");
        worksheet.Cells["A2"].PutValue(string.Join(" - ", student.Scores));

        workbook.Save("output_numericArray.xlsx");
    }
}
```

### **Kodexempel 3 — Jämförelse av standard- och ArrayAsSingle-beteende**

```csharp
using System;
using Aspose.Cells;

public class Program
{
    public static void Main()
    {
        var order = new Order
        {
            Items = new string[] { "Apple", "Banana", "Cherry", "Date" }
        };

        var workbook = new Workbook();
        var sheet = workbook.Worksheets[0];
        var cells = sheet.Cells;

        // Sektion 1: Standard Smart Marker - värden sprids horisontellt över celler
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");

        // Sektion 2: Ny encellrendering med arrayasSingle och extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

        // Bind datakällan och bearbeta Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();

        // Spara den resulterande arbetsboken
        workbook.Save("output_comparison.xlsx");
    }
}

public class Order
{
    public string[] Items { get; set; }
}
```

### **Anteckningar och bästa praxis**

Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:

- Värdet `extraDelimiter` behandlas som en strängliteral; escape:a eventuella specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`true` / `false`). Endast `true` aktiverar enkelcellsbeteendet; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om matrisen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatyp).
- Funktionen fungerar med objektdatakällor samt `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i matriser.
- För nyradsseparerad utdata kan du använda `\n` eller `Environment.NewLine` som avgränsarvärde.
- Placera Smartmarkören i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt spilla över i intilliggande celler beroende på formatet.

## **Relaterade artiklar**

- [Smartmarkörer](/cells/sv/net/smart-markers/)
- [Sammanfoga och dela celler](/cells/sv/net/merging-and-unmerging-cells/)

{{< app/cells/assistant language="csharp" >}}