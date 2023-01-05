---
title: Formatera och ändra namngivna intervall
type: docs
weight: 85
url: /sv/net/format-and-modify-named-ranges/
---
## **Formatintervall**

### **Ställa in bakgrundsfärg och teckensnittsattribut för ett namngivet område**

 För att tillämpa formatering, definiera en[**Stil**](https://reference.aspose.com/cells/net/aspose.cells/style) objekt för att ange stilinställningar och tillämpa det på[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range)objekt.

Följande exempel visar hur man ställer in den solida fyllningsfärgen (skuggfärg) med teckensnittsinställningar till ett intervall.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges1-1.cs" >}}

### **Lägga till gränser till ett namngivet område**

 Det är möjligt att lägga till gränser till ett cellintervall istället för bara en enda cell. De[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt ger en[**SetOutlineBorder**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/setoutlineborder)metod som använder följande parametrar för att lägga till en kantlinje till cellområdet:

-  Border type, typen av kant, vald från[**BorderType**](https://reference.aspose.com/cells/net/aspose.cells/bordertype)uppräkning.
-  Linjestil, linjestilen, vald från[**CellBorderType**](https://reference.aspose.com/cells/net/aspose.cells/cellbordertype)uppräkning.
- Färg, linjefärgen, vald från färguppräkningen.

Följande exempel visar hur man ställer in en konturgräns för ett område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-FormatRanges2-1.cs" >}}

Följande exempel visar hur man ställer in gränser runt varje cell i intervallet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-SetBorderAroundEachCell-1.cs" >}}

## **Byt namn på ett namngivet intervall**

 Aspose.Cells låter dig byta namn på ett namngivet område för ditt behov. Du kan få det namngivna intervallet och byta namn på det genom att använda[**Namn.Text**](https://reference.aspose.com/cells/net/aspose.cells/name/properties/text)attribut. Följande exempel visar hur man byter namn på ett namngivet område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RenameNamedRange-1.cs" >}}

## **Union of Ranges**

 Aspose.Cells tillhandahåller[**Range.Union**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/union)metod för att ta unionen för intervall, returnerar metoden en[*ArrayList*](https://docs.microsoft.com/en-gb/dotnet/api/system.collections.arraylist?view=netframework-4.8)objekt. Följande exempel visar hur man tar union för intervall.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-UnionOfRanges-1.cs" >}}

## **Skärning av Ranges**

 Aspose.Cells tillhandahåller[**Range.Skärning**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect) metod för att skära två områden. Metoden returnerar en[**Räckvidd**](https://reference.aspose.com/cells/net/aspose.cells/range) objekt. För att kontrollera om ett område skär ett annat område, använd[**Range.Skärning**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/intersect)metod som returnerar ett booleskt värde. Följande exempel visar hur man skär intervallen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-IntersectionofRanges-1.cs" >}}

## **Slå samman Cells i det namngivna området**

 Aspose.Cells tillhandahåller[**Range.Merge()**](https://reference.aspose.com/cells/net/aspose.cells/range/methods/merge)metod för att slå samman cellerna i området. Följande exempel visar hur man slår samman de enskilda cellerna i ett namngivet område.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-MergeCellsInNamedRange-1.cs" >}}

## **Ta bort ett namngivet intervall**

 Aspose.Cells tillhandahåller[**NameCollection.RemoveAt()**](https://reference.aspose.com/cells/net/aspose.cells/namecollection/methods/removeat) metod för att radera namnet på området. För att rensa innehållet i intervallet, använd[**Cells.ClearRange()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/clearrange/index)metod. Följande exempel visar hur man tar bort ett namngivet område med dess innehåll.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Data-AddOn-NamedRanges-RemoveANamedRange-1.cs" >}}
