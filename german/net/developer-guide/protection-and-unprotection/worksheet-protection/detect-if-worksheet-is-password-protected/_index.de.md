---
title: Erkennen, ob das Arbeitsblatt passwortgeschützt ist
type: docs
weight: 360
url: /de/net/detect-if-worksheet-is-password-protected/
---
{{% alert color="primary" %}}

Es ist möglich, die Arbeitsmappen und Arbeitsblätter separat zu schützen. Beispielsweise kann eine Tabellenkalkulation ein oder mehrere passwortgeschützte Arbeitsblätter enthalten, die Tabellenkalkulation selbst kann jedoch geschützt sein oder nicht. Aspose.Cells APIs bieten die Möglichkeit zu erkennen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. Dieser Artikel demonstriert die Verwendung von Aspose.Cells for .NET API, um dasselbe zu erreichen.

{{% /alert %}}

 Aspose.Cells for .NET 8.7.0 hat die ausgesetzt[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) -Eigenschaft, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht. Boolescher Typ[**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword) Eigenschaft Renditen**Stimmt** wenn[**Arbeitsblatt**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) ist passwortgeschützt und**FALSCH** wenn nicht.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-CheckIfPasswordProtected-CheckIfPasswordProtected.cs" >}}
