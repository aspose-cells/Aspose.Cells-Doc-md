---
title: Hinzufügen von VBA Modul und Code mit Aspose.Cells
type: docs
weight: 20
url: /de/java/adding-vba-module-and-code-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht das Hinzufügen eines neuen VBA-Moduls und Makro-Codes mittels Aspose.Cells. Bitte verwenden Sie die Methode [**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add-com.aspose.cells.Worksheet-) zur Hinzufügung eines neuen VBA-Moduls im Arbeitsbuch.

{{% /alert %}}

## **Hinzufügen von VBA-Modul und Code mit Aspose.Cells**

Der folgende Beispielcode erstellt ein neues Arbeitsblatt, fügt ein neues VBA-Modul und einen Makrocode hinzu und speichert die Ausgabe im XLSM-Format. Sobald Sie die Ausgabe-XLSM-Datei in Microsoft Excel öffnen und auf die Menübefehle **Entwickler > Visual Basic** klicken, sehen Sie ein Modul namens "TestModule", und darin sehen Sie den folgenden Makrocode.

{{< highlight java >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Beispielcode

Hier ist ein Beispielcode, um die Ausgabedatei XLSM mit VBA-Modul und Makrocode zu generieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
{{< app/cells/assistant language="java" >}}
