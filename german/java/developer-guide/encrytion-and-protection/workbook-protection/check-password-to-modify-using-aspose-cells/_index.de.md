---
title: Überprüfen Sie das zu ändernde Passwort mit Aspose.Cells
type: docs
weight: 190
url: /de/java/check-password-to-modify-using-aspose-cells/
---
{{% alert color="primary" %}}

 Sie können a zuweisen**Passwort zum öffnen** und ein**Zu änderndes Passwort** beim Erstellen Ihrer Arbeitsmappen in Microsoft Excel. Bitte sehen Sie sich diesen Screenshot an, der die Schnittstelle Microsoft zeigt, die Excel bereitstellt, um diese Passwörter anzugeben.

![todo: Bild_alt_Text](check-password-to-modify-using-aspose-cells_1.png)

 Manchmal müssen Sie überprüfen, ob das angegebene Passwort mit dem übereinstimmt**Zu änderndes Passwort** programmatisch. Aspose.Cells bietet[**workbook.getSettings().getWriteProtection().validatePassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/writeprotection#validatePassword(java.lang.String))-Methode, mit der Sie überprüfen können, ob das angegebene zu ändernde Passwort korrekt ist oder nicht.

{{% /alert %}}

## Java Code zum Überprüfen des Passworts zum Ändern mit Aspose.Cells

 Die folgenden Beispielcodes laden die[Quelle Excel](5473057.xlsx) Datei. Es hat ein Passwort zum Öffnen als*1234* und Passwort zu ändern als*5678* . Der Code prüft zuerst, ob*567* ist das richtige Passwort zum Ändern und es kehrt zurück**FALSCH** und dann prüft es ob*5678* ist ein Passwort, das geändert werden soll, und es kehrt zurück**wahr**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CheckPassword-CheckPassword.java" >}}

## Konsolenausgabe, die vom Code Java generiert wird

 Hier ist die Konsolenausgabe des obigen Beispielcodes nach dem Laden der[Quelle Excel](5473057.xlsx) Datei.

{{< highlight "java" >}}

Is 567 correct Password to modify: false

Is 5678 correct Password to modify: true

{{< /highlight >}}
