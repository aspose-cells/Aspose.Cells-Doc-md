---
title: Renderizza i caratteri Unicode supplementari nel PDF di output con Golang tramite C++ usando Aspose.Cells
linktitle: Renderizza caratteri Supplementari Unicode
type: docs
weight: 350
url: /it/go-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Scopri come rendere i caratteri Supplementari Unicode nel PDF di output usando Aspose.Cells for C++.
---

{{% alert color="primary" %}}

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri supplementari Unicode sono lunghi 4 byte. Aspose.Cells ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati a punti codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità di 16 bit).

{{% /alert %}}

## Rendere i caratteri supplementari Unicode nel PDF di output con Aspose.Cells

La seguente schermata mostra come Aspose.Cells ha reso il [file di Excel di origine](5115563.xlsx) nel [PDF di output](5115564.pdf). Come puoi vedere, tutti e tre i caratteri supplementari Unicode sono stati resi esattamente come fatto da Microsoft Excel.

![todo:image_alt_text](output.png)

## Codice di esempio

Puoi utilizzare questo codice di esempio per convertire [file di Excel di origine](5115563.xlsx) in [PDF di output](5115564.pdf).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderUnicodeSupplementaryCharactersInOutputPdfByAsposeCells.go" >}}
