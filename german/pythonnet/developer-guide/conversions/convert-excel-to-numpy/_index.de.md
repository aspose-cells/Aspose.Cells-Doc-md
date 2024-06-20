---
title: Excel in NumPy konvertieren
type: docs
weight: 30
url: /de/python-net/convert-excel-to-numpy/
description: Konvertieren Sie Excel in NumPy, indem Sie die Aspose.Cells für Python via .NET API verwenden.
keywords: Python Konvertieren Sie Excel in ein NumPy Array, Exportieren Sie Arbeitsmappe in ein NumPy Array in Python via NET, Python Konvertieren Sie Reihe in ein NumPy Array, Python Konvertieren Sie Tabelle in ein NumPy Array, Exportieren Sie ListObject in ein NumPy Array in Python via NET, Python Konvertieren Sie Bereich in ein NumPy Array, Spalte in ein NumPy Array mit Python umwandeln.
---

## **Einführung in NumPy**
NumPy (Numerisches Python) ist eine Open-Source-numerische Rechenerweiterung für Python. Dieses Tool kann verwendet werden, um große Matrizen zu speichern und zu verarbeiten, was effizienter ist als die verschachtelte Listenstruktur von Python (die ebenfalls zur Darstellung von Matrizen verwendet werden kann). Es unterstützt eine große Anzahl von Dimensionalarrays und Matrixoperationen und bietet auch eine große Anzahl von mathematischen Funktionsbibliotheken für Arrayoperationen. 

Die Hauptfunktionen von NumPy:
1. Ndarray, ein mehrdimensionales Array-Objekt, ist eine schnelle, flexible und platzsparende Datenstruktur.
1. Lineare Algebraoperationen, einschließlich Matrixmultiplikation, Transposition, Inversion usw.
1. Fourier-Transformation, Durchführung einer schnellen Fourier-Transformation an einem Array.
1. Schnelle Verarbeitung von Gleitkommazahlenarrays.
1. Integration von C-Sprachencode in Python, um die Ausführung zu beschleunigen.

Mit Aspose.Cells für Python via .NET API können Sie Excel, TSV, CSV, Json und viele verschiedene Formate in Numpy ndarray konvertieren.

## **Wie man Excel-Arbeitsmappe in ein NumPy-Array umwandelt**
Hier ist ein Beispielcode-Schnipsel, um zu demonstrieren, wie man Excel-Daten mit Aspose.Cells für Python via .NET in ein NumPy-Array exportiert.
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Durchsuchen Sie Excel-Daten und exportieren Sie Daten in ein NumPy-Array mit Aspose.Cells für Python via .NET.


{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Workbook-to-NDArray.py" >}}

Das Ausgabenergebnis:
```
[[['City' 'Region' 'Store']    
  ['Chicago' 'Central' '3055'] 
  ['New York' 'East' '3036']   
  ['Detroit' 'Central' '3074']]

 [['City2' 'Region2' 'Store3']
  ['Seattle' 'West' '3000']
  ['philadelph' 'East' '3082']
  ['Detroit' 'Central' '3074']]

 [['City3' 'Region3' 'Store3']
  ['Seattle' 'West' '3166']
  ['New York' 'East' '3090']
  ['Chicago' 'Central' '3055']]]
```

## **Wie man Arbeitsblatt in ein NumPy-Array umwandelt**
Hier ist ein Beispielcode-Schnipsel, um zu demonstrieren, wie man Arbeitsblattdaten mit Aspose.Cells für Python via .NET in Numpy ndarray exportiert:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Arbeitsblattdaten in Numpy ndarray mit Aspose.Cells für die Python Excel-Bibliothek umwandeln.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Worksheet-to-NDArray.py" >}}

Das Ausgabenergebnis:
```
[['City' 'Region' 'Store']    
 ['Chicago' 'Central' '3055'] 
 ['New York' 'East' '3036']   
 ['Detroit' 'Central' '3074']]
```
## **Wie man einen Bereich von Excel in ein NumPy ndarray umwandelt**
Hier ist ein Beispielcode-Schnipsel, um zu zeigen, wie man Bereichsdaten in ein NumPy ndarray mithilfe von Aspose.Cells für Python via .NET exportiert:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Erstellen Sie den Bereich.
1. Konvertieren Sie Bereichsdaten in ein NumPy ndarray mithilfe der Aspose.Cells for Python Excel-Bibliothek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Range-to-NDArray.py" >}}

Das Ausgabenergebnis:
```
[['Region' 'Store']
 ['Central' '3055']
 ['East' '3036']]
```

## **Wie man ein ListObject von Excel in ein NumPy ndarray umwandelt**
Hier ist ein Beispielcode-Schnipsel, um zu zeigen, wie man ListObject-Daten in ein NumPy ndarray mithilfe von Aspose.Cells für Python via .NET exportiert:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Erstellen Sie das ListObject-Objekt.
1. Konvertieren Sie ListObject-Daten in ein NumPy ndarray mithilfe der Aspose.Cells for Python Excel-Bibliothek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-ListObject-to-NDArray.py" >}}

Das Ausgabenergebnis:
```
[['City' 'Region' 'Store']
 ['Chicago' 'Central' '3055']
 ['New York' 'East' '3036']
 ['Detroit' 'Central' '3074']]
```

## **Wie man eine Zeile aus Excel in ein NumPy ndarray umwandelt**
Hier ist ein Beispielcode-Schnipsel, um zu zeigen, wie man Zeilendaten in ein NumPy ndarray mithilfe von Aspose.Cells für Python via .NET exportiert:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Holen Sie das Zeilenobjekt anhand des Zeilenindex.
1. Konvertieren von Zeilendaten in ein NumPy-Array unter Verwendung der Aspose.Cells for Python Excel-Bibliothek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Row-to-NDArray.py" >}}

Das Ausgabenergebnis:
```
['Detroit' 'Central' '3074']
```

## **Wie man eine Spalte von Excel in ein NumPy-Array konvertiert**
Hier ist ein Beispiel-Code-Schnipsel, um zu demonstrieren, wie man Spaltendaten in ein NumPy-Array exportiert, indem man Aspose.Cells for Python via .NET verwendet:
1. Laden Sie die [Beispieldatei](sample_data.xlsx).
1. Holen Sie sich das erste Arbeitsblatt.
1. Holen Sie das Spaltenobjekt nach Spaltenindex.
1. Konvertieren von Spaltendaten in ein NumPy-Array unter Verwendung der Aspose.Cells for Python Excel-Bibliothek.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Convert-Column-to-NDArray.py" >}}

Das Ausgabenergebnis:
```
['Store' '3055' '3036' '3074']
```
