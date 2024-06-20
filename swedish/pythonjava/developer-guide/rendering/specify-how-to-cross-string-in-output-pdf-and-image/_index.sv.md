---
title: Ange hur du ska korsa strängen i utdata PDF och bild
type: docs
weight: 20
url: /sv/python-java/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Ange hur textsträngar ska korsas i utgående PDF och bild**
När en cell innehåller text eller sträng som är större än cellens bredd, då översvämmar strängen om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil till PDF/Bild kan du kontrollera detta översvämning genom att ange krysstypen med hjälp av [TextCrossType](https://reference.aspose.com/cells/python/asposecells.api/TextCrossType) uppräkningen. Den har följande värden

- [TextCrossType.DEFAULT](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#DEFAULT): Visa som MS Excel, beror på nästa cell. Om nästa cell är null, kommer strängen att korsa eller den kommer att bli avkortad.
- [TextCrossType.CROSS_KEEP](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_KEEP) :Visa strängen liknande MS Excel exportera PDF/Bild
- [TextCrossType.CROSS_OVERRIDE](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#CROSS_OVERRIDE) :Visa hela texten genom att korsa andra celler och skriva över texten överkorsade celler
- [TextCrossType.STRICT_IN_CELL](https://reference.aspose.com/cells/python/asposecells.api/textcrosstype#STRICT_IN_CELL) :Visa endast strängen inom bredden av cellen.

Följande exempelkod laddar den provisoriska Excel-filen och sparar den till PDF/Bild-format genom att ange olika TextCrossType. Den provisoriska Excel-filen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](sampleCrossType.xlsx)

[outputCrossType.pdf](outputCrossType.pdf)

[outputCrossType.png](outputCrossType.png)
## **Exempelkod**
{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Rendering-RenderUsingTextCrossType.py" >}}
