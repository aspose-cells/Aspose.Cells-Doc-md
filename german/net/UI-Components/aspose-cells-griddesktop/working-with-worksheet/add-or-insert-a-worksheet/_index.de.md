---
title: Ein Arbeitsblatt hinzufügen oder einfügen
type: docs
weight: 20
url: /de/net/aspose-cells-griddesktop/add-or-insert-a-worksheet/
keywords: GridDesktop,Einfügen,Arbeitsblatt,Ein Arbeitsblatt einfügen
description: Dieser Artikel stellt vor, wie man ein Arbeitsblatt in GridDesktop hinzufügt oder einfügt.
---

{{% alert color="primary" %}} 

In diesem Thema werden die Techniken zum Hinzufügen oder Einfügen von Arbeitsblättern in einer Excel-Datei mithilfe von Aspose.Cells.GridDesktop diskutiert. Der Unterschied zwischen Hinzufügen und Einfügen von Arbeitsblättern besteht darin, dass ein Arbeitsblatt beim Hinzufügen einfach am Ende der Arbeitsblattsammlung der Excel-Datei hinzugefügt wird. Das Einfügen bedeutet jedoch, dass ein Arbeitsblatt an einer bestimmten Position in der Arbeitsblattsammlung hinzugefügt wird.

{{% /alert %}} 
## **Ein Arbeitsblatt hinzufügen**
Um ein Arbeitsblatt mithilfe von Aspose.Cells.GridDesktop hinzuzufügen, befolgen Sie bitte die folgenden Schritte:

1. Fügen Sie das Aspose.Cells.GridDesktop-Steuerelement zu einem Formular hinzu.
1. Rufen Sie die Add-Methode der Arbeitsblattsammlung in der GridDesktop-Steuerung auf.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Viele überladene Versionen der Add-Methode sind verfügbar. Mit der oben genannten überladenen Version wird beispielsweise ein Arbeitsblatt mit einem Standard-Blattnamen zur Excel-Datei hinzugefügt. Mit anderen überladenen Versionen der Add-Methode ist es möglich, den Namen wie im folgenden Beispiel angegeben zu definieren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Ein Arbeitsblatt einfügen**
Um ein Arbeitsblatt mithilfe von Aspose.Cells.GridDesktop einzufügen, befolgen Sie bitte die folgenden Schritte:

1. Fügen Sie der Form die Aspose.Cells.GridDesktop-Steuerung hinzu.
1. Rufen Sie die Insert-Methode der Arbeitsblattsammlung in der GridDesktop-Steuerung auf.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Microsoft Excel (97-2003 XLS) unterstützt Excel-Tabellen mit bis zu 65.536 Zeilen und 256 Spalten. Aspose.Cells.GridDesktop folgt denselben Standards. In der Aspose.Cells.GridDesktop-Steuerung können Entwickler Arbeitsblätter mit mehr Zeilen und Spalten als die Standardgrenze hinzufügen oder einfügen. Wenn sie jedoch versuchen, die Rasterdaten in eine Excel-Datei zu speichern, wird eine Ausnahme ausgelöst. Dies bedeutet, dass nur Daten, die in den 65.536 Zeilen und 256 Spalten enthalten sind, in einer Excel-XLS-Datei mit Aspose.Cells.GridDesktop gespeichert werden können. Wenn Sie das Dateiformat XLSX (MS Excel 2007/2010) verwenden, gibt es jedoch keine solche Einschränkung.

{{% /alert %}}
