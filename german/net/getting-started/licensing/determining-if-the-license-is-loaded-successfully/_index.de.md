---
title: Bestimmen, ob die Lizenz erfolgreich geladen wurde
type: docs
weight: 260
url: /de/net/determining-if-the-license-is-loaded-successfully/
---
{{% alert color="primary" %}}

 Aspose.Cells bietet[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) -Eigenschaft, mit der Sie feststellen können, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie auf diese Eigenschaft zugreifen, bevor Sie die Lizenz festlegen, wird sie zurückgegeben**FALSCH**und wenn Sie diese Eigenschaft nach dem Festlegen der Lizenz aufrufen, wird sie zurückgegeben**Stimmt** zeigt an, dass die Lizenz erfolgreich geladen wurde.

{{% /alert %}}

## C#-Code, um festzustellen, ob die Lizenz erfolgreich geladen wurde

 Der folgende Code greift auf die[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) -Eigenschaft vor dem Festlegen einer Lizenz und kehrt zurück**FALSCH** . Dann lädt es die Lizenz und greift erneut auf die Eigenschaft zu, die jetzt zurückkehrt**Stimmt**.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe (Debug) des obigen Beispielcodes

{{< highlight "java" >}}

False

True

{{< /highlight >}}
