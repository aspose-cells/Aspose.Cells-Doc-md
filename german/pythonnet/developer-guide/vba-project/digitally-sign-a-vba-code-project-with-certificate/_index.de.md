---
title: Digitale Signatur eines VBA Codeprojekts mit Zertifikat
type: docs
weight: 110
url: /de/python-net/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Sie können Ihr VBA-Codeprojekt digital signieren mit Aspose.Cells for Python via .NET mittels seiner [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature)-Methode. Folgen Sie diesen Schritten, um zu überprüfen, ob Ihre Excel-Datei digital mit einem Zertifikat signiert ist.

- Klicken Sie auf **Visual Basic** im **Entwicklertools**-Tab, um die **Visual Basic for Applications-IDE** zu öffnen
- Klicken Sie auf **Extras** > **Digitale Signaturen...** im **Visual Basic for Applications-IDE**

und es wird das **Digitale Signaturformular** anzeigen, das anzeigt, ob das Dokument digital mit einem Zertifikat signiert ist oder nicht.

{{% /alert %}} 

## **Digitale Signatur eines VBA-Codeprojekts mit Zertifikat in Python**

Der folgende Beispielcode veranschaulicht, wie die Methode [**Workbook.vba_project.sign()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbaproject/sign/#aspose.cells.digitalsignatures.DigitalSignature) verwendet wird. Hier sind die Eingabe- und Ausgabedateien des Beispielcodes. Sie können jede Excel-Datei und jedes Zertifikat verwenden, um diesen Code zu testen.

- [Quell-Excel-Datei](5115028.xlsm), die im Beispielcode verwendet wird.
- [Beispiel-PFX-Datei](5115039.pfx) zur Erstellung einer digitalen Signatur. Bitte installieren Sie diese auf Ihrem Computer, um diesen Code auszuführen. Das Kennwort lautet 1234.
- [Ausgabe-Excel-Datei](5115029.xlsm), die vom Beispielcode generiert wurde.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-DigitallySignVbaProjectWithCertificate-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
