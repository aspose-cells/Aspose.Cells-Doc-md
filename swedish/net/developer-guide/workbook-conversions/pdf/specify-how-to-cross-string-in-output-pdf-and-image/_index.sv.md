---
title: Ange hur strängen ska korsas i utdata-PDF och bild
type: docs
weight: 120
url: /sv/net/specify-how-to-cross-string-in-output-pdf-and-image/
---
## **Möjliga användningsscenarier**

När en cell innehåller text eller sträng men den är större än cellens bredd, svämmar strängen över om nästa cell i nästa kolumn är null eller tom. När du sparar din Excel-fil i PDF/Bild kan du kontrollera detta överflöde genom att ange korstypen med hjälp av[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)uppräkning. Den har följande värden

- **TextCrossType.Default**Visa text som MS Excel som beror på nästa cell. Om nästa cell är null kommer strängen att korsas eller trunkeras.

- **TextCrossType.CrossKeep**: Visa strängen som MS Excel exporterar PDF/bild

- **TextCrossType.CrossOverride**: Visa all text genom att korsa andra celler och åsidosätta texten i korsade celler

- **TextCrossType.StrictInCell**: Visa endast strängen inom cellens bredd.

## **Ange hur strängen ska korsas i utdata PDF/bild med TextCrossType**

Följande exempelkod läser in exemplet på Excel-filen och sparar den i PDF-/bildformat genom att ange olika[**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)Exemplet på Excel-filen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
