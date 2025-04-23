---
title: Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird
type: docs
weight: 880
url: /de/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---

{{% alert color="primary" %}} 

Aspose.Cells bietet die Eigenschaft [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible), die Sie verwenden können, um anzugeben, ob die Pivot-Tabelle beim Aktualisieren der Pivot-Tabelle für Excel2003 kompatibel ist. Wenn **true**, muss ein String kleiner oder gleich 255 Zeichen sein. Ist der String länger als 255 Zeichen, wird er abgeschnitten. Wenn **false**, hat ein String keine restriktion. Der Standardwert ist **true**.

{{% /alert %}} 
## **Geben Sie an, ob das PivotTable für Excel2003 kompatibel ist, während das PivotTable aktualisiert wird**
Der folgende Beispielcode erläutert die Verwendung der Eigenschaft [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible). Der Original-String ist 383 Zeichen lang. Aber wenn die Eigenschaft [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) auf **true** gesetzt ist und die Pivot-Tabelle aktualisiert wird, wird die Datenzelle B5 der Pivot-Tabelle abgeschnitten und sie wird 255 Zeichen lang. Wenn die Eigenschaft [PivotTable.IsExcel2003Compatible](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) auf **false** gesetzt ist und die Pivot-Tabelle erneut aktualisiert wird, wird die Datenzelle B5 der Pivot-Tabelle nicht abgeschnitten und bleibt 383 Zeichen lang. Laden Sie bitte die [Beispiel-Excel-Datei](5472558.xlsx) für diesen Code, die von ihm generierte [Ausgabedatei](5472557.xlsx) und deren Konsolenausgabe für Ihre Referenz herunter. Bitte lesen Sie auch die Kommentare im Code für ein besseres Verständnis dieser Eigenschaft.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit der angegebenen [Beispiel-Excel-Datei](5472558.xlsx) ausgeführt wird.



{{< highlight java >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
