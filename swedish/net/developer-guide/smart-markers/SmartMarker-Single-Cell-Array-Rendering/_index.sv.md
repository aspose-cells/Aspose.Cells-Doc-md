---
title: SmartMarker Single Cell Array Rendering | Aspose.Cells .NET
linktitle: SmartMarker Single Cell Array Rendering | Aspose.Cells .NET
description: Lär dig hur du renderar matriser i en enda cell med attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for .NET.
keywords: Aspose.Cells, .NET-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, single cell array, matrisrendering, mall
type: docs
weight: 195
url: /sv/net/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells stöder rendering av matrisdata till en enda cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur matriselement separeras inom en enda cell, vilket ger flexibel formettering för rapporter och mallar.
{{% /alert %}}

## **Introduction**
Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla i kalkylbladsdata med hjälp av marköruttryck som `&=DataSource.Field`. Markören placeras i en designarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.
Som standard, när en Smart Marker refererar till en matrisegenskap (till exempel `&=DataSource.Numbers`), expanderar motorn matrisen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt ner i en kolumn. Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela matrisen i en enda cell, med elementen sammanfogade och separerade med en avgränsare efter eget val.
Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inom en Smart Marker-tagg, uppfyller just detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar med matriser som datakällor.

## **Why This Feature Is Needed**

### **Default Array Spreading Behavior**
När en Smart Marker refererar till en matrisegenskap expanderar Aspose.Cells matrisen över flera celler som standard. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, vilket skjuter annat mallinnehåll utåt och potentiellt bryter noggrant utformade rapportlayouter.

### **Use Case Limitations**
Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:
- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller pipe-separerade värden inom en enda cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformskompatibilitet**, där vissa konsumenter inte kan tolerera matriser som sprider sig över flera celler.

### **The Gap It Fills**
Utan en inbyggd mekanism skulle utvecklare tvingas förbearbeta data i C# eller VB.NET — sammanfoga matriser till avgränsade strängar innan de binder dem till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar denna lösning genom att hantera formateringen deklarativt inuti Smart Marker-taggen.

## **Feature Benefits**
Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:
- **Inneslutning i en cell**: Alla matriselement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng — komma, semikolon, bindestreck, pipe, nyrad eller annan anpassad text.
- **Malldriven formatering**: Ingen ytterligare kod krävs för att förbearbeta data; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Matrisdata skjuter inte längre ut intilliggande mallinnehåll till andra rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **How to Use This Feature**

### **Smart Marker Syntax**
Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en vanlig Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:
- `&=DataSource.ArrayProperty` — standard-Smart Marker som refererar till matrisegenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela matrisen i en enda cell. Endast värdet `true` utlöser encellsbeteendet.
- `extraDelimiter=", "` — definierar avgränsaren som placeras mellan matriselement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en flerteckensträng.

{{% alert color="primary" %}}
Attributet `extraDelimiter` accepterar alla strängliterals, inklusive flerteckenavgränsare, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om matrisen är tom lämnas den resulterande cellen tom.

### **Step-by-Step Workflow**
Följande arbetsflöde beskriver hur man renderar en matris till en enda cell med hjälp av Smart Markers.
1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en matris. Egenskapen kan returnera `string[]`, `int[]` eller annan matristyp som stöds.
2. **Skapa en designarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till matrisegenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, koppla designarbetsboken till det och bind din datakälla med metoden `SetDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.Process()` för att expandera Smart Markers och fylla arbetsboken med verklig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller annat filformat som stöds.

### **Code Example 1 — Basic String Array Rendering**

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

### **Code Example 2 — Numeric Array with Custom Delimiter**

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

### **Code Example 3 — Comparing Default vs. ArrayAsSingle Behavior**

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
        // Section 1: Default Smart Marker - values spread horizontally across cells
        cells["A1"].PutValue("Default Spreading Behavior:");
        cells["A2"].PutValue("&=Order.Items");
        // Section 2: New single-cell rendering using arrayasSingle and extraDelimiter
        cells["A4"].PutValue("Single Cell Rendering (arrayasSingle=true):");
        cells["A5"].PutValue("&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");
        // Bind the data source and process Smart Markers
        var designer = new WorkbookDesigner(workbook);
        designer.SetDataSource("Order", order);
        designer.Process();
        // Save the resulting workbook
        workbook.Save("output_comparison.xlsx");
    }
}
public class Order
{
    public string[] Items { get; set; }
}
```

### **Notes & Best Practices**
Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:
- Värdet på `extraDelimiter` behandlas som en strängliteral; escapea eventuella specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett boolskt värde (`true` / `false`). Endast `true` utlöser encellsbeteendet; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om matrisen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatyp).
- Funktionen fungerar med objektdatakällor samt `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i matriser.
- För nyradsseparerad utdata kan du använda `\n` eller `Environment.NewLine` som avgränsarvärde.
{{% /alert %}}

## Related Articles
- [Lägg till filterfält i en pivottabell i Aspose.Cells for .NET](/cells/sv/net/add-page-field-in-pivot-table/)
- [Tillämpa stilar på pivottabeller i Aspose.Cells for .NET](/cells/sv/net/apply-style-to-pivot-table/)
- [Ändra sidfältslayout i pivottabell](/cells/sv/net/change-page-field-layout/)
- [Konvertera sparkline till bild och HTML i Aspose.Cells for .NET](/cells/sv/net/convert-sparkline-to-image-and-html/)
- [Konvertera Excel till OFD-format](/cells/sv/net/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="csharp" >}}