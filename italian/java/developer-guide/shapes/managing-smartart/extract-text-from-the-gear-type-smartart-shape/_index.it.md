---
title: Estrai il testo dalla forma SmartArt Tipo di ingranaggio
type: docs
weight: 130
url: /it/java/extract-text-from-the-gear-type-smartart-shape/
---
## **Possibili scenari di utilizzo**

Aspose.Cells può estrarre il testo dalla forma artistica intelligente del tipo di ingranaggio. Per fare ciò, devi prima convertire Smart Art Shape in Group Shape usando il[**Shape.getResultOfSmartArt()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#getResultOfSmartArt()) metodo. Quindi dovresti ottenere l'array di tutte le forme individuali che formano la forma del gruppo usando il[**GroupShape.getGroupedShapes()**](https://reference.aspose.com/cells/java/com.aspose.cells/groupshape#getGroupedShapes()) metodo. Infine, puoi iterare tutte le singole forme una per una in un ciclo ed estrarre il loro testo usando il[**Forma.Testo**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Text)proprietà.

## **Estrai il testo dalla forma SmartArt Tipo di ingranaggio**

Il codice di esempio seguente carica il file[esempio di file Excel](67338510.xlsx)che contiene Gear Type Smart Art Shape. Quindi estrae il testo dalle sue singole forme come discusso sopra. Si prega di consultare l'output della console del codice fornito di seguito per un riferimento.

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.java" >}}

## **Uscita console**

{{< highlight "java" >}}

Gear Type Shape Text: Nice Gear Type Shape Text: Good Gear Type Shape Text: Excellent

{{< /highlight >}}
