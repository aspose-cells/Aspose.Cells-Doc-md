---
title: Disabilita i commenti rivelati di livello inferiore durante il salvataggio in HTML con Golang via C++
linktitle: Disabilita Commenti Rivelati di livello inferiore
type: docs
weight: 20
url: /it/go-cpp/disable-downlevel-revealed-comments-while-saving-to/
description: Elimina i commenti rivelati di livello inferiore durante il salvataggio di file Excel in HTML usando Aspose.Cells con Golang via C++.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, Aspose.Cells rivela i Commenti Condizionali Downlevel. Questi commenti condizionali sono per lo più rilevanti per versioni più vecchie di Internet Explorer e sono irrilevanti per browser Web moderni. Puoi leggerne i dettagli al seguente link.

- [Commento condizionale - Commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells ti permette di eliminare questi Commenti Rivelati Downlevel impostando la proprietà [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/) su **true**.

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.GetDisableDownlevelRevealedComments()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisabledownlevelrevealedcomments/). Lo screenshot mostra l'effetto di questa proprietà quando non è impostata su true. Scarica il [file Excel di esempio](50528257.xlsx) usato in questo codice e l'[HTML di output](50528258.zip) generato per un riferimento.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableDownlevelRevealedCommentsWhileSavingToHtml.go" >}}
