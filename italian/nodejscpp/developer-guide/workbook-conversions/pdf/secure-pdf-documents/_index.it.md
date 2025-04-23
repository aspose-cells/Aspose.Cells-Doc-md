---
title: Doc PDF sicuri con Node.js tramite C++
linktitle: Documenti PDF sicuri
type: docs
weight: 120
url: /it/nodejs-cpp/secure-pdf-documents/
description: Impara come proteggere i documenti PDF usando password proprietario e utente, e impostare permessi sui file PDF usando Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

A volte, gli sviluppatori devono lavorare con file PDF criptati. Ad esempio:

- Proteggere i documenti con password per proprietario e utente in modo che non possa aprirlo chiunque.
- Impostare restrizioni o autorizzazioni al documento dopo l'apertura del documento, ad esempio limitare se È possibile stampare o estrarre il contenuto del documento.

Questo articolo spiega come passare le opzioni di sicurezza PDF durante il salvataggio dei fogli di calcolo in PDF.

{{% /alert %}}

Aspose.Cells fornisce [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) per lavorare sulla sicurezza. Puoi impostare password proprietarie e utente durante il salvataggio in PDF. La password proprietaria o la password utente sarà richiesta per aprire il documento PDF criptato per la visualizzazione.

- La password utente può essere nulla o una stringa vuota; in questo caso, non verrà richiesta password dall'utente all'apertura del documento PDF.
- Aprire il documento PDF con la corretta password proprietaria consente l'accesso completo (senza restrizioni di accesso specificate) al documento.
- L'apertura del documento PDF con la corretta password dell'utente (o l'apertura di un documento che non ha una password utente) consente l'accesso limitato come le autorizzazioni specificate.

Il codice di esempio qui sotto descrive come proteggere i PDF con Aspose.Cells.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "input.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const saveOption = new AsposeCells.PdfSaveOptions();
saveOption.setSecurityOptions(new AsposeCells.PdfSecurityOptions());

saveOption.getSecurityOptions().setUserPassword("user");
saveOption.getSecurityOptions().setOwnerPassword("owner");
saveOption.getSecurityOptions().setExtractContentPermission(false);
saveOption.getSecurityOptions().setPrintPermission(false);

workbook.save(path.join(dataDir, "securepdf_test.out.pdf"), saveOption);
```

{{% alert color="primary" %}}

Se il foglio di calcolo contiene formule, è meglio chiamare [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) proprio prima di renderlo in PDF. Ciò garantisce che i valori dipendenti dalle formule vengano ricalcolati e i valori corretti siano resi nel PDF.

{{% /alert %}}
