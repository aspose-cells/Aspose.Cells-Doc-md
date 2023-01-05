---
title: Konvertierung zwischen Zellenname und Zeilen-/Spaltenindex
linktitle: Cell Namens- und Indexkonvertierung
type: docs
weight: 10
url: /de/net/names-and-indices/
---
## **Rufen Sie den Namen Cell aus den Zeilen- und Spaltenindizes ab**
Es ist möglich, den Namen einer Zelle anhand des Zeilen- und Spaltenindex zu finden. Dieser Artikel erklärt, wie.
Aspose.Cells stellt die CellsHelper.CellIndexToName-Methode bereit, mit der Entwickler den Namen einer Zelle abrufen können, wenn sie den Zeilen- und Spaltenindex bereitstellen.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht die Verwendung von CellsHelper.CellIndexToName für den Zugriff auf den Namen der Zelle bei einem bekannten Zeilen- und Spaltenindex. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-IndexToName-1.cs" >}}
## **Rufen Sie Zeilen- und Spaltenindizes von Cell Name ab**
Es ist möglich, einen Zeilen- und Spaltenindex der Zelle anhand ihres Namens zu finden. Dieser Artikel erklärt, wie.
Aspose.Cells stellt die CellsHelper.CellNameToIndex-Methode bereit, mit der Entwickler einen Zeilen- und Spaltenindex aus dem Namen der Zelle abrufen können.

{{% alert color="primary" %}} 

Im Gegensatz zu Microsoft Excel, wo Zeilen- und Spaltenindizes bei 1 beginnen, beginnt Aspose.Cells mit dem Zählen von Zeilen- und Spaltenindizes bei 0.

{{% /alert %}} 

Der folgende Beispielcode veranschaulicht, wie CellsHelper.CellNameToIndex verwendet wird, um den Zeilen- und Spaltenindex aus dem Namen der Zelle abzurufen. Der Code generiert die folgende Ausgabe.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelperClass-NameToIndex-1.cs" >}}
## **Erstellen Sie sichere Blattnamen**
 Manchmal muss der Blattname zur Laufzeit zugewiesen werden. In diesem Szenario kann es Blattnamen geben, die einige zusätzliche Zeichen enthalten können, wie z<>+(?". Es ist notwendig, solche Zeichen, die als Blattname nicht zulässig sind, durch ein vom Benutzer bereitgestelltes voreingestelltes Zeichen zu ersetzen. Ebenso kann die Länge auf mehr als 31 Zeichen ansteigen, die abgeschnitten werden müssen. Apache POI bietet Bestimmte Funktionen zum Erstellen sicherer Namen, daher wird eine ähnliche Funktion von Aspose.Cells bereitgestellt, um all diese Probleme zu behandeln. Der folgende Beispielcode demonstriert diese Funktion:



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-CellsHelper-CreateSafeSheetNames.cs" >}}

Ausgabe:

Dies ist der Vorname, der cre ist

` `<> + (Adj. Privat _ "Privat"
