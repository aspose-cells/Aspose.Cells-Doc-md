---
title: Estrarre il testo dalla forma di Arte intelligente di tipo Gear
type: docs
weight: 130
url: /it/java/extract-text-from-the-gear-type-smartart-shape/
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells può estrarre il testo dalla forma di arte Smart Art dei tipi di ingranaggi. Per farlo, devi prima convertire la Forma di Arte Intelligente in Forma di Gruppo utilizzando il metodo [**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt--). Poi dovresti ottenere l'array di tutte le Forme Individuali che formano la Forma di Gruppo utilizzando il metodo [**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes--). Infine, puoi iterare tutte le Forme Individuali una per una in un ciclo ed estrarre il loro testo utilizzando la proprietà [**Shape.Text**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text).

## **Estrarre il testo dalla forma SmartArt di tipo ingranaggio**

Il seguente codice di esempio carica il [file di Excel di esempio](67338510.xlsx) che contiene la Forma di Arte Smart Art dei tipi di ingranaggi. Quindi estrae il testo dalle sue forme individuali come discusso sopra. Si prega di vedere l'output console del codice riportato di seguito per riferimento.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Output della console**

{{< highlight java >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
