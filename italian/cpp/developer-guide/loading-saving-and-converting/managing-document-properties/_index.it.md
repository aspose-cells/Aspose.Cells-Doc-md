---
title: Gestione delle proprietà del documento
type: docs
weight: 30
url: /it/cpp/managing-document-properties/
---

## **Scenario di utilizzo possibile**
Aspose.Cells consente di lavorare con le proprietà del documento integrate e personalizzate. Ecco l'interfaccia di Microsoft Excel per aprire queste *Proprietà del documento*. Basta fare clic su *Proprietà avanzate* come mostrato in questa schermata e visualizzarle.

![todo:image_alt_text](managing-document-properties_1.png)
## **Gestione delle proprietà del documento**
Il seguente codice di esempio carica il [file di Excel di esempio](23166989.xlsx) e legge le proprietà del documento integrate ad es. *Titolo, Oggetto* e poi le cambia. Poi legge anche la proprietà del documento personalizzata cioè *MyCustom1* e poi ne aggiunge una nuova personalizzata cioè *MyCustom5* e scrive il [file di Excel di output](23166986.xlsx). La schermata seguente mostra l'effetto del codice di esempio sul file di Excel di esempio.

![todo:image_alt_text](managing-document-properties_2.png)
## **Codice di Esempio**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Examples-CellsCPP-LoadingSavingAndConverting-ManagingDocumentProperties-new.cpp" >}}


## **Output della console**
Questo è l'output della console del codice di esempio sopra quando eseguito con il [file di Excel di esempio](23166989.xlsx).

{{< highlight java >}}

 Title: Aspose Team

Subject: Aspose.Cells for C++

MyCustom1: This is my custom one.

{{< /highlight >}}
