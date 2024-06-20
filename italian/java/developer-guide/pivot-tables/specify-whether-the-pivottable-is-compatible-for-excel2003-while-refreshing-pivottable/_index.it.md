---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l aggiornamento della tabella pivot
type: docs
weight: 880
url: /it/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells fornisce la proprietà [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) che è possibile utilizzare per specificare se la tabella pivot è compatibile per Excel2003 durante l'aggiornamento della tabella pivot. Se **true**, una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se **false**, una stringa non avrà la suddetta restrizione. Il valore predefinito è **true**.

{{% /alert %}} 
## **Specificare se la tabella pivot è compatibile per Excel2003 durante l'aggiornamento della tabella pivot**
Il seguente codice di esempio spiega l'uso della proprietà [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible). La stringa originale è lunga 383 caratteri. Ma quando [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) property è impostata su **true** e la tabella pivot è aggiornata, i dati della cella B5 della tabella pivot sono troncati e diventano lunghi 255 caratteri. Tuttavia, quando [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) property è impostata su **false** e la tabella pivot viene nuovamente aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di scaricare il [file excel di esempio](5472558.xlsx) utilizzato in questo codice, il [file excel di output](5472557.xlsx) generato da esso e la relativa output console per riferimento. Si prega inoltre di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Output della console**
Ecco l'output console del codice di esempio sopra quando viene eseguito con il [file excel di esempio](5472558.xlsx) specificato.



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
