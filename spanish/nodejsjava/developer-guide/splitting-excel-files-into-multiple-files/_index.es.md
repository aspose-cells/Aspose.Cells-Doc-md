---
title: Dividir archivos Excel en varios archivos
description: Aspose.Cells es una biblioteca Aspose.Cells for Node.js via Java para trabajar con archivos de hojas de cálculo, que admite dividir un único archivo Excel en varios archivos. Este artículo presentará cómo dividir archivos Excel copiando cada hoja de cálculo a un libro de trabajo separado y copiando rangos de celdas específicos a otros libros de trabajo.
keywords: Aspose.Cells, Aspose.Cells for Node.js via Java, hoja de cálculo, dividir archivo Excel, copiar hoja de cálculo, copiar rango, múltiples libros de trabajo, guardar como archivos separados
type: docs
weight: 195
url: /es/nodejs-java/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells admite dividir un único archivo Excel en varios archivos. Existen dos formas principales de hacerlo: (1) copiando cada hoja de cálculo del libro de trabajo de origen a un nuevo libro de trabajo y guardando cada uno como un archivo separado, y (2) copiando un rango de celdas específico desde una hoja de cálculo a un nuevo libro de trabajo. Ambos enfoques son útiles cuando necesita distribuir subconjuntos de datos, crear informes más pequeños para diferentes destinatarios o aislar datos para su procesamiento individual.

{{% /alert %}}

## **Introducción**

Existen muchos escenarios del mundo real en los que un desarrollador necesita dividir un único archivo Excel en varios archivos más pequeños. Por ejemplo, un libro de trabajo puede contener una hoja de cálculo por departamento, y cada jefe de departamento necesita recibir solo su propia hoja. En otros casos, es posible que desee extraer una tabla o bloque de datos particular de una hoja de cálculo y enviarlo como un archivo independiente por correo electrónico, sin exponer el resto del libro de trabajo. Los libros de trabajo consolidados grandes también pueden necesitar dividirse en piezas más pequeñas para un manejo más fácil, una carga más rápida o un procesamiento posterior por parte de otros sistemas.

Aspose.Cells proporciona dos enfoques flexibles para esta tarea. El primer enfoque itera a través de cada hoja de cálculo en el libro de trabajo de origen y copia su contenido en una nueva instancia de `Workbook`, guardando cada uno como un archivo separado. El segundo enfoque se enfoca en un rango de celdas específico dentro de una hoja de cálculo y copia solo ese rango en un nuevo libro de trabajo. En ambos casos, el flujo general es el mismo: cargue el libro de trabajo de origen usando la clase `Workbook`, acceda a los datos relevantes a través de los objetos `Worksheet` y `Cells`, transfiera el contenido a un `Workbook` de destino y luego guarde el destino en disco.

## **Dividir un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo**

### **Descripción general del enfoque**

En este enfoque, el libro de trabajo de origen se abre una vez, y luego para cada `Worksheet` en su colección `Worksheets`, se crea un nuevo `Workbook` de destino. El contenido de la hoja de cálculo de origen se copia luego en la primera hoja de cálculo del libro de trabajo de destino, y el libro de trabajo de destino se guarda como un archivo cuyo nombre se deriva del nombre de la hoja de cálculo de origen. El resultado es un archivo de salida por hoja de cálculo, donde cada archivo de salida contiene los datos de una sola hoja de origen.

Este método es la opción correcta cuando cada hoja de cálculo en su libro de trabajo de origen representa una unidad de información lógicamente independiente (como un departamento, región, mes o línea de productos) y desea entregar o procesar cada unidad por separado.

### **Pasos**

Los siguientes pasos describen cómo dividir un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo:

1. Abra el archivo Excel de origen instanciando un objeto `Workbook` y pasando la ruta del archivo a su constructor.
2. Itere a través de la colección `Workbook.Worksheets` usando un bucle `for` o `foreach` para que cada `Worksheet` en el archivo de origen sea procesado.
3. Dentro del bucle, cree una nueva instancia de `Workbook` de destino (un libro de trabajo vacío) para la hoja de cálculo actual.
4. Agregue un nuevo `Worksheet` al libro de trabajo de destino (o use la primera hoja de cálculo predeterminada) y asígnele un nombre significativo, idealmente el mismo que la propiedad `Name` de la hoja de cálculo de origen.
5. Copie el contenido de la hoja de cálculo de origen en la hoja de cálculo de destino. Esto se puede hacer iterando las celdas de la colección `Cells` de la hoja de cálculo de origen y escribiendo sus valores en las celdas correspondientes de la hoja de cálculo de destino, o usando el método `Cells.copy` para transferir un rango completo de una vez.
6. Construya una ruta de archivo de salida que incorpore el nombre de la hoja de cálculo de origen (por ejemplo, `dataDir + worksheet.getName() + ".xls"`) para que cada archivo generado tenga un nombre único.
7. Llame al método `Workbook.save` del libro de trabajo de destino para escribir el archivo en disco.
8. Repita los pasos 3 a 7 para la siguiente hoja de cálculo hasta que todas las hojas de cálculo hayan sido procesadas.

