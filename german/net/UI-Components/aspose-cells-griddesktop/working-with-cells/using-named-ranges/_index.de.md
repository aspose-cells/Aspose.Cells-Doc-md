---
title: Verwenden von benannten Bereichen
type: docs
weight: 110
url: /de/net/aspose-cells-griddesktop/use-named-ranges/
keywords: GridDesktop, benannte Bereiche, Namen
description: Dieser Artikel stellt die benannten Bereiche in GridDesktop vor.
---

{{% alert color="primary" %}} 

Normalerweise verwenden Sie die Beschriftungen von Spalten und Zeilen in einem Arbeitsblatt, um auf die Zellen innerhalb dieser Spalten und Zeilen zu verweisen. Sie können jedoch aussagekräftige Namen erstellen, um Zellen, Zellbereiche, Formeln oder konstante Werte zu repräsentieren. Das Wort **Name** kann sich auf eine Zeichenkette beziehen, die eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert darstellt. Verwenden Sie beispielsweise leicht verständliche Namen wie z.B. Produkte, um auf schwer verständliche Bereiche wie z.B. Verkäufe!C20:C30 zu verweisen, um eine Zelle, einen Zellbereich, eine Formel oder einen konstanten Wert zu repräsentieren. Beschriftungen können in Formeln verwendet werden, die sich auf Daten im gleichen Arbeitsblatt beziehen; wenn Sie einen Bereich auf einem anderen Arbeitsblatt darstellen möchten, können Sie einen Namen verwenden. **Benannte Bereiche** zählen zu den leistungsfähigsten Funktionen von Microsoft. Benutzer können einem benannten Bereich einen Namen zuweisen, so dass auf diesen Bereich von Zellen in den Formeln mit seinem Namen verwiesen werden kann. **Aspose.Cells.GridDesktop** unterstützt diese Funktion.

{{% /alert %}} 
## **Hinzufügen/Referenzierung benannter Bereiche in Formeln**
Das GridDesktop-Control unterstützt das Importieren/Exportieren benannter Bereiche in den Excel-Dateien. Es bietet zwei Klassen (**Name** und **NameCollection**) zum Arbeiten mit benannten Bereichen.

Der folgende Code-Auszug hilft Ihnen, wie Sie sie verwenden können.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithCells-UsingNamedRanges-1.cs" >}}
