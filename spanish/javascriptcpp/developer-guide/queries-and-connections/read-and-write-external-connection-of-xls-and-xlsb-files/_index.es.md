---
title: Leer y Escribir Conexión Externa de archivos XLS y XLSB con JavaScript a través de C++
linktitle: Leer y Escribir Conexión Externa de Archivos XLS y XLSB
type: docs
weight: 80
url: /es/javascript-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/
description: Aprende cómo leer y escribir conexiones externas de archivos XLS y XLSB usando Aspose.Cells for JavaScript a través de C++.
---

## **Escenarios de uso posibles**  

Aspose.Cells ya soporta la lectura y escritura de conexiones externas de archivos XLSX, pero ahora también soporta esta función para archivos XLSB y XLS. Sin embargo, el código es el mismo para todos los tipos de formatos.  

## **Leer y Escribir Conexión Externa de Archivo XLS/XLSB**  

El siguiente código de ejemplo carga el archivo XLSB de muestra (también se puede cargar XLS) y lee su primera conexión externa, que en realidad es una conexión de base de datos Microsoft Access. Luego modifica la propiedad [**DBConnection.name**](https://reference.aspose.com/cells/javascript-cpp/dbconnection/#name--) y lo guarda como archivo XLS/XLSB de salida. La captura de pantalla muestra el efecto del código en el [archivo XLSB de ejemplo](51740722.xlsb) y el [archivo XLSB de salida](51740723.xlsb) después de su ejecución. Por favor, también vea la salida de la consola del código de ejemplo a continuación para referencia.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Código de muestra**  

El siguiente código funcionará tanto para archivos XLSB como para archivos XLS cargándolos y guardándolos con la extensión apropiada.  

```html
<!DOCTYPE html>
<html>
    <head>
        <title>Aspose.Cells Example</title>
    </head>
    <body>
        <h1>Read and Modify External DB Connection (XLSB)</h1>
        <input type="file" id="fileInput" accept=".xls,.xlsx,.xlsb,.csv" />
        <button id="runExample">Run Example</button>
        <a id="downloadLink" style="display: none;">Download Result</a>
        <div id="result"></div>
    </body>

    <script src="aspose.cells.js.min.js"></script>
    <script type="text/javascript">
        const { Workbook, SaveFormat, Utils } = AsposeCells;

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
            if (!fileInput.files.length) {
                document.getElementById('result').innerHTML = '<p style="color: red;">Please select an Excel file (.xlsb).</p>';
                return;
            }

            const file = fileInput.files[0];
            const arrayBuffer = await file.arrayBuffer();

            // Load the source Excel Xlsb file
            const workbook = new Workbook(new Uint8Array(arrayBuffer));

            // Read the first external connection which is actually a DB-Connection
            const dbCon = workbook.dataConnections.get(0);

            // Print the Name, Command and Connection Info of the DB-Connection
            const outputLines = [];
            outputLines.push("Connection Name: " + dbCon.name);
            outputLines.push("Command: " + dbCon.command);
            outputLines.push("Connection Info: " + dbCon.connectionString);

            // Modify the Connection Name
            dbCon.name = "NewCust";

            // Save the Excel Xlsb file
            const outputData = workbook.save(SaveFormat.Xlsb);
            const blob = new Blob([outputData]);
            const downloadLink = document.getElementById('downloadLink');
            downloadLink.href = URL.createObjectURL(blob);
            downloadLink.download = 'outputExternalConnection_XLSB.xlsb';
            downloadLink.style.display = 'block';
            downloadLink.textContent = 'Download Modified Excel File';

            document.getElementById('result').innerHTML = '<pre style="color: green;">' + outputLines.join('\n') + '\n\nModified connection name to: NewCust</pre>';
        });
    </script>
</html>
```  

## **Salida de la consola**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}
