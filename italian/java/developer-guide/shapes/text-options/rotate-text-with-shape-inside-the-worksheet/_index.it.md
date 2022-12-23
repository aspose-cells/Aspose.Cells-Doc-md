---
title: Ruota il testo con la forma all'interno del foglio di lavoro
type: docs
weight: 110
url: /it/java/rotate-text-with-shape-inside-the-worksheet/
---
## **Possibili scenari di utilizzo**

Puoi aggiungere testo all'interno di qualsiasi forma utilizzando Microsoft Excel. Se aggiungi la forma usando il vecchio Excel 2003 Microsoft, il testo non ruoterà con la forma. Ma se aggiungi la forma utilizzando le versioni più recenti di Microsoft Excel, ad esempio 2007, 2010, 2013 o 2016, ecc., il testo ruoterà con la forma. Puoi controllare se il testo deve ruotare con la forma o meno usando il[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)proprietà. Il valore predefinito è**VERO**il che significa che il testo ruoterà con la forma ma se lo imposti come**falso**, il testo non ruoterà con la forma.

## **Ruota il testo con la forma all'interno del foglio di lavoro**

Il codice di esempio seguente carica il file[esempio di file Excel](64716919.xlsx)che ha una forma triangolare e il suo testo ruota con la forma. Se apri il file Excel di esempio in Microsoft Excel e ruoti la forma triangolare, anche il testo ruoterà con esso. Il codice quindi imposta il[**ShapeTextAlignment.RotateTextWithShape**](https://reference.aspose.com/cells/java/com.aspose.cells/shapetextalignment#RotateTextWithShape)proprietà come**falso**e lo salva come[file Excel di output](64716917.xlsx). Se ora apri il file Excel di output in Microsoft Excel e ruoti la forma triangolare, il testo non ruoterà con esso. Si prega di vedere lo screenshot seguente che mostra l'effetto del codice sul file Excel di esempio per un riferimento.

![cose da fare:immagine_alt_testo](rotate-text-with-shape-inside-the-worksheet_1.png)

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "DrawingObjects-RotateTextWithShapeInsideWorksheet.java" >}}
