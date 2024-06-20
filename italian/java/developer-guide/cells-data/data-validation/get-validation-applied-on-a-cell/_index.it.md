---
title: Ottenere la convalida applicata su una cella
type: docs
weight: 80
url: /it/java/get-validation-applied-on-a-cell/
description: Questo articolo mostra come applicare la convalida su una cella con Java
keywords: applicare la convalida della cella in excel con java, applicare la convalida su una cella in excel con java, applicare la convalida in excel con java, convalida della cella in excel con java, convalida della cella in excel con java, convalida della cella in excel con java, convalida java della cella in excel, convalida java della cella in excel
---

{{% alert color="primary" %}}

Puoi utilizzare l'API Aspose.Cells per ottenere la convalida applicata a qualsiasi cella. Aspose.Cells fornisce il metodo [**Cell.getValidation()**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation--) per questo scopo. Se non c'è alcuna convalida sulla cella, restituisce null. Allo stesso modo, puoi utilizzare il metodo [**Worksheet.getValidations().getValidationInCell(int row, int column)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) per acquisire la convalida applicata a una cella fornendo i suoi indici di riga e colonna.

{{% /alert %}}

La schermata seguente mostra il file di esempio di Microsoft Excel utilizzato nel codice di esempio qui sotto. La cella **C1** ha la **convalida decimale** applicata e può assumere solo valori **compresi tra 10 e 20**.

**Una cella con convalida**

![todo:image_alt_text](get-validation-applied-on-a-cell_1.png)

Il codice di esempio di seguito ottiene la convalida applicata a C1 e legge le sue varie proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Ecco l'output della console dal codice di esempio eseguito con il file di esempio mostrato nello snapshot sopra.

{{< highlight java >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## Articoli correlati

- [Convalida Dati](/cells/it/java/data-validation/)
