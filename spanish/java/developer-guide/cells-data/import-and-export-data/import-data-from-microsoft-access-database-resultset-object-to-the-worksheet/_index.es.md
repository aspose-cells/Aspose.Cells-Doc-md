---
title: Importar Datos del Objeto ResultSet de la Base de Datos de Microsoft Access a la Hoja de Cálculo
type: docs
weight: 200
url: /es/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---

## **Escenarios de uso posibles**
Aspose.Cells puede importar datos a las hojas de cálculo desde un objeto ResultSet que puede crearse desde cualquier base de datos. Sin embargo, este artículo específicamente crea un objeto ResultSet desde la Base de Datos de Microsoft Access. Dado que el código es el mismo para todos los tipos de bases de datos, puedes usarlo en general.
## **UCanAccess - Requerido para Conectar con la Base de Datos de Microsoft Access**
Por favor, descarga [UCanAccess](http://ucanaccess.sourceforge.net/site.html). Incluye los siguientes archivos JAR. Agrégalos todos en el classpath.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Para obtener más ayuda, por favor visita este enlace de Stack Overflow.

- [Agregando Manualmente los JARs a tu Proyecto](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Archivo de Base de Datos de Microsoft Access 2016 de Muestra utilizado en el Código de Muestra**
El siguiente archivo de base de datos de muestra de Microsoft Access 2016 se usó dentro del código de muestra. Puede utilizar cualquier archivo de base de datos o crear el suyo propio.

- [Students.accdb](48496712.accdb)

La siguiente captura de pantalla muestra el archivo de base de datos cuando se abre en Microsoft Access 2016.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importar Datos del Objeto ResultSet de la Base de Datos de Microsoft Access a la Hoja de Cálculo.**
El siguiente código de muestra ejecuta la consulta SQL desde la Base de Datos de Microsoft Access y crea un objeto ResultSet. Luego importa datos desde el objeto ResultSet a la hoja de cálculo utilizando el método [Worksheet.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)). La primera vez, utiliza índices de fila y columna y luego utiliza el nombre de la celda para importar datos a la hoja de cálculo. Finalmente, guarda el libro como un [Archivo de Excel de Salida](48496713.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo de Excel de salida para su referencia.

![todo:image_alt_text](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
