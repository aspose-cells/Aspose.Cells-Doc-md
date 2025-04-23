---
title: Erkennen, ob Arbeitsblatt passwortgeschützt ist
type: docs
weight: 360
url: /de/net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Es ist möglich, die Arbeitsmappen und Arbeitsblätter getrennt zu schützen. Beispielsweise kann eine Tabelle ein oder mehrere Arbeitsblätter enthalten, die passwortgeschützt sind, während die Tabelle selbst geschützt sein kann oder auch nicht. Die Aspose.Cells-APIs bieten die Möglichkeit zu erkennen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. In diesem Artikel wird die Verwendung der Aspose.Cells for .NET-API zur Erreichung desselben demonstriert.

{{% /alert %}}

Aspose.Cells for .NET 8.7.0 hat die [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword)-Eigenschaft freigegeben, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht. Die boolesche Eigenschaft [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) gibt **true** zurück, wenn [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) passwortgeschützt ist, und **false**, wenn nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
{{< app/cells/assistant language="csharp" >}}
