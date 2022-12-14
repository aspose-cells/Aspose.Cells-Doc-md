---
title: Renderizza i caratteri supplementari Unicode nel PDF di output di Aspose.Cells
type: docs
weight: 350
url: /it/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}}

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri Supplementari Unicode sono lunghi 4 byte. Aspose.Cells ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati ai punti di codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi ciascuno 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità a 16 bit).

{{% /alert %}}

## Renderizza i caratteri supplementari Unicode nel PDF di output di Aspose.Cells

 Lo screenshot seguente mostra come Aspose.Cells ha reso il file[file excel di origine](5115563.xlsx) dentro[uscita PDF](5115564.pdf). Come puoi vedere, tutti e tre i caratteri supplementari Unicode sono stati resi esattamente come da Microsoft Excel.

![cose da fare:immagine_alt_testo](output.png)

## Codice di esempio

 È possibile utilizzare questo codice di esempio per convertire[file excel di origine](5115563.xlsx) in[uscita PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderUnicodeInOutput-RenderUnicodeInOutput.cs" >}}
