---
title: Ricezione di notifiche durante l'unione dei dati con i marcatori intelligenti
type: docs
weight: 20
url: /it/net/getting-notifications-while-merging-data-with-smart-markers/
---
{{% alert color="primary" %}} 

 Aspose.Cells Le API forniscono il[Workbook Designer](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) classe a[lavorare con gli Smart Marker](https://docs.aspose.com/cells/net/smart-markers/) dove la formattazione e le formule sono inserite nel file[fogli di calcolo del progettista](/cells/it/net/what-is-a-designer-spreadsheet/) e poi elaborato con[Workbook Designer](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner) class per riempire i dati in base agli Smart Marker specificati. A volte, potrebbe essere necessario ricevere le notifiche sul riferimento della cella o sul particolare Smart Marker in fase di elaborazione. Ciò può essere ottenuto utilizzando il[WorkbookDesigner.CallBack](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/properties/callback) proprietà e[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interfaccia esposta con il rilascio di Aspose.Cells for .NET 8.6.2.

{{% /alert %}} 

 La parte di codice seguente illustra l'utilizzo di[ISmartMarkerCallBack](https://reference.aspose.com/cells/net/aspose.cells/ismartmarkercallback) interface per definire una nuova classe che gestisce la richiamata per[WorkbookDesigner.Process](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner/methods/process)metodo.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-ISmartMarkerCallBack.cs" >}}



 Il resto del processo include il caricamento del foglio di calcolo del designer contenente gli Smart Marker con[Workbook Designer](https://reference.aspose.com/cells/net/aspose.cells/workbookdesigner)ed elaborarlo impostando l'origine dati. Per semplificare l'esempio, abbiamo utilizzato un foglio di calcolo predefinito contenente solo due Smart Marker, come mostrato nell'istantanea sottostante, in cui l'origine dati viene creata dinamicamente per unire i dati in base agli Smart Marker specificati.

|![cose da fare:immagine_alt_testo](getting-notifications-while-merging-data-with-smart-markers_1.png)|
|:- |
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetSmartMarkerNotifications-1.cs" >}}
