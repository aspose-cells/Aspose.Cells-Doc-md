---  
title: Verifica si el libro de trabajo contiene enlaces externos ocultos con Node.js a través de C++  
linktitle: Verificar si el libro de trabajo contiene enlaces externos ocultos  
type: docs  
weight: 230  
url: /es/nodejs-cpp/check-if-workbook-contains-hidden-external-links/  
description: Aprende cómo verificar si un libro de trabajo contiene enlaces externos ocultos usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  
A veces, el libro de trabajo contiene enlaces externos que están ocultos y no se pueden ver en Microsoft Excel. Aspose.Cells recupera todos los enlaces externos, ya sean visibles o ocultos. Sin embargo, puedes verificar la propiedad [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--) para verificar si el enlace externo es visible o no.

## **Verificar si la Hoja de Cálculo contiene Enlaces Externos Ocultos**  
El siguiente código de ejemplo carga el [archivo Excel fuente](5115413.xlsx) que contiene enlaces externos ocultos. Estos enlaces no se pueden ver en Microsoft Excel, pero están presentes en el libro de trabajo. Después de imprimir las propiedades [ExternalLink.getDataSource()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#getDataSource--) y [ExternalLink.isReferred()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isReferred--), se imprime la propiedad [ExternalLink.isVisible()](https://reference.aspose.com/cells/nodejs-cpp/externallink/#isVisible--). En la salida de la consola a continuación, verás que todos sus enlaces externos no son visibles.

### **Código de muestra**  
```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access the external link collection of the workbook
const links = workbook.getWorksheets().getExternalLinks();

// Print all the external links and check their IsVisible property
for (let i = 0; i < links.getCount(); i++) {
console.log("Data Source: " + links.get(i).getDataSource());
console.log("Is Referred: " + links.get(i).getIsReferred());
console.log("Is Visible: " + links.get(i).getIsVisible());
console.log();
}
```  

### **Salida de la consola**  
Aquí está la salida de la consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra proporcionado](5115413.xlsx).

{{< highlight java >}}  
 Data Source: C:\International\DDB\FAS 133\Swap Rates\GS_1M_3M_1_2_5_¥$_(B)IRSwaps_0400.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\DIST DAY\MAY TEMPLATES\030601t.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\AREVIEW\2002 Controllable\Autobrct.xls  

Is Referred: True  

Is Visible: False  

Data Source: C:\CARDSFO\Main Files\Rate Forecast\FY 11\IFR 11 01 (New Model REPORTS 11.08.07).xls  

Is Referred: True  

Is Visible: False  
{{< /highlight >}}  
