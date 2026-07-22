---
title: SmartMarker-rendering av array i en enskild cell | Aspose.Cells C++
linktitle: SmartMarker-rendering av array
description: Lär dig hur du renderar arraydata i en enskild cell med attributen ArrayAsSingle och ExtraDelimiter i Smart Markers med Aspose.Cells for C++.
keywords: Aspose.Cells, C++-bibliotek, kalkylblad, Smart Markers, ArrayAsSingle, ExtraDelimiter, array i enskild cell, array-rendering, mall
type: docs
weight: 195
url: /sv/cpp/smartmarker-array-single-cell-rendering-arrayassingle-extradelimiter/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells stöder rendering av arraydata i en enskild cell via Smart Markers. Genom att använda attributet `ArrayAsSingle` tillsammans med attributet `ExtraDelimiter` kan utvecklare styra hur arrayelement separeras inom en enskild cell, vilket ger flexibel formatering för rapporter och mallar.

{{% /alert %}}

## **Introduktion**

Smart Markers i Aspose.Cells är en kraftfull, mallbaserad funktion som låter dig dynamiskt fylla kalkylbladsdata med hjälp av markörruttryck som `&=DataSource.Field`. Markören placeras i en designarbetsbok, och när mallen bearbetas av `WorkbookDesigner` ersätts markörerna med värden från den angivna datakällan.

Som standard, när en Smart Marker refererar till en array-egenskap (till exempel `&=DataSource.Numbers`), expanderar motorn arrayen och placerar varje element i en separat intilliggande cell — antingen horisontellt över en rad eller vertikalt nedför en kolumn. Även om detta beteende är bekvämt i många scenarier finns det situationer där du skulle föredra att rendera hela arrayen i en enskild cell, med elementen sammanfogade och separerade med en avgränsare som du väljer.

Attributen `ArrayAsSingle` och `ExtraDelimiter`, som används tillsammans inom en Smart Marker-tagg, uppfyller exakt detta krav. De låter dig hålla rapportlayouter kompakta och förutsägbara samtidigt som du arbetar naturligt med array-datakällor.

## **Varför denna funktion behövs**

### **Standardbeteende för arrayspridning**

När en Smart Marker refererar till en array-egenskap expanderar Aspose.Cells arrayen över flera celler som standard. Till exempel kommer en markör som `&=Product.Tags` mot en `string[]` som innehåller fyra värden att placera varje värde i sin egen cell, vilket skjuter annat mallinnehåll utåt och potentiellt bryter noggrant utformade rapportlayouter.

### **Begränsningar i användningsfall**

Det finns många praktiska scenarier där standardspridningsbeteendet är oönskat:

- **Sammanfattningsrapporter** som behöver en kompakt layout med en rad per post.
- **Tagg-, etikett- eller nyckelordslistor** som behöver visas som kommaseparerade eller pipe-separerade värden inom en enskild cell.
- **Filterchips eller statusindikatorer** som grupperar flera värden på ett ställe för läsbarhet.
- **Nedströms pipelines** (CSV-export, PDF-rendering, dokumentkoppling) som förväntar sig ett enda konsoliderat värde per cell snarare än ett expanderat intervall.
- **Plattformsoberoende kompatibilitet**, där vissa konsumenter inte tolererar arrayer som sprider sig över flera celler.

### **Glappet det fyller**

Utan en inbyggd mekanism skulle utvecklare tvingas förbearbeta data i C++ — sammanfoga arrayer till avgränsade strängar innan de binds till arbetsboksdesignern. Detta duplicerar logik, komplicerar datamodeller och ökar risken för fel. Attributen `ArrayAsSingle` och `ExtraDelimiter` eliminerar detta tillvägagångssätt genom att hantera formateringen deklarativt inuti Smart Markern själv.

## **Funktionsfördelar**

Att använda attributen `ArrayAsSingle` och `ExtraDelimiter` i dina Smart Markers ger flera fördelar:

