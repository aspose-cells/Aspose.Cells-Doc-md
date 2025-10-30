---
title: Excel in Python Daten konvertieren
type: docs
weight: 30
url: /de/python-net/convert-excel-to-list/
description: Excel in Liste konvertieren mithilfe der Aspose.Cells für Python via .NET API.
keywords: Excel in Wörterbuch umwandeln mithilfe der Python Excel Bibliothek, Arbeitsmappe in Wörterbuch umwandeln mithilfe der Python Excel Bibliothek, Zeilenobjekt in Liste umwandeln mithilfe der Python Excel Bibliothek, Wie man ListObject in Liste umwandelt, Spaltenobjekt in Liste umwandeln mithilfe der Python Excel Bibliothek, Bereich in Liste umwandeln mithilfe der Python Excel Bibliothek, Arbeitsblatt in Liste umwandeln mithilfe der Python Excel Bibliothek.
---

{{% alert color="primary" %}}

Mit der Aspose.Cells für Python via .NET API können Sie Arbeitsmappe, Arbeitsblatt, Bereich, Zeile, Spalte und andere Excel-Daten in Python-Liste konvertieren.

{{% /alert %}}

## **Wie man Excel-Arbeitsmappe in Wörterbuch umwandelt**
Hier ist ein Beispielcode-Schnipsel, der zeigt, wie Excel-Daten mithilfe der Aspose.Cells für Python via .NET in ein Wörterbuch exportiert werden können:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Alle Arbeitsblätter durchlaufen und Arbeitsmappe in ein Wörterbuch mit der Aspose.Cells für Python Excel-Bibliothek umwandeln.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-Dictionary.py" >}}

Das Ausgabenergebnis:
```
{'Sheet1': [['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 'Sheet2': [['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], 'Sheet3': [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]}
```

## **Wie man Excel-Arbeitsmappe in Liste umwandelt**
Hier ist ein Beispielcodeausschnitt, um zu demonstrieren, wie man Excel-Daten in eine Liste exportiert, indem man Aspose.Cells für Python via .NET verwendet:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Durchlaufen Sie alle Arbeitsblätter und konvertieren Sie die Arbeitsmappe in eine Liste, indem Sie die Aspose.Cells für Python Excel-Bibliothek verwenden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-List.py" >}}

Das Ausgabenergebnis:
```
[[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]], 
[['City2', 'Region2', 'Store3'], ['Seattle', 'West', 3000], ['philadelph', 'East', 3082], ['Detroit', 'Central', 3074]], [['City3', 'Region3', 'Store3'], ['Seattle', 'West', 3166], ['New York', 'East', 3090], ['Chicago', 'Central', 3055]]] 
```

## **Wie man ein Arbeitsblatt in eine Liste konvertiert**
Hier ist ein Beispielcodeausschnitt, um zu demonstrieren, wie man Arbeitsblattdaten in eine Liste exportiert, indem man Aspose.Cells für Python via .NET verwendet:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Konvertieren Sie Arbeitsblattdaten in eine Liste, indem Sie die Aspose.Cells für Python Excel-Bibliothek verwenden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-List.py" >}}

Das Ausgabenergebnis:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```

## **Wie man ein ListObject von Excel in eine Liste konvertiert**
Hier ist ein Beispielcodeausschnitt, um zu demonstrieren, wie man ListObject-Daten in eine Liste exportiert, indem man Aspose.Cells für Python via .NET verwendet:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Erstellen Sie das ListObject-Objekt.
1. Konvertieren Sie ListObject-Daten in eine Liste, indem Sie die Aspose.Cells für Python Excel-Bibliothek verwenden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-List.py" >}}

Das Ausgabenergebnis:
```
[['City', 'Region', 'Store'], ['Chicago', 'Central', 3055], ['New York', 'East', 3036], ['Detroit', 'Central', 3074]]
```


## **Wie man eine Excel-Zeile in eine Liste konvertiert**
Hier ist ein Beispielcodeausschnitt, um zu demonstrieren, wie man Zeilendaten in eine Liste exportiert, indem man Aspose.Cells für Python via .NET verwendet:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Holen Sie das Zeilenobjekt anhand des Zeilenindex.
1. Konvertieren Sie Zeilendaten mithilfe der Aspose.Cells für die Python Excel-Bibliothek in eine Liste.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-List.py" >}}

Das Ausgabenergebnis:
```
['Detroit', 'Central', 3074]
```

## **Wie man eine Excel-Spalte in eine Liste konvertiert**
Hier ist ein Beispiel-Codeausschnitt, der zeigt, wie Spaltendaten mithilfe der Aspose.Cells für Python via .NET in eine Liste exportiert werden.
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Holen Sie das Spaltenobjekt nach Spaltenindex.
1. Konvertieren Sie Spaltendaten mithilfe der Aspose.Cells für die Python Excel-Bibliothek in eine Liste.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-List.py" >}}

Das Ausgabenergebnis:
```
['Store', 3055, 3036, 3074]
```

## **Wie man einen Bereich von Excel in eine Liste konvertiert**
Hier ist ein Beispiel-Codeausschnitt, der zeigt, wie Bereichsdaten mithilfe der Aspose.Cells für Python via .NET in eine Liste exportiert werden.
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Erstellen Sie den Bereich.
1. Konvertieren Sie Bereichsdaten mithilfe der Aspose.Cells für Python Excel-Bibliothek in eine Liste.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-List.py" >}}

Das Ausgabenergebnis:
```
[['Region', 'Store'], ['Central', 3055], ['East', 3036]]
```
{{< app/cells/assistant language="python-net" >}}
