---
title: Ricezione di notifiche durante la fusione dei dati con Smart Markers
type: docs
weight: 20
url: /it/net/getting-notifications-while-merging-data-with-smart-markers/
---

{{% alert color="primary" %}} 

Le API Aspose.Cells forniscono la classe [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) per [lavorare con Smart Markers](https://docs.aspose.com/cells/net/smart-markers/) dove la formattazione e le formule vengono inserite nei [fogli di calcolo del designer](/cells/it/net/what-is-a-designer-spreadsheet/) e quindi processate con la classe [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) per riempire i dati in base ai Smart Markers specificati. A volte può essere necessario ricevere notifiche sul riferimento della cella o sul particolare Smart Marker in fase di elaborazione. Questo può essere ottenuto utilizzando la proprietà [WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) e l'interfaccia [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) esposta con il rilascio di Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

Il seguente frammento di codice dimostra l'uso dell'interfaccia [ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) per definire una nuova classe che gestisce il richiamo del metodo [WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



Il resto del processo include il caricamento del foglio di calcolo del designer contenente gli Smart Markers con [WorkbookDesigner](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) e il suo processamento impostando la sorgente dei dati. Per mantenere l'esempio semplice, è stato utilizzato un foglio di calcolo del designer predefinito contenente solo due Smart Markers come mostrato nella schermata sottostante, dove la sorgente dei dati viene creata dinamicamente per unire i dati in base agli Smart Markers specificati.

|![todo:image_alt_text](getting-notifications-while-merging-data-with-smart-markers_1.png)|
| :- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
