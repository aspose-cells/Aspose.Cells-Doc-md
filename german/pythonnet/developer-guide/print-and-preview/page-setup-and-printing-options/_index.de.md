---
title: Seiteneinrichtung und Druckoptionen
type: docs
weight: 60
url: /de/python-net/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Manchmal müssen Entwickler die Seiteneinrichtung und Druckeinstellungen konfigurieren, um den Druckvorgang zu steuern. Die Seiteneinrichtung und die Druckeinstellungen bieten verschiedene Optionen und werden vollständig in Aspose.Cells für Python via .NET unterstützt.

Dieser Artikel zeigt, wie man eine Konsolenanwendung in Visual Studio.Net erstellt und mit wenigen einfachen Zeilen Code mit der Aspose.Cells für Python via .NET API die Seiteneinrichtung und Druckoptionen auf ein Arbeitsblatt anwendet.

{{% /alert %}}

## **Arbeiten mit Seiten- und Druckeinstellungen**

Für dieses Beispiel haben wir eine Arbeitsmappe in Microsoft Excel erstellt und Aspose.Cells für Python via .NET benutzt, um die Seiteneinrichtung und Druckoptionen festzulegen.

### **Verwenden von Aspose.Cells zum Festlegen von Seiteneinrichtungsoptionen**

Erstellen Sie zuerst ein einfaches Arbeitsblatt in Microsoft Excel. Wenden Sie dann Seiteneinrichtungsoptionen darauf an. Das Ausführen des Codes ändert die Seiteneinrichtungsoptionen, wie im Screenshot unten dargestellt.

|**Ausgabedatei.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_1.png)|

1. Erstellen Sie ein Arbeitsblatt mit einigen Daten in Microsoft Excel:
   1. Öffnen Sie eine neue Arbeitsmappe in Microsoft Excel.
   1. Fügen Sie einige Daten hinzu.
1. Legen Sie Seiteneinrichtungsoptionen fest:
   Wenden Sie die Seiteneinrichtungsoptionen auf die Datei an. Unten ist ein Screenshot der Standardoptionen vor der Anwendung der neuen Optionen zu sehen.

|**Standardseiteneinrichtungsoptionen.**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_2.png)|


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPageSetup-1.py" >}}

### **Druckoptionen festlegen**

Die Seiteneinrichtungseinstellungen bieten auch mehrere Druckoptionen (auch Blattoptionen genannt), mit denen Benutzer steuern können, wie Arbeitsblattseiten gedruckt werden. Sie ermöglichen Benutzern:

- Eine bestimmte Druckbereich eines Arbeitsblatts auswählen.
- Titel drucken.
- Gitternetzlinien drucken.
- Zeilen-/Spaltenüberschriften drucken.
- Entwurfsqualität erreichen.
- Kommentare drucken.
- Zellenfehler drucken.
- Seiteneinteilung definieren.

Das folgende Beispiel wendet Druckoptionen auf die Datei an, die im obigen Beispiel erstellt wurde (PageSetup.xls). Der nachfolgende Screenshot zeigt die Standard-Druckoptionen, bevor neue Optionen angewendet werden.

|**Eingabedokument**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_3.png)|
Das Ausführen des Codes ändert die Druckoptionen.

|**Ausgabedatei**|
| :- |
|![todo:image_alt_text](page-setup-and-printing-options_4.png)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PrintAndPreview-SettingPrintingOptions-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
