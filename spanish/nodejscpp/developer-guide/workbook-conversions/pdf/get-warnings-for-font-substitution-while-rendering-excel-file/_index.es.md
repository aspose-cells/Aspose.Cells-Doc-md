---  
title: Obtener advertencias por sustitución de fuente mientras se renderiza un archivo Excel con Node.js a través de C++  
linktitle: Obtener Advertencias por Sustitución de Fuentes al Renderizar un Archivo de Excel  
type: docs  
weight: 230  
url: /es/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/  
description: Aprenda cómo obtener advertencias por sustitución de fuentes al renderizar archivos excel a PDF usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

A veces, al renderizar un archivo Microsoft Excel a PDF, Aspose.Cells sustituye fuentes. Aspose.Cells proporciona una característica que permite a los desarrolladores saber qué fuente específica ha sido sustituida al activar una advertencia. Esta es una característica útil que puede ayudar a identificar por qué un PDF renderizado con Aspose.Cells se ve diferente al archivo original de Microsoft Excel, para que puedan tomar las acciones apropiadas. Por ejemplo, instalar las fuentes faltantes para que los resultados de renderizado se vean igual.

{{% /alert %}}  

Para obtener advertencias por sustitución de fuente al renderizar archivos Excel a PDF, implemente la interfaz IWarningCallback y configure la propiedad PdfSaveOptions.warningCallback con su interfaz implementada.

La captura de pantalla a continuación muestra un archivo de Excel fuente que utilizaremos en el siguiente código. Tiene algo de texto en las celdas A6 y A7 en fuentes que no son renderizadas correctamente por Microsoft Excel.

|**No todas las fuentes se renderizan correctamente**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|  
Aspose.Cells sustituirá las fuentes en las celdas A6 y A7 con fuentes adecuadas como se muestra a continuación.

|**Fuentes Sustituidas**|  
| :- |  
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|  
## **Descargar Archivo Fuente y PDF de Salida**  
Puedes descargar el archivo de Excel fuente y el PDF de salida desde los siguientes enlaces

- [source.xlsx](5112611.xlsx)  
- [output.pdf](5112616.pdf)  
## **Código**  
El siguiente código implementa IWarningCallback y configura la propiedad PdfSaveOptions.warningCallback con la interfaz implementada. Ahora, cada vez que una fuente sea sustituida en alguna celda, Aspose.Cells generará una advertencia dentro del método WarningCallback.Warning().

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

class GetWarningsForFontSubstitution {
static warning(info) {
if (info.getType() === AsposeCells.WarningType.FontSubstitution) {
console.log("WARNING INFO: " + info.getDescription());
}
}

static run() {
// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "source.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

const options = new AsposeCells.PdfSaveOptions();
options.setWarningCallback(GetWarningsForFontSubstitution);
const outputFilePath = path.join(dataDir, "output_out.pdf");
workbook.save(outputFilePath, options);
}
}
```  
## **Salida**  
Después de convertir el archivo de Excel fuente a PDF, las advertencias se emiten en la consola de depuración de esta manera:

{{< highlight java >}}  

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].  

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].  

{{< /highlight >}}  

{{% alert color="primary" %}}  

Si tu hoja de cálculo contiene fórmulas, es mejor llamar al método Workbook.calculateFormula justo antes de renderizar la hoja de cálculo al formato PDF. Al hacerlo, te asegurarás de que los valores dependientes de la fórmula se recalculen y los valores correctos se rendericen en el PDF.

{{% /alert %}}  

