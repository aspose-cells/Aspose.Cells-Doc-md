---
title: Render Unicode Caratteri supplementari nell'output PDF di Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /it/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Scopri come eseguire il rendering dei caratteri supplementari Unicode durante la conversione di Excel in PDF con Aspose.Cells for Python via .NET API.
keywords: Python Render Unicode Supplementary characters while saving file to PDF, Print Unicode Supplementary characters while saving Excel to PDF using Python, Python Show Unicode Supplementary characters when converting Excel to PDF, Output Unicode Supplementary characters for excel to pdf
---
{{% alert color="primary" %}}

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri supplementari Unicode sono lunghi 4 byte. Aspose.Cells for Python via .NET ora supporta il rendering di questi caratteri Unicode a 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri a cui sono assegnati punti di codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi ciascuno 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità a 16 bit).

{{% /alert %}}

##  Render Unicode Caratteri supplementari nell'output PDF di Aspose.Cells for Python via .NET

 Lo screenshot seguente mostra come Aspose.Cells for Python via .NET ha reso il[file Excel di origine](5115563.xlsx) dentro[uscita PDF](5115564.pdf). Come puoi vedere, tutti e tre i caratteri supplementari Unicode sono stati renderizzati esattamente come fatto da Microsoft Excel.

![cose da fare:immagine_alt_testo](output.png)

##  Codice d'esempio

È possibile utilizzare questo codice di esempio per la conversione[file Excel di origine](5115563.xlsx) in[uscita PDF](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
