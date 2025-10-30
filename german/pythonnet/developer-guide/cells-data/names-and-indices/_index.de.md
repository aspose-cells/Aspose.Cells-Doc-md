---
title: Umwandlung zwischen Zellnamen und Zeile/Spaltenindex
linktitle: Zellname und Indexumwandlung
type: docs
weight: 10
url: /de/python-net/names-and-indices/
description: Erfahren Sie, wie Sie die Umwandlung zwischen Zellnamen und Zeilen /Spaltenindex mit der Aspose.Cells for Python via .NET API erhalten können.
keywords: Python Excel Bibliothek, Python Abrufen des Zellnamens aus Zeilen und Spaltenindizes, Python Abrufen von Zeilen und Spaltenindizes aus Zellnamen, Python Sichere Arbeitsblattnamen erstellen, Python Sichere Arbeitsblattnamen hinzufügen
---

## **Zellnamen aus Zeilen- und Spaltenindizes erhalten**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells for Python via .NET bietet die [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) Methode, mit der Entwickler den Zellnamen erhalten können, wenn sie den Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells for Python via .NET die Zählung der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie [**CellsHelper.cell_index_to_name**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_index_to_name/#int-int) verwendet wird, um den Zellnamen anhand eines bekannten Zeilen- und Spaltenindexes zu erhalten. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-IndexToName-1.py" >}}

## **Zeilen- und Spaltenindizes aus Zellnamen erhalten**
Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells for Python via .NET bietet die [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) Methode, mit der Entwickler den Zeilen- und Spaltenindex aus dem Zellnamen erhalten können.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo die Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells for Python via .NET die Zählung der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie [**CellsHelper.cell_name_to_index**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/cell_name_to_index/#str-any-any) verwendet wird, um den Zeilen- und Spaltenindex aus dem Zellnamen zu erhalten. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-NameToIndex-1.py" >}}

## **Sichere Blattnamen erstellen**
Manchmal ist es erforderlich, den Blattnamen zur Laufzeit zuzuweisen. In diesem Szenario können Blattnamen zusätzliche Zeichen wie <>+(?” enthalten. Es ist erforderlich, ein solches Zeichen, das nicht als Blattname erlaubt ist, durch ein vom Benutzer bereitgestelltes voreingestelltes Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, was gekürzt werden muss. Apache POI bietet bestimmte Funktionen zum Erstellen sicherer Namen, daher bietet Aspose.Cells for Python via .NET eine ähnliche Funktion, um all diese Probleme zu behandeln. Der folgende Beispielcode demonstriert diese Funktion:



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-CellsHelper-CreateSafeSheetNames.py" >}}

Ergebnis:

das ist der erste Name, der erstellt wurde

` `<> + (Adj. Privat _ "Privat"
{{< app/cells/assistant language="python-net" >}}
