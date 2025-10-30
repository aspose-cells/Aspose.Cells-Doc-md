---
title: Ange formel för namngivet område
type: docs
weight: 20
url: /sv/python-net/setting-formula-for-named-range/
---

## **Ange formel för namngivet område**
Precis som Excel-appen, ger Aspose.Cells för Python via .NET API:erna möjlighet att ange en formel för ett namngivet område medan du använder dess [**Range.refers_to**](https://reference.aspose.com/cells/python-net/aspose.cells/range/refers_to)-egenskap. Det finns många användbarhetsscenarier för denna funktion, några av vilka är detaljerade nedan.
### **Ange enkel formel för namngivet område**
Enkel formel skulle kunna vara en hänvisning till en annan cell i samma (eller annan) kalkylblad. Följande exempel skapar ett namngivet område i en ny kalkyl och anger dess hänvisning till en annan cell.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingSimpleFormulaForNamedRanges.py" >}}
### **Ange komplex formel för namngivet område**
En komplex formel kan vara vad som helst, till exempel en dynamiskt område eller en formel som sträcker sig över flera celler i olika kalkylblad. Följande exempel skapar ett dynamiskt område med hjälp av INDEX-funktionen för att hämta värdet från en lista baserat på dess plats.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-SettingComplexFormulaNamedRange.py" >}}



Här är ytterligare ett exempel som använder ett namngivet område för att summera värden från 2 celler i olika kalkylblad.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Formulas-CalculatingSumUsingNamedRangeOnDifferentSheets.py" >}}
{{< app/cells/assistant language="python-net" >}}
