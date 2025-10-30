---
title: Specificare se la tabella pivot è compatibile con Excel2003 durante l aggiornamento della tabella pivot
type: docs
weight: 80
url: /it/nodejs-cpp/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}}

Aspose.Cells for Node.js via C++ fornisce la proprietà [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) che puoi usare per specificare se la PivotTable è compatibile con Excel 2003 durante l'aggiornamento. Se vero, la stringa deve essere lunga al massimo 255 caratteri, quindi se la stringa supera questa lunghezza verrà troncata. Se **falso**, la stringa non avrà questa restrizione. Il valore predefinito è **true**.

{{% /alert %}}

## **Specificare se la tabella pivot è compatibile per Excel2003 durante l'aggiornamento della tabella pivot**

Il codice di esempio seguente spiega l'uso della proprietà [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-). La stringa originale è lunga 383 caratteri. Ma quando la proprietà [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) è impostata su **true** e la tabella pivot viene aggiornata, i dati della cella B5 della tabella pivot vengono troncati e diventano lunghi 255 caratteri. Tuttavia, quando la proprietà [**PivotTable.setIsExcel2003Compatible**](https://reference.aspose.com/cells/nodejs-cpp/pivottable/#setIsExcel2003Compatible-boolean-) è impostata su **false** e la tabella pivot viene di nuovo aggiornata, i dati della cella B5 della tabella pivot non vengono troncati e rimangono lunghi 383 caratteri. Si prega di leggere i commenti all'interno del codice per una migliore comprensione di questa proprietà.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-SpecifyCompatibility-1.js" >}}

{{< app/cells/assistant language="nodejs-cpp" >}}
