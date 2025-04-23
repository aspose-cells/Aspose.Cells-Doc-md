---
title: Kontrollera om VBA projektet i en arbetsbok är signerat
type: docs
weight: 70
url: /sv/python-net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Du kan kontrollera om ditt VBA-projekt är undertecknat eller inte med Microsoft Excel via **Verktyg > Digitala signaturer...**-menyn. På samma sätt kan du kontrollera detta programmatiskt med Aspose.Cells för Python via .NET [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed)-egenskap.

{{% /alert %}}

## **Kontrollera om VBA-projekt i en arbetsbok är signerat i Python**

Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med hjälp av [**Workbook.vba_project.is_signed**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/is_signed) egenskapen. Egenskapen returnerar **true** om projektet är signerat, annars returnerar den **false**.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-CheckVbaProjectSigned-1.py" >}}

