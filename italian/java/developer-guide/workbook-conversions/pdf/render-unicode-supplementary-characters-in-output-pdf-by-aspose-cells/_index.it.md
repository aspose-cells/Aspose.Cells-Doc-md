---
title: Renderizza i caratteri supplementari Unicode nel PDF di output di Aspose.Cells
type: docs
weight: 690
url: /it/java/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
---
{{% alert color="primary" %}} 

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri Supplementari Unicode sono lunghi 4 byte. Aspose.Cells ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati ai punti di codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi ciascuno 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità a 16 bit).

{{% /alert %}} 
## **Renderizza i caratteri supplementari Unicode nel PDF di output di Aspose.Cells**
 Lo screenshot seguente mostra come Aspose.Cells ha reso il file[file excel di origine](5473390.xlsx) dentro[uscita PDF](5473391.pdf)Come puoi vedere, tutti e tre i caratteri supplementari Unicode sono stati resi esattamente come da Microsoft Excel.

![cose da fare:immagine_alt_testo](render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells_1.png)

È possibile utilizzare questo codice di esempio per convertire il file[file excel di origine](5473390.xlsx) in[uscita PDF](5473391.pdf).

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-RenderUnicodeSupplimentaryCharacterToPDF-1.java" >}}
