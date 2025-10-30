---
title: Verificare se la Firma Digitale del Codice VBA è Valida con Golang tramite C++
linktitle: Verifica se la Firma Digitale del Codice VBA è Valida
type: docs
weight: 120
url: /it/go-cpp/check-if-digital-signature-of-vba-code-is-valid/
description: Impara come verificare la validità di una firma digitale nel codice VBA usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di verificare se la firma digitale del codice VBA è valida usando la proprietà [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/go-cpp/vbaproject/isvalidsigned/). Restituirà **true** se la firma è valida; altrimenti, restituirà **false**. La firma digitale del codice VBA diventa invalida quando si modifica il codice VBA.

{{% /alert %}}

## **Verifica se la Firma Digitale del Codice VBA è Valida in C++**

Il seguente esempio di codice dimostra l’uso di questa proprietà utilizzando il [file Excel di esempio](5115030.xlsm) che puoi scaricare dal link fornito. Lo stesso file Excel ha una firma valida, ma quando modifichiamo il suo codice VBA e salviamo il workbook, poi lo rifacciamo controllare, troviamo che la firma è diventata invalida.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CheckIfDigitalSignatureOfVbaCodeIsValid.go" >}}