### **Ejemplo de código**

```javascript
const AsposeCells = require("aspose.cells");
const path = require("path");

const dataDir = "data/";
const workbook = new AsposeCells.Workbook(dataDir + "book1.xls");

for (let i = 0; i < workbook.getWorksheets().getCount(); i++) {
    const sourceSheet = workbook.getWorksheets().get(i);
    const sheetName = sourceSheet.getName();
    
    const destWorkbook = new AsposeCells.Workbook();
    const destIndex = destWorkbook.getWorksheets().add();
    const destSheet = destWorkbook.getWorksheets().get(destIndex);
    destSheet.setName(sheetName);
    
    destSheet.copy(sourceSheet);
    
    const destFile = dataDir + sheetName + ".xls";
    destWorkbook.save(destFile, AsposeCells.SaveFormat.Excel97To2003);
}
```

El resultado esperado es un conjunto de nuevos archivos en el directorio de datos, un archivo por hoja de cálculo del libro de trabajo de origen. Cada archivo recibe el nombre de su hoja de origen correspondiente, y el archivo contiene los datos (y opcionalmente el formato) de esa única hoja.

## **Dividir un archivo Excel copiando un rango a un nuevo libro de trabajo**

### **Descripción general del enfoque**

A veces, los datos que necesita dividir no corresponden a una hoja de cálculo completa sino a una región rectangular específica de una hoja de cálculo, como `A1:D10` o un rango con nombre que representa una tabla particular. En estos casos, copiar hojas de cálculo completas es un desperdicio, y se requiere un enfoque más preciso: identifique el rango de origen, copie solo ese rango en un nuevo libro de trabajo y guarde el nuevo archivo.

Este enfoque es ideal cuando desea extraer una sola tabla, bloque de informes o área de datos de una hoja de cálculo más grande mientras descarta todo el contenido no relacionado. También es útil para exportar regiones seleccionadas por el usuario de una hoja como archivos independientes.

### **Pasos**

Los siguientes pasos describen cómo dividir un archivo Excel copiando un rango específico a un nuevo libro de trabajo:

1. Abra el archivo Excel de origen instanciando un objeto `Workbook` con la ruta del archivo.
2. Recupere el `Worksheet` de origen que contiene el rango que desea copiar, ya sea por índice (por ejemplo, la primera hoja) o por su nombre en la colección `Worksheets`.
3. Identifique el rango que se va a copiar. Puede ser un rango de celdas con valores literales como `A1:C10`, o un rango con nombre obtenido a través de la colección `Worksheet.Cells`, o un rango creado mediante `Worksheet.Cells.createRange`.
4. Cree una nueva instancia de `Workbook` de destino.
5. Acceda al primer `Worksheet` del libro de trabajo de destino (la hoja predeterminada).
6. Copie el rango de origen en la hoja de cálculo de destino, generalmente comenzando desde la celda `A1`. El método `Cells.copy` en la colección `Cells` de destino se puede usar para copiar un rango completo, o puede iterar a través de las celdas del rango de origen y escribir sus valores en las celdas de destino con `putValue`. Se pueden proporcionar `CopyOptions` opcionales para controlar lo que se transfiere (solo valores, valores y estilos, fórmulas, etc.).
7. Guarde el libro de trabajo de destino en una nueva ruta de archivo en disco usando el método `Workbook.save`.

### **Ejemplo de código**

```javascript
let sourceWorkbook = new AsposeCells.Workbook(sourcePath);

// Obtener la primera hoja de cálculo del libro de origen
let sourceWorksheet = sourceWorkbook.getWorksheets().get(0);

// Definir el rango de celdas de origen A1:C10 (10 filas, 3 columnas comenzando en fila 0, columna 0)
let sourceRange = sourceWorksheet.getCells().createRange(0, 0, 10, 3);

// Crear un nuevo libro de destino
let destWorkbook = new AsposeCells.Workbook();

// Acceder a la primera hoja de cálculo en el libro de destino
let destWorksheet = destWorkbook.getWorksheets().get(0);

// Crear el rango de destino en A1 con las mismas dimensiones que el rango de origen
let destRange = destWorksheet.getCells().createRange(0, 0, 10, 3);

// Copiar el rango de origen al rango de destino
destRange.copy(sourceRange);

// Guardar el libro de destino en un nuevo archivo .xls
destWorkbook.save(outputPath, AsposeCells.SaveFormat.Excel97To2003);
```

El resultado esperado es un único archivo nuevo en el directorio de datos que contiene solo los valores (y opcionalmente el formato) del rango especificado extraído del libro de trabajo de origen. El archivo de destino no tiene relación con ningún otro dato en el archivo de origen; contiene solo el rango extraído, comenzando en la celda `A1` de su primera hoja de cálculo.



{{< app/cells/assistant language="javascript" >}}