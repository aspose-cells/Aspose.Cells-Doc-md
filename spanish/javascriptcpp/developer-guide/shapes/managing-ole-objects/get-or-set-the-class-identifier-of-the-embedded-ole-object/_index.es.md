---
title: Obtén o establece el Identificador de Clase del objeto OLE incrustado con JavaScript vía C++
linktitle: Obtener o establecer el identificador de clase del objeto OLE incrustado
type: docs
weight: 200
url: /es/javascript-cpp/get-or-set-the-class-identifier-of-the-embedded-ole-object/
description: Aprende cómo obtener o establecer el identificador de clase de objetos OLE incrustados en JavaScript usando Aspose.Cells a través de C++.
---

## **Escenarios de uso posibles**  
Aspose.Cells proporciona la propiedad [OleObject.classIdentifier](https://reference.aspose.com/cells/javascript-cpp/oleobject/#classIdentifier--) que puedes usar para obtener o establecer el identificador de clase de un objeto OLE incrustado. Los identificadores de clase de objetos OLE son en realidad GUIDs, es decir, Identificadores Únicos Globales. El GUID siempre tiene 16 bytes; por lo tanto, los identificadores de clase también miden 16 bytes. A menudo se encuentran en el Registro de Windows y proporcionan información a la aplicación host sobre cómo abrir objetos OLE incrustados que contienen diversos recursos incrustados dentro de la aplicación cliente.

## **Obtener o establecer el identificador de clase del objeto OLE incrustado**  
 La siguiente captura de pantalla muestra el identificador de clase del objeto OLE, es decir, GUID, que ha sido leído del [archivo de Excel de muestra](5115190.xls) que contiene el objeto PowerPoint OLE incrustado.

![todo:image_alt_text](get-or-set-the-class-identifier-of-the-embedded-ole-object_1.png)  
### **Código de muestra**  
Por favor, vea el siguiente código de muestra ejecutado con [archivo de Excel de muestra](5115190.xls) y su salida en consola, que imprime el identificador de clase del objeto OLE, es decir, GUID. El GUID impreso es exactamente el mismo que se muestra en la captura de pantalla.

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Extract OLE Object Class Identifier (GUID)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Worksheet, Cell, Utils } = AsposeCells;

        AsposeCells.onReady({
            license: "/lic/aspose.cells.enc",
            fontPath: "/fonts/",
            fontList: [
                "arial.ttf",
                "NotoSansSC-Regular.ttf"
            ]
        }).then(() => {
            console.log("Aspose.Cells initialized");
        });

        document.getElementById('runExample').addEventListener('click', async () => {
            const fileInput = document.getElementById('fileInput');
            const resultDiv = document.getElementById('result');

            if (!fileInput.files.length) {
                resultDiv.innerHTML = '<p style="color: red;">Please select an Excel file.</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Instantiating a Workbook object from the uploaded file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Access its first worksheet
            const worksheet = workbook.worksheets.get(0);

            // Access first ole object inside the worksheet
            const oleObject = worksheet.oleObjects.get(0);

            // Convert 16-bytes array into GUID
            const bytes = new Uint8Array(oleObject.classIdentifier);
            const guid = bytes.reduce((acc, byte) => acc + String.fromCharCode(byte), '');

            // Print the GUID
            console.log(guid.toUpperCase());
            resultDiv.innerHTML = `<p style="color: green;">GUID: ${guid.toUpperCase()}</p>`;
        });
    </script>
</html>
```  
### **Salida de la consola**  
Esta es la salida de consola del código de muestra anterior cuando se ejecuta con el [archivo de Excel de muestra](5115190.xls).

{{< highlight java >}}  
 DC020317-E6E2-4A62-B9FA-B3EFE16626F4  
{{< /highlight >}}
