---
title: Digitale Signaturen zuweisen und validieren
linktitle: Signatur
type: docs
weight: 140
url: /de/net/assign-and-validate-digital-signatures/
description: Digitale Signatur von Excel Dateien, Verifizierung. Um die Authentizität des Inhalts einer Excel Datei Arbeitsmappe zu schützen, können Sie mit Aspose.Cells für .Net digitale Signaturen mittels C# Codes hinzufügen.
keywords: Digitale Signatur für Excel Datei, Digitale Signatur für Excel hinzufügen, Wie man eine digitale Signatur validiert.
---

{{% alert color="primary" %}}

Eine digitale Signatur gewährleistet, dass eine Arbeitsmappe gültig ist und niemand sie verändert hat. Sie können eine persönliche digitale Signatur mithilfe des **Microsoft Selfcert.exe** oder eines anderen Tools erstellen oder eine digitale Signatur erwerben. Nachdem Sie eine digitale Signatur erstellt haben, müssen Sie sie Ihrer Arbeitsmappe hinzufügen. Das Anhängen einer digitalen Signatur ähnelt dem Versiegeln eines Umschlags. Wenn ein versiegelter Umschlag ankommt, haben Sie eine gewisse Sicherheit, dass niemand seinen Inhalt manipuliert hat.

{{% /alert %}}

## **Einführung**

Verwenden Sie den Digital Signature-Dialog, um eine digitale Signatur anzuhängen. Der Digital Signature-Dialog listet gültige Zertifikate auf. Sie können den Digital Signature-Dialog verwenden, um Zertifikate anzuzeigen und das gewünschte Zertifikat auszuwählen. Wenn eine Arbeitsmappe eine digitale Signatur hat, erscheint der Name der Signatur im **Zertifikatname**-Feld. Wenn Sie auf die Schaltfläche **Entfernen** im Digital Signature-Dialog klicken, entfernt Microsoft Excel auch die digitale Signatur.

## **Wie man eine digitale Signatur für Excel hinzufügt**

Aspose.Cells bietet den Namespace [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/net/aspose.cells.digitalsignatures/digitalsignature) zur Durchführung der Aufgabe (Zuweisen und Validieren digitaler Signaturen). Der Namespace verfügt über einige nützliche Funktionen zum Hinzufügen und Validieren digitaler Signaturen.

Bitte sehen Sie sich den folgenden Beispielcode an, der beschreibt, wie Sie die Aufgabe mit der Aspose.Cells for .NET-API durchführen können.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-AssignAndValidateDigitalSignatures-AssignAndValidateDigitalSignatures.cs" >}}



## **Erweiterte Themen**
- [Fügen Sie eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu](/cells/de/net/add-digital-signature-to-an-already-signed-excel-file/)
- [Fügen Sie der Arbeitsmappe eine Signaturzeile hinzu](/cells/de/net/add-signature-line/)
- [Unterstützung für XAdES-Signatur](/cells/de/net/support-for-xades-signature/)
