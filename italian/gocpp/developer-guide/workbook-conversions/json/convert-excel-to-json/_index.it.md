---
title: Converti Excel in JSON con Golang tramite C++
linktitle: Converti Excel in JSON
type: docs
weight: 300
url: /it/go-cpp/convert-excel-to-json/
description: Impara come convertire un file Excel in JSON con Aspose.Cells usando C++.
keywords: Esportazione del Workbook in json senza office 2013, office 2016, office 2019 e office 365
---

{{% alert color="primary" %}}

Aspose.Cells supporta la conversione di un Workbook in un file Json(JavaScript Object Notation).

{{% /alert %}}

## **Converti Workbook Excel in JSON**

Non c'è bisogno di chiedersi come convertire un Workbook di Excel in JSON, perché la libreria Aspose.Cells for C++ offre la soluzione migliore. L'API Aspose.Cells supporta la conversione di fogli di calcolo in formato JSON. Per esportare il workbook in JSON, passa [**SaveFormat.Json**](https://reference.aspose.com/cells/go-cpp/saveformat/) come secondo parametro del metodo [**Workbook.Save**](https://reference.aspose.com/cells/cpp/aspose.cells/workbook/save/). Puoi anche usare la classe [**JsonSaveOptions**](https://reference.aspose.com/cells/cpp/aspose.cells/jsonsaveoptions/) per specificare impostazioni aggiuntive per esportare il foglio di lavoro in JSON.

Il seguente esempio di codice dimostra come esportare un Workbook di Excel in JSON. Consulta il codice per convertire il file di origine (sample.xlsx) nel file JSON generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson.go" >}}
Il seguente esempio di codice, che utilizza la classe JsonSaveOptions per specificare impostazioni aggiuntive, dimostra come esportare un Workbook di Excel in JSON. Consulta il codice per convertire il file di origine (sample.xlsx) nel file JSON generato dal codice come riferimento.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ConvertExcelToJson-1.go" >}}
