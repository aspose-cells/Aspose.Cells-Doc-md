---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot
type: docs
weight: 880
url: /it/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells fornisce il[PivotTable.IsExcel2003Compatibile](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)proprietà che è possibile utilizzare per specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot. Se**VERO** , una stringa deve essere inferiore o uguale a 255 caratteri, quindi se la stringa è maggiore di 255 caratteri, verrà troncata. Se**falso** , una stringa non avrà la suddetta restrizione. Il valore predefinito è**VERO**.

{{% /alert %}} 
## **Specificare se la tabella pivot è compatibile con Excel2003 durante l'aggiornamento della tabella pivot**
 Il seguente codice di esempio spiega l'utilizzo di[PivotTable.IsExcel2003Compatibile](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) proprietà. La stringa originale è lunga 383 caratteri. Ma quando[PivotTable.IsExcel2003Compatibile](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) proprietà è impostata su**VERO** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando[PivotTable.IsExcel2003Compatibile](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) proprietà è impostata**falso** e la tabella pivot viene nuovamente aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di scaricare il[file excel di esempio](5472558.xlsx) utilizzato in questo codice,[file excel di output](5472557.xlsx) generato da esso e il suo output della console come riferimento. Si prega di leggere anche i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Uscita console**
Ecco l'output della console del codice di esempio precedente quando viene eseguito con il file given[file excel di esempio](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
