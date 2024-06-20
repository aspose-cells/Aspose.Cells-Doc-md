---
title: Ruota il testo con la forma all interno del foglio di lavoro
type: docs
weight: 110
url: /it/java/rotate-text-with-shape-inside-the-worksheet/
---

## **Possibili Scenari di Utilizzo**

È possibile aggiungere testo all'interno di qualsiasi forma utilizzando Microsoft Excel. Se si aggiunge una forma utilizzando la vecchissima versione di Microsoft Excel 2003, quindi il testo non ruoterà con la forma. Ma se si aggiunge una forma utilizzando le versioni più recenti di Microsoft Excel, ad esempio 2007, 2010, 2013 o 2016, ecc., il testo ruoterà con la forma. Puoi controllare se il testo deve ruotare con la forma o meno utilizzando la proprietà [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape). Il valore predefinito è **true**, il che significa che il testo ruoterà con la forma, ma se lo imposti come **false**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il codice di esempio seguente carica il [file di Excel di esempio](64716919.xlsx) che ha una forma triangolare e il suo testo ruota con la forma. Se apri il file di Excel di esempio in Microsoft Excel e ruoti la forma triangolare, il testo ruoterà anche con essa. Il codice imposta quindi la proprietà [**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape) come **false** e lo salva come [file di Excel di output](64716917.xlsx). Se ora apri il file di Excel di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà con essa. Si prega di vedere la seguente schermata che mostra l'effetto del codice sul file di Excel di esempio come riferimento.

![todo:image_alt_text](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
