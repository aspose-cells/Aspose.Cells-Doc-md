---  
title: Leer y escribir conexiones externas de archivos XLS y XLSB con Node.js a través de C++  
linktitle: Leer y Escribir Conexión Externa de Archivos XLS y XLSB  
type: docs  
weight: 80  
url: /es/nodejs-cpp/read-and-write-external-connection-of-xls-and-xlsb-files/  
description: Aprende cómo leer y escribir conexiones externas de archivos XLS y XLSB usando Aspose.Cells for Node.js via C++.  
---  

## **Escenarios de uso posibles**  

Aspose.Cells ya soporta la lectura y escritura de conexiones externas de archivos XLSX, pero ahora también soporta esta función para archivos XLSB y XLS. Sin embargo, el código es el mismo para todos los tipos de formatos.  

## **Leer y Escribir Conexión Externa de Archivo XLS/XLSB**  

El siguiente código de ejemplo carga el archivo XLSB de muestra (también se puede cargar XLS) y lee su primera conexión externa, que en realidad es una conexión de base de datos Microsoft Access. Luego modifica la propiedad [**DBConnection.getName()**](https://reference.aspose.com/cells/nodejs-cpp/dbconnection/#getName--) y lo guarda como archivo XLS/XLSB de salida. La captura de pantalla muestra el efecto del código en el [archivo XLSB de ejemplo](51740722.xlsb) y el [archivo XLSB de salida](51740723.xlsb) después de su ejecución. Por favor, también vea la salida de la consola del código de ejemplo a continuación para referencia.  

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)  

## **Código de muestra**  

El siguiente código funcionará tanto para archivos XLSB como para archivos XLS cargándolos y guardándolos con la extensión apropiada.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleExternalConnection_XLSB.xlsb");

// Load the source Excel Xlsb file
const workbook = new AsposeCells.Workbook(filePath);

// Read the first external connection which is actually a DB-Connection
const dbCon = workbook.getDataConnections().get(0);

// Print the Name, Command and Connection Info of the DB-Connection
console.log("Connection Name: " + dbCon.getName());
console.log("Command: " + dbCon.getCommand());
console.log("Connection Info: " + dbCon.getConnectionString());

// Modify the Connection Name
dbCon.setName("NewCust");

// Save the Excel Xlsb file
workbook.save("outputExternalConnection_XLSB.xlsb");
```  

## **Salida de la consola**  

{{< highlight js >}}  

Connection Name: Cust  

Command: Customer  

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False  

{{< /highlight >}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
