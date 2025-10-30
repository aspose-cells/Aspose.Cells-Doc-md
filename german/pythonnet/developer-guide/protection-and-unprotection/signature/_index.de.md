---
title: Digitale Signaturen zuweisen und validieren
linktitle: Signatur
type: docs
weight: 140
url: /de/python-net/assign-and-validate-digital-signatures/
description: Digitale Signatur, Verifizierung einer Excel Datei. Um die Echtheit des Inhalts einer Excel Arbeitsmappe zu schützen, können Sie mithilfe von C# Code und Aspose.Cells für Python via .NET eine digitale Signatur hinzufügen.
keywords: Digitale Signatur für Excel Datei, Digitale Signatur für Excel hinzufügen, Wie man eine digitale Signatur validiert.
---

{{% alert color="primary" %}}

Eine digitale Signatur gewährleistet, dass eine Arbeitsmappe gültig ist und niemand sie verändert hat. Sie können eine persönliche digitale Signatur mithilfe des **Microsoft Selfcert.exe** oder eines anderen Tools erstellen oder eine digitale Signatur erwerben. Nachdem Sie eine digitale Signatur erstellt haben, müssen Sie sie Ihrer Arbeitsmappe hinzufügen. Das Anhängen einer digitalen Signatur ähnelt dem Versiegeln eines Umschlags. Wenn ein versiegelter Umschlag ankommt, haben Sie eine gewisse Sicherheit, dass niemand seinen Inhalt manipuliert hat.

{{% /alert %}}

## **Einführung**

Verwenden Sie den Digital Signature-Dialog, um eine digitale Signatur anzuhängen. Der Digital Signature-Dialog listet gültige Zertifikate auf. Sie können den Digital Signature-Dialog verwenden, um Zertifikate anzuzeigen und das gewünschte Zertifikat auszuwählen. Wenn eine Arbeitsmappe eine digitale Signatur hat, erscheint der Name der Signatur im **Zertifikatname**-Feld. Wenn Sie auf die Schaltfläche **Entfernen** im Digital Signature-Dialog klicken, entfernt Microsoft Excel auch die digitale Signatur.

## **Wie man eine digitale Signatur für Excel hinzufügt**

Aspose.Cells für Python via .NET bietet den [**Aspose.Cells.DigitalSignatures**](https://reference.aspose.com/cells/python-net/aspose.cells.digitalsignatures/digitalsignature)-Namespace, um die Aufgabe (zuzuordnen und digitale Signaturen zu validieren) auszuführen. Dieser Namespace verfügt über einige nützliche Funktionen zum Hinzufügen und Validieren digitaler Signaturen.

Siehe den folgenden Beispielcode, der beschreibt, wie Sie die Aufgabe mithilfe der Aspose.Cells für Python via .NET API ausführen können.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AssignAndValidateDigitalSignatures.py" >}}



## **Erweiterte Themen**
- [Fügen Sie eine digitale Signatur zu einer bereits signierten Excel-Datei hinzu](/cells/de/python-net/add-digital-signature-to-an-already-signed-excel-file/)
- [Fügen Sie der Arbeitsmappe eine Signaturzeile hinzu](/cells/de/python-net/add-signature-line/)
- [Unterstützung für XAdES-Signatur](/cells/de/python-net/support-for-xades-signature/)

{{< app/cells/assistant language="python-net" >}}
