---
title: Erkennen, ob Arbeitsblatt passwortgeschützt ist
type: docs
weight: 360
url: /de/python-net/detect-if-worksheet-is-password-protected/
---

{{% alert color="primary" %}}

Es ist möglich, Arbeitsmappen und Arbeitsblätter separat zu schützen. Ein Spreadsheet kann ein oder mehrere Arbeitsblätter enthalten, die passwortgeschützt sind, während die gesamte Tabelle möglicherweise oder möglicherweise nicht geschützt ist. Aspose.Cells für Python via .NET APIs bieten die Möglichkeit, zu erkennen, ob ein bestimmtes Arbeitsblatt passwortgeschützt ist oder nicht. Dieser Artikel demonstriert die Nutzung der Aspose.Cells für Python via .NET API, um dasselbe zu erreichen.

{{% /alert %}}

Aspose.Cells für Python via .NET hat die Eigenschaft [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) bereitgestellt, um zu erkennen, ob ein Arbeitsblatt passwortgeschützt ist oder nicht. Der boolesche Typ [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password) gibt **wahr** zurück, wenn [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) passwortgeschützt ist, und **falsch**, wenn nicht.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-CheckIfPasswordProtected.py" >}}

