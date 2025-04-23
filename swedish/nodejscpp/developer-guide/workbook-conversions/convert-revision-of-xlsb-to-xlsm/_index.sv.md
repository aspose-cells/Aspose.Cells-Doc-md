---  
title: Konvertera revision av XLSB till XLSM med Node.js via C++  
linktitle: Konvertera revision av XLSB till XLSM  
type: docs  
weight: 290  
url: /sv/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/  
description: Lär dig hur du helt konverterar revisioner av XLSB filer till XLSM format med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Aspose.Cells stödjer nu fullständig konvertering av revisioner av XLSB-filer till XLSM-filer. Revisionerna finns i vägen \xl\revisions. Du kan visa dem genom att byta ut din XLSB-filändelse till ZIP. Vägen \xl\revisions innehåller filer som slutar med .bin-extensioner.  

När du konverterar din XLSB-fil till en XLSM-fil med Aspose.Cells, konverteras dessa .bin-filer till framgångsrikt till .xml-filer, som visas i dessa två skärmbilder.  

{{% /alert %}}  

Följande kodexempel visar hur du konverterar XLSB-filen till XLSM-format med Aspose.Cells for Node.js via C++.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsb");

// Open workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save Workbook to XLSM format
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```  

