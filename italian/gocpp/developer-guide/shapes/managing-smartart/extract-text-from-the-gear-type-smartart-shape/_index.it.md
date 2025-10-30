---
title: Estrai il testo dalla forma SmartArt di tipo ingranaggio con Golang tramite C++
linktitle: Estrarre il testo dalla forma di Arte intelligente di tipo Gear
type: docs
weight: 500
url: /it/go-cpp/extract-text-from-the-gear-type-smartart-shape/
description: Impara come estrarre testo da forme SmartArt di tipo Gear in Excel usando Aspose.Cells for C++ con guida passo passo ed esempi di codice.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells for C++ può estrarre testo da SmartArt di tipo Gear. Per farlo, segui questi passi:
1. Converti SmartArt Shape in forma di gruppo usando il metodo [**Shape::GetResultOfSmartArt()**](https://reference.aspose.com/cells/go-cpp/).
2. Recupera tutte le forme individuali che compongono il SmartArt Shape utilizzando il metodo [**GroupShape::GetGroupedShapes()**](https://reference.aspose.com/cells/go-cpp/).
Itera attraverso ogni singola forma ed estrai il testo usando il metodo [**GetText()**](https://reference.aspose.com/cells/go-cpp/).

## **Estrarre il testo dalla forma SmartArt di tipo ingranaggio**

Il seguente esempio di codice carica un [file Excel di esempio](67338483.xlsx) contenente una Forma SmartArt di Tipo Ingranaggio e ne estrae il testo dalle sue forme individuali. Consulta l'output della console sotto per i risultati.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractTextFromTheGearTypeSmartartShape.go" >}}
## **Output della console**

{{< highlight java >}}
Gear Type Shape Text: Nice
Gear Type Shape Text: Good
Gear Type Shape Text: Excellent
{{< /highlight >}}
