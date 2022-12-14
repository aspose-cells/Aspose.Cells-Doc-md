---
title: Arbeitsblatt hinzufügen oder einfügen
type: docs
weight: 20
url: /de/net/add-or-insert-a-worksheet/
---
{{% alert color="primary" %}} 

In diesem Thema werden die Techniken zum Hinzufügen oder Einfügen von Arbeitsblättern in einer Excel-Datei mit Aspose.Cells.GridDesktop erläutert. Der Unterschied zwischen dem Hinzufügen und Einfügen von Arbeitsblättern besteht darin, dass zusätzlich ein Arbeitsblatt einfach am Ende der Arbeitsblattsammlung der Excel-Datei hinzugefügt wird. Einfügen bedeutet jedoch, ein Arbeitsblatt an einer bestimmten Position in der Arbeitsblattsammlung hinzuzufügen.

{{% /alert %}} 
## **Hinzufügen eines Arbeitsblatts**
Um ein Arbeitsblatt mit Aspose.Cells.GridDesktop hinzuzufügen, führen Sie bitte die folgenden Schritte aus:

1. Fügen Sie einem Formular das Aspose.Cells.GridDesktop-Steuerelement hinzu.
1. Rufen Sie die Add-Methode der Worksheet-Auflistung im GridDesktop-Steuerelement auf.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheet.cs" >}}


Viele überladene Versionen der Add-Methode sind verfügbar. Mit der obigen überladenen Version wird beispielsweise ein Arbeitsblatt mit einem Standardblattnamen zur Excel-Datei hinzugefügt. Bei Verwendung anderer überladener Versionen der Add-Methode ist es möglich, den Namen wie unten im Beispiel gezeigt zu definieren.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-AddingWorksheetWithName.cs" >}}
## **Arbeitsblatt einfügen**
Um ein Arbeitsblatt mit Aspose.Cells.GridDesktop einzufügen, gehen Sie bitte wie folgt vor:

1. Fügen Sie einem Formular das Aspose.Cells.GridDesktop-Steuerelement hinzu.
1. Rufen Sie die Insert-Methode der Worksheets-Auflistung im GridDesktop-Steuerelement auf.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AddInsertWorksheet-InsertingWorksheet.cs" >}}

{{% alert color="primary" %}} 

WICHTIG: Microsoft Excel (97-2003 XLS) unterstützt Excel-Tabellen mit bis zu 65.536 Zeilen und 256 Spalten. Aspose.Cells.GridDesktop folgt denselben Standards. Im Aspose.Cells.GridDesktop-Steuerelement können Entwickler Arbeitsblätter mit mehr Zeilen und Spalten als das Standardlimit hinzufügen oder einfügen, aber wenn sie versuchen, die Grid-Daten in einer Excel-Datei zu speichern, wird eine Ausnahme ausgelöst. Das bedeutet, dass nur Daten, die in den 65.536 Zeilen und 256 Spalten enthalten sind, mit Aspose.Cells.GridDesktop in einer Excel-XLS-Datei gespeichert werden können, wenn Sie das XLSX-Dateiformat (MS Excel 2007/2010) verwenden, gibt es jedoch keine solche Einschränkung.

{{% /alert %}}
