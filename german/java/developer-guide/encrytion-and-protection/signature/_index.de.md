---
title: Digitale Signaturen zuweisen und validieren
linktitle: Unterschrift
type: docs
weight: 100
url: /de/java/assign-and-validate-digital-signatures/
description: Excel-Datei digitale Signatur, Verifizierung. Um die Authentizität des Inhalts einer Arbeitsmappe in einer Excel-Datei zu schützen, können Sie eine digitale Signatur mit C#-Codes und Aspose.Cells für .Net hinzufügen.
---
{{% alert color="primary" %}}

 Eine digitale Signatur stellt sicher, dass eine Arbeitsmappendatei gültig ist und niemand sie geändert hat. Sie können eine persönliche digitale Signatur erstellen, indem Sie die verwenden**SELBSTBEWUSST** Tool, das mit Microsoft Office Suite geliefert wird, oder ein anderes Tool. Sie können sogar eine digitale Signatur erwerben. Nachdem Sie eine digitale Signatur erstellt oder erworben haben, müssen Sie sie an Ihre Arbeitsmappe anhängen. Das Anhängen einer digitalen Signatur ähnelt dem Verschließen eines Umschlags. Wenn ein Umschlag versiegelt ankommt, haben Sie ein gewisses Maß an Sicherheit, dass niemand seinen Inhalt manipuliert hat.

 Aspose.Cells for Java API bieten die[**com.aspose.cells.DigitalSignatureCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignatureCollection) & [**com.aspose.cells.DigitalSignature**](https://reference.aspose.com/cells/java/com.aspose.cells/DigitalSignature) Klassen, um die Tabellenkalkulationen zu signieren und zu validieren.

{{% /alert %}}

## **Signieren der Spreadsheets**

Der Signiervorgang erfordert ein Zertifikat, wie oben beschrieben. Zusammen mit dem Zertifikat sollte man auch sein Passwort haben, um die Tabellen erfolgreich mit der Aspose.Cells API zu signieren.

Das folgende Code-Snippet veranschaulicht die Verwendung von Aspose.Cells for Java API zum Signieren einer Tabelle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SigningSpreadsheets-SigningSpreadsheets.java" >}}

{{% alert color="primary" %}}

 Falls das angegebene Passwort nicht mit dem Passwort des Zertifikats übereinstimmt, dann eine Ausnahme vom Typ*javax.crypto.BadPaddingException* wird geworfen.

{{% /alert %}}

## **Validierung der Tabellenkalkulationen**

Das folgende Code-Snippet veranschaulicht die Verwendung von Aspose.Cells for Java API zur Validierung der Tabelle.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ValidatingSpreadsheets-ValidatingSpreadsheets.java" >}}
