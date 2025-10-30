---
title: Ottieni il valore di una stringa della cella con o senza formattazione
type: docs
weight: 240
url: /it/nodejs-cpp/get-cell-string-value-with-and-without-formatting/
description: Impara come ottenere il valore stringa della cella con e senza formattazione attraverso l API Aspose.Cells for Node.js via C++.
keywords: Ottieni il valore stringa della cella con e senza formattazione Node.js tramite C++, Recupera il valore stringa della cella con e senza formattazione Node.js tramite C++, Ottieni il valore stringa della cella con e senza formattazione Node.js tramite C++
---

{{% alert color="primary" %}}

Aspose.Cells fornisce un metodo [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--) che può essere usato per ottenere il valore stringa della cella con o senza formattazione. Supponi di avere una cella con valore 0.012345 e di averla formattata per visualizzare solo due decimali. Verrà visualizzata come 0.01 in Excel. Puoi recuperare i valori stringa sia come 0.01 che come 0.012345 usando il metodo [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--). Prende come parametro l’enumerazione [**CellValueFormatStrategy**](https://reference.aspose.com/cells/nodejs-cpp/cellvalueformatstrategy/) che ha i seguenti valori.

- CellValueFormatStrategy.CellStyle
- CellValueFormatStrategy.DisplayStyle
- CellValueFormatStrategy.DisplayString
- CellValueFormatStrategy.None

{{% /alert %}}

Il seguente esempio di codice spiega l'uso del metodo [**Cell.getStringValue()**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStringValue--).

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-GetCellStringWithOrWithoutFormatting.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
