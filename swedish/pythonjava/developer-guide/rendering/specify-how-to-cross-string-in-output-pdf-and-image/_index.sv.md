---
title: Ange hur strängen ska korsas i utgång PDF och bild
type: docs
weight: 20
url: /sv/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Ange hur strängen ska korsas i utgång PDF och bild**
 När en cell innehåller text eller sträng som är större än cellens bredd, svämmar strängen över om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i PDF/Image kan du kontrollera detta överflöde genom att ange korstypen med hjälp av[TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) uppräkning. Den har följande värden

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Visa som MS Excel, beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller trunkeras.
- [TextCrossType. CROSS_BEHÅLL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP): Visa strängen som liknar MS Excel som exporterar PDF/bild
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE)Visa all text genom att korsa andra celler och åsidosätta texten i korsade celler
- [TextCrossType.STRICT_I_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL): Visar endast strängen inom cellens bredd.

Följande exempelkod laddar exemplet i Excel-filen och sparar den i PDF/bildformat genom att ange en annan TextCrossType. Exemplet på Excel-filen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