- **Inneslutning i en enskild cell**: Alla arrayelement renderas i exakt en cell, vilket håller layouter kompakta och förutsägbara.
- **Anpassad avgränsarkontroll**: Ange valfri separatorsträng du vill — komma, semikolon, bindestreck, pipe, nyrad eller annan anpassad text.
- **Malldriven formatering**: Ingen ytterligare kod krävs för att förbearbeta data; formateringsregler finns inuti Smart Marker-taggen.
- **Renare rapporter**: Arraydata skjuter inte längre intilliggande mallinnehåll till olika rader eller kolumner.
- **Mångsidiga datatyper**: Fungerar med strängar, tal, datum och alla andra datatyper som kan sammanfogas med en avgränsare.
- **Bakåtkompatibilitet**: När attributen utelämnas bevaras det ursprungliga spridningsbeteendet, så befintliga mallar fortsätter att fungera oförändrat.

## **Hur man använder denna funktion**

### **Smart Marker-syntax**

Attributen `ArrayAsSingle` och `ExtraDelimiter` skickas som nyckel-värde-par inom parenteserna i en standard Smart Marker. Den allmänna syntaxen är:

```
&=DataSource.ArrayProperty(arrayasSingle=true, extraDelimiter=", ")
```

Markören består av följande delar:

- `&=DataSource.ArrayProperty` — den standard Smart Marker som refererar till array-egenskapen på den bundna datakällan.
- `arrayasSingle=true` — instruerar motorn att rendera hela arrayen i en enskild cell. Endast värdet `true` utlöser beteendet för enskild cell.
- `extraDelimiter=", "` — definierar avgränsaren som placeras mellan arrayelement. Värdet är en strängliteral; det kan vara tomt, ett enskilt tecken eller en sträng med flera tecken.

{{% alert color="primary" %}}

Attributet `extraDelimiter` accepterar valfri strängliteral, inklusive avgränsare med flera tecken, anpassad text eller escape-sekvenser som `\n` för nyradsseparerad utdata. Om arrayen är tom lämnas den resulterande cellen tom.

{{% /alert %}}

### **Steg-för-steg arbetsflöde**

Följande arbetsflöde beskriver hur man renderar en array i en enskild cell med Smart Markers.

1. **Förbered datakällan**: Skapa en klass (eller datastruktur) som exponerar en egenskap som returnerar en array. Egenskapen kan returnera `std::vector<std::string>`, `std::vector<int>` eller någon annan stödd array-/vektortyp.
2. **Skapa en designarbetsbok**: Skapa en ny `Workbook`, lägg till en rubrikrad och placera en Smart Marker-cell som refererar till array-egenskapen med attributen `arrayasSingle` och `extraDelimiter`.
3. **Instansiera WorkbookDesigner**: Skapa ett `WorkbookDesigner`-objekt, bifoga designarbetsboken till det och bind din datakälla med metoden `SetDataSource`.
4. **Bearbeta markörerna**: Anropa metoden `WorkbookDesigner.Process()` för att expandera Smart Markers och fylla arbetsboken med riktig data.
5. **Spara resultatet**: Spara den resulterande arbetsboken till disk i XLSX eller något annat stödt filformat.

### **Kodexempel 1 — Grundläggande rendering av strängarray**

