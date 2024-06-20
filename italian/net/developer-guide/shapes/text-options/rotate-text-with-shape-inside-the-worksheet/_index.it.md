---
title: Ruota il testo con la forma all interno del foglio di lavoro
type: docs
weight: 1300
url: /it/net/rotate-text-with-shape-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

È possibile aggiungere del testo all'interno di qualsiasi forma utilizzando Microsoft Excel. Se si aggiunge la forma utilizzando la vecchissima Microsoft Excel 2003, il testo non ruoterà con la forma. Ma se si aggiunge la forma utilizzando le versioni più recenti di Microsoft Excel come ad esempio 2007, 2010, 2013 o 2016, ecc., allora il testo ruoterà con la forma. È possibile controllare se il testo deve ruotare con la forma o meno utilizzando la proprietà [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape). Il valore predefinito è **true**, il che significa che il testo ruoterà con la forma, ma se lo imposti su **false**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il seguente codice di esempio carica il [file di Excel di esempio](64716896.xlsx) che contiene una forma triangolare e il suo testo ruota con la forma. Se apri il file di Excel di esempio in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice imposta quindi la proprietà [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/net/aspose.cells.drawing.texts/shapetextalignment/properties/rotatetextwithshape) su **false** e lo salva come [file di Excel di output](64716897.xlsx). Se apri ora il file di Excel di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà con essa. Si prega di vedere la seguente schermata che mostra l'effetto del codice sul file di Excel di esempio per riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "DrawingObjects-RotateTextWithShapeInsideWorksheet.cs" >}}
