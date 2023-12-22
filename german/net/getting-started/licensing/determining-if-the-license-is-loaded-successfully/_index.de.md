---
title: Feststellen, ob die Lizenz erfolgreich geladen wurde
type: docs
weight: 260
url: /de/net/determining-if-the-license-is-loaded-successfully/
description: Erfahren Sie, wie Sie über die APIs Aspose.Cells für NET erkennen, ob die Lizenz erfolgreich geladen wurde.
keywords: How to Detect if the License is loaded successfully in C#, Determine if the License is loaded successfully using C#, Check if the License is loaded successfully via C#, check the status of license.
---
{{% alert color="primary" %}}

 Aspose.Cells bietet[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) Eigenschaft, mit der Sie feststellen können, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie auf diese Eigenschaft zugreifen, bevor Sie die Lizenz festlegen, wird sie zurückgegeben**FALSCH** und wenn Sie diese Eigenschaft nach dem Festlegen der Lizenz aufrufen, wird sie zurückgegeben**WAHR** Zeigt an, dass die Lizenz erfolgreich geladen wurde.

{{% /alert %}}

##  C#-Code, um festzustellen, ob die Lizenz erfolgreich geladen wurde

 Der folgende Code greift auf zu[**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed)Eigenschaft vor dem Festlegen einer Lizenz und gibt *false** zurück. Dann lädt es die Lizenz und greift erneut auf die Eigenschaft zu, die nun *true** zurückgibt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

##  **Konsolenausgabe**

Hier ist die Konsolenausgabe (Debug) des obigen Beispielcodes

{{< highlight "java" >}}

False

True

{{< /highlight >}}
