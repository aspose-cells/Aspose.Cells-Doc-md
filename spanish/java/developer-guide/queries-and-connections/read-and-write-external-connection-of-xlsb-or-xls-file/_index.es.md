---
title: Leer y escribir conexión externa de archivo XLSB o XLS
type: docs
weight: 80
url: /es/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---
## **Posibles escenarios de uso**

Aspose.Cells ya admite la conexión externa de lectura y escritura del archivo XLSX, pero ahora también admite esta función para los archivos XLSB y XLS. Sin embargo, el código es el mismo para ambos tipos de formato.

## **Lectura y escritura de la conexión externa del archivo XLSB/XLS**

El siguiente código de muestra carga el archivo XLSB de muestra (también se puede cargar XLS) y lee su primera conexión externa, que en realidad es una conexión de base de datos de acceso Microsoft. Luego modifica la[**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name)propiedad y la guarda como archivo XLSB de salida. La captura de pantalla muestra el efecto del código en[ejemplo de archivo XLSB](51740743.xlsb)y[archivo XLSB de salida](51740742.xlsb)después de su ejecución. Consulte también la salida de la consola del código de muestra que se proporciona a continuación para obtener una referencia.

![todo:imagen_alternativa_texto](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Código de muestra**

El siguiente código funcionará tanto para XLSB como para XLS al cargar y guardar archivos con la extensión adecuada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Salida de consola**

{{< highlight "java" >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
