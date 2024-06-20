---
title: Salva file ODS nelle specifiche ODF 1.1 e 1.2
linktitle: Salva come ODF 1.1 e 1.2 
description: Converti Excel in specifiche ODF 1.1 e 1.2 con Aspose.Cells.
type: docs
weight: 230
url: /it/net/save-ods-file-in-odf-1-1-and-1-2-specifications/
---

{{% alert color="primary" %}}

Aspose.Cells supporta il salvataggio di un file ODS (OpenDocument Spreadsheet) nelle specifiche ODF (OpenDocument Format) 1.1 e 1.2. Aspose.Cells dispone della proprietà [**OdsSaveOptions.IsStrictSchema11**](https://reference.aspose.com/cells/net/aspose.cells/odssaveoptions/properties/isstrictschema11) che specifica l'uso della specifica ODF 1.1 per il salvataggio dei file ODS. Il valore predefinito di questa proprietà è **false**, quindi il file ODS salvato senza questa impostazione utilizza le specifiche 1.2.

{{% /alert %}}

Il codice di esempio seguente crea un oggetto workbook, aggiunge un valore alla cella A1 sul primo foglio di lavoro e quindi salva il file ODS nelle specifiche ODF 1.1 e 1.2. Per impostazione predefinita, il file ODS viene salvato nella specifica ODF 1.2.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-OdsFileSaveOptions-SaveODSFileinODF11and12Specifications.cs" >}}
