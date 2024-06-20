---
title: Verifica se il progetto VBA in un workbook è firmato
type: docs
weight: 70
url: /it/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Puoi verificare se il tuo progetto VBA è firmato o meno utilizzando Microsoft Excel tramite il comando del menu **Strumenti > Firme digitali...**. Analogamente, puoi verificarlo in modo programmatico utilizzando la proprietà [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) di Aspose.Cells.

{{% /alert %}}

## **Verifica se il progetto VBA in un Workbook è Firmato in C#**

Il codice seguente carica il workbook e verifica se il suo progetto VBA è firmato utilizzando la proprietà [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned). La proprietà restituirà **true** se il progetto è firmato, altrimenti restituirà **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
