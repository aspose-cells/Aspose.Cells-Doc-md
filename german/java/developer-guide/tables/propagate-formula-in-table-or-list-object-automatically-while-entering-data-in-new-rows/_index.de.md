---
title: Formel in Tabelle oder List Objekt automatisch propagieren, während neue Zeilen eingegeben werden
type: docs
weight: 980
url: /de/java/propagate-formula-in-table-or-list-object-automatically-while-entering-data-in-new-rows/
---

## **Mögliche Verwendungsszenarien**
Manchmal möchten Sie, dass sich eine Formel in Ihrer Tabelle oder Ihrem Listenobjekt automatisch auf neue Zeilen ausbreitet, während Sie neue Daten eingeben. Dies ist das Standardverhalten von Microsoft Excel. Um dasselbe mit Aspose.Cells zu erreichen, verwenden Sie bitte die [ListColumn.Formula](https://reference.aspose.com/cells/java/com.aspose.cells/listcolumn#Formel)-Eigenschaft.
## **Formel in Tabelle oder List-Objekt automatisch propagieren, während neue Zeilen eingegeben werden**
Der folgende Beispielcode erstellt eine Tabelle oder ein Listenobjekt so, dass die Formel in Spalte B automatisch auf neue Zeilen ausbreitet, wenn Sie neue Daten eingeben. Bitte überprüfen Sie die mit diesem Code generierte [Ausgabe-Excel-Datei](5472519.xlsx). Wenn Sie eine beliebige Zahl in Zelle A3 eingeben, sehen Sie, dass die Formel in Zelle B2 automatisch auf Zelle B3 ausbreitet.
## **Beispielcode**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-PropagateFormulaInTableorListObject-PropagateFormulaInTableorListObject.java" >}}
{{< app/cells/assistant language="java" >}}
