---
title: Specifica delle cifre significative da memorizzare nel file Excel
type: docs
weight: 30
url: /it/net/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Possibili Scenari di Utilizzo**

Per impostazione predefinita, Aspose.Cells memorizza 17 cifre significative dei valori double all'interno del file excel, a differenza di MS-Excel che memorizza solo 15 cifre significative. È possibile modificare il comportamento predefinito di Aspose.Cells da 17 cifre significative a 15 cifre significative utilizzando la proprietà [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits).

## **Specifica delle cifre significative da memorizzare nel file Excel**

Il codice di esempio seguente impone ad Aspose.Cells di utilizzare 15 cifre significative durante la memorizzazione dei valori double all'interno del file Excel. Si prega di controllare il [file Excel di output](22774105.xlsx). Cambia la sua estensione in .zip e decomprimilo e vedrai, solo 15 cifre significative sono memorizzate all'interno del file Excel. La seguente schermata spiega l'effetto della proprietà [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits) sul file Excel di output.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
