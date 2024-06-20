---
title: Digitale Signatur eines VBA Codeprojekts mit Zertifikat
type: docs
weight: 110
url: /de/java/digitally-sign-a-vba-code-project-with-certificate/
---

{{% alert color="primary" %}}

Sie können mithilfe von Aspose.Cells Ihr VBA-Codeprojekt digital signieren mit dessen [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature))-Methode. Bitte befolgen Sie diese Schritte, um zu überprüfen, ob Ihre Excel-Datei mit einem Zertifikat digital signiert ist.

- Klicken Sie auf **Visual Basic** im **Entwicklertools**-Tab, um die **Visual Basic for Applications-IDE** zu öffnen
- Klicken Sie auf **Extras** > **Digitale Signaturen...** des **Visual Basic for Applications IDE**

und es wird das **Digitale Signaturformular** anzeigen, das anzeigt, ob das Dokument digital mit einem Zertifikat signiert ist oder nicht.

{{% /alert %}} 

## **Digitale Signatur eines VBA-Codeprojekts mit Zertifikat in C#**

Der folgende Beispielcode veranschaulicht, wie die Methode [**Workbook.VbaProject.Sign()**](https://reference.aspose.com/cells/java/com.aspose.cells/vbaproject#sign(com.aspose.cells.DigitalSignature)) verwendet wird. Hier sind die Eingabe- und Ausgabedateien des Beispielcodes. Sie können beliebige Excel-Datei und beliebiges Zertifikat verwenden, um diesen Code zu testen.

- [Quell-Excel-Datei](5115028.xlsm), die im Beispielcode verwendet wird.
- [Beispiel-PFX-Datei](5115039.pfx) zur Erstellung einer digitalen Signatur. Bitte installieren Sie diese auf Ihrem Computer, um diesen Code auszuführen. Das Kennwort lautet 1234.
- [Ausgabe-Excel-Datei](5115029.xlsm), die vom Beispielcode generiert wurde.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "ManagingVBAModules-DigitallySignVbaProjectWithCertificate.java" >}}
