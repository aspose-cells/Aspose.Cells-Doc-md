---
title: Ottieni il valore della stringa della cella con la strategia di formattazione
type: docs
weight: 240
url: /it/python-net/get-cell-string-value-with-format-strategy/
description: Scopri come ottenere il valore della stringa della cella con e senza formattazione tramite Aspose.Cells for Python via .NET API.
keywords: Libreria Excel Python, Python Ottieni il valore della stringa della cella con e senza formattazione, Python Recupera il valore della stringa della cella con e senza formattazione, Python Ottieni il valore della stringa della cella con e senza formattazione
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET fornisce un metodo [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/) che può essere utilizzato per ottenere il valore della stringa della cella con o senza formattazione. Supponiamo che tu abbia una cella con valore 0.012345 e l'abbia formattata per visualizzare solo due cifre decimali. Visualizzerà quindi come 0.01 in Excel. Puoi recuperare i valori della stringa sia come 0.01 che come 0.012345 utilizzando il metodo [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/). Richiede come parametro l'enum [**CellValueFormatStrategy**](https://reference.aspose.com/cells/python-net/aspose.cells/cellvalueformatstrategy/) che ha i seguenti valori

- CellValueFormatStrategy.CELL_STYLE
- CellValueFormatStrategy.DISPLAY_STYLE
- CellValueFormatStrategy.DISPLAY_STRING
- CellValueFormatStrategy.NONE

{{% /alert %}}

Il seguente codice di esempio spiega l'uso del metodo [**Cell.get_string_value(format_strategy)**](https://reference.aspose.com/cells/python-net/aspose.cells/cell/get_string_value/).

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-HtmlStringValue-GetStringValueWithOrWithoutFormatting.py" >}}
{{< app/cells/assistant language="python-net" >}}
