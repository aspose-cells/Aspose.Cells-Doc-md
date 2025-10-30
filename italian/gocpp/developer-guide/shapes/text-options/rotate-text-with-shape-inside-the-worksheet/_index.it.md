---
title: Ruota il testo con forma all interno del foglio di lavoro con Golang via C++
linktitle: Ruota il testo con la forma
type: docs
weight: 1300
url: /it/go-cpp/rotate-text-with-shape-inside-the-worksheet/
description: Impara come controllare la rotazione del testo con le forme nei fogli di lavoro di Excel usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Puoi aggiungere testo all’interno di qualsiasi forma usando Microsoft Excel. Se aggiungi una forma usando la vecchia versione di Microsoft Excel 2003, il testo non ruoterà con la forma. Tuttavia, se usi versioni più recenti come 2007, 2010, 2013 o 2016, il testo ruoterà con la forma. Puoi controllare se il testo dovrebbe ruotare con la forma o meno usando la proprietà [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/). Il valore predefinito di questa proprietà è **true**, il che significa che il testo ruoterà con la forma. Se lo imposti su **false**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il seguente esempio di codice carica il [file Excel di esempio](64716896.xlsx) che contiene una forma triangolare, e il suo testo ruota con la forma. Se apri il file in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice quindi imposta la proprietà [**ShapeTextAlignment.GetRotateTextWithShape()**](https://reference.aspose.com/cells/go-cpp/shapetextalignment/getrotatetextwithshape/) su **false** e lo salva come [file Excel di output](64716897.xlsx). Se ora apri il file di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà più con essa. Vedi lo screenshot seguente che mostra l’effetto del codice sul file Excel di esempio per riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RotateTextWithShapeInsideTheWorksheet.go" >}}
