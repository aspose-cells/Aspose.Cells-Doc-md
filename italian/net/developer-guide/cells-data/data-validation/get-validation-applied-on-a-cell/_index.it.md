---
title: Ottenere la convalida applicata su una cella
type: docs
weight: 200
url: /it/net/get-validation-applied-on-a-cell/
description: Questo articolo mostra come applicare la convalida su una cella con C#
keywords: applicare la convalida della cella in excel con c#, applicare la convalida su una cella in excel con c#, applicare la convalida in excel con c#, convalida della cella in excel con c#, c# applica la convalida della cella in excel, c# applica la convalida su una cella in excel, c# convalida della cella in excel, c# convalida della cella
---

{{% alert color="primary" %}}

È possibile utilizzare Aspose.Cells per ottenere la convalida applicata a una cella. Aspose.Cells fornisce il metodo [**Cell.GetValidation()**](https://reference.aspose.com/cells/net/aspose.cells/cell/methods/getvalidation) a tale scopo. Se sulla cella non è applicata alcuna convalida, restituisce null.

Allo stesso modo, è possibile utilizzare il metodo [**Worksheet.Validations.GetValidationInCell**](https://reference.aspose.com/cells/net/aspose.cells/validationcollection/methods/getvalidationincell) per acquisire la convalida applicata a una cella fornendo i suoi indici di riga e colonna.

{{% /alert %}}

## Codice C# per ottenere la convalida applicata su una cella

Nella seguente esempio di codice, ti mostra come ottenere la convalida applicata su una cella.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingRowsColumnsCells-GetValidationAppliedOnCell-GetValidationAppliedOnCell.cs" >}}

## Articoli correlati

- [Convalida Dati](/cells/it/net/data-validation/)
