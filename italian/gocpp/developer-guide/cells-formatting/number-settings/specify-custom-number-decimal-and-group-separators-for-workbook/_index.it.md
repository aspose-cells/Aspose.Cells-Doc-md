---
title: Specifica i Separatori Decimali e di Gruppo Personalizzati per il Workbook con Golang tramite C++
linktitle: Specificare i separatori decimali e di gruppo personalizzati
type: docs
weight: 110
url: /it/go-cpp/specify-custom-number-decimal-and-group-separators-for-workbook/
description: Cambia i separatori decimali e di gruppo per i numeri in MS Excel e con Golang tramite codice C++ usando l API Aspose.Cells for C++.
keywords: specificare separatore decimale personalizzato excel, specificare separatore decimale personalizzato C++, specificare separatore di gruppo personalizzato excel, specificare separatore di gruppo personalizzato C++, specificare separatore decimale e di gruppo personalizzato excel, specificare separatore decimale e di gruppo personalizzato C++, cambiare separatore decimale in excel, cambiare separatore di gruppo in excel, cambiare separatore decimale in excel C++, cambiare separatore di gruppo in excel C++
---

{{% alert color="primary" %}}

In Microsoft Excel, è possibile specificare i separatori decimali e migliaia personalizzati invece di utilizzare i separatori di sistema dalle **Opzioni Avanzate di Excel** come mostrato nella schermata sottostante.

Aspose.Cells fornisce le proprietà [**WorkbookSettings.GetNumberDecimalSeparator()**](https://reference.aspose.com/cells/go-cpp/workbooksettings/getnumberdecimalseparator/) e [**WorkbookSettings.GetNumberGroupSeparator()**](https://reference.aspose.com/cells/cpp/aspose.cells/workbooksettings/getnumbergroupseparator/) per impostare i separatori personalizzati per la formattazione/analisi dei numeri.

{{% /alert %}}

## **Specificare i Separatori Personalizzati utilizzando Microsoft Excel**

La seguente schermata mostra le **Opzioni Avanzate di Excel** e evidenzia la sezione per specificare i **Separatori Personalizzati**.

![todo:image_alt_text](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Specificare separatori personalizzati utilizzando Aspose.Cells**

Il seguente codice di esempio illustra come specificare i separatori personalizzati utilizzando l'API Aspose.Cells. Specifica i separatori personalizzati per il numero decimale e per il raggruppamento come rispettivamente punto e spazio.

### Codice C++ per specificare separatori decimali e di gruppo personalizzati

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyCustomNumberDecimalAndGroupSeparatorsForWorkbook.go" >}}
