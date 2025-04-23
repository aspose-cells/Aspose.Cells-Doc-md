---
title: Ruota il testo con la forma all interno del foglio di lavoro
type: docs
weight: 1300
url: /it/python-net/rotate-text-with-shape-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

È possibile aggiungere del testo all'interno di qualsiasi forma utilizzando Microsoft Excel. Se si aggiunge la forma utilizzando la vecchissima Microsoft Excel 2003, il testo non ruoterà con la forma. Ma se si aggiunge la forma utilizzando le versioni più recenti di Microsoft Excel come ad esempio 2007, 2010, 2013 o 2016, ecc., allora il testo ruoterà con la forma. È possibile controllare se il testo deve ruotare con la forma o meno utilizzando la proprietà [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape). Il valore predefinito è **true**, il che significa che il testo ruoterà con la forma, ma se lo imposti su **false**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il seguente codice di esempio carica il [file di Excel di esempio](64716896.xlsx) che contiene una forma triangolare e il suo testo ruota con la forma. Se apri il file di Excel di esempio in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice imposta quindi la proprietà [**ShapeTextAlignment.rotate_text_with_shape**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing.texts/shapetextalignment/rotate_text_with_shape) su **false** e lo salva come [file di Excel di output](64716897.xlsx). Se apri ora il file di Excel di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà con essa. Si prega di vedere la seguente schermata che mostra l'effetto del codice sul file di Excel di esempio per riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Text-Options-RotateTextWithShapeInsideWorksheet.py" >}}
