---
title: Specifica delle cifre significative da memorizzare nel file Excel
type: docs
weight: 20
url: /it/java/specifying-significant-digits-to-be-stored-in-excel-file/
---
## **Possibili scenari di utilizzo**

Per impostazione predefinita, Aspose.Cells memorizza 17 cifre significative di valori doppi nei fogli di calcolo a differenza dell'applicazione Excel che memorizza solo 15 cifre significative. È possibile modificare il comportamento predefinito di Aspose.Cells per questo caso, ovvero; è possibile modificare il numero di cifre significative da 17 a 15 mentre si utilizza il[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)proprietà.

## **Specifica delle cifre significative da memorizzare nel file Excel**

 Il seguente codice di esempio impone a Aspose.Cells di utilizzare 15 cifre significative durante l'archiviazione di valori doppi all'interno del file Excel. Si prega di controllare[file excel di output](23166982.xlsx) . Cambia la sua estensione in .zip e decomprimilo e vedrai che solo 15 cifre significative sono memorizzate all'interno del file excel. Lo screenshot seguente spiega l'effetto di[**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits)proprietà sul file excel di output.

![cose da fare:immagine_alt_testo](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Codice di esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
