---
title: Verifica se il progetto VBA in un workbook è firmato
type: docs
weight: 70
url: /it/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Puoi verificare se il tuo progetto VBA è firmato o meno utilizzando Microsoft Excel tramite il comando del menu **Tools > Digital Signatures...**. In modo analogo, puoi verificarlo programmando usando la proprietà [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) di Aspose.Cells per Python via .NET.

{{% /alert %}}

## **Verifica se il progetto VBA di un Workbook è firmato in Python**

Il codice seguente carica il workbook e verifica se il suo progetto VBA è firmato utilizzando la proprietà [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed). La proprietà restituirà **true** se il progetto è firmato, altrimenti restituirà **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

