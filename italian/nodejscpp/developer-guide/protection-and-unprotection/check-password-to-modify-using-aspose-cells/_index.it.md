---  
title: Verifica password per modificare usando Aspose.Cells for Node.js via C++  
linktitle: Verifica password per modificare  
type: docs  
weight: 2400  
url: /it/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: Impara come verificare se una password per modificare corrisponde usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
A volte, è necessario verificare se la password fornita corrisponde alla **Password per modificare** programmaticamente. Aspose.Cells offre il metodo `WorkbookSettings.writeProtection.validatePassword()` che puoi usare per verificare se la Password per modificare è corretta o meno.  
{{% /alert %}}  

## **Verificare la password per modificare in Microsoft Excel**  

È possibile assegnare **Password per aprire** e **Password per modificare** durante la creazione dei propri workbook in Microsoft Excel. Si prega di vedere questa schermata che mostra l'interfaccia fornita da Microsoft Excel per specificare queste password.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **Verifica password per modificare usando Aspose.Cells for Node.js via C++**  

Gli esempi di codice caricanno il [file Excel di origine](5112232.xlsx). Ha una Password di apertura 1234 e una Password di modifica 5678. Il codice verifica prima se 567 è la password corretta per modificare, restituendo false, e poi verifica se 5678 è corretta, restituendo true.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **Output della console**  

Ecco l'output della console del codice di esempio precedente dopo aver caricato il [file Excel di origine](5112232.xlsx).  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
