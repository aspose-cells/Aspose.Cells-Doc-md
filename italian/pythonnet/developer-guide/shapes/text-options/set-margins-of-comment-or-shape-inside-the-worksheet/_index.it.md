---
title: Imposta i margini del commento o della forma all interno del foglio di lavoro
type: docs
weight: 1500
url: /it/python-net/set-margins-of-comment-or-shape-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells per Python via .NET consente di impostare i margini di qualsiasi forma o commento utilizzando la proprietà [**Shape.text_body.text_alignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/fontsettingcollection/text_alignment). Questa proprietà restituisce l'oggetto della classe [**ShapeTextAlignment**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment) che ha proprietà diverse come [**top_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/top_margin_pt), [**left_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/left_margin_pt), [**bottom_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/bottom_margin_pt), [**right_margin_pt**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/right_margin_pt), ecc. che possono essere utilizzate per impostare i margini superiore, sinistro, inferiore e destro.

## **Imposta i Margini del Commento o della Forma all'interno del Foglio di Lavoro**

Si prega di vedere il seguente codice di esempio. Carica il [file di Excel di esempio](61767851.xlsx) che contiene due forme. Il codice accede alle forme una per volta e imposta i loro margini superiore, sinistro, inferiore e destro. Si prega di vedere il [file di Excel di output](61767852.xlsx) generato dal codice e la schermata che mostra l'effetto del codice sul file di Excel di output.

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-SetMarginsOfCommentOrShapeInsideTheWorksheet.py" >}}
{{< app/cells/assistant language="python-net" >}}
