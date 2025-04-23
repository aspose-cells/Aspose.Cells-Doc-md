---
title: Disabilitare i commenti rivelati di livello inferiore durante il salvataggio in formato HTML
type: docs
weight: 20
url: /it/python-net/disable-downlevel-revealed-comments-while-saving-to/
---

## **Possibili Scenari di Utilizzo**

Quando salvi il tuo file Excel in HTML, allora Aspose.Cells per Python via .NET rivelano Commenti Condizionali di Livello Inferiore. Questi commenti condizionali sono principalmente rilevanti per versioni più vecchie di Internet Explorer e sono irrilevanti per i browser Web moderni. Puoi leggerli in dettaglio al seguente link.

- [Commento condizionale - Commento condizionale rivelato di livello inferiore](https://en.wikipedia.org/wiki/Conditional_comment#Downlevel-revealed_conditional_comment)

Aspose.Cells per Python via .NET permette di eliminare questi Commenti Rivelati di Livello Inferiore impostando la proprietà [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments) su **true**.

## **Disabilita i Commenti Rivelati di Basso Livello durante il Salvataggio in HTML**

Il seguente codice di esempio mostra l'uso della proprietà [**HtmlSaveOptions.disable_downlevel_revealed_comments**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/disable_downlevel_revealed_comments). La schermata mostra l'effetto di questa proprietà quando non è impostata su **true**. Si prega di scaricare il [file Excel di esempio](50528257.xlsx) utilizzato in questo codice e l'[HTML di output](50528258.zip) generato da esso per un riferimento.

![todo:image_alt_text](disable-downlevel-revealed-comments-while-saving-to-html_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-DisableDownlevelRevealedCommentsWhileSavingToHTML.py" >}}
