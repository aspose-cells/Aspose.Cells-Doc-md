---
title: Tabla dinámica y datos de origen
type: docs
weight: 30
url: /es/net/pivot-table-and-source-data/
---
## **Datos de origen de la tabla dinámica**

Hay momentos en los que desea crear Microsoft informes de Excel con tablas dinámicas que toman datos de diferentes fuentes de datos (como una base de datos) que no se conocen en el momento del diseño. Este artículo proporciona un enfoque para cambiar dinámicamente la fuente de datos de una tabla dinámica.

### **Cambiar los datos de origen de una tabla dinámica**

1. Creación de una nueva plantilla de diseñador.
1. Cree un nuevo archivo de plantilla de diseñador como se muestra en la siguiente captura de pantalla.
 1. Luego defina un rango con nombre,**Fuente de datos**, que se refiere a este rango de celdas.

      **Creando una plantilla de diseñador y definiendo un rango con nombre, DataSource** 

![todo:imagen_alternativa_texto](pivot-table-and-source-data_1.png)
   
1. Creación de una tabla dinámica basada en este rango con nombre.
 1. En Microsoft Excel, elija**Datos** , después**Tabla dinámica** y**Informe de gráfico dinámico**.
 1. Cree una tabla dinámica basada en el rango con nombre creado en el primer paso.

      **Creación de una tabla dinámica basada en el rango con nombre, DataSource** 

![todo:imagen_alternativa_texto](pivot-table-and-source-data_2.png)

   
 1. Arrastre el campo correspondiente a la fila y columna de la tabla dinámica, luego cree la tabla dinámica resultante como se muestra en la siguiente captura de pantalla.

   **Crear una tabla dinámica basada en un campo correspondiente** 

![todo:imagen_alternativa_texto](pivot-table-and-source-data_3.png)

   
1.  Haga clic derecho en la tabla dinámica y seleccione**Opciones de mesa**.
 1. Comprobar**Actualizar al abrir** en**Opciones de datos** ajustes.

      **Configuración de las opciones de la tabla dinámica** 

![todo:imagen_alternativa_texto](pivot-table-and-source-data_4.png)


Ahora, puede guardar este archivo como su archivo de plantilla de diseñador.

1. Rellenar nuevos datos y cambiar los datos de origen de una tabla dinámica.
1. Una vez que se crea la plantilla del diseñador, use el siguiente código para cambiar los datos de origen de la tabla dinámica.

Ejecutar el código de ejemplo a continuación cambia los datos de origen de la tabla dinámica.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-PivotTable-ChangeSourceData-1.cs" >}}

