---
title: VBA Codes einer Excel Makro aktivierten Arbeitsmappe verwalten.
linktitle: Makro Projekt
type: docs
weight: 200
url: /de/python-net/manage-vba-project/
description: Hinzufügen eines VBA Moduls und Ändern von VBA oder Makros mit der Aspose.Cells für Python via .NET Bibliothek.
---

## **Fügen Sie in Python ein VBA-Modul hinzu**
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, mit Aspose.Cells für Python via .NET ein neues VBA-Modul und Makrocode hinzuzufügen. Verwenden Sie die Methode [**Workbook.vba_project.modules.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.vba/vbamodulecollection/add/), um das neue VBA-Modul im Arbeitsbuch hinzuzufügen

{{% /alert %}}

Der folgende Beispielcode erstellt ein neues Arbeitsblatt, fügt ein neues VBA-Modul und einen Makrocode hinzu und speichert die Ausgabe im XLSM-Format. Sobald Sie die Ausgabe-XLSM-Datei in Microsoft Excel öffnen und auf die Menübefehle **Entwickler > Visual Basic** klicken, sehen Sie ein Modul namens "TestModule", und darin sehen Sie den folgenden Makrocode.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Hier ist der Beispielcode zum Erzeugen der Ausgabe-XLSM-Datei mit VBA-Modul und Makrocode.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-AddVBAModuleOrCode.py" >}}

## **VBA oder Makro in Python ändern**

{{% alert color="primary" %}} 

Sie können VBA- oder Makro-Code mit Aspose.Cells für Python via .NET modifizieren. Aspose.Cells für Python via .NET hat den folgenden Namensraum und Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu modifizieren.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makro-Code innerhalb der Quellexcel-Datei mit Aspose.Cells für Python via .NET ändern.

{{% /alert %}} 

Der folgende Beispielcode lädt die Quell-Excel-Datei, die den folgenden VBA- oder Makrocode enthält

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Nach der Ausführung des Beispielcodes von Aspose.Cells für Python via .NET wird der VBA- oder Makro-Code wie folgt modifiziert sein

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Sie können die [Quell-Excel-Datei](5112508.xlsm) und die [Ausgabe-Excel-Datei](5112511.xlsm) über die angegebenen Links herunterladen.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-ModifyingVBAOrMacroCode.py" >}}

## **Erweiterte Themen**
- [Fügen Sie einen Bibliotheksverweis zum VBA-Projekt im Arbeitsblatt hinzu](/cells/de/python-net/add-a-library-reference-to-vba-project-in-workbook/)
- [Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist](/cells/de/python-net/check-if-digital-signature-of-vba-code-is-valid/)
- [Überprüfen Sie, ob der VBA-Code signiert ist](/cells/de/python-net/check-if-vba-code-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist](/cells/de/python-net/check-if-vba-project-in-a-workbook-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt geschützt und zum Anzeigen gesperrt ist](/cells/de/python-net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Digitales Signieren eines VBA-Codeprojekts mit Zertifikat](/cells/de/python-net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportieren Sie das VBA-Zertifikat in eine Datei oder einen Stream](/cells/de/python-net/export-vba-certificate-to-file-or-stream/)
- [Filtern eines VBA-Projekts beim Laden einer Arbeitsmappe](/cells/de/python-net/filter-vba-project-while-loading-a-workbook/)
- [Herausfinden, ob das VBA-Projekt geschützt ist](/cells/de/python-net/find-out-if-vba-project-is-protected/)
- [Passwortschutz des VBA-Projekts der Excel-Arbeitsmappe](/cells/de/python-net/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="python-net" >}}
