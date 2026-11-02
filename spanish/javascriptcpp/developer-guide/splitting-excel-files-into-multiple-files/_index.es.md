---
title: Dividir archivos Excel en varios archivos
linktitle: Dividir archivos Excel en varios archivos
description: Aspose.Cells for JavaScript via C++ es una biblioteca JavaScript via C++ para trabajar con archivos de hojas de cálculo, que admite dividir un único archivo Excel en varios archivos, este artículo presentará cómo dividir archivos Excel copiando cada hoja de cálculo a un libro de trabajo separado y copiando rangos de celdas específicos a otros libros de trabajo
keywords: Aspose.Cells, Aspose.Cells for JavaScript via C++ biblioteca, hoja de cálculo, dividir archivo Excel, copiar hoja de cálculo, copiar rango, varios libros de trabajo, guardar como archivos separados
type: docs
weight: 195
url: /es/javascript-cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_javascriptcpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells for JavaScript via C++ admite dividir un único archivo Excel en varios archivos. Existen dos formas principales de hacerlo: (1) copiando cada hoja de cálculo del libro de trabajo fuente a un nuevo libro de trabajo y guardando cada uno como un archivo separado, y (2) copiando un rango de celdas específico de una hoja de cálculo a un nuevo libro de trabajo. Ambos enfoques son útiles cuando necesita distribuir subconjuntos de datos, crear informes más pequeños para diferentes destinatarios o aislar datos para procesamiento individual.
{{% /alert %}}

## **Introducción**
Existen muchos escenarios reales en los que un desarrollador necesita dividir un único archivo Excel en varios archivos más pequeños. Por ejemplo, un libro de trabajo puede contener una hoja de cálculo por departamento, y cada responsable de departamento necesita recibir solo su propia hoja. En otros casos, puede querer extraer una tabla o bloque de datos particular de una hoja y enviarlo como un archivo independiente por correo electrónico, sin exponer el resto del libro. Los libros de trabajo consolidados y de gran tamaño también pueden necesitar dividirse en piezas más pequeñas para facilitar su manejo, acelerar la carga o permitir el procesamiento posterior por otros sistemas.  
Aspose.Cells for JavaScript via C++ ofrece dos enfoques flexibles para esta tarea. El primer enfoque itera por cada hoja de cálculo del libro de trabajo fuente y copia su contenido en una nueva instancia de `Workbook`, guardando cada una como un archivo separado. El segundo enfoque se centra en un rango de celdas específico dentro de una hoja y copia solo ese rango a un nuevo libro de trabajo. En ambos casos, el flujo general es el mismo: cargar el libro de trabajo fuente usando la clase `Workbook`, acceder a los datos relevantes mediante los objetos `Worksheet` y `Cells`, transferir el contenido a un `Workbook` de destino y luego guardar el destino en disco.

## **Dividir un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo**

### **Descripción general del enfoque**
En este enfoque, el libro de trabajo fuente se abre una sola vez y, para cada `Worksheet` de su colección `Worksheets`, se crea un nuevo `Workbook` de destino. El contenido de la hoja de cálculo fuente se copia en la primera hoja del libro de trabajo de destino y luego se guarda el libro de trabajo de destino con un nombre derivado del nombre de la hoja fuente. El resultado es un archivo de salida por hoja de cálculo, cada uno conteniendo los datos de una sola hoja fuente.  
Este método es la elección adecuada cuando cada hoja de cálculo en su libro de trabajo fuente representa una unidad de información lógicamente independiente (como un departamento, región, mes o línea de producto) y desea entregar o procesar cada unidad por separado.

### **Pasos**
Los pasos siguientes describen cómo dividir un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo:
1. Abra el archivo Excel fuente instanciando un objeto `Workbook` y pasando la ruta del archivo a su constructor.  
2. Recorra la colección `Workbook.Worksheets` utilizando un bucle `for` o `for...of` para que cada `Worksheet` del archivo fuente sea procesada.  
3. Dentro del bucle, cree una nueva instancia de `Workbook` de destino (un libro vacío) para la hoja actual.  
4. Copie el contenido de la hoja fuente en la hoja de destino. Esto puede hacerse iterando las celdas de la colección `Cells` de la hoja fuente y escribiendo sus valores en las celdas correspondientes de la hoja de destino, o usando el método `Cells.Copy` para transferir un rango completo de una sola vez.  
5. Construya una ruta de archivo de salida que incorpore el nombre de la hoja fuente (por ejemplo, `dataDir + worksheet.Name + ".xls"`), de modo que cada archivo generado tenga un nombre único.  
6. Llame al método `Workbook.Save` del libro de trabajo de destino para escribir el archivo en disco.  
7. Repita los pasos 3 a 6 para la siguiente hoja hasta que se hayan procesado todas las hojas.

