---
title: Opzioni di caricamento per GridWeb
type: docs
weight: 90
url: /it/net/aspose-cells-gridweb/aspose-cells-gridweb/loadoptions/
keywords: opzionedicaricamento, opzionedicaricamento, impostazione, carica, opzioni, opzione
description: Questo articolo introduce come lavorare con le opzioni di caricamento in GridWeb.
---

{{% alert color="primary" %}} 

Ci sono alcune opzioni di caricamento che possiamo impostare prima di importare il file.

Possiamo usare [GridLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridloadoptions/) (per file generico) e [GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose-cells-gridweb/aspose.cells.gridweb.data/gridtxtloadoptions/) (per file csv)	

{{% /alert %}} 
## **carica con altro codificare**
Per il file csv, è in realtà un file basato su testo, senza la codifica specifica descritta nel file di formato xlsx.

Pertanto, gli utenti possono impostare la codifica dei caratteri specifica prima di caricare il file.

Ecco un codice di esempio per caricare con il cinese:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```
