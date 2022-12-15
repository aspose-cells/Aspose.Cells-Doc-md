---
title: Specifica delle cifre significative da memorizzare nel file Excel
type: docs
weight: 30
url: /it/net/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Possibili scenari di utilizzo**

Per impostazione predefinita, Aspose.Cells memorizza 17 cifre significative di valori doppi all'interno del file excel, a differenza di MS-Excel che memorizza solo 15 cifre significative. È possibile modificare il comportamento predefinito di Aspose.Cells da 17 cifre significative a 15 cifre significative utilizzando il[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)proprietà.

## **Specifica delle cifre significative da memorizzare nel file Excel**

 Il seguente codice di esempio impone a Aspose.Cells di utilizzare 15 cifre significative durante l'archiviazione di valori doppi all'interno del file Excel. Si prega di controllare[file excel di output](22774105.xlsx) . Cambia la sua estensione in .zip e decomprimilo e vedrai che solo 15 cifre significative sono memorizzate all'interno del file excel. Lo screenshot seguente spiega l'effetto di[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/net/aspose.cells/cellshelper/properties/significantdigits)proprietà sul file excel di output.

![cose da fare:immagine_alt_testo](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-SignificantDigits.cs" >}}
