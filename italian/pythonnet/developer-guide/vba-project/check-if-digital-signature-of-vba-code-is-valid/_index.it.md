---
title: Verifica se la Firma Digitale del Codice VBA è Valida
type: docs
weight: 120
url: /it/python-net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET permette di verificare se la firma digitale del codice VBA è valida usando la proprietà [**Workbook.vba_project.is_valid_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_valid_signed). Restituirà **true** se la firma è valida, altrimenti restituirà **false**. La firma digitale del codice VBA diventa invalida quando si modifica il codice VBA.

{{% /alert %}}

## **Verifica se la firma digitale del codice VBA è valida in Python**

Il codice seguente dimostra l'uso di questa proprietà utilizzando il [file Excel di esempio](5115030.xlsm) che puoi scaricare dal link fornito. Lo stesso file Excel ha una firma valida ma quando modifichiamo il suo codice VBA e salviamo il workbook e poi ricontrolliamo, troviamo che la sua firma è diventata non valida.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaSignatureIsValid.py" >}}

