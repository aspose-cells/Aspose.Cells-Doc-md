---
title: Umwandlung zwischen Zellnamen und Zeile/Spaltenindex
linktitle: Zellname und Indexumwandlung
type: docs
weight: 10
url: /de/nodejs-cpp/names-and-indices/
description: Lernen Sie, wie Sie die Umwandlung zwischen Zellname und Zeilen /Spaltenindex mithilfe der Aspose.Cells for Node.js via C++ API durchführen.
keywords: Node.js via C++ Zellname aus Zeilen und Spaltenindizes erhalten, Zeilen und Spaltenindizes aus Zellname erhalten, Sicheres Arbeitsblatt Namen erstellen, Sichere Arbeitsblatt Namen hinzufügen
---

## **Zellnamen aus Zeilen- und Spaltenindizes erhalten**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erläutert, wie.
 Aspose.Cells for Node.js via C++ bietet die Methode CellsHelper.cellIndexToName, mit der Entwickler den Namen einer Zelle anhand des Zeilen- und Spaltenindexes erhalten können.

{{% alert color="primary" %}} 

 Microsoft Excel beginnt die Zählung der Zeilen- und Spaltenindizes bei 1. Im Gegensatz dazu beginnt Aspose.Cells for Node.js via C++ die Zählung bei 0.

{{% /alert %}} 

 Der folgende Beispielcode zeigt, wie man CellsHelper.cellIndexToName verwendet, um den Namen der Zelle anhand eines bekannten Zeilen- und Spaltenindex zu erhalten. Der Code erzeugt die folgende Ausgabe.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-IndexToName-1.js" >}}
## **Zeilen- und Spaltenindizes aus Zellnamen erhalten**
Es ist möglich, den Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erläutert, wie.
 Aspose.Cells for Node.js via C++ bietet die Methode CellsHelper.cellNameToIndex, mit der Entwickler einen Zeilen- und Spaltenindex aus dem Zellnamen erhalten können.

{{% alert color="primary" %}} 

 Microsoft Excel beginnt die Zählung der Zeilen- und Spaltenindizes bei 1. Im Gegensatz dazu beginnt Aspose.Cells for Node.js via C++ die Zählung bei 0.

{{% /alert %}} 

 Der folgende Beispielcode zeigt, wie man CellsHelper.cellNameToIndex verwendet, um den Zeilen- und Spaltenindex anhand des Zellnamens zu erhalten. Der Code erzeugt die folgende Ausgabe.



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-NameToIndex-1.js" >}}

## **Sichere Blattnamen erstellen**
 Manchmal besteht die Notwendigkeit, den Blattnamen zur Laufzeit zuzuweisen. In diesem Szenario können Blattnamen enthalten sein, die zusätzliche Zeichen wie <>+(?” enthalten. Es ist notwendig, solche Zeichen, die als Blattname nicht erlaubt sind, durch ein vom Benutzer vorgegebenes Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, was gekürzt werden muss. Apache POI bietet Funktionen zum Erstellen sicherer Namen, daher bietet Aspose.Cells for Node.js via C++ eine ähnliche Funktion zur Handhabung dieser Probleme. Das folgende Beispiel demonstriert diese Funktion:



{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Data-CellsHelper-CreateSafeSheetNames.js" >}}

Ergebnis:

das ist der erste Name, der erstellt wurde

` `<> + (Adj. Privat _ "Privat"
