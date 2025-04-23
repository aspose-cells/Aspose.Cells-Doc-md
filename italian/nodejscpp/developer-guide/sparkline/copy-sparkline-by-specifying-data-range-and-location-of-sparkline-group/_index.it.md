---  
title: Copia Sparkline specificando l intervallo di dati e la posizione del gruppo di sparklines con Node.js tramite C++  
linktitle: Copia Sparkline specificando intervallo dati e posizione del gruppo di Sparkline  
type: docs  
weight: 300  
url: /it/nodejs-cpp/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/  
description: Impara come copiare uno sparkline in Excel specificando l intervallo di dati e la posizione del gruppo di sparklines usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
Microsoft Excel consente di copiare una linea di tendenza specificando l'intervallo di dati e la posizione di un gruppo di linee di tendenza. Aspose.Cells supporta questa funzionalità  
{{% /alert %}}  

Per copiare una linea di tendenza in altre celle in Microsoft Excel  

1. Selezionare la cella contenente la linea di tendenza  
1. Selezionare **Modifica dati** dalla sezione **Linee di tendenza** della scheda **Progettazione**  
1. Selezionare **Modifica posizione gruppo e dati**  
1. Specificare l'intervallo di dati e la posizione  
1. Fai clic su **OK**.  

Aspose.Cells fornisce il metodo `SparklineCollection.add(dataRange, riga, colonna)` per specificare l'intervallo di dati e la posizione di un gruppo di sparklines. Il seguente esempio di codice carica il file excel di origine come mostrato nello screenshot sopra, poi accede al primo gruppo di sparklines e aggiunge intervalli di dati e posizioni nel gruppo di sparklines. Infine, scrive il file excel di output su disco, come mostrato sopra nello screenshot.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "copy_sparkline.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access the first sparkline group
const group = worksheet.getSparklineGroups().get(0);

// Add Data Ranges and Locations inside this sparkline group
group.getSparklines().add("Sheet1!D5:O5", 4, 15);
group.getSparklines().add("Sheet1!D6:O6", 5, 15);
group.getSparklines().add("Sheet1!D7:O7", 6, 15);
group.getSparklines().add("Sheet1!D8:O8", 7, 15);

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

