---
title: Alle versteckten Zeilen nach dem Aktualisieren des AutoFilters mit Golang via C++ ermitteln
linktitle: Alle versteckten Zeilenindizes nach dem Aktualisieren des Autofilters abrufen.
type: docs
weight: 320
url: /de/go-cpp/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Erfahren Sie, wie Sie alle versteckten Zeilen nach der Aktualisierung des AutoFilters mithilfe der API Aspose.Cells for C++ ermitteln.
keywords: Erhalten Sie alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters, Alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters erhalten, Alle versteckten Zeilenindizes nach dem Aktualisieren des AutoFilters abrufen
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den Autofilter auf Zellen des Arbeitsblattes anwenden, werden einige der Zeilen automatisch ausgeblendet. Es könnte jedoch sein, dass einige der Zeilen bereits manuell vom Excel-Endbenutzer ausgeblendet wurden und nicht vom Autofilter ausgeblendet sind. Daher ist es schwierig zu wissen, welche der Zeilen vom Autofilter ausgeblendet sind und welche manuell vom Excel-Endbenutzer ausgeblendet wurden. Aspose.Cells behandelt dieses Problem mit der Methode int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/). Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die vom Autofilter ausgeblendet und nicht manuell vom Excel-Endbenutzer ausgeblendet wurden.

## **Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen**

Bitte sehen Sie sich den folgenden Beispielscode an, der die [Beispieldatei Excel](64716909.xlsx) lädt, die einige Zeilen enthält, die vom Excel-Endbenutzer manuell ausgeblendet wurden. Der Code wendet den Autofilter an und aktualisiert ihn mit der Methode int[] [**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/go-cpp/autofilter/refresh/), die die Zeilenindizes aller ausgeblendeten Zeilen durch den Autofilter zurückgibt. Anschließend werden die Indizes der ausgeblendeten Zeilen zusammen mit Zellennamen und Werten auf der Konsole ausgegeben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetAllHiddenRowsIndicesAfterRefreshingAutofilter.go" >}}
## **Konsolenausgabe**

{{< highlight java >}}

Printing Rows Indices, Cell Names and Values Hidden By AutoFilter.

\--------------------------

1       A2      Apple

2       A3      Apple

3       A4      Apple

6       A7      Apple

7       A8      Apple

11      A12     Pear

12      A13     Pear

{{< /highlight >}}
