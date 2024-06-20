---
title: Aggiorna automaticamente l oggetto OLE tramite Microsoft Excel utilizzando Aspose.Cells
type: docs
weight: 270
url: /it/net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**OleObject.AutoLoad**](https://reference.aspose.com/cells/net/aspose.cells.drawing/oleobject/properties/autoload) per aggiornare l'oggetto OLE quando il file Excel viene aperto in Microsoft Excel. Grazie a questa proprietà, l'oggetto OLE visualizzerà l'immagine OLE corretta generata da Microsoft Excel.

{{% /alert %}}

Il seguente codice di esempio carica il [file Excel di esempio](5115231.xlsx) che contiene un'immagine OLE non reale. L'oggetto OLE è effettivamente un documento di Microsoft Word ma il file Excel di esempio mostra l'immagine dell'animale invece dell'immagine di Microsoft Word. Ma se si apre il [file Excel di output](5115225.xlsx), si vedrà che Microsoft Excel mostra l'immagine OLE corretta.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-OLE-RefreshOLEObjects-1.cs" >}}
