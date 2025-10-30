---
title: Ange hur du ska korsa strängen i utdata PDF och bild
type: docs
weight: 120
url: /sv/python-net/specify-how-to-cross-string-in-output-pdf-and-image/
description: Lär dig hur man korsar strängar i utdata PDF och bild med Aspose.Cells för Python via .NET API.
keywords: Python Korsa strängar i utdata PDF och bild
---

## **Möjliga användningsscenario**

När en cell innehåller text eller sträng men den är större än bredden på cellen, då överflödar strängen om nästa cell i nästa kolumn är tom eller tom. När du sparar din Excelfil till PDF/bild kan du styra det här flödet genom att specificera korsningsunikt med [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/)-uppräkning. Det har följande värden

- **TextCrossType.DEFAULT**: Visa text som MS Excel som beror på nästa cell. Om nästa cell är tom kommer strängen att korsa eller bli avkortad.

- **TextCrossType.CROSS_KEEP**: Visa strängen som MS Excel exporterar PDF/bild

- **TextCrossType.CROSS_OVERRIDE**: Visa all text genom att korsa andra celler och åsidosätta texten i korsade celler

- **TextCrossType.STRICT_IN_CELL**: Visa endast strängen inom cellens bredd.

## **Ange hur du ska korsa strängen i utdata PDF/Bild med hjälp av TextCrossType**

Följande exempelkod laddar den prov Excel-filen och sparar den i PDF/Bildformat genom att specificera olika [**TextCrossType**](https://reference.aspose.com/cells/python-net/aspose.cells/textcrosstype/). Provfilen och utdatafilerna kan laddas ner från följande länkar:

[sampleCrossType.xlsx](81920905.xlsx)

[outputCrossType.pdf](81920903.pdf)

[outputCrossType.png](81920904.png)

### Exempelkod

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUsingTextCrossType-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
