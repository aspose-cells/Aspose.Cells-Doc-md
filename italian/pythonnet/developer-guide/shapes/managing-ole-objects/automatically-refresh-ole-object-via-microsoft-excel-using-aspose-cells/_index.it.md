---
title: Aggiorna automaticamente l oggetto OLE
type: docs
weight: 270
url: /it/python-net/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
---

{{% alert color="primary" %}}

Aspose.Cells per Python via .NET fornisce la proprietà [**OleObject.auto_load**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/oleobject/auto_load) per aggiornare l'oggetto OLE quando il file Excel viene aperto in Microsoft Excel. Grazie a questa proprietà, l'oggetto OLE mostrerà l'immagine OLE corretta generata da Microsoft Excel.

{{% /alert %}}

Il seguente codice di esempio carica il [file Excel di esempio](5115231.xlsx) che contiene un'immagine OLE non reale. L'oggetto OLE è effettivamente un documento di Microsoft Word ma il file Excel di esempio mostra l'immagine dell'animale invece dell'immagine di Microsoft Word. Ma se si apre il [file Excel di output](5115225.xlsx), si vedrà che Microsoft Excel mostra l'immagine OLE corretta.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-OLE-RefreshOLEObjects-1.py" >}}
