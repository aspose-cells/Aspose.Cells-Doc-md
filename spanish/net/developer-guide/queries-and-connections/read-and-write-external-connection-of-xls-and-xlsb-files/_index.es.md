---
title: Leer y escribir la conexión externa de los archivos XLS y XLSB
type: docs
weight: 80
url: /es/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---
## **Posibles escenarios de uso**

Aspose.Cells ya admite la conexión externa de lectura y escritura del archivo XLSX, pero ahora también admite esta función para los archivos XLSB y XLS. Sin embargo, el código es el mismo para todos los tipos de formatos.

## **Leer y escribir la conexión externa del archivo XLS/XLSB**

 El siguiente código de muestra carga el archivo de muestra XLSB (también se puede cargar XLS) y lee su primera conexión externa, que en realidad es una conexión de base de datos de acceso Microsoft. Luego modifica la[**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) property y lo guarda como archivo de salida XLS/XLSB. La captura de pantalla muestra el efecto del código en[muestra XLSB archivo](51740722.xlsb) y[archivo de salida XLSB](51740723.xlsb) después de su ejecución. Consulte también la salida de la consola del código de muestra que se proporciona a continuación para obtener una referencia.

![todo:imagen_alternativa_texto](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Código de muestra**

El siguiente código funcionará para los archivos XLSB y XLS al cargar y guardar archivos con la extensión adecuada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Salida de consola**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
