---
title: Verifica se la Firma Digitale del Codice VBA è Valida
type: docs
weight: 120
url: /it/net/check-if-digital-signature-of-vba-code-is-valid/
---

{{% alert color="primary" %}}

Aspose.Cells ti permette di verificare se la firma digitale del codice VBA è valida utilizzando la proprietà [**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned). Restituirà **true** se la firma è valida, altrimenti restituirà **false**. La firma digitale del codice VBA diventa non valida quando si cambia il codice VBA.

{{% /alert %}}

## **Verifica se la Firma Digitale del Codice VBA è Valida in C#**

Il codice seguente dimostra l'uso di questa proprietà utilizzando il [file Excel di esempio](5115030.xlsm) che puoi scaricare dal link fornito. Lo stesso file Excel ha una firma valida ma quando modifichiamo il suo codice VBA e salviamo il workbook e poi ricontrolliamo, troviamo che la sua firma è diventata non valida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
{{< app/cells/assistant language="csharp" >}}
