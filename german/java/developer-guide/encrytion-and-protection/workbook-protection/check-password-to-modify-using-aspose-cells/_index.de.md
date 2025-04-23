---
title: Passwort zum Ändern mit Aspose.Cells überprüfen
type: docs
weight: 190
url: /de/java/check-password-to-modify-using-aspose-cells/
---

{{% alert color="primary" %}}

Sie können beim Erstellen Ihrer Arbeitsmappen in Microsoft Excel ein **Passwort zum Öffnen** und ein **Passwort zum Ändern** zuweisen. Bitte sehen Sie sich diesen Screenshot an, der die Benutzeroberfläche zeigt, die Microsoft Excel bietet, um diese Passwörter anzugeben.

![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)

Manchmal müssen Sie programmgesteuert überprüfen, ob das angegebene Passwort mit dem **Passwort zum Ändern** übereinstimmt. Aspose.Cells bietet die Methode [**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword-java.lang.String-), mit der Sie überprüfen können, ob das angegebene Änderungspasswort korrekt ist oder nicht.

{{% /alert %}}

## Java-Code zum Überprüfen des Änderungspassworts mit Aspose.Cells

Die folgenden Beispielscodes laden die [Quell-Excel](5473057.xlsx)-Datei. Sie hat ein Öffnungspasswort *1234* und ein Änderungspasswort *5678*. Der Code überprüft zunächst, ob *567* das korrekte Änderungspasswort ist, und gibt **false** zurück. Dann wird überprüft, ob *5678* das Änderungspasswort ist, und es wird **true** zurückgegeben.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Konsolenausgabe generiert durch den Java-Code

Hier ist die Konsolenausgabe des obigen Beispielcodes nach dem Laden der [Quell-Excel](5473057.xlsx)-Datei.

{{< highlight java >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
