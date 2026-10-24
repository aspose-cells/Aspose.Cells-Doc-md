---
title: Digitale Signaturen zuweisen und validieren
linktitle: Signatur
type: docs
weight: 100
url: /de/java/assign-and-validate-digital-signatures/
description: Excel Dateisignatur, Überprüfung. Um die Echtheit des Inhalts einer Excel Arbeitsmappe zu schützen, können Sie eine digitale Signatur mit Java Code hinzufügen, mit Aspose.Cells for Java.
---

{{% alert color="primary" %}}

Eine digitale Signatur gewährleistet, dass eine Arbeitsbuchdatei gültig ist und niemand sie verändert hat. Sie können eine persönliche digitale Signatur mithilfe des mit der Microsoft Office-Suite gelieferten **SELFCERT**-Tools oder eines anderen Tools erstellen. Sie können auch eine digitale Signatur erwerben. Nachdem Sie eine digitale Signatur erstellt oder erworben haben, müssen Sie sie an Ihr Arbeitsbuch anhängen. Das Anfügen einer digitalen Signatur ähnelt dem Versiegeln eines Umschlags. Wenn ein versiegelter Umschlag ankommt, haben Sie eine gewisse Sicherheitsgewährleistung, dass niemand den Inhalt manipuliert hat.

Aspose.Cells for Java API bietet die Klassen [**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) und [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) zum Signieren von Arbeitsmappen sowie zur Validierung von ihnen.

{{% /alert %}}

## **Signieren der Arbeitsmappen**

Der Signiervorgang erfordert wie oben diskutiert ein Zertifikat. Neben dem Zertifikat sollte man auch sein Passwort haben, um die Arbeitsmappen mit Hilfe der Aspose.Cells-API erfolgreich zu signieren.

Das folgende Code-Snippet zeigt die Verwendung der Aspose.Cells for Java-API zum Signieren einer Arbeitsmappe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

Wenn das angegebene Passwort nicht mit dem Passwort des Zertifikats übereinstimmt, wird eine Ausnahme des Typs *javax.crypto.BadPaddingException* ausgelöst.

{{% /alert %}}

## **Validieren der Arbeitsmappen**

Das folgende Code-Snippet zeigt die Verwendung der Aspose.Cells for Java-API zur Validierung der Arbeitsmappe.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
{{< app/cells/assistant language="java" >}}
