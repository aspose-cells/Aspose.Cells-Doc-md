---
title: Inställningsformel för namngett intervall
type: docs
weight: 20
url: /sv/net/setting-formula-for-named-range/
---
## **Inställningsformel för namngett intervall**
 Precis som Excel-applikationen ger Aspose.Cells API:er möjligheten att ange en formel för ett namngivet intervall medan du använder dess[Refererar till](https://reference.aspose.com/cells/net/aspose.cells/range/properties/refersto)fast egendom. Det kan finnas många användbarhetsscenarier för den här funktionen, av vilka några är detaljerade enligt följande.
### **Ställa in en enkel formel för namngiven intervall**
En enkel formel kan vara en referens till en annan cell i samma (eller ett annat) kalkylblad. Följande exempel skapar ett namngivet intervall i ett nytt kalkylblad och anger dess referens till en annan cell.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingSimpleFormula-SettingSimpleFormulaForNamedRanges.cs" >}}
### **Ställa in en komplex formel för namngiven intervall**
En komplex formel kan vara vad som helst som ett dynamiskt område eller en formel som spänner över flera celler i olika kalkylblad. Följande exempel skapar ett dynamiskt område med hjälp av INDEX-funktionen för att hämta värdet från en lista baserat på dess plats.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SettingComplexFormula-SettingComplexFormulaNamedRange.cs" >}}



Här är ett annat exempel som använder ett namngivet intervall för att summera värden från 2 celler i olika kalkylblad.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-CalculatingSumUsingNamedRange-CalculatingSumUsingNamedRangeOnDifferentSheets.cs" >}}
