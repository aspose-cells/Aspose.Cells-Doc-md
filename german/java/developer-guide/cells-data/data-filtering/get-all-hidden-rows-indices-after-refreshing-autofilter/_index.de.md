---
title: Alle versteckten Zeilenindizes nach dem Aktualisieren des Autofilters abrufen.
type: docs
weight: 240
url: /de/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---

## **Mögliche Verwendungsszenarien**

Wenn Sie einen AutoFilter auf Arbeitsblattzellen anwenden, werden einige Zeilen automatisch ausgeblendet. Es könnte jedoch der Fall sein, dass einige der Zeilen bereits manuell vom Excel-Benutzer ausgeblendet wurden und nicht vom AutoFilter ausgeblendet werden. Es ist daher schwer zu wissen, welche der Zeilen vom AutoFilter ausgeblendet sind und welche vom Excel-Benutzer manuell ausgeblendet wurden. Aspose.Cells behandelt dieses Problem mit der Methode int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-). Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die vom Autofilter ausgeblendet und nicht manuell vom Excel-Benutzer ausgeblendet wurden.

## **Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen**

Bitte beachten Sie den folgenden Beispielcode, der die [Beispiel-Excel-Datei](64716913.xlsx) lädt, die einige der Zeilen enthält, die vom Excel-Benutzer manuell ausgeblendet wurden. Der Code wendet den Autofilter an und aktualisiert ihn unter Verwendung der Methode int[] [**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh-boolean-), die die Zeilenindizes aller versteckten Zeilen durch den Autofilter zurückgibt. Anschließend werden die Indizes der versteckten Zeilen mit den Zellennamen und Werten auf der Konsole ausgegeben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

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
{{< app/cells/assistant language="java" >}}
