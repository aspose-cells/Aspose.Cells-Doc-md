---
title: Format och ändra namngivna områden
type: docs
weight: 85
url: /sv/net/format-and-modify-named-ranges/
---

## ** Formatområden**

### **Ställa in bakgrundsfärg och teckensnittsegenskaper för ett namngivet område**

För att tillämpa formatering, definiera en [**Style**](https://reference.aspose.com/cells/net/aspose.cells/style)-objekt för att ange stilinställningarna och tillämpa det på [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-objektet.

Följande exempel visar hur du ställer in en fyllfärg (skuggningsfärg) med teckensnittsinställningar till ett område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Lägga till ramar för ett namngivet område**

Det är möjligt att lägga till ramar i ett område med celler istället för bara en enda cell. [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range)-objektet tillhandahåller en [**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)-metod som tar följande parametrar för att lägga till en ram i cellområdet:

- Ramtyp, ramtypen, vald från [**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)-uppräkningen.
- Linjestil, linjestilen, vald från [**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)-uppräkningen.
- Färg, linjefärgen, vald från Färg-uppräkningen.

Följande exempel visar hur du ställer in en konturram till ett område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Följande exempel visar hur man ställer in ramar runt varje cell i området.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Byt namn på ett namngivet område**

Aspose.Cells låter dig byta namn på ett namngivet område efter behov. Du kan hämta det namngivna området och döpa om det med hjälp av [**Name.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)-attributet. Följande exempel visar hur du byter namn på ett namngivet område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Förbund av områden**

Aspose.Cells tillhandahåller [**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)-metoden för att ta förbund för områden, metoden returnerar ett [*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)-objekt. Följande exempel visar hur man tar förbund för områden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Skärning av områden**

Aspose.Cells tillhandahåller [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) metod för att skära två intervaller. Metoden returnerar ett [**Range**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt. För att kontrollera om ett intervall skär ett annat intervall, använd [**Range.Intersect**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) metoden som returnerar ett booleskt värde. Följande exempel visar hur man skär intervallerna.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Sammanfoga celler i det namngivna området**

Aspose.Cells tillhandahåller [**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge) metod för att förena cellerna i intervallet. Följande exempel visar hur man förenar de enskilda cellerna i en namngiven intervall.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Ta bort ett namngivet område**

Aspose.Cells tillhandahåller [**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat)-metoden för att radera namnet på området. Använd [**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)-metoden för att rensa innehållet i området. Fö...

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
