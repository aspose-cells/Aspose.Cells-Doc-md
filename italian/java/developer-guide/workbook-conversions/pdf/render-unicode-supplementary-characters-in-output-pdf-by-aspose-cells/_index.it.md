---
title: Rendere i caratteri supplementari Unicode nel PDF di output con Aspose.Cells
type: docs
weight: 690
url: /it/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---

{{% alert color="primary" %}} 

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri supplementari Unicode sono lunghi 4 byte. Aspose.Cells ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati a punti codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità di 16 bit).

{{% /alert %}} 
## **Rende i Caratteri Unicode Supplementari nell'output PDF con Aspose.Cells**
Lo screenshot seguente mostra come Aspose.Cells abbia reso il [file excel di origine](5473390.xlsx) in [PDF di output](5473391.pdf). Come si può vedere, tutti e tre i Caratteri Unicode Supplementari sono stati resi esattamente allo stesso modo come fatto da Microsoft Excel.

![todo:image_alt_text](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

Puoi utilizzare questo codice di esempio per convertire il [file excel di origine](5473390.xlsx) in [PDF di output](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
