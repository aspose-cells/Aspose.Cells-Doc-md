---
title: Ottieni la convalida applicata su uno Cell
type: docs
weight: 80
url: /it/java/get-validation-applied-on-a-cell/
description: Questo articolo mostra come applicare la convalida su uno Cell con Java
keywords: apply cell validation in excel with java, apply validation on a cell in excel with java, apply validation in excel with java, cell validation in excel with java, java apply cell validation in excel, java apply validation on a cell in excel, java cell validation in excel, java cell validation
---
{{% alert color="primary" %}}

 È possibile utilizzare Aspose.Cells API per ottenere la convalida applicata a qualsiasi cella. Aspose.Cells fornisce il[**Cell.getValidation**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#getValidation() ) metodo per questo scopo. Se non c'è convalida sulla cella, restituisce null. Allo stesso modo, puoi usare il[**Worksheet.getValidations().getValidationInCell(int riga, int colonna)**](https://reference.aspose.com/cells/java/com.aspose.cells/validationcollection#getValidationInCell(int,%20int)) per acquisire la validazione applicata ad una cella fornendo i suoi indici di riga e colonna.

{{% /alert %}}

 Lo snapshot seguente mostra il file Excel Microsoft di esempio utilizzato nel codice di esempio riportato di seguito. Cell**C1** ha**convalida decimale** applicato e può assumere solo valori**tra le 10 e le 20**.

**Una cella con convalida**

![cose da fare:immagine_alt_testo](get-validation-applied-on-a-cell_1.png)

Il codice di esempio seguente ottiene la convalida applicata a C1 e ne legge le varie proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-GetValidationAppliedonCell-GetValidationAppliedonCell.java" >}}

Ecco l'output della console dal codice di esempio eseguito con il file di esempio mostrato nell'istantanea sopra.

{{< highlight "java" >}}

Reading Properties of Validation

\--------------------------------

Type: 2

Operator: 0

Formula1: =10

Formula2: =20

Ignore blank: true

{{< /highlight >}}

## articoli Correlati

- [Convalida dei dati](/cells/it/java/data-validation/)
