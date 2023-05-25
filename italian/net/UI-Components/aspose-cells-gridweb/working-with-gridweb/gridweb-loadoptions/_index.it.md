---
title: LoadOptions per GridWeb
type: docs
weight: 90
url: /it/net/aspose-cells-gridweb/loadoptions/
keywords: loadoption,loadoptions,setting,
---
{{% alert color="primary" %}} 

Ci sono alcune opzioni di caricamento che possiamo impostare prima di importare il file.

 possiamo usare[GridLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridloadoptions/)(per file generale) e[GridTxtLoadOptions](https://reference.aspose.com/cells/net/aspose.cells.gridweb.data/gridtxtloadoptions/) (per file csv)
 
{{% /alert %}} 
##  ** caricare con altra codifica**
Per il file csv, è in realtà un file basato su testo, senza la codifica specifica descritta nel file in formato xlsx.

Pertanto, gli utenti possono impostare una codifica dei caratteri specifica prima di caricare il file.

ecco un esempio di codice da caricare con il cinese:

```csharp
    GridTxtLoadOptions topt = new GridTxtLoadOptions();
    topt.Encoding = (Encoding.GetEncoding("GB2312"));
    GridWeb1.LoadOptions = topt;
    String filePath = Server.MapPath("~/workbook/chinesefile.csv");
    GridWeb1.ImportExcelFile(filePath);
```