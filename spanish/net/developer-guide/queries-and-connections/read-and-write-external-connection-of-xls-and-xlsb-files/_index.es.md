---
title: Leer y Escribir Conexión Externa de Archivos XLS y XLSB
type: docs
weight: 80
url: /es/net/read-and-write-external-connection-of-xls-and-xlsb-files/
---

## **Escenarios de uso posibles**

Aspose.Cells ya admite la lectura y escritura de conexiones externas de archivos XLSX, pero ahora también admite esta característica para archivos XLSB y XLS. Sin embargo, el código es el mismo para todos los tipos de formatos.

## **Leer y Escribir Conexión Externa de Archivo XLS/XLSB**

El siguiente código de ejemplo carga el archivo de ejemplo XLSB (también se puede cargar XLS) y lee su primera conexión externa, que es en realidad una conexión de base de datos Microsoft Access. Luego modifica la propiedad [**DBConnection.Name**](https://reference.aspose.com/cells/net/aspose.cells.externalconnections/externalconnection/properties/name) y lo guarda como archivo de salida XLS/XLSB. La captura de pantalla muestra el efecto del código en el [archivo de ejemplo XLSB](51740722.xlsb) y el [archivo de salida XLSB](51740723.xlsb) después de su ejecución. También consulte la salida de consola del código de ejemplo que se muestra a continuación para obtener una referencia.

![todo:image_alt_text](read-and-write-external-connection-of-xls-and-xlsb-files_1.png)

## **Código de muestra**

El siguiente código funcionará tanto para archivos XLSB como para archivos XLS cargándolos y guardándolos con la extensión apropiada.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.cs" >}}

## **Salida de la consola**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