### **Ejemplo de código**

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Aspose.Cells Example</h1>
        <input type="file" id="fileInput" accept=".xls" />
        <button id="runExample">Run Example</button>
        <div id="result"></div>
        <script src="aspose.cells.js.min.js"></script>
        <script type="text/javascript">
            const { Workbook } = AsposeCells;
            const readyPromise = AsposeCells.onReady({
                license: "/lic/aspose.cells.enc",
                fontPath: "/fonts/",
                fontList: ["arial.ttf", "NotoSansSC-Regular.ttf"]
            });
            document.getElementById('runExample').addEventListener('click', async () => {
                const result = document.getElementById('result');
                try {
                    const fileInput = document.getElementById('fileInput');
                    const file = fileInput.files[0];
                    if (!file) {
                        result.innerHTML = '<p style="color: red;">Please select an .xls file.</p>';
                        return;
                    }
                    result.innerHTML = '<p>Processing...</p>';
                    const workbook = new Workbook(new Uint8Array(await file.arrayBuffer()));
                    const downloadLinks = document.createElement('div');
                    for (let i = 0; i < workbook.worksheets.count; i++) {
                        const sourceSheet = workbook.worksheets.get(i);
                        const sheetName = sourceSheet.name;
                        const destWorkbook = new Workbook();
                        const destIndex = destWorkbook.worksheets.add();
                        const destSheet = destWorkbook.worksheets.get(destIndex);
                        destSheet.name = sheetName;
                        destSheet.copy(sourceSheet);
                        const outputData = destWorkbook.save(AsposeCells.SaveFormat.Excel97To2003);
                        const blob = new Blob([outputData], { type: "application/vnd.ms-excel" });
                        const downloadLink = document.createElement('a');
                        downloadLink.href = URL.createObjectURL(blob);
                        downloadLink.download = `${sheetName}.xls`;
                        downloadLink.textContent = `Download ${sheetName}.xls`;
                        downloadLink.style.display = 'block';
                        downloadLink.style.marginTop = '8px';
                        downloadLinks.appendChild(downloadLink);
                    }
                    result.innerHTML = '<p style="color: green;">Done! Click a download link to get the result file.</p>';
                    result.appendChild(downloadLinks);
                } catch (error) {
                    console.error(error);
                    const errorMessage = document.createElement('p');
                    errorMessage.style.color = 'red';
                    errorMessage.textContent = `Error: ${error instanceof Error ? error.message : error}`;
                    result.replaceChildren(errorMessage);
                }
            });
        </script>
    </body>
</html>
```

Se espera que la salida sea un conjunto de nuevos archivos en el directorio de datos, un archivo por hoja de cálculo del libro de trabajo fuente. Cada archivo lleva el nombre de la hoja correspondiente y contiene los datos (y opcionalmente el formato) de esa hoja única.

## **Dividir un archivo Excel copiando un rango a un nuevo libro de trabajo**

### **Descripción general del enfoque**
A veces los datos que necesita dividir no corresponden a una hoja completa, sino a una región rectangular específica de una hoja, como `A1:D10` o un rango con nombre que representa una tabla concreta. En estos casos, copiar hojas enteras es innecesario y se requiere un enfoque más preciso: identificar el rango fuente, copiar solo ese rango a un nuevo libro de trabajo y guardar el nuevo archivo.  
Este enfoque es ideal cuando desea extraer una tabla única, un bloque de informe o un área de datos de una hoja más grande mientras descarta todo el contenido no relacionado. También es útil para exportar regiones seleccionadas por el usuario como archivos independientes.

### **Pasos**
Los pasos siguientes describen cómo dividir un archivo Excel copiando un rango específico a un nuevo libro de trabajo:
1. Abra el archivo Excel fuente instanciando un objeto `Workbook` con la ruta del archivo.  
2. Obtenga la `Worksheet` objetivo que contiene el rango que desea copiar, ya sea por índice (por ejemplo, la primera hoja) o por nombre desde la colección `Worksheets`.  
3. Identifique el rango a copiar. Puede ser un rango de celdas codificado como `A1:C10`, un rango con nombre obtenido mediante la colección `Worksheet.Cells`, o un rango creado mediante `Worksheet.Cells.CreateRange`.  
4. Cree una nueva instancia de `Workbook` de destino.  
5. Acceda a la primera `Worksheet` del libro de trabajo de destino (la hoja predeterminada).  
6. Copie el rango fuente en la hoja de destino, normalmente comenzando en la celda `A1`. El método `Cells.Copy` de la colección `Cells` de destino puede usarse para copiar un rango completo, o puede iterar las celdas del rango fuente y escribir sus valores en las celdas de destino con `PutValue`. Opcionalmente, se pueden proporcionar `CopyOptions` para controlar qué se transfiere (solo valores, valores y estilos, fórmulas, etc.).  
7. Guarde el libro de trabajo de destino en una nueva ruta de archivo en disco utilizando el método `Workbook.Save`.

### **Ejemplo de código**
Se espera que la salida sea un único archivo nuevo en el directorio de datos que contenga solo los valores (y opcionalmente el formato) del rango especificado extraído del libro de trabajo fuente. El archivo de destino no tiene relación con ningún otro dato del archivo fuente; contiene únicamente el rango extraído, comenzando en la celda `A1` de su primera hoja de cálculo.

## **Artículos relacionados**
- [Agregar campos de filtro a una Tabla Dinámica en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/add-page-field-in-pivot-table/)
- [Aplicar estilos a Tablas Dinámicas en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/apply-style-to-pivot-table/)
- [Modificar diseño de campo de página en Tabla Dinámica](/cells/es/javascript-cpp/change-page-field-layout/)
- [Convertir Sparkline a Imagen y HTML en Aspose.Cells for JavaScript via C++](/cells/es/javascript-cpp/convert-sparkline-to-image-and-html/)
- [Convertir Excel a formato OFD](/cells/es/javascript-cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="javascript-cpp" >}}