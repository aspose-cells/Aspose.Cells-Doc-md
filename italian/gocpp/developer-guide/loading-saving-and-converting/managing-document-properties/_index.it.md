---
title: Gestione delle proprietà del documento
type: docs
weight: 30
url: /it/go-cpp/managing-document-properties/
---

## **Scenario di utilizzo possibile**

Aspose.Cells consente di lavorare con le proprietà del documento integrate e personalizzate. Ecco l'interfaccia di Microsoft Excel per aprire queste *Proprietà del documento*. Basta fare clic su *Proprietà avanzate* come mostrato in questa schermata e visualizzarle.

![todo:image_alt_text](managing-document-properties_1.png)

## **Gestione delle proprietà del documento**

Il seguente esempio di codice carica [file Excel di esempio](23166989.xlsx) e legge le proprietà del documento integrate, ad esempio, *Titolo e Soggetto*, e poi le modifica. Successivamente, legge anche la proprietà personalizzata del documento, ad esempio, *MyCustom1*, e aggiunge una nuova proprietà personalizzata, cioè, *MyCustom5* e scrive il [file Excel di output](23166986.xlsx). La schermata seguente mostra l’effetto del codice di esempio sul file Excel di esempio.

![todo:image_alt_text](managing-document-properties_2.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ManagingDocumentProperties.go" >}}

## **Output della console**

Questo è l'output della console del codice di esempio sopra quando eseguito con il [file Excel di esempio](23166989.xlsx) fornito.

{{< highlight java >}}

Title: Aspose Team

Subject: Aspose.Cells for Go via C++

MyCustom1: This is my custom one.

{{< /highlight >}}
