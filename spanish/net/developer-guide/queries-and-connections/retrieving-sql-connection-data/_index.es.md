---
title: Recuperación de datos de conexión SQL
type: docs
weight: 10
url: /es/net/retrieving-sql-connection-data/
---

{{% alert color="primary" %}}

Aspose.Cells puede ayudarte a recuperar datos de conexión SQL. Esto incluye cualquier dato necesario para realizar una conexión al servidor SQL, por ejemplo, URL del servidor, nombre de usuario, nombre de la tabla, consulta SQL completa, tipo de consulta, ubicación de la tabla y nombre del rango con nombre asociado.

{{% /alert %}}

En Microsoft Excel, conectarse a una base de datos mediante:

1. Haga clic en el menú **Datos** y seleccione **Desde otras fuentes** seguido de **Desde SQL Server**.
1. Luego seleccione **Datos** seguido de **Conexiones**.
1. Utilice el asistente de conexiones para conectarse a la base de datos y crear una consulta de base de datos.

Aspose.Cells proporciona la propiedad Workbook.DataConnections para recuperar conexiones externas. Devuelve una colección de objetos ExternalConnection en el libro de trabajo.

Si el objeto ExternalConnection contiene datos de conexión SQL, se puede convertir en un objeto DBConnection y sus propiedades se pueden usar para recuperar el comando de la base de datos, el tipo de comando, la descripción de la conexión, la información de la conexión, las credenciales, y más.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
