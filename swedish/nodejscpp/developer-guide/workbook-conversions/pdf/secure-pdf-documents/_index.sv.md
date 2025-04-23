---
title: Säkra PDF dokument med Node.js via C++
linktitle: Säkra PDF dokument
type: docs
weight: 120
url: /sv/nodejs-cpp/secure-pdf-documents/
description: Lär dig hur du säkrar PDF dokument med ägar och användarlösenord och sätter behörigheter för PDF filer med Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Ibland behöver utvecklare arbeta med krypterade PDF-filer. Till exempel:

- Säkra dokumenten med ägar- och användarlösenord så att inte vem som helst kan öppna dem.
- Ange begränsningar eller behörigheter för dokumentet efter att dokumentet har öppnats. t.ex. begränsa om dokumentinnehållet kan skrivas ut eller extraheras.

Den här artikeln förklarar hur man skickar in PDF-säkerhetsalternativ när man sparar kalkylblad till PDF.

{{% /alert %}}

Aspose.Cells tillhandahåller [**PdfSecurityOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/) för att arbeta med säkerhet. Du kan ange ägar- och användarlösenord vid sparning till PDF. Ägarlösenord eller användarlösenord krävs för att öppna den krypterade PDF-dokumentet för visning.

- Användarlösenordet kan vara null eller en tom sträng; i så fall krävs inget lösenord av användaren när PDF-dokumentet öppnas.
- Att öppna PDF-dokumentet med rätt ägarlösenord ger full tillgång (utan några tillgångsrestriktioner angivna) till dokumentet.
- Öppning av PDF-dokumentet med det korrekta användarlösenordet (eller öppnande av ett dokument som inte har ett användarlösenord) tillåter begränsad åtkomst enligt de angivna behörigheterna.

Exempelkoden nedan beskriver hur du säkrar PDF:er med Aspose.Cells.

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

Om kalkylbladet innehåller formler är det bäst att anropa [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--) precis innan det renderas till PDF. Detta ser till att formelberoende värden omberäknas och de korrekta värdena renderas i PDF-filen.

{{% /alert %}}
