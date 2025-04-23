---
title: Ottenere la convalida applicata su una cella
type: docs
weight: 200
url: /it/nodejs-cpp/get-validation-applied-on-a-cell/
description: Questo articolo mostra come applicare la validazione su una cella con Node.js tramite C++.
keywords: Applica la validazione delle celle in Excel con Node.js tramite C++, applica la validazione su una cella in excel con Node.js tramite C++, applica la validazione in excel con Node.js tramite C++, validazione della cella in excel con Node.js tramite C++, Node.js tramite C++ applica validazione cella in excel, Node.js tramite C++ applica validazione su una cella in excel, Node.js tramite C++ validazione della cella in excel
---

{{% alert color="primary" %}}

Puoi usare Aspose.Cells per Node.js per ottenere la validazione applicata a una cella. Aspose.Cells fornisce il metodo [**Cell.getValidation()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getValidation--) per questo scopo. Se non c'è alcuna validazione applicata alla cella, restituisce null.

Allo stesso modo, è possibile utilizzare il metodo [**Worksheet.validations.getValidationInCell(number, number)**](https://reference.aspose.com/cells/nodejs-cpp/validationcollection/#getValidationInCell-number-number-) per acquisire la convalida applicata a una cella fornendo i suoi indici di riga e colonna.

{{% /alert %}}

## Codice Node.js per ottenere la validazione applicata su una cella

Il seguente esempio di codice mostra come ottenere la validazione applicata a una cella.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-DataValidation-ReadingValidationPropertiesOfCell.js" >}}


## Articoli correlati

- [Convalida Dati](/cells/it/nodejs-cpp/data-validation/)
