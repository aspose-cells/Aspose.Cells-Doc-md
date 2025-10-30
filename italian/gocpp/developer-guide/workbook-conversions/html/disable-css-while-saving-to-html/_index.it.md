---
title: Disabilita i CSS durante il salvataggio in HTML con Golang via C++
linktitle: Disabilitare CSS durante il salvataggio in HTML
type: docs
weight: 320
url: /it/go-cpp/disable-css-while-saving-to-html/
description: Impara come disattivare il CSS durante il salvataggio di file Excel in HTML usando Aspose.Cells for C++.
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel come HTML a pagina singola, di solito gli elementi CSS saranno incorporati nel file HTML e si troveranno nella sezione HEAD. Se allegi questo file come contenuto/corpo di un'email, gli elementi CSS saranno rimossi dalla maggior parte dei client di posta elettronica, causando rendering scorretto. La versione 24.12 di Aspose.Cells introduce un’opzione che permette di disabilitare opzionalmente il CSS, consentendo di applicare gli stili direttamente agli elementi HTML stessi. Se vuoi impostare l’HTML come contenuto/corpo dell’email, utilizza la proprietà [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/) e impostala su **true**.

## **Disabilita CSS durante il salvataggio in HTML**

Il seguente esempio di codice mostra l'uso della proprietà [**HtmlSaveOptions.GetDisableCss()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getdisablecss/).

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DisableCssWhileSavingToHtml.go" >}}
