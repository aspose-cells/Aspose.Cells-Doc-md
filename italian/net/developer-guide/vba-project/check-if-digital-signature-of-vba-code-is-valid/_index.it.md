---
title: Controlla se la firma digitale del codice VBA è valida
type: docs
weight: 120
url: /it/net/check-if-digital-signature-of-vba-code-is-valid/
---
{{% alert color="primary" %}}

 Aspose.Cells permette di verificare se la firma digitale del codice VBA è valida utilizzando il[**Workbook.VbaProject.IsValidSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/isvalidsigned) proprietà. Tornerà**VERO** se la firma è valida altrimenti tornerà**falso**. La firma digitale del codice VBA diventa non valida quando si modifica il codice VBA.

{{% /alert %}}

## **Verifica se la firma digitale del codice VBA è valida in C#**

 Il codice seguente illustra l'utilizzo di questa proprietà utilizzando il[file excel di esempio](5115030.xlsm)che puoi scaricare dal link fornito. Lo stesso file excel ha una firma valida ma quando modifichiamo il suo codice VBA e salviamo la cartella di lavoro e quindi ricontrolliamo, scopriamo che la sua firma non è più valida.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaSignatureIsValid-CheckVbaSignatureIsValid.cs" >}}
