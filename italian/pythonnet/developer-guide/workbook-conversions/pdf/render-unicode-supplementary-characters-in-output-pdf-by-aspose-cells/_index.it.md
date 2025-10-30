---
title: Renderizza caratteri Unicode Supplementari nell output PDF con Aspose.Cells for Python via .NET
type: docs
weight: 350
url: /it/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/
description: Scopri come renderizzare i caratteri Unicode Supplementari durante la conversione di Excel in PDF con l API Aspose.Cells for Python via .NET.
keywords: Python renderizza caratteri Unicode Supplementari durante il salvataggio del file in PDF, Stampa caratteri Unicode Supplementari durante il salvataggio di Excel in PDF usando Python, Python Mostra caratteri Unicode Supplementari durante la conversione di Excel in PDF, Caratteri Unicode Supplementari per excel in pdf
---

{{% alert color="primary" %}}

I caratteri Unicode normali sono lunghi 2 byte mentre i caratteri Unicode supplementari sono lunghi 4 byte. Aspose.Cells for Python via .NET supporta ora il rendering di questi caratteri Unicode di 4 byte.

Nello standard dei caratteri Unicode, i caratteri supplementari sono i caratteri assegnati a punti codice da U+10000 a U+10FFFF. In altre parole, questi sono i caratteri Unicode maggiori di U+FFFF.

- In UTF-8 questi caratteri sono lunghi 4 byte.
- In UTF-16 questi caratteri richiedono 2 surrogati (unità di 16 bit).

{{% /alert %}}

## Renderizza caratteri Unicode Supplementari nell'output PDF con Aspose.Cells for Python via .NET

La seguente schermata mostra come Aspose.Cells for Python via .NET ha reso il [file di Excel di origine](5115563.xlsx) nel [PDF di output](5115564.pdf). Come puoi vedere, tutti e tre i caratteri Unicode supplementari sono stati resi esattamente come fatto da Microsoft Excel.

![todo:image_alt_text](output.png)

## Codice di esempio

Puoi utilizzare questo codice di esempio per convertire [file di Excel di origine](5115563.xlsx) in [PDF di output](5115564.pdf).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-RenderUnicodeInOutput.py" >}}
{{< app/cells/assistant language="python-net" >}}
