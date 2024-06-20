---
title: VBA Codes einer Excel Makro aktivierten Arbeitsmappe verwalten.
linktitle: Makro Projekt
type: docs
weight: 200
url: /de/net/manage-vba-project/
description: Fügen Sie ein VBA Modul hinzu und modifizieren Sie VBA oder Makro mit der Aspose.Cells Bibliothek.
---

## **Fügen Sie ein VBA-Modul in C# hinzu**
{{% alert color="primary" %}}

Aspose.Cells ermöglicht es Ihnen, ein neues VBA-Modul und einen Makrocode mit Aspose.Cells hinzuzufügen. Bitte verwenden Sie die [**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index)-Methode, um das neue VBA-Modul im Arbeitsblatt hinzuzufügen

{{% /alert %}}

Der folgende Beispielcode erstellt ein neues Arbeitsblatt, fügt ein neues VBA-Modul und einen Makrocode hinzu und speichert die Ausgabe im XLSM-Format. Sobald Sie die Ausgabe-XLSM-Datei in Microsoft Excel öffnen und auf die Menübefehle **Entwickler > Visual Basic** klicken, sehen Sie ein Modul namens "TestModule", und darin sehen Sie den folgenden Makrocode.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Hier ist der Beispielcode zum Erzeugen der Ausgabe-XLSM-Datei mit VBA-Modul und Makrocode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **VBA oder Makro in C# modifizieren**

{{% alert color="primary" %}} 

Sie können VBA- oder Makrocode mit Aspose.Cells modifizieren. Aspose.Cells hat den folgenden Namensraum und Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu modifizieren.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makrocode in der Quell-Excel-Datei mithilfe von Aspose.Cells ändern können.

{{% /alert %}} 

Der folgende Beispielcode lädt die Quell-Excel-Datei, die den folgenden VBA- oder Makrocode enthält

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Nach der Ausführung des Beispielcodes von Aspose.Cells wird der VBA- oder Makrocode wie folgt modifiziert sein

{{< highlight java >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

Sie können die [Quell-Excel-Datei](5112508.xlsm) und die [Ausgabe-Excel-Datei](5112511.xlsm) über die angegebenen Links herunterladen.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Erweiterte Themen**
- [Fügen Sie einen Bibliotheksverweis zum VBA-Projekt im Arbeitsblatt hinzu](/cells/de/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Makro einem Formularsteuerelement zuweisen](/cells/de/net/assign-macro-to-form-control/)
- [Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist](/cells/de/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Überprüfen Sie, ob der VBA-Code signiert ist](/cells/de/net/check-if-vba-code-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist](/cells/de/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt geschützt und zum Anzeigen gesperrt ist](/cells/de/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopieren Sie den VBA-Makro UserForm-DesignerStorage von der Vorlage in die Zieldatei](/cells/de/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Digitales Signieren eines VBA-Codeprojekts mit Zertifikat](/cells/de/net/digitally-sign-a-vba-code-project-with-certificate/)
- [Exportieren Sie das VBA-Zertifikat in eine Datei oder einen Stream](/cells/de/net/export-vba-certificate-to-file-or-stream/)
- [Filtern eines VBA-Projekts beim Laden einer Arbeitsmappe](/cells/de/net/filter-vba-project-while-loading-a-workbook/)
- [Herausfinden, ob das VBA-Projekt geschützt ist](/cells/de/net/find-out-if-vba-project-is-protected/)
- [Passwortschutz des VBA-Projekts der Excel-Arbeitsmappe](/cells/de/net/password-protect-the-vba-project-of-excel-workbook/)

