---
title: Benachrichtigungen erhalten, während Daten mit Smart Markern zusammengeführt werden
type: docs
weight: 20
url: /de/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells APIs bieten die[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) Klasse zu[Arbeiten Sie mit Smart Markern](https://docs.aspose.com/cells/net/smart-markers/) wo die Formatierungen und Formeln platziert werden[Designer-Tabellen](/cells/de/net/what-is-a-designer-spreadsheet/) und dann mit verarbeitet[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) Klasse, um die Daten gemäß den angegebenen Smart Markern aufzufüllen. Manchmal kann es erforderlich sein, Benachrichtigungen über den Zellbezug oder den bestimmten Smart Marker zu erhalten, der verarbeitet wird. Dies kann mit der erreicht werden[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) Eigentum und[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) Schnittstelle ausgesetzt mit der Veröffentlichung von Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

 Der folgende Codeabschnitt demonstriert die Verwendung von[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) -Schnittstelle, um eine neue Klasse zu definieren, die den Rückruf verarbeitet[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)Methode.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 Der Rest des Prozesses umfasst das Laden der Designer-Tabelle mit den Smart Markers[WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)und verarbeiten Sie es, indem Sie die Datenquelle festlegen. Um das Beispiel einfach zu halten, haben wir ein vordefiniertes Designer-Arbeitsblatt verwendet, das nur zwei Smart Marker enthält, wie im folgenden Schnappschuss gezeigt, wo die Datenquelle dynamisch erstellt wird, um die Daten gemäß den angegebenen Smart Markern zusammenzuführen.

|![todo: Bild_alt_Text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
