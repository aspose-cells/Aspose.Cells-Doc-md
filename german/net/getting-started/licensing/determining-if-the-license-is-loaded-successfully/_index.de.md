---
title: Feststellen, ob die Lizenz erfolgreich geladen wird
type: docs
weight: 260
url: /de/net/determining-if-the-license-is-loaded-successfully/
description: Erfahren Sie, wie Sie über die Aspose.Cells for NET APIs feststellen können, ob die Lizenz erfolgreich geladen wurde.
keywords: Wie Sie in C# feststellen, ob die Lizenz erfolgreich geladen wurde, Bestimmen, ob die Lizenz erfolgreich geladen wurde, indem sie C# verwenden, Überprüfen Sie, ob die Lizenz erfolgreich über C# geladen wurde, Überprüfen Sie den Status der Lizenz.
---

{{% alert color="primary" %}}

Aspose.Cells bietet die Eigenschaft [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed), die Sie verwenden können, um festzustellen, ob die Lizenz erfolgreich geladen wurde oder nicht. Wenn Sie auf diese Eigenschaft zugreifen, bevor Sie die Lizenz festlegen, wird **false** zurückgegeben, und wenn Sie diese Eigenschaft nach dem Festlegen der Lizenz aufrufen, wird **true** zurückgegeben, was darauf hindeutet, dass die Lizenz erfolgreich geladen wurde.

{{% /alert %}}

## C#-Code zur Feststellung, ob die Lizenz erfolgreich geladen wurde

Der folgende Code greift vor dem Setzen einer Lizenz auf die Eigenschaft [**Workbook.IsLicensed**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/islicensed) zu und gibt **false** zurück. Dann wird die Lizenz geladen und die Eigenschaft wird erneut aufgerufen, was nun **true** zurückgibt.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-DeterminingLicenseLoading-DeterminingLicenseLoading.cs" >}}

## **Konsolenausgabe**

Hier ist die Konsolenausgabe des obigen Beispiels

{{< highlight java >}}

False

True

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
