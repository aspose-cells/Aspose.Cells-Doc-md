---
title: Format och ändra namngivna områden
type: docs
weight: 85
url: /sv/python-net/format-and-modify-named-ranges/
description: Denna artikel visar hur man formaterar och ändrar namngivna områden med Aspose.Cells för Python via .NET API.
keywords: Python Excel bibliotek, Python Formatera och ändra namngivna områden, Python Ange bakgrundsfärg och teckensnittsegenskaper till ett namngivet område, Python Lägg till ramar till ett namngivet område, Python Byt namn på ett namngivet område, Python Union av områden, Python Skärning av områden, Python Sammanfoga celler i det namngivna området.
---

## ** Formatområden**

### **Så här ställer du in bakgrundsfärg och teckensnittsegenskaper till ett namngivet område**

För att tillämpa formatering, definiera en [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style)-objekt för att ange stilinställningarna och tillämpa det på [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-objektet.

Följande exempel visar hur du ställer in en fyllfärg (skuggningsfärg) med teckensnittsinställningar till ett område.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges1-1.py" >}}

### **Hur du lägger till ramar i ett namngivet område**

Det är möjligt att lägga till ramar i ett område med celler istället för bara en enda cell. [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range)-objektet tillhandahåller en [**set_outline_border**](https://reference.aspose.com/cells/python-net/aspose.cells/range/set_outline_border/#aspose.cells.BorderType-aspose.cells.CellBorderType-aspose.cells.CellsColor)-metod som tar följande parametrar för att lägga till en ram i cellområdet:

- Ramtyp, ramtypen, vald från [**BorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/bordertype)-uppräkningen.
- Linjestil, linjestilen, vald från [**CellBorderType**](https://reference.aspose.com/cells/python-net/aspose.cells/cellbordertype)-uppräkningen.
- Färg, linjefärgen, vald från Färg-uppräkningen.

Följande exempel visar hur du ställer in en konturram till ett område.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-FormatRanges2-1.py" >}}


## **Hur du byter namn på ett namngivet område**

Aspose.Cells låter dig byta namn på ett namngivet område efter behov. Du kan hämta det namngivna området och döpa om det med hjälp av [**Name.text**](https://reference.aspose.com/cells/python-net/aspose.cells/name/text)-attributet. Följande exempel visar hur du byter namn på ett namngivet område.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-RenameNamedRange-1.py" >}}

## **Hur du tar union av områden**

Aspose.Cells tillhandahåller [**Range.union**](https://reference.aspose.com/cells/python-net/aspose.cells/range/union/#aspose.cells.Range) metod för att ta unionen för intervaller. Följande exempel visar hur man tar unionen för intervaller.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-UnionOfRanges-1.py" >}}

## **Hur man skär intervallerna**

Aspose.Cells tillhandahåller [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) metod för att skära två intervaller. Metoden returnerar ett [**Range**](https://reference.aspose.com/cells/python-net/aspose.cells/range) objekt. För att kontrollera om ett intervall skär ett annat intervall, använd [**Range.intersect**](https://reference.aspose.com/cells/python-net/aspose.cells/range/intersect/#aspose.cells.Range) metoden som returnerar ett booleskt värde. Följande exempel visar hur man skär intervallerna.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-IntersectionofRanges-1.py" >}}

## **Hur man förenar celler i det namngivna intervallet**

Aspose.Cells tillhandahåller [**Range.merge()**](https://reference.aspose.com/cells/python-net/aspose.cells/range/merge/#) metod för att förena cellerna i intervallet. Följande exempel visar hur man förenar de enskilda cellerna i en namngiven intervall.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Ranges-NamedRanges-MergeCellsInNamedRange-1.py" >}}
