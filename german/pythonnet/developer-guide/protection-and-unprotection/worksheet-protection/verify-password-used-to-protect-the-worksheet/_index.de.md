---
title: Das Verifizieren des zum Schutz des Arbeitsblatts verwendeten Passworts
type: docs
weight: 370
url: /de/python-net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Die APIs von Aspose.Cells für Python via .NET haben die [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection)-Klasse durch die Einführung nützlicher Eigenschaften & Methoden verbessert. Eine davon ist die [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password), mit der man ein Passwort als Instanz vom Typ *string* angeben und überprüfen kann, ob dasselbe Passwort zum Schutz des [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) verwendet wurde.

{{% /alert %}}

Die Methode [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) gibt **true** zurück, wenn das angegebene Passwort mit dem zum Schutz des entsprechenden Arbeitsblatts verwendeten Passwort übereinstimmt, und **false**, wenn das angegebene Passwort nicht übereinstimmt. Der folgende Code verwendet die Methode [**Protection.verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/verify_password) in Verbindung mit der Eigenschaft [**Protection.is_protected_with_password**](https://reference.aspose.com/cells/python-net/aspose.cells/protection/is_protected_with_password), um den Passwortschutz zu erkennen und das Passwort zu überprüfen.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPasswordUsedToProtectWorksheets.py" >}}

