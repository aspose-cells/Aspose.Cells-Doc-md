---
title: Recuperación de datos de conexión SQL
type: docs
weight: 20
url: /es/java/retrieving-sql-connection-data/
---

{{% alert color="primary" %}} 

Aspose.Cells puede ayudarlo a recuperar datos de conexión SQL. Esto incluye cualquier dato requerido para realizar una conexión con el servidor SQL, como la **URL del servidor**, el **nombre de usuario**, el **nombre de la tabla**, la **consulta SQL completa**, el **tipo de consulta**, la **ubicación de la tabla** y el **nombre del rango con nombre** asociado con ella.

{{% /alert %}} 

En Microsoft Excel, conectarse a una base de datos mediante:

1. Haga clic en el menú **Datos** y seleccione **Desde otras fuentes** seguido de **Desde SQL Server**.
1. Luego seleccione **Datos** seguido de **Conexiones**.
1. Utilice el asistente de conexiones para conectarse a la base de datos y crear una consulta de base de datos.

**Mostrando la opción de conexión SQL en Microsoft Excel** 

![todo:image_alt_text](retrieving-sql-connection-data_1.png)

Aspose.Cells proporciona el método Workbook.getDataConnections() para recuperar conexiones externas. Devuelve una colección de objetos ExternalConnection en el libro de trabajo.

Si el objeto ExternalConnection contiene datos de conexión SQL, puede ser convertido en un objeto DBConnection y sus propiedades utilizadas para recuperar el comando de base de datos, el tipo de comando, la descripción de la conexión, la información de la conexión, las credenciales, y más.







{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RetrieveSQLConnectionData-RetrieveSQLConnectionData.java" >}}






{{< app/cells/assistant language="java" >}}
