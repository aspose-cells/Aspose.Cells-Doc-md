---
title: Kontrollera om VBA projektet i en arbetsbok är signerat
type: docs
weight: 70
url: /sv/net/check-if-vba-project-in-a-workbook-is-signed/
---

{{% alert color="primary" %}}

Du kan kontrollera om ditt VBA-projekt är signerat eller inte med Microsoft Excel via kommandot **Verktyg > Digitala signaturer...**. På liknande sätt kan du kontrollera det programmatiskt med hjälp av egenskapen [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) i Aspose.Cells.

{{% /alert %}}

## **Kontrollera om VBA-projektet i en Arbetsbok är signerat i C#**

Följande kod laddar arbetsboken och kontrollerar om dess VBA-projekt är signerat med hjälp av [**Workbook.VbaProject.IsSigned**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbaproject/properties/issigned) egenskapen. Egenskapen returnerar **true** om projektet är signerat, annars returnerar den **false**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-CheckVbaProjectSigned-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
