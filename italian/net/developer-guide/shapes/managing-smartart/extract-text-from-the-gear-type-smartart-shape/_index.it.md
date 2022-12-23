---
title: Estrai il testo dalla forma SmartArt Tipo di ingranaggio
type: docs
weight: 500
url: /it/net/extract-text-from-the-gear-type-smartart-shape/
---
## **Possibili scenari di utilizzo**

 Aspose.Cells può estrarre il testo dalla forma artistica intelligente del tipo di ingranaggio. Per fare ciò, devi prima convertire Smart Art Shape in Group Shape usando il[**Shape.GetResultOfSmartArt()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/methods/getresultofsmartart) metodo. Quindi dovresti ottenere l'array di tutte le forme individuali che formano la forma del gruppo usando il[**GroupShape.GetGroupedShapes()**](https://reference.aspose.com/cells/net/aspose.cells.drawing/groupshape/methods/getgroupedshapes) metodo. Infine, puoi iterare tutte le singole forme una per una in un ciclo ed estrarre il loro testo usando il[**Forma.Testo**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/text)proprietà.

## **Estrai il testo dalla forma SmartArt Tipo di ingranaggio**

 Il codice di esempio seguente carica il file[esempio di file Excel](67338483.xlsx) che contiene Gear Type Smart Art Shape. Quindi estrae il testo dalle sue singole forme come discusso sopra. Si prega di consultare l'output della console del codice fornito di seguito per un riferimento.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-ExtractTextFromGearTypeSmartArtShape.cs" >}}

## **Uscita console**

{{< highlight "java" >}}

Gear Type Shape Text: Nice

Gear Type Shape Text: Good

Gear Type Shape Text: Excellent

{{< /highlight >}}
