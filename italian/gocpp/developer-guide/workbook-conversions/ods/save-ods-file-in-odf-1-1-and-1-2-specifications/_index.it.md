---
title: Salva file ODS in specifiche ODF 1.1, 1.2 e 1.3 con Golang tramite C++
linktitle: Salva come ODF 1.1, 1.2 e 1.3
description: Converti Excel in specifiche ODF 1.1, 1.2 e 1.3 con Aspose.Cells usando C++.
type: docs
weight: 230
url: /it/go-cpp/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il salvataggio di un file ODS (**OpenDocument Spreadsheet**) nei requisiti ODF (**OpenDocument Format**) 1.1, 1.2 e 1.3. Aspose.Cells ha la proprietà [**OdsSaveOptions.GetOdfStrictVersion()**](https://reference.aspose.com/cells/go-cpp/odssaveoptions/getodfstrictversion/) che specifica la versione ODF per il salvataggio dei file ODS. Il valore predefinito di questa proprietà è [**OpenDocumentFormatVersionType.Odf12**](https://reference.aspose.com/cells/cpp/aspose.cells.ods/opendocumentformatversiontype/), quindi il file ODS salvato senza questa impostazione utilizza le specifiche 1.2.

{{% /alert %}}

Il codice di esempio di seguito crea un oggetto workspace, aggiunge alcuni valori alla cella A1 del primo foglio di lavoro e quindi salva il file ODS secondo le specifiche ODF 1.1, 1.2 e 1.3. Per impostazione predefinita, il file ODS viene salvato secondo le specifiche ODF 1.2.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-SaveOdsFileInOdf11And12Specifications.go" >}}
