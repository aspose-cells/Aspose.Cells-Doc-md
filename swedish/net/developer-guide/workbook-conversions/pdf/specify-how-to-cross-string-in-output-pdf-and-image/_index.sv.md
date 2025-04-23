---
title: Ange hur du ska korsa strängen i utdata PDF och bild
type: docs
weight: 120
url: /sv/net/specify-how-to-cross-string-in-output-pdf-and-image/
---

## **Möjliga användningsscenario**

När en cell innehåller text eller sträng men den är större än bredden på cellen, då överflödar strängen om nästa cell i nästa kolumn är tom eller tom. När du sparar din Excelfil till PDF/bild kan du styra det här flödet genom att specificera korsningsunikt med [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype)-uppräkning. Det har följande värden

- **TextCrossType.Default**: Visar text som MS Excel vilket beror på nästa cell. Om nästa cell är null korsar strängen eller så kommer den att bli avkortad.

- **TextCrossType.CrossKeep**: Visar strängen som MS Excel exporterar PDF/Bild

- **TextCrossType.CrossOverride**: Visar all text genom att korsa andra celler och ersätta texten i korsade celler

- **TextCrossType.StrictInCell**: Visar endast strängen inom cellens bredd.

## **Ange hur du ska korsa strängen i utdata PDF/Bild med hjälp av TextCrossType**

Följande exempelkod laddar den prov Excel-filen och sparar den i PDF/Bildformat genom att specificera olika [**TextCrossType**](https://reference.aspose.com/cells/net/aspose.cells/textcrosstype). Provfilen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Exempelkod

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-RenderUsingTextCrossType-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
