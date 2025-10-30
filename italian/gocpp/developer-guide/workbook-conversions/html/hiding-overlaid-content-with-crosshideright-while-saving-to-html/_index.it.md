---
title: Nascondi contenuti sovrapposti con CrossHideRight durante il salvataggio in HTML con Golang via C++
linktitle: Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML
type: docs
weight: 100
url: /it/go-cpp/hiding-overlaid-content-with-crosshideright-while-saving-to/
description: Usa CrossHideRight con Aspose.Cells in C++ per nascondere contenuto sovrapposto durante il salvataggio in HTML.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, puoi specificare diversi tipi di incrocio per le stringhe di celle. Per impostazione predefinita, Aspose.Cells genera HTML come Microsoft Excel, ma quando cambi il tipo di incrocio in [**CrossHideRight**](https://reference.aspose.com/cells/go-cpp/htmlcrosstype), allora nasconde tutte le stringhe sul lato destro della cella sovrapposte o sopraffatte dalla stringa della cella.

## **Nascondere il contenuto sovrapposto con CrossHideRight durante il salvataggio in HTML**

Il seguente esempio di codice carica il [file Excel di esempio](64716894.xlsx) e lo salva in [HTML di output](64716893.zip) dopo aver impostato [**HtmlSaveOptions.GetHtmlCrossStringType()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/gethtmlcrossstringtype/) come [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype). Lo screenshot mostra come [**CrossHideRight**](https://reference.aspose.com/cells/cpp/aspose.cells/htmlcrosstype) influenza l'HTML di output rispetto all'output predefinito.

![todo:image_alt_text](hiding-overlaid-content-with-crosshideright-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HidingOverlaidContentWithCrosshiderightWhileSavingToHtml.go" >}}
