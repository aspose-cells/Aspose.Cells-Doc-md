---  
title: Imposta i margini del commento o della forma all interno del foglio di lavoro con Golang via C++  
linktitle: Imposta i margini del commento o della forma all interno del foglio di lavoro  
type: docs  
weight: 1500  
url: /it/go-cpp/set-margins-of-comment-or-shape-inside-the-worksheet/  
description: Impara come impostare i margini dei commenti o delle forme all interno di un foglio di lavoro utilizzando Aspose.Cells con Golang via C++.  
---  

## **Possibili Scenari di Utilizzo**  

Aspose.Cells consente di impostare i margini di qualsiasi forma o commento usando la proprietà [**Shape.GetTextAlignment()**](https://reference.aspose.com/cells/go-cpp/fontsettingcollection/gettextalignment/). Questa proprietà restituisce l’oggetto della classe [**Aspose.Cells.Drawing.Texts.ShapeTextAlignment**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment) che ha diverse proprietà, ad esempio [**GetTopMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/gettopmarginpt/), [**GetLeftMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getleftmarginpt/), [**GetBottomMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getbottommarginpt/), [**GetRightMarginPt()**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing.texts/shapetextalignment/getrightmarginpt/), ecc., che possono essere usate per impostare i margini superiore, sinistro, inferiore e destro.  

## **Imposta i Margini del Commento o della Forma all'interno del Foglio di Lavoro**  

Vedi il seguente esempio di codice. Carica il [file Excel di esempio](61767851.xlsx) che contiene due forme. Il codice accede alle forme una alla volta e imposta i loro margini superiore, sinistro, inferiore e destro. Vedi il [file Excel di output](61767852.xlsx) generato dal codice e uno screenshot che mostra l’effetto del codice sul file di output.  

![todo:image_alt_text](set-margins-of-comment-or-shape-inside-the-worksheet_1.png)  

## **Codice di Esempio**  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SetMarginsOfCommentOrShapeInsideTheWorksheet.go" >}}  
