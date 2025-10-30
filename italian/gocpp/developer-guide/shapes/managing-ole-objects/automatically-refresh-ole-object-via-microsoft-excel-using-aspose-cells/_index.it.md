---
title: Aggiorna automaticamente l oggetto OLE tramite Microsoft Excel con Golang tramite C++
linktitle: Aggiorna automaticamente l oggetto OLE
type: docs
weight: 270
url: /it/go-cpp/automatically-refresh-ole-object-via-microsoft-excel-using-aspose-cells/
description: Impara come aggiornare automaticamente gli oggetti OLE in Microsoft Excel usando Aspose.Cells con Golang tramite C++.
---

{{% alert color="primary" %}}

Aspose.Cells fornisce la proprietà [**OleObject.GetAutoLoad()**](https://reference.aspose.com/cells/go-cpp/oleobject/getautoload/) per aggiornare l'oggetto OLE quando il file Excel viene aperto in Microsoft Excel. Grazie a questa proprietà, l'oggetto OLE mostrerà l'immagine OLE corretta generata da Microsoft Excel.

{{% /alert %}}

Il codice di esempio seguente carica il [file Excel di esempio](5115231.xlsx) che contiene un'immagine OLE non reale. L'oggetto OLE è in realtà un documento Microsoft Word, ma il file Excel di esempio mostra invece l'immagine dell'animale. Tuttavia, se apri il [file Excel di output](5115225.xlsx), vedrai che Microsoft Excel visualizza l'immagine OLE corretta.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AutomaticallyRefreshOleObjectViaMicrosoftExcelUsingAsposeCells.go" >}}
