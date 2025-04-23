---
title: Überprüfen, ob das VBA Projekt in einer Arbeitsmappe signiert ist
type: docs
weight: 70
url: /de/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Sie können über Microsoft Excel mithilfe des Menübefehls **Extras > Digitale Signaturen...** prüfen, ob Ihr VBA-Projekt signiert ist oder nicht. Ebenso können Sie dies programmgesteuert mithilfe der Aspose.Cells-[**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned)-Eigenschaft überprüfen.

{{% /alert %}}

## **Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe in C# signiert ist**

Der folgende Code lädt die Arbeitsmappe und überprüft, ob ihr VBA-Projekt mithilfe der [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned)-Eigenschaft signiert ist. Die Eigenschaft gibt **true** zurück, wenn das Projekt signiert ist, andernfalls **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
