---
title: Rufen Sie nach dem Aktualisieren von AutoFilter alle Indizes für ausgeblendete Zeilen ab
type: docs
weight: 320
url: /de/net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Erfahren Sie, wie Sie alle ausgeblendeten Zeilenindizes nach der Aktualisierung von AutoFilter mithilfe von Aspose.Cells for .NET API abrufen.
keywords: Get All Hidden Rows Indices after Refreshing AutoFilter, Obtain All Hidden Rows Indices after Refreshing AutoFilter, Retrieve All Hidden Rows Indices after Refreshing AutoFilter
---
##  **Mögliche Nutzungsszenarien**

Wenn Sie den automatischen Filter auf Arbeitsblattzellen anwenden, werden einige Zeilen automatisch ausgeblendet. Es kann jedoch vorkommen, dass einige der Zeilen vom Excel-Endbenutzer bereits manuell ausgeblendet wurden und nicht durch einen automatischen Filter ausgeblendet werden. Daher ist es schwierig zu erkennen, welche Zeilen vom automatischen Filter ausgeblendet werden und welche vom Excel-Endbenutzer manuell ausgeblendet werden. Aspose.Cells behandelt dieses Problem mithilfe des int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)Methode. Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die vom automatischen Filter und nicht manuell vom Excel-Endbenutzer ausgeblendet werden.

##  **Rufen Sie nach dem Aktualisieren von AutoFilter alle Indizes für ausgeblendete Zeilen ab**

 Bitte sehen Sie sich den folgenden Beispielcode an, der das lädt[Beispiel-Excel-Datei](64716909.xlsx) die einige der vom Excel-Endbenutzer manuell ausgeblendeten Zeilen enthält. Der Code wendet den automatischen Filter an und aktualisiert ihn mithilfe von int[][**AutoFilter.Refresh(bool hideRows)**](https://reference.aspose.com/cells/net/aspose.cells.autofilter/refresh/methods/1)Methode, die die Zeilenindizes aller vom automatischen Filter ausgeblendeten Zeilen zurückgibt. Anschließend werden die Indizes der ausgeblendeten Zeilen zusammen mit den Zellnamen und -werten auf der Konsole gedruckt.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.cs" >}}

##  **Konsolenausgabe**

{{< highlight "java" >}}

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
