---
title: Avskärma ett kalkblad med Node.js via C++
linktitle: Avskydda ett kalkylark
type: docs
weight: 20
url: /sv/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

Om en utvecklare behöver ta bort skydd från ett skyddat kalkylark vid körning så att vissa ändringar kan göras i filen? Detta kan enkelt göras med Aspose.Cells.

{{% /alert %}}

## **Avskydda ett kalkylblad**

### **Använda Microsoft Excel**

För att ta bort skydd från ett arbetsblad:

Från **Verktyg**-menyn, välj **Skydd** följt av **Avskärma blad**. Skyddet tas bort om kalkbladet inte är lösenordsskyddat. I så fall visas en dialog för att ange lösenordet. Ange lösenordet så är kalkbladet olåst.

### **Avskydda ett enkelt skyddat kalkylark med hjälp av Aspose.Cells**

Ett kalkblad kan avskärmas genom att anropa [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)-klassens [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)-metod. Ett enkelt skyddat kalkblad är ett som inte är lösenordsskyddat. Sådana kalkblad kan avskärmas genom att anropa [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)-metoden utan att passera in någon parameter.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **Avskydda ett lösenordsskyddat kalkylark med hjälp av Aspose.Cells**

Ett kalkblad som är lösenordsskyddat är ett som är skyddat med ett lösenord. Sådana kalkblad kan avskärmas genom att anropa en överlagrad version av [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--)-metoden som tar lösenordet som parameter.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