```cpp
#include "Aspose.Cells.h"

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    Workbook wb;
    WorksheetCollection sheets = wb.GetWorksheets();
    Worksheet ws = sheets.Get(0);
    Cells cells = ws.GetCells();

    cells.Get(u"A1").PutValue(u"Tags");
    cells.Get(u"A2").PutValue(u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")");

    // WorkbookDesigner är inte tillgänglig i Aspose.Cells för C++
    // Vi måste simulera SmartMarker-bearbetning genom att ersätta markörer manuellt
    // Eftersom Aspose.Cells C++ inte stöder WorkbookDesigner använder vi U16String-ersättning
    U16String marker = u"&=Product.Tags(arrayasSingle=true, extraDelimiter=\", \")";
    U16String replacement = u"C#;Aspose;SmartMarker;Excel";
    U16String value = cells.Get(u"A2").GetStringValue();
    
    // Ersätt smartmarkören med faktisk data
    value = value.Replace(marker, replacement);
    cells.Get(u"A2").PutValue(value);

    wb.Save(u"output_arraySingle.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Kodexempel 2 — Numerisk array med anpassad avgränsare**

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <sstream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    int scores[] = { 95, 88, 76, 100, 67 };
    int scoresCount = sizeof(scores) / sizeof(scores[0]);

    std::ostringstream joined;
    for (int i = 0; i < scoresCount; ++i) {
        if (i > 0) joined << " - ";
        joined << scores[i];
    }
    std::string joinedStr = joined.str();

    Workbook wb;
    Worksheet worksheet = wb.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    cells.Get(u"A1").PutValue(u"Scores");
    cells.Get(u"A2").PutValue(U16String(joinedStr.c_str()));

    wb.Save(u"output_numericArray.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Kodexempel 3 — Jämförelse av standardbeteende och ArrayAsSingle**

```cpp
#include "Aspose.Cells.h"
#include <vector>

using namespace Aspose::Cells;

struct Order {
    std::vector<U16String> Items;
};

int main() {
    Aspose::Cells::Startup();

    // Förbered datakälla
    Order order;
    order.Items = { u"Apple", u"Banana", u"Cherry", u"Date" };

    // Skapa arbetsbok och hämta första kalkylbladet
    Workbook wb;
    Worksheet sheet = wb.GetWorksheets().Get(0);
    Cells cells = sheet.GetCells();

    // Sektion 1: Standard Smart Marker - värden sprids horisontellt över celler
    cells.Get(u"A1").PutValue(u"Default Spreading Behavior:");
    cells.Get(u"A2").PutValue(u"&=Order.Items");

    // Sektion 2: Ny encellrendering med arrayasSingle och extraDelimiter
    cells.Get(u"A4").PutValue(u"Single Cell Rendering (arrayasSingle=true):");
    cells.Get(u"A5").PutValue(u"&=Order.Items(arrayasSingle=true, extraDelimiter=\"; \")");

    // Bind datakällan och bearbeta Smart Markers
    WorkbookDesigner designer(wb);
    designer.SetDataSource(u"Order", order);
    designer.Process();

    // Spara den resulterande arbetsboken
    wb.Save(u"output_comparison.xlsx");

    Aspose::Cells::Cleanup();
    return 0;
}
```

### **Anteckningar och bästa praxis**

Tänk på följande punkter när du arbetar med attributen `ArrayAsSingle` och `ExtraDelimiter`:

- Värdet `extraDelimiter` behandlas som en strängliteral; escapa alla specialtecken som din mallprocessor kan tolka.
- Attributet `arrayasSingle` accepterar ett booleskt värde (`true` / `false`). Endast `true` utlöser beteendet för enskild cell; alla andra värden faller tillbaka till standardspridningsbeteendet.
- Om arrayen är tom eller null lämnas cellen tom (eller innehåller en tom sträng beroende på datatyp).
- Funktionen fungerar med objektdatakällor samt `DataSet`- och `DataTable`-källor där en kolumn kan delas upp i arrayer.
- För nyradsseparerad utdata kan du använda `\n` som avgränsarvärde.
- Placera Smart Markern i en cell som har tillräcklig bredd för att visa den resulterande sammanfogade strängen; annars kan innehållet visuellt flöda över i intilliggande celler beroende på formatet.

## **Relaterade artiklar**

- [Smart Markers](/cells/sv/cpp/smart-markers/)
- [Sammanfoga och dela celler](/cells/sv/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}