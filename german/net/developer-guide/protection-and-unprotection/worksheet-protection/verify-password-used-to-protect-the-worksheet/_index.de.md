---
title: Das Verifizieren des zum Schutz des Arbeitsblatts verwendeten Passworts
type: docs
weight: 370
url: /de/net/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Die Aspose.Cells-APIs haben die Klasse [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) durch die Einführung einiger nützlicher Eigenschaften und Methoden verbessert. Eine solche Methode ist die [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword), die die Angabe eines Passworts als Instanz von *string* ermöglicht und überprüft, ob dasselbe Passwort zum Schutz des [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) verwendet wurde.

{{% /alert %}}

Die Methode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) gibt **true** zurück, wenn das angegebene Passwort mit dem zum Schutz des entsprechenden Arbeitsblatts verwendeten Passwort übereinstimmt, und **false**, wenn das angegebene Passwort nicht übereinstimmt. Der folgende Code verwendet die Methode [**Protection.VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/methods/verifypassword) in Verbindung mit der Eigenschaft [**Protection.IsProtectedWithPassword**](https://reference.aspose.com/cells/net/aspose.cells/protection/properties/isprotectedwithpassword), um den Passwortschutz zu erkennen und das Passwort zu überprüfen.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-VerifyPasswordUsedToProtectWorksheets-VerifyPasswordUsedToProtectWorksheets.cs" >}}
{{< app/cells/assistant language="csharp" >}}
