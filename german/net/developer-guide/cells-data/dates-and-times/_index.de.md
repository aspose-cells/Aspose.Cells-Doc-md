---
title: So verwalten Sie Datum und Uhrzeit
type: docs
weight: 600
url: /de/net/how-to-manage-dates-and-times/
description: Erfahren Sie, wie Sie Datum und Uhrzeit unter Aspose.Cells for .NET API verwalten.
keywords: How to Manage Dates and Times, The 1900 date system, The 1904 date system, Set Dates and Times, Get Dates and Times, Manage Dates and Times, Store Dates and Times in Excel, Display Dates and Times in Cells.
---
##  **So speichern Sie Datums- und Uhrzeitangaben in Excel**
Datums- und Uhrzeitangaben werden in Zellen als Zahlen gespeichert. Daher sind die Werte von Zellen, die Datums- und Uhrzeitangaben enthalten, vom numerischen Typ. Eine Zahl, die ein Datum und eine Uhrzeit angibt, besteht aus den Komponenten Datum (ganzzahliger Teil) und Uhrzeit (Bruchteil). Die Eigenschaft Cell.DoubleValue gibt diese Zahl zurück.

##  **So zeigen Sie Datum und Uhrzeit in Aspose.Cells an**
Um eine Zahl als Datum und Uhrzeit anzuzeigen, wenden Sie über das das erforderliche Datums- und Uhrzeitformat auf eine Zelle an[Stil.Nummer](https://reference.aspose.com/cells/net/aspose.cells/style/number/) oder[Stil.Benutzerdefiniert]() Eigentum. Die CellValue.DateTimeValue-Eigenschaft gibt das DateTime-Objekt zurück, das das Datum und die Uhrzeit angibt, die durch die in einer Zelle enthaltene Zahl dargestellt werden.
<br>
<image src="1.png" width="70%" />

##  **So wechseln Sie zwei Datumssysteme in Aspose.Cells**
MS-Excel speichert Datumsangaben als Zahlen, die als serielle Werte bezeichnet werden. Ein serieller Wert ist eine Ganzzahl, die die Anzahl der verstrichenen Tage seit dem ersten Tag im Datumssystem angibt. Excel unterstützt die folgenden Datumssysteme für serielle Werte:

1. Das Datumssystem von 1900. Das erste Datum ist der 1. Januar 1900 und sein fortlaufender Wert ist 1. Das letzte Datum ist der 31. Dezember 9999 und sein fortlaufender Wert ist 2.958.465. Dieses Datumssystem wird standardmäßig in der Arbeitsmappe verwendet.
1.  Das Datumssystem von 1904. Das erste Datum ist der 1. Januar 1904 und sein fortlaufender Wert ist 0. Das letzte Datum ist der 31. Dezember 9999 und sein fortlaufender Wert ist 2.957.003. Um dieses Datumssystem in der Arbeitsmappe zu verwenden, legen Sie fest[Arbeitsmappe.Einstellungen.Datum1904](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/date1904/) Eigenschaft zu wahr.


Dieses Beispiel zeigt, dass die zum gleichen Datum in verschiedenen Datumssystemen gespeicherten Serienwerte unterschiedlich sind.
{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Datetime-1904.cs" >}}
Ausgabeergebnis:
```
A1 is Numeric Value: 45253
use The 1904 date system====================
A2 is Numeric Value: 43791
```

##  **So legen Sie den DateTime-Wert in Aspose.Cells fest**
In diesem Beispiel wird ein DateTime-Wert in den Zellen A1 und A2 festgelegt, das benutzerdefinierte Format A1 und das Zahlenformat A2 festgelegt und anschließend die Werttypen ausgegeben.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Set-Datetime.cs" >}}

Ausgabeergebnis:
```
A1 is Numeric Value: True
Cell A1 contains a DateTime value.
A2 is Numeric Value: True
Cell A2 contains a DateTime value.
```

##  **So erhalten Sie den DateTime-Wert in Aspose.Cells**
In diesem Beispiel wird ein DateTime-Wert in den Zellen A1 und A2 festgelegt, das benutzerdefinierte Format A1 und das Zahlenformat A2 festgelegt, die Werttypen von zwei Zellen überprüft und dann der DateTime-Wert und die formatierte Zeichenfolge ausgegeben.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Cells-Get-Datetime.cs" >}}

Ausgabeergebnis:
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
