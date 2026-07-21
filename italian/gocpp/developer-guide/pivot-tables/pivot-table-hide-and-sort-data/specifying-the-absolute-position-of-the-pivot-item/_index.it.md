---
title: Specificare la posizione assoluta dell elemento pivot con Golang tramite C++
linktitle: Specificare la posizione assoluta dell elemento pivot
type: docs
weight: 50
url: /it/go-cpp/specifying-the-absolute-position-of-the-pivot-item/
description: Impara come specificare la posizione assoluta degli elementi pivot in C++ usando Aspose.Cells.
---

{{% alert color="primary" %}}

A volte, gli utenti hanno bisogno di specificare la posizione assoluta degli elementi pivot. L'API Aspose.Cells ha introdotto alcune nuove proprietà e un metodo per raggiungere questo obiettivo.

- Aggiunta la proprietà [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/) che può essere utilizzata per specificare l'indice di posizione in tutti i PivotItems indipendentemente dal nodo genitore. Aggiunta la proprietà [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) che può essere utilizzata per specificare l'indice di posizione nei PivotItems sotto lo stesso nodo genitore.
- Aggiunto il metodo [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/) per spostare l'elemento su o giù in base al valore del conteggio, dove il conteggio è il numero di posizioni da spostare l'elemento Pivot su o giù. Se il valore del conteggio è inferiore a zero, l'elemento verrà spostato verso l'alto, mentre se il valore è maggiore di zero, l'elemento Pivot si sposterà verso il basso. Il parametro di tipo Boolean `isSameParent` specifica se l'operazione di spostamento deve essere eseguita nello stesso nodo genitore o meno.
- Come risposta, il metodo `PivotItem.Move(int count)` è stato deprecato; si consiglia di utilizzare invece il nuovo metodo [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/go-cpp/pivotitem/move/).

{{% /alert %}}

Il seguente esempio di codice crea una tabella pivot e poi specifica le posizioni degli elementi Pivot nello stesso nodo genitore. Puoi scaricare il file Excel [sorgente](5112632.xlsx) e [output](5112619.xlsx) per tuo riferimento. Se apri il file Excel di output, vedrai che l'elemento Pivot "4H12" si trova alla posizione 0 nel genitore "K11" e "DIF400" è alla posizione 3. Similarmente, CA32 si trova alla posizione 1 e AAA3 alla posizione 2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SpecifyingTheAbsolutePositionOfThePivotItem.go" >}}
{{% alert color="primary" %}}

Nota: è necessario chiamare i metodi `PivotTable.RefreshData` e `PivotTable.CalculateData` prima di utilizzare le proprietà [**PivotItem.GetPosition()**](https://reference.aspose.com/cells/go-cpp/pivotitem/getposition/), [**PivotItem.GetPositionInSameParentNode()**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/getpositioninsameparentnode/) e il metodo [**PivotItem.Move(int count, bool isSameParent)**](https://reference.aspose.com/cells/cpp/aspose.cells.pivot/pivotitem/move/).

{{% /alert %}}
