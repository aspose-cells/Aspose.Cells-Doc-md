---
title: Converti-Excel-in-JSON
type: docs
weight: 20
url: /it/java/convert-excel-to-json/
description: Scopri come convertire file excel in json con Aspose.Cells.
keywords: Exporting Workbook to json without office 2013, office 2016, office 2019 and office 365
---
{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di una cartella di lavoro in un file Json (JavaScript Object Notation).

{{% /alert %}}

## **Converti la cartella di lavoro di Excel in JSON**

 Non c'è bisogno di chiedersi come convertire la cartella di lavoro di Excel in JSON, perché la libreria Java Aspose.Cells ha la decisione migliore. L'API Java Aspose.Cells fornisce supporto per la conversione di fogli di calcolo in formato JSON. Per esportare la cartella di lavoro in JSON, passare[**SaveFormat.JSON**](https://reference.aspose.com/cells/java/com.aspose.cells/SaveFormat) come secondo parametro di[**Cartella di lavoro.save**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.lang.String,%20int) ) metodo. Puoi anche usare[**JsonSaveOptions**](https://reference.aspose.com/cells/java/com.aspose.cells/JsonSaveOptions) class per specificare impostazioni aggiuntive per l'esportazione del foglio di lavoro in JSON.

 L'esempio di codice seguente illustra l'esportazione della cartella di lavoro di Excel in Json. Si prega di consultare il codice per convertire[file sorgente](sample.xlsx) al file Json generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON.java" >}}

 L'esempio di codice seguente che utilizza la classe JsonSaveOptions per specificare impostazioni aggiuntive illustra l'esportazione della cartella di lavoro di Excel in Json. Si prega di consultare il codice per convertire[file sorgente](sample.xlsx) al file Json generato dal codice per riferimento.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Convert-Excel-to-JSON2.java" >}}
