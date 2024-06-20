---
title: Benachrichtigungen beim Zusammenführen von Daten mit Smart Markern erhalten
type: docs
weight: 20
url: /de/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Die Aspose.Cells APIs bieten die [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)-Klasse, um mit [Smart Markers](https://docs.aspose.com/cells/net/smart-markers/) zu arbeiten, wo die Formatierung und Formeln in den [Designer-Arbeitsblättern](/cells/de/net/what-is-a-designer-spreadsheet/) platziert und dann mit der [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)-Klasse verarbeitet werden, um die Daten gemäß der festgelegten Smart Markers einzufüllen. Manchmal ist es erforderlich, Benachrichtigungen über den Zellbezug oder den bestimmten Smart Marker, der verarbeitet wird, zu erhalten. Dies kann mithilfe der [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback)-Eigenschaft und des über die Version Aspose.Cells for .NET 8.6.2 bereitgestellten [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback)-Interface erreicht werden.

{{% /alert %}} 

Der folgende Codeausschnitt zeigt die Verwendung des [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) Interfaces, um eine neue Klasse zu definieren, die den Rückruf für die [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process) Methode behandelt.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



Der restliche Prozess umfasst das Laden des Designer-Arbeitsblatts mit den Smart Markern mit [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) und die Verarbeitung durch Festlegen der Datenquelle. Um das Beispiel einfach zu halten, haben wir ein vordefiniertes Designer-Arbeitsblatt mit nur zwei Smart Markern verwendet, wie im folgenden Schnappschuss gezeigt, wobei die Datenquelle dynamisch erstellt wird, um die Daten gemäß den angegebenen Smart Markern zusammenzuführen.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
