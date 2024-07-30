---
title: Umwandlung zwischen Zellnamen und Zeile/Spaltenindex
linktitle: Zellname und Indexumwandlung
type: docs
weight: 10
url: /de/net/names-and-indices/
description: Lernen Sie, wie Sie durch die Aspose.Cells for .NET API die Umrechnung zwischen Zellnamen und Zeilen /Spaltenindex erhalten.
keywords: Z cell Name aus Zeilen und Spaltenindizes erhalten, Zeilen und Spaltenindizes aus Zellnamen erhalten, Sichere Tabellennamen erstellen, Sichere Tabellennamen hinzufügen
---

## **Zellnamen aus Zeilen- und Spaltenindizes erhalten**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells bietet die Methode CellsHelper.CellIndexToName, mit der Entwickler den Namen einer Zelle erhalten, wenn sie den Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Microsoft Excel beginnt mit der Zählung von Zeilen- und Spaltenindizes bei 1. Im Gegensatz zu Microsoft Excel beginnt Aspose.Cells mit der Zählung von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie CellsHelper.CellIndexToName verwendet wird, um den Namen der Zelle anhand eines bekannten Zeilen- und Spaltenindexes abzurufen. Der Code erzeugt die folgende Ausgabe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Zeilen- und Spaltenindizes aus Zellnamen erhalten**
Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.
Aspose.Cells bietet die Methode CellsHelper.CellNameToIndex, mit der Entwickler den Zeilen- und Spaltenindex aus dem Namen der Zelle erhalten.

{{% alert color="primary" %}} 

Microsoft Excel beginnt mit der Zählung von Zeilen- und Spaltenindizes bei 1. Im Gegensatz zu Microsoft Excel beginnt Aspose.Cells mit der Zählung von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie CellsHelper.CellNameToIndex verwendet wird, um den Zeilen- und Spaltenindex aus dem Namen der Zelle zu erhalten. Der Code erzeugt die folgende Ausgabe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Sichere Blattnamen erstellen**
Manchmal besteht die Notwendigkeit, den Blattnamen zur Laufzeit zuzuweisen. In diesem Szenario können Blattnamen zusätzliche Zeichen wie <>+(?” enthalten. Es besteht die Notwendigkeit, ein solches Zeichen, das als Blattnamen nicht zulässig ist, durch ein vom Benutzer bereitgestelltes voreingestelltes Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, was abgeschnitten werden muss. Apache POI bietet bestimmte Funktionen zum Erstellen sicherer Namen, daher wird ein ähnliches Feature von Aspose.Cells bereitgestellt, um all diese Probleme zu behandeln. Der folgende Beispielcode zeigt dieses Feature:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Ergebnis:

das ist der erste Name, der erstellt wurde

` `<> + (Adj. Privat _ "Privat"
