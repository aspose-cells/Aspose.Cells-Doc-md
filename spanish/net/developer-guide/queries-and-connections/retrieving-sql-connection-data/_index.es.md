---
title: Recuperación de datos de conexión SQL
type: docs
weight: 10
url: /es/net/retrieving-sql-connection-data/
---
{{% alert color="primary" %}}

 Aspose.Cells puede ayudarlo a recuperar datos de conexión SQL. Esto incluye todos y cada uno de los datos necesarios para establecer una conexión con el servidor SQL, por ejemplo,**URL del servidor**, **nombre de usuario**, **nombre de la tabla**, **consulta SQL completa**, **Tipo de consulta**, **ubicación de la mesa** , y**nombre del rango nombrado** asociado a ello.

{{% /alert %}}

En Microsoft Excel, conéctese a una base de datos mediante:

1.  Al hacer clic en el**Datos** menú y seleccionando**De otras fuentes** seguido por**Desde el servidor SQL**.
1.  Luego seleccione**Datos** seguido por**Conexiones**.
1. Utilice el asistente de conexiones para conectarse a la base de datos y crear una consulta de base de datos.

Aspose.Cells proporciona la propiedad Workbook.DataConnections para recuperar conexiones externas. Devuelve una colección de objetos ExternalConnection en el libro de trabajo.

Si el objeto ExternalConnection contiene datos de conexión SQL, se puede asignar a un objeto DBConnection y sus propiedades se pueden usar para recuperar el comando de la base de datos, el tipo de comando, la descripción de la conexión, la información de la conexión, las credenciales, etc.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManageDatabaseConnection-RetrievingSQLConnectionData-1.cs" >}}
