---
title: Estrarre il testo dalla forma di Arte intelligente di tipo Gear
type: docs
weight: 500
url: /it/python-net/extract-text-from-the-gear-type-smartart-shape/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells può estrarre il testo dalla forma di Arte intelligente di tipo Gear. Per farlo, devi prima convertire la forma di Arte intelligente in Forma di gruppo utilizzando il metodo [**Shape.get_result_of_smart_art()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/get_result_of_smart_art). Poi dovresti ottenere l'array di tutte le forme individuali che compongono la Forma di gruppo utilizzando il metodo [**GroupShape.get_grouped_shapes()**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/groupshape/get_grouped_shapes). Infine, puoi iterare tutte le forme individuali una per una in un loop ed estrarre il loro testo utilizzando la proprietà [**Shape.text**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/text).

## **Estrarre il testo dalla forma SmartArt di tipo ingranaggio**

Il seguente codice di esempio carica il [file di Excel di esempio](67338483.xlsx) che contiene la forma di Arte intelligente di tipo Gear. Quindi estrae il testo dalle sue forme individuali come discusso in precedenza. Si prega di consultare l'output della console del codice fornito di seguito per riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractTextFromGearTypeSmartArtShape.py" >}}

## **Output della console**

{{< highlight java >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
