---
title: Alle versteckten Zeilenindizes nach dem Aktualisieren des Autofilters abrufen.
type: docs
weight: 320
url: /de/python-net/get-all-hidden-rows-indices-after-refreshing-autofilter/
description: Lernen Sie, wie Sie nach dem Aktualisieren des AutoFilters mit der Aspose.Cells für Python via .NET API alle versteckten Zeilenindizes erhalten
keywords: Python Excel Bibliothek, Python Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters erhalten, Python Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters erhalten, Python Verdeckte Zeilenindizes nach Aktualisierung des AutoFilters erhalten
---

## **Mögliche Verwendungsszenarien**

Wenn Sie den AutoFilter auf Arbeitsblattzellen anwenden, werden einige der Zeilen automatisch ausgeblendet. Es kann jedoch sein, dass einige der Zeilen bereits manuell vom Excel-Benutzer ausgeblendet wurden und nicht vom AutoFilter ausgeblendet wurden. Daher ist es schwierig zu wissen, welche der Zeilen vom AutoFilter ausgeblendet sind und welche vom Excel-Benutzer manuell ausgeblendet wurden. Aspose.Cells für Python via .NET behandelt dieses Problem mit der Methode [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool). Diese Methode gibt die Zeilenindizes aller Zeilen zurück, die vom AutoFilter ausgeblendet und nicht manuell vom Excel-Benutzer ausgeblendet wurden.

## **Alle versteckten Zeilenindizes nach Aktualisierung des AutoFilters abrufen**

Bitte beachten Sie den folgenden Beispielcode, der die [Beispiel-Excel-Datei](64716909.xlsx) lädt, die einige der Zeilen enthält, die vom Excel-Benutzer manuell ausgeblendet wurden. Der Code wendet den AutoFilter an und aktualisiert ihn mit der Methode [**AutoFilter.refresh(hide_rows)**](https://reference.aspose.com/cells/python-net/aspose.cells/autofilter/refresh/#bool), die die Zeilenindizes aller versteckten Zeilen durch den AutoFilter zurückgibt. Anschließend werden die Indizes der versteckten Zeilen zusammen mit Zellennamen und -werten auf der Konsole ausgegeben.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Data-GetAllHiddenRowsIndicesAfterRefreshingAutoFilter.py" >}}

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
{{< app/cells/assistant language="python-net" >}}
