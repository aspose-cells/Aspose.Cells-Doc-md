---
title: Importar datos desde Microsoft Acceder al objeto ResultSet de la base de datos a la hoja de trabajo
type: docs
weight: 200
url: /es/java/import-data-from-microsoft-access-database-resultset-object-to-the-worksheet/
---
## **Posibles escenarios de uso**
Aspose.Cells puede importar datos a hojas de trabajo desde el objeto ResultSet que se puede crear desde cualquier base de datos. Sin embargo, este artículo crea específicamente un objeto ResultSet a partir de la base de datos de acceso Microsoft. Dado que el código es el mismo para todos los tipos de bases de datos, puede usarlo en general.
## **UCanAccess: necesario para conectarse a la base de datos de acceso Microsoft**
 por favor descargue[UCanAcceso](http://ucanaccess.sourceforge.net/site.html). Incluye los siguientes archivos JAR. Agréguelos todos en el classpath.

- ucanaccess-4.0.1.jar
- commons-lang-2.6.jar
- commons-logging-1.1.1.jar
- hsqldb.jar
- jackcess-2.1.6.jar

Para obtener más ayuda, visite este enlace de desbordamiento de pila.

- [Agregar manualmente los JAR a su proyecto](https://stackoverflow.com/questions/21955256/manipulating-an-access-database-from-java-without-odbc/21955257#21955257)
## **Muestra Microsoft Archivo de base de datos de Access 2016 utilizado dentro del código de muestra**
El siguiente ejemplo Microsoft Archivo de base de datos de Access 2016 se usó dentro del código de ejemplo. Puede usar cualquier archivo de base de datos o crear uno propio.

- [Estudiantes.accdb](48496712.accdb)

La siguiente captura de pantalla muestra el archivo de la base de datos cuando se abre en Microsoft Access 2016.

![todo:imagen_alternativa_texto](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_1.png)
## **Importar datos desde Microsoft Acceder al objeto ResultSet de la base de datos a la hoja de trabajo.**
 El siguiente código de ejemplo ejecuta la consulta SQL desde Microsoft Access Database y crea un objeto ResultSet. Luego importa datos del objeto ResultSet a la hoja de trabajo usando[Hoja de trabajo.getCells().importResultSet()](https://reference.aspose.com/cells/java/com.aspose.cells/cells#importResultSet\(java.sql.ResultSet,%20int,%20int,%20boolean\)) método. La primera vez, usa índices de fila y columna y luego usa el nombre de la celda para importar datos a la hoja de trabajo. Finalmente, guarda el libro de trabajo como un[Archivo de Excel de salida](48496713.xlsx). La captura de pantalla muestra el efecto del código de muestra en el archivo de salida de Excel como referencia.

![todo:imagen_alternativa_texto](import-data-from-microsoft-access-database-resultset-object-to-the-worksheet_2.png)
## **Código de muestra**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Data-ImportDataFromMicrosoftAccessDatabaseResultSetObjectToWorksheet.java" >}}
