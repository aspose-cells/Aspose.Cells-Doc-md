---
title: Hinzufügen von VBA-Modul und Code mit Aspose.Cells
type: docs
weight: 20
url: /de/java/adding-vba-module-and-code-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells ermöglicht es Ihnen, ein neues VBA-Modul und Makrocode mit Aspose.Cells hinzuzufügen. Bitte verwenden Sie die[**Workbook.getVbaProject().getModules().add(**)](https://reference.aspose.com/cells/java/com.aspose.cells/vbamodulecollection#add(com.aspose.cells.Worksheet))-Methode, um das neue VBA-Modul in der Arbeitsmappe hinzuzufügen

{{% /alert %}}

## **Hinzufügen von VBA-Modul und Code mit Aspose.Cells**

Der folgende Beispielcode erstellt eine neue Arbeitsmappe, fügt ein neues VBA-Modul und einen neuen Makrocode hinzu und speichert die Ausgabe im Format XLSM. Einmal öffnen Sie die Ausgabedatei XLSM in Microsoft Excel und klicken auf die**Entwickler > Visual Basic** Menübefehle sehen Sie ein Modul namens "TestModule" und darin sehen Sie den folgenden Makrocode.

{{< highlight "java" >}}

 Sub ShowMessage()

    MsgBox "Welcome to Aspose!"

End Sub

{{< /highlight >}}

## Beispielcode

Hier ist ein Beispielcode zum Generieren der Ausgabedatei XLSM mit VBA-Modul und Makrocode.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-AddVBAModuleAndCode-AddVBAModuleAndCode.java" >}}
