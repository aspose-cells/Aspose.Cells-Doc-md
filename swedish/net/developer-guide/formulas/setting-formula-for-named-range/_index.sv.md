---
title: Ange formel för namngivet område
type: docs
weight: 20
url: /sv/net/setting-formula-for-named-range/
---

## **Ange formel för namngivet område**
Som Excel-programmet tillhandahåller Aspose.Cells API:er möjligheten att ange en formel för ett namngivet område medan du använder dess [RefersTo](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto) egenskap. Det finns många användbarhetsscenario för denna funktion, några av dem detaljeras nedan.
### **Ange enkel formel för namngivet område**
Enkel formel skulle kunna vara en hänvisning till en annan cell i samma (eller annan) kalkylblad. Följande exempel skapar ett namngivet område i en ny kalkyl och anger dess hänvisning till en annan cell.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Ange komplex formel för namngivet område**
En komplex formel kan vara vad som helst, till exempel en dynamiskt område eller en formel som sträcker sig över flera celler i olika kalkylblad. Följande exempel skapar ett dynamiskt område med hjälp av INDEX-funktionen för att hämta värdet från en lista baserat på dess plats.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Här är ytterligare ett exempel som använder ett namngivet område för att summera värden från 2 celler i olika kalkylblad.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
