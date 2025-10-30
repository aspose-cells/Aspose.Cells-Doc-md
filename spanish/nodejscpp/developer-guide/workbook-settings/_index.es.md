---
title: Administrar configuraciones de archivos de hojas de cálculo de Excel con Node.js vía C++
linktitle: Configuraciones de libros de trabajo
type: docs
weight: 185
url: /es/nodejs-cpp/workbook-settings/
description: Administrar configuraciones de archivos de Excel usando Aspose.Cells for Node.js via C++.
---


## **Resumen de configuración del libro de trabajo**
Trabajar con archivos de Excel implica varias configuraciones que se pueden manipular programáticamente usando Aspose.Cells for Node.js via C++. Este documento describe cómo administrar estas configuraciones de manera efectiva.

## **Escenarios de uso posibles**
Los siguientes escenarios ilustran cuándo puede ser necesario administrar las configuraciones del libro de trabajo:
- Ajustar opciones de pantalla
- Configurar modo de cálculo
- Configurar parámetros de configuración de página

## **Administrar configuración del libro de trabajo usando Aspose.Cells for Node.js via C++**
Este ejemplo demuestra cómo administrar configuraciones del libro de trabajo como opciones de cálculo y configuraciones de pantalla.

1. Cree un nuevo libro de trabajo o cargue uno existente.
2. Modifique las configuraciones del libro de acuerdo a sus requisitos.
3. Guarde el libro de trabajo para mantener los cambios.

### **Código de ejemplo**

```javascript
const { Workbook, SaveFormat } = require('aspose.cells');

// Create a new workbook
let workbook = new Workbook();

// Access the settings of the workbook
let settings = workbook.getSettings();
settings.setCalculationMode(1); // Manual calculation

// Display options
settings.setShowGridLines(false); // Disable gridlines

// Save the workbook
workbook.save('WorkbookSettingsExample.xlsx', SaveFormat.XLSX);
```

## **Propiedades y métodos clave de configuración del libro de trabajo**
Aspose.Cells para Node.js ofrece varias propiedades y métodos para ajustar la configuración del libro:
- **Workbook.getSettings()**: Accede a la configuración del libro.
- **Settings.setCalculationMode(mode)**: Establece el modo de cálculo para el libro.
- **Settings.setShowGridLines(value)**: Habilita o deshabilita las líneas de cuadrícula en la pantalla.

## **Conclusión**
Administrar configuraciones del libro en Aspose.Cells for Node.js via C++ es sencillo y ofrece muchas opciones para personalizar el comportamiento del archivo Excel. Al utilizar las configuraciones disponibles, puede adaptar el libro a sus requisitos específicos.

{{< app/cells/assistant language="nodejs-cpp" >}}
