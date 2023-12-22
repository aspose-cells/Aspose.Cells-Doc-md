---
title: Konvertierung zwischen Zellenname und Zeilen-/Spaltenindex
linktitle: Cell Namens- und Indexkonvertierung
type: docs
weight: 10
url: /de/net/names-and-indices/
description: Erfahren Sie, wie Sie über Aspose.Cells for .NET API eine Konvertierung zwischen Zellennamen und Zeilen-/Spaltenindex durchführen.
keywords: Get Cell Name from Row and Column Indices, Get Row and Column Indices from Cell Name, Create safe worksheet names, Add safe worksheet names
---
##  **Rufen Sie den Namen Cell aus den Zeilen- und Spaltenindizes ab**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. In diesem Artikel wird erklärt, wie.
Aspose.Cells stellt die Methode CellsHelper.CellIndexToName bereit, mit der Entwickler den Namen einer Zelle abrufen können, wenn sie den Zeilen- und Spaltenindex angeben.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit der Zählung der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie Sie mit CellsHelper.CellIndexToName auf den Namen der Zelle zugreifen, wenn ein bekannter Zeilen- und Spaltenindex vorliegt. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
##  **Rufen Sie Zeilen- und Spaltenindizes vom Namen Cell ab**
Es ist möglich, anhand des Namens einen Zeilen- und Spaltenindex der Zelle zu ermitteln. In diesem Artikel wird erklärt, wie.
Aspose.Cells stellt die Methode CellsHelper.CellNameToIndex bereit, die es Entwicklern ermöglicht, einen Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit der Zählung der Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie CellsHelper.CellNameToIndex verwendet wird, um den Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
##  **Erstellen Sie sichere Blattnamen**
 Manchmal ist es erforderlich, den Blattnamen zur Laufzeit zuzuweisen. In diesem Szenario kann es Blattnamen geben, die einige zusätzliche Zeichen enthalten, z<>+(?“. Es besteht die Notwendigkeit, solche Zeichen, die nicht als Blattname zulässig sind, durch einige vom Benutzer bereitgestellte voreingestellte Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, die gekürzt werden müssen. Apache POI bietet bestimmte Funktionen zum Erstellen sicherer Namen, daher bietet Aspose.Cells eine ähnliche Funktion, um all diese Probleme zu lösen. Der folgende Beispielcode demonstriert diese Funktion:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Ausgabe:

Dies ist der Vorname, der cre ist

` `<> + (adj.Private _ „Privat“
