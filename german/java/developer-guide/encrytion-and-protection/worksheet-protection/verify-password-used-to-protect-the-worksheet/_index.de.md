---
title: Das Verifizieren des zum Schutz des Arbeitsblatts verwendeten Passworts
type: docs
weight: 290
url: /de/java/verify-password-used-to-protect-the-worksheet/
---

{{% alert color="primary" %}}

Die Aspose.Cells-APIs haben die Klasse [**Protection**](https://reference.aspose.com/cells/java/com.aspose.cells/Protection) durch die Einführung einiger nützlicher Eigenschaften und Methoden verbessert. Eine solche Methode ist die [**verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)), mit der ein Passwort als Instanz von String angegeben und überprüft wird, ob dasselbe Passwort verwendet wurde, um das Arbeitsblatt zu schützen.

{{% /alert %}}

## **Überprüfen Sie das verwendete Kennwort zum Schutz des Arbeitsblatts**

Die Methode [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) gibt **true** zurück, wenn das angegebene Passwort mit dem zum Schutz des angegebenen Arbeitsblatts verwendeten Passwort übereinstimmt, andernfalls **false**. Der folgende Code verwendet die Methode [**Protection.verifyPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#verifyPassword(java.lang.String)) in Verbindung mit der Eigenschaft [**Protection.isProtectedWithPassword**](https://reference.aspose.com/cells/java/com.aspose.cells/protection#IsProtectedWithPassword), um den Passwortschutz zu erkennen und das Passwort zu überprüfen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-VerifyPasswordtoProtectWorksheet-VerifyPasswordtoProtectWorksheet.java" >}}
