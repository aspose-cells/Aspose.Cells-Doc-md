---
title: Wie man Daten und Zeiten verwaltet
type: docs
weight: 600
url: /de/python-net/how-to-manage-dates-and-times/
description: Erfahren Sie, wie man Daten und Zeiten durch die API Aspose.Cells for .NET verwaltet.
keywords: Wie man Daten und Zeiten verwaltet, das 1900 Datensystem, das 1904 Datensystem, Daten und Zeiten setzen, Daten und Zeiten abrufen, Daten und Zeiten verwalten, Daten und Zeiten in Excel speichern, Daten und Zeiten in Zellen anzeigen.
---

## **Wie man Daten und Zeiten in Excel speichert**
Daten und Zeiten werden in Zellen als Zahlen gespeichert. Daher sind die Werte von Zellen, die Daten und Zeiten enthalten, vom numerischen Typ. Eine Zahl, die ein Datum und eine Uhrzeit angibt, besteht aus den Datum (Ganzzahlteil) und Uhrzeit (Bruchteilteil) Komponenten. Die Eigenschaft Cell.DoubleValue gibt diese Zahl zurück.

## **Wie man Daten und Zeiten in Aspose.Cells anzeigt**
Um eine Zahl als Datum und Uhrzeit anzuzeigen, wenden Sie das erforderliche Datums- und Uhrzeitformat an eine Zelle über die Eigenschaft [Style.Number](https://reference.aspose.com/cells/net/aspose.cells/style/number/) oder [Style.Custom]() an. Die Eigenschaft CellValue.DateTimeValue gibt das DateTime-Objekt zurück, das das Datum und die Uhrzeit angibt, die durch die in einer Zelle enthaltene Zahl dargestellt werden.
<br>
<image src="1.png" width="70%" />

## **Wie man zwischen zwei Datumsystemen in Aspose.Cells wechselt**
MS-Excel speichert Daten als Zahlen, die als Serienwerte bezeichnet werden. Ein Serienwert ist eine Ganzzahl, die die Anzahl der vergangenen Tage seit dem ersten Tag im Datensystem angibt. Excel unterstützt die folgenden Datensysteme für Serienwerte:

1. Das 1900-Datensystem. Das erste Datum ist der 1. Januar 1900 und sein Serienwert ist 1. Das letzte Datum ist der 31. Dezember 9999 und sein Serienwert beträgt 2.958.465. Dieses Datensystem wird standardmäßig in der Arbeitsmappe verwendet.
1. Das 1904-Datensystem. Das erste Datum ist der 1. Januar 1904 und sein Serienwert beträgt 0. Das letzte Datum ist der 31. Dezember 9999 und sein Serienwert beträgt 2.957.003. Um dieses Datensystem in der Arbeitsmappe zu verwenden, setzen Sie die Eigenschaft [Workbook.Settings.Date1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) auf true.


Dieses Beispiel zeigt, dass die in verschiedenen Datensystemen gespeicherten Serienwerte für dasselbe Datum unterschiedlich sind.
{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Datetime-1904.py" >}}
Ausgabenergebnis:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

## **So legen Sie den DateTime-Wert in Aspose.Cells fest**
Dieses Beispiel legt einen DateTime-Wert in Zelle A1 und A2 fest, legt ein benutzerdefiniertes Format für A1 und ein Zahlenformat für A2 fest und gibt dann die Werttypen aus.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Set-Datetime.py" >}}

Ausgabenergebnis:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

## **So erhalten Sie den DateTime-Wert in Aspose.Cells**
Dieses Beispiel legt einen DateTime-Wert in Zelle A1 und A2 fest, legt ein benutzerdefiniertes Format für A1 und ein Zahlenformat für A2 fest, überprüft die Werttypen von zwei Zellen und gibt dann den DateTime-Wert und den formatierten String aus.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-DatesAndTimes-Get-Datetime.py" >}}

Ausgabenergebnis:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A1 DateTime Value: 11/23/2023 5:59:09 PM
A1 DateTime String Value: 11-23-23 17:59:09
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
A2 DateTime Value: 11/23/2023 5:59:09 PM
A2 DateTime String Value: 11/23/2023 17:59
```
