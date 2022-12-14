---
title: Verwalten Sie VBA-Codes von Excel-Arbeitsmappen mit Makros.
linktitle: Makroprojekt
type: docs
weight: 200
url: /de/net/manage-vba-project/
description: VBA-Modul hinzufügen und VBA oder Makro mit Aspose.Cells-Bibliothek ändern.
---
## **Fügen Sie ein VBA-Modul in C# hinzu**
{{% alert color="primary" %}}

 Aspose.Cells ermöglicht es Ihnen, ein neues VBA-Modul und Makrocode mit Aspose.Cells hinzuzufügen. Bitte verwenden Sie die[**Workbook.VbaProject.Modules.Add()**](https://reference.aspose.com/cells/net/aspose.cells.vba/vbamodulecollection/methods/add/index) -Methode, um das neue VBA-Modul in der Arbeitsmappe hinzuzufügen

{{% /alert %}}

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, fügt ein neues VBA-Modul und Makrocode hinzu und speichert die Ausgabe im XLSM-Format. Einmal öffnen Sie die XLSM-Ausgabedatei in Microsoft Excel und klicken auf die**Entwickler > Visual Basic** Menübefehle sehen Sie ein Modul namens "TestModule" und darin sehen Sie den folgenden Makrocode.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

Hier ist der Beispielcode zum Generieren der XLSM-Ausgabedatei mit VBA-Modul und Makrocode.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-AddVBAModuleOrCode-AddVBAModuleOrCode.cs" >}}

## **Ändern Sie VBA oder Makro in C#**

{{% alert color="primary" %}} 

Sie können VBA- oder Makrocode mit Aspose.Cells ändern. Aspose.Cells hat den folgenden Namespace und die folgenden Klassen hinzugefügt, um das VBA-Projekt in der Excel-Datei zu lesen und zu ändern.

- Aspose.Cells.Vba
- VbaProjekt
- VbaModuleCollection
- VbaModul

Dieser Artikel zeigt Ihnen, wie Sie den VBA- oder Makrocode in der Excel-Quelldatei mit Aspose.Cells ändern.

{{% /alert %}} 

Der folgende Beispielcode lädt die Excel-Quelldatei, die den folgenden VBA- oder Makrocode enthält

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is test message."

End Sub

{{< /highlight >}}

Nach der Ausführung des Beispielcodes Aspose.Cells wird der VBA- oder Makrocode wie folgt geändert

{{< highlight "java" >}}

 Sub Button1_Click()

    MsgBox "This is Aspose.Cells message."

End Sub

{{< /highlight >}}

 Sie können die herunterladen[Excel-Quelldatei](5112508.xlsm) und die[Excel-Datei ausgeben](5112511.xlsm) aus den angegebenen Links.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingVBAModules-ModifyingVBAOrMacroCode-ModifyingVBAOrMacroCode.cs" >}}

## **Themen vorantreiben**
- [Fügen Sie einen Bibliotheksverweis zum VBA-Projekt in der Arbeitsmappe hinzu](/cells/de/net/add-a-library-reference-to-vba-project-in-workbook/)
- [Makro dem Formularsteuerelement zuweisen](/cells/de/net/assign-macro-to-form-control/)
- [Überprüfen Sie, ob die digitale Signatur des VBA-Codes gültig ist](/cells/de/net/check-if-digital-signature-of-vba-code-is-valid/)
- [Überprüfen Sie, ob der VBA-Code signiert ist](/cells/de/net/check-if-vba-code-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt in einer Arbeitsmappe signiert ist](/cells/de/net/check-if-vba-project-in-a-workbook-is-signed/)
- [Überprüfen Sie, ob das VBA-Projekt geschützt und für die Anzeige gesperrt ist](/cells/de/net/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Kopieren Sie VBA Macro UserForm DesignerStorage aus der Vorlage in die Zielarbeitsmappe](/cells/de/net/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Signieren Sie ein VBA-Code-Projekt digital mit Zertifikat](/cells/de/net/digitally-sign-a-vba-code-project-with-certificate/)
- [VBA-Zertifikat in Datei oder Stream exportieren](/cells/de/net/export-vba-certificate-to-file-or-stream/)
- [Filtern Sie VBA-Projekte beim Laden einer Arbeitsmappe](/cells/de/net/filter-vba-project-while-loading-a-workbook/)
- [Finden Sie heraus, ob das VBA-Projekt geschützt ist](/cells/de/net/find-out-if-vba-project-is-protected/)
- [Schützen Sie das VBA-Projekt der Excel-Arbeitsmappe mit einem Kennwort](/cells/de/net/password-protect-the-vba-project-of-excel-workbook/)

