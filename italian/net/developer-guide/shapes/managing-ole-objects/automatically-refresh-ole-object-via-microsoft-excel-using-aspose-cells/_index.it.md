---
title: Aggiorna automaticamente l'oggetto OLE tramite Microsoft Excel utilizzando Aspose.Cells
type: docs
weight: 270
url: /it/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---
{{% alert color="primary" %}}

 Aspose.Cells fornisce il[**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) proprietà per aggiornare l'oggetto OLE quando il file excel viene aperto in Microsoft Excel. A causa di questa proprietà, l'oggetto OLE visualizzerà l'immagine OLE corretta generata da Microsoft Excel.

{{% /alert %}}

 Il codice di esempio seguente carica il file[file excel di esempio](5115231.xlsx) che ha un'immagine OLE non reale. L'oggetto OLE è in realtà un documento di Microsoft Word, ma il file Excel di esempio mostra l'immagine dell'animale anziché l'immagine di Microsoft Word. Ma se apri il file[file excel di output](5115225.xlsx), vedrai che Microsoft Excel visualizza l'immagine OLE corretta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
