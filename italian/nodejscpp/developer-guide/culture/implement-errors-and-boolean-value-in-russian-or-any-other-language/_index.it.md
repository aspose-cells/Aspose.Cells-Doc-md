---
title: Implementa errori e valori Booleani in Russo o in altre lingue con Node.js via C++
linktitle: Implementare gli errori e il valore booleano in russo o in qualsiasi altra lingua
type: docs
weight: 40
url: /it/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Impara come implementare errori e valori booleani in diverse lingue usando Aspose.Cells for Node.js via C++. 
---

## **Possibili Scenari di Utilizzo**

Se usi Microsoft Excel in Russo o in altre lingue o localizzazioni, verranno visualizzati Errori e valori Booleani in base a quella lingua o regione. Puoi ottenere un comportamento simile usando Aspose.Cells for Node.js via C++ tramite la proprietà [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--). Devi sovrascrivere i seguenti metodi della classe [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Implementare gli errori e il valore booleano in russo o in qualsiasi altra lingua**

Il seguente codice di esempio illustra come implementare gli errori e il valore booleano in russo o in qualsiasi altra lingua. Controlla il [File Excel di esempio](73990159.xlsx) utilizzato in questo codice e il suo [PDF di output](73990160.pdf). Lo screenshot mostra la differenza tra il file Excel di esempio e il PDF di output a titolo di riferimento.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Codice di Esempio**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Russian Globalization
class RussianGlobalization extends AsposeCells.GlobalizationSettings {
getErrorValueString(err) {
switch (err.toUpperCase()) {
case "#NAME?":
return "#RussianName-имя?";
}
return "RussianError-ошибка";
}

getBooleanValueString(bv) {
return bv ? "RussianTrue-правда" : "RussianFalse-ложный";
}
}

//--------------------------------
//--------------------------------

class ImplementErrorsAndBooleanValueInRussianOrAnyOtherLanguage {
static run() {
// Load the source workbook
const workbook = new AsposeCells.Workbook("sampleRussianGlobalization.xlsx");

// Set GlobalizationSettings in Russian Language
workbook.getSettings().setGlobalizationSettings(new RussianGlobalization());

// Calculate the formula
workbook.calculateFormula();

// Save the workbook in pdf format
workbook.save("outputRussianGlobalization.pdf");
}
}
```
{{< app/cells/assistant language="nodejs-cpp" >}}
