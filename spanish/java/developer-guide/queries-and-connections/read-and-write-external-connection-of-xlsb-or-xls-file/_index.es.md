---
title: Leer y Escribir Conexión Externa de Archivo XLSB o XLS
type: docs
weight: 80
url: /es/java/read-and-write-external-connection-of-xlsb-or-xls-file/
---

## **Escenarios de uso posibles**

Aspose.Cells ya admite la lectura y escritura de conexión externa de archivos XLSX, pero ahora también admite esta función para archivos XLSB y XLS. Sin embargo, el código es el mismo para ambos tipos de formato.

## **Leer y Escribir Conexión Externa de Archivo XLSB/XLS**

El siguiente código de ejemplo carga el archivo XLSB de ejemplo (también se puede cargar XLS) y lee su primera Conexión Externa que es en realidad una Conexión de Base de Datos de Microsoft Access. Luego modifica la propiedad [**DBConnection.Name**](https://reference.aspose.com/cells/java/com.aspose.cells/dbconnection#Name) y lo guarda como archivo XLSB de salida. La captura de pantalla muestra el efecto del código en el [archivo XLSB de ejemplo](51740743.xlsb) y el [archivo XLSB de salida](51740742.xlsb) después de su ejecución. También consulte la salida de consola del código de ejemplo que se muestra a continuación para su referencia.

![todo:image_alt_text](read-and-write-external-connection-of-xlsb-or-xls-file_1.png)

## **Código de muestra**

El siguiente código funcionará tanto para XLSB como para XLS al cargar y guardar archivos con la extensión adecuada.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-ReadAndWriteExternalConnectionOfXLSBFile.java" >}}

## **Salida de la consola**

{{< highlight java >}}

Connection Name: Cust

Command: Customer

Connection Info: Provider=Microsoft.ACE.OLEDB.12.0;Password="";User ID=Admin;Data Source=C:\TempSha\Cust.accdb;Mode=Share Deny Write;Extended Properties="";Jet OLEDB:System database="";Jet OLEDB:Registry Path="";Jet OLEDB:Database Password="";Jet OLEDB:Engine Type=6;Jet OLEDB:Database Locking Mode=0;Jet OLEDB:Global Partial Bulk Ops=2;Jet OLEDB:Global Bulk Transactions=1;Jet OLEDB:New Database Password="";Jet OLEDB:Create System Database=False;Jet OLEDB:Encrypt Database=False;Jet OLEDB:Don't Copy Locale on Compact=False;Jet OLEDB:Compact Without Replica Repair=False;Jet OLEDB:SFP=False;Jet OLEDB:Support Complex Data=False;Jet OLEDB:Bypass UserInfo Validation=False;Jet OLEDB:Limited DB Caching=False;Jet OLEDB:Bypass ChoiceField Validation=False

{{< /highlight >}}
