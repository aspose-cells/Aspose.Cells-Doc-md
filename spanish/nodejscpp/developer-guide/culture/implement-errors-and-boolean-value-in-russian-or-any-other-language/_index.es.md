---
title: Implementar errores y valores booleanos en ruso u otro idioma con Node.js a través de C++
linktitle: Implementar Errores y Valor Booleano en Ruso u Otro Idioma
type: docs
weight: 40
url: /es/nodejs-cpp/implement-errors-and-boolean-value-in-russian-or-any-other-language/
description: Aprende cómo implementar errores y valores booleanos en diferentes idiomas usando Aspose.Cells for Node.js via C++. 
---

## **Escenarios de uso posibles**

Si estás usando Microsoft Excel en idioma o región rusa u otra, mostrará errores y valores booleanos según esa configuración. Puedes lograr un comportamiento similar usando Aspose.Cells for Node.js via C++ con la propiedad [**WorkbookSettings.getGlobalizationSettings()**](https://reference.aspose.com/cells/nodejs-cpp/workbooksettings/#getGlobalizationSettings--). Tendrás que sobrescribir los siguientes métodos de la clase [**GlobalizationSettings**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings).

- [**GlobalizationSettings.getErrorValueString(string)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getErrorValueString-string-)
- [**GlobalizationSettings.getBooleanValueString(boolean)**](https://reference.aspose.com/cells/nodejs-cpp/globalizationsettings/#getBooleanValueString-boolean-)

## **Implementar Errores y Valor Booleano en Ruso u Otro Idioma**

El siguiente código de ejemplo ilustra cómo implementar Errores y Valor Booleano en Ruso u Otro Idioma. Por favor revise el [archivo de Excel de muestra](73990159.xlsx) usado en este código y su [PDF de salida](73990160.pdf). La captura de pantalla muestra la diferencia entre el archivo de Excel de muestra y el PDF de salida para referencia.

![todo:image_alt_text](implement-errors-and-boolean-value-in-russian-or-any-other-language_1.png)

## **Código de muestra**

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
