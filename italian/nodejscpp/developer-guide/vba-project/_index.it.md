---
title: Gestisci i codici VBA del workbook macro abilitato Excel
linktitle: Progetto macro
type: docs
weight: 200
url: /it/nodejs-cpp/manage-vba-project/
description: Aggiungi modulo VBA e modifica VBA o Macro con Aspose.Cells for Node.js via C++.
---

## **Aggiungi un modulo VBA in Node.js**
{{% alert color="primary" %}}

Aspose.Cells consente di aggiungere un nuovo modulo VBA e codice macro utilizzando Aspose.Cells for Node.js via C++. Si prega di usare il metodo [**Workbook.add(Worksheet)**](https://reference.aspose.com/cells/nodejs-cpp/vbamodulecollection/#add-worksheet-) per aggiungere il nuovo modulo VBA all'interno del workbook

{{% /alert %}}

Il seguente esempio di codice crea un nuovo workbook e aggiunge un nuovo modulo VBA e codice macro e salva l'output in formato XLSM. Una volta aperto il file XLSM in Microsoft Excel e cliccato sui comandi di menu **Sviluppatore > Visual Basic**, vedrai un modulo chiamato "TestModule" e al suo interno vedrai il seguente codice macro.

{{< highlight javascript >}}
Sub ShowMessage() {
    MsgBox "Welcome to Aspose!"
}
{{< /highlight >}}

Ecco il codice di esempio per generare il file XLSM di output con modulo VBA e codice macro.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create new workbook
const workbook = new AsposeCells.Workbook();

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Add VBA Module
const idx = workbook.getVbaProject().getModules().add(worksheet);

// Access the VBA Module, set its name and codes
const module = workbook.getVbaProject().getModules().get(idx);
module.setName("TestModule");

module.setCodes("Sub ShowMessage()" + "\r\n" +
"    MsgBox \"Welcome to Aspose!\"" + "\r\n" +
"End Sub");

// Save the workbook
workbook.save(path.join(dataDir, "output_out.xlsm"), AsposeCells.SaveFormat.Xlsm);
```

## **Modifica VBA o Macro in Node.js**

{{% alert color="primary" %}} 

Puoi modificare il codice VBA o Macro usando Aspose.Cells for Node.js via C++. Aspose.Cells ha aggiunto il seguente modulo e classi per leggere e modificare il progetto VBA nel file Excel.

- Aspose.Cells.Vba
- VbaProject
- VbaModuleCollection
- VbaModule

Questo articolo ti mostrerà come modificare il codice VBA o Macro all'interno del file Excel di origine usando Aspose.Cells.

{{% /alert %}} 

Il seguente esempio di codice carica il file Excel sorgente che contiene il codice VBA o Macro

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is test message."
}
{{< /highlight >}}

Dopo l'esecuzione del codice di esempio di Aspose.Cells, il codice VBA o Macro sarà modificato in questo modo

{{< highlight javascript >}}
Sub Button1_Click() {
    MsgBox "This is Aspose.Cells message."
}
{{< /highlight >}}

Puoi scaricare il [file Excel di origine](5112508.xlsm) e il [file Excel di output](5112511.xlsm) dai link forniti.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create workbook object from source Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsm"));

// Change the VBA Module Code
const modules = workbook.getVbaProject().getModules();
const moduleCount = modules.getCount();
for (let i = 0; i < moduleCount; i++) {
const module = modules.get(i);
const code = module.getCodes();
if (code.includes("This is test message.")) 
{
code = code.replace("This is test message.", "This is Aspose.Cells message.");
module.setCodes(code);
}
}


// Save the output Excel file
workbook.save(path.join(dataDir, "output_out.xlsm"));
```

## **Argomenti avanzati**
- [Aggiungi un riferimento alla libreria al progetto VBA nel foglio di lavoro](/cells/it/nodejs-cpp/add-a-library-reference-to-vba-project-in-workbook/)
- [Assegna una Macro al controllo del modulo](/cells/it/nodejs-cpp/assign-macro-to-form-control/)
- [Verifica se la firma digitale del codice VBA è valida](/cells/it/nodejs-cpp/check-if-digital-signature-of-vba-code-is-valid/)
- [Verifica se il codice VBA è firmato](/cells/it/nodejs-cpp/check-if-vba-code-is-signed/)
- [Verifica se il progetto VBA in un foglio di lavoro è firmato](/cells/it/nodejs-cpp/check-if-vba-project-in-a-workbook-is-signed/)
- [Verifica se il progetto VBA è protetto e bloccato per la visualizzazione](/cells/it/nodejs-cpp/check-if-vba-project-is-protected-and-locked-for-viewing/)
- [Copia il DesignerStorage del modulo utente VBA Macro dal modello al foglio di lavoro di destinazione](/cells/it/nodejs-cpp/copy-vba-macro-userform-designerstorage-from-template-to-target-workbook/)
- [Firma digitalmente un progetto di codice VBA con un certificato](/cells/it/nodejs-cpp/digitally-sign-a-vba-code-project-with-certificate/)
- [Esporta il certificato VBA su file o flusso](/cells/it/nodejs-cpp/export-vba-certificate-to-file-or-stream/)
- [Filtra il progetto VBA durante il caricamento di un libro di lavoro](/cells/it/nodejs-cpp/filter-vba-project-while-loading-a-workbook/)
- [Scopri se il progetto VBA è protetto](/cells/it/nodejs-cpp/find-out-if-vba-project-is-protected/)
- [Proteggi con password il progetto VBA del foglio di lavoro Excel](/cells/it/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/)

{{< app/cells/assistant language="nodejs-cpp" >}}
