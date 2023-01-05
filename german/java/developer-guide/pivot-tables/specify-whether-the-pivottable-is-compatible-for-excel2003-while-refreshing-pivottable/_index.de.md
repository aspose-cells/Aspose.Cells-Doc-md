---
title: Geben Sie beim Aktualisieren der PivotTable an, ob die PivotTable mit Excel2003 kompatibel ist
type: docs
weight: 880
url: /de/java/specify-whether-the-pivottable-is-compatible-for-excel2003-while-refreshing-pivottable/
---
{{% alert color="primary" %}} 

 Aspose.Cells bietet die[PivotTable.IstExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible)-Eigenschaft, mit der Sie angeben können, ob die PivotTable beim Aktualisieren der PivotTable mit Excel2003 kompatibel ist. Wenn**wahr** , muss eine Zeichenfolge kleiner oder gleich 255 Zeichen sein. Wenn die Zeichenfolge also länger als 255 Zeichen ist, wird sie abgeschnitten. Wenn**FALSCH** , hat eine Zeichenfolge die oben genannte Einschränkung nicht. Der Standardwert ist**wahr**.

{{% /alert %}} 
## **Geben Sie beim Aktualisieren der PivotTable an, ob die PivotTable mit Excel2003 kompatibel ist**
 Der folgende Beispielcode erläutert die Verwendung von[PivotTable.IstExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) Eigentum. Die ursprüngliche Zeichenfolge ist 383 Zeichen lang. Aber wenn[PivotTable.IstExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) Eigenschaft eingestellt ist**wahr** und Pivot-Tabelle aktualisiert wird, werden die Daten der Zelle B5 der Pivot-Tabelle abgeschnitten und werden 255 Zeichen lang. Allerdings wann[PivotTable.IstExcel2003kompatibel](https://reference.aspose.com/cells/java/com.aspose.cells/pivottable#IsExcel2003Compatible) Eigenschaft eingestellt ist**FALSCH** und die Pivot-Tabelle erneut aktualisiert wird, werden die Daten der Zelle B5 der Pivot-Tabelle nicht abgeschnitten und bleiben 383 Zeichen lang. Bitte laden Sie die herunter[Excel-Beispieldatei](5472558.xlsx) in diesem Code verwendet,[Excel-Datei ausgeben](5472557.xlsx) generiert von ihm und seine Konsolenausgabe für Ihre Referenz. Bitte lesen Sie auch die Kommentare im Code, um diese Eigenschaft besser zu verstehen.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-utility-IsPivotTableCompatibleForExcel2003-.java" >}}
## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes, wenn er mit dem angegebenen ausgeführt wird[Excel-Beispieldatei](5472558.xlsx).



{{< highlight "java" >}}

 Length of original data string: 383

Length of cell B5 after setting IsExcel2003Compatible property to True: 255

Length of cell B5 after setting IsExcel2003Compatible property to False: 383

{{< /highlight >}}
