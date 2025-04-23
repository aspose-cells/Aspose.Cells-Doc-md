---
title: Specificare le cifre significative da memorizzare nel file Excel
type: docs
weight: 20
url: /it/java/specifying-significant-digits-to-be-stored-in-excel-file/
---

## **Possibili Scenari di Utilizzo**

Per impostazione predefinita, Aspose.Cells memorizza 17 cifre significative dei valori double nei fogli di calcolo, a differenza dell'applicazione Excel che ne memorizza solo 15. È possibile modificare il comportamento predefinito di Aspose.Cells per questo caso, ovvero è possibile cambiare il numero di cifre significative da 17 a 15 durante l'utilizzo della proprietà [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits).

## **Specificare le cifre significative da memorizzare nel file Excel**

Il seguente codice di esempio impone ad Aspose.Cells di utilizzare 15 cifre significative mentre memorizza i valori doppi all'interno del file di Excel. Si prega di controllare il [file di Excel di output](23166982.xlsx). Cambia la sua estensione in .zip e decomprimilo e vedrai che all'interno del file di Excel sono memorizzate solo 15 cifre significative. La seguente schermata mostra l'effetto della proprietà [**CellsHelper.SignificantDigits**](https://reference.aspose.com/cells/java/com.aspose.cells/cellshelper#SignificantDigits) sul file di Excel di output.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-CellsHelperClass-SignificantDigits-SignificantDigits.java" >}}
{{< app/cells/assistant language="java" >}}
