---
title: Abrufen aller ausgeblendeten Zeilenindizes nach dem Aktualisieren von AutoFilter
type: docs
weight: 240
url: /de/java/get-all-hidden-rows-indices-after-refreshing-autofilter/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie einen automatischen Filter auf Arbeitsblattzellen anwenden, werden einige der Zeilen automatisch ausgeblendet. Es kann jedoch vorkommen, dass einige der Zeilen bereits manuell vom Excel-Endbenutzer ausgeblendet wurden und nicht vom automatischen Filter ausgeblendet werden. Es ist daher schwierig zu wissen, welche der Zeilen durch den automatischen Filter ausgeblendet werden und welche von ihnen manuell durch den Excel-Endbenutzer ausgeblendet werden. Aspose.Cells behandelt dieses Problem mit int[][**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean)) Methode. Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die vom automatischen Filter und nicht manuell vom Excel-Endbenutzer ausgeblendet wurden.

## **Abrufen aller ausgeblendeten Zeilenindizes nach dem Aktualisieren von AutoFilter**

Bitte sehen Sie sich den folgenden Beispielcode an, der die lädt[Beispiel-Excel-Datei](64716913.xlsx)die einige der Zeilen enthält, die vom Excel-Endbenutzer manuell ausgeblendet wurden. Der Code wendet den automatischen Filter an und aktualisiert ihn mit int[][**AutoFilter.refresh(bool hideRows)**](https://reference.aspose.com/cells/java/com.aspose.cells/autofilter#refresh(boolean))-Methode, die die Zeilenindizes aller ausgeblendeten Zeilen durch den automatischen Filter zurückgibt. Anschließend werden die Indizes der verborgenen Zeilen zusammen mit den Zellennamen und -werten auf der Konsole ausgegeben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.java" >}}

## **Konsolenausgabe**

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
