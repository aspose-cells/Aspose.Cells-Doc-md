---
title: Aggiungi firma digitale a un file Excel già firmato con Node.js tramite C++
linktitle: Aggiungere firma digitale a un file Excel già firmato
type: docs
weight: 20
url: /it/nodejs-cpp/add-digital-signature-to-an-already-signed-excel-file/
description: Questo articolo descrive come aggiungere una firma digitale a un file Excel già firmato usando Node.js con Aspose.Cells for Node.js via C++.
keywords: Aggiungi firma digitale a un file Excel già firmato, come aggiungere una firma digitale a un documento Excel già firmato utilizzando Node.js tramite C++.
---

## **Possibili Scenari di Utilizzo**

Aspose.Cells for Node.js via C++ fornisce il metodo [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) che puoi usare per aggiungere una firma digitale a un file Excel già firmato.

{{% alert color="primary" %}}

Si prega di notare che durante l'aggiunta di una firma digitale a un documento Excel già firmato, se il documento originale è stato generato da Aspose.Cells, tutto funziona correttamente. Ma se il documento originale è stato generato da altri motori (es. Microsoft Excel), Aspose.Cells non può mantenere il file invariato dopo averlo caricato e risalvato, il che invalidarà la firma originale.

{{% /alert %}}

## **Come Aggiungere una Firma Digitale a un Documento Excel Già Firmato**

Il codice di esempio seguente dimostra come usare il metodo [**Workbook.addDigitalSignature(digitalSignatureCollection)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#addDigitalSignature-digitalSignatureCollection-) per aggiungere una firma digitale a un file Excel già firmato. Verifica il [file Excel di esempio](50528280.xlsx) usato in questo esempio. Questo file è già firmato digitalmente. Verifica il [file Excel di output](50528281.xlsx) generato dal codice. Nel codice abbiamo usato il certificato demo chiamato [AsposeDemo.pfx](50528279.pfx), con password **aspose**. La schermata mostra l'effetto del codice di esempio sul file Excel di esempio dopo l'esecuzione.

![todo:image_alt_text](add-digital-signature-to-an-already-signed-excel-file_1.png)

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

const dataDir = path.join(__dirname, "data");
// Certificate file path and password
const certFileName = path.join(dataDir, "AsposeDemo.pfx");
const password = "aspose";

// Load the workbook which is already digitally signed to add new digital signature
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleDigitallySignedByCells.xlsx"));

// Create the digital signature collection
const dsCollection = new AsposeCells.DigitalSignatureCollection();


// Create new digital signature and add it in digital signature collection
const signature = new AsposeCells.DigitalSignature(certFileName, password, "Aspose.Cells added new digital signature in existing digitally signed workbook.", new Date());
dsCollection.add(signature);

// Add digital signature collection inside the workbook
workbook.addDigitalSignature(dsCollection);

// Save the workbook and dispose of it.
workbook.save(path.join(__dirname, "outputDigitallySignedByCells.xlsx"));
workbook.dispose();
```
{{< app/cells/assistant language="nodejs-cpp" >}}
