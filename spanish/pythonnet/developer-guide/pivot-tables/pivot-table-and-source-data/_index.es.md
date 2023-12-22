---
title: Tabla dinámica y datos de origen
type: docs
weight: 30
url: /es/python-net/pivot-table-and-source-data/
description: Este artículo muestra cómo cambiar los datos de origen de la tabla dinámica con Aspose.Cells for Python via .NET.
keywords: Change Pivot Table's Source Data
---
##  **Datos de origen de la tabla dinámica**

Hay ocasiones en las que desea crear Microsoft informes de Excel con tablas dinámicas que toman datos de diferentes fuentes de datos (como una base de datos) que no se conocen en el momento del diseño. Este artículo proporciona un enfoque para cambiar dinámicamente la fuente de datos de una tabla dinámica.

###  **Cambiar los datos de origen de una tabla dinámica**

1. Creando una nueva plantilla de diseñador.
 1. Cree un nuevo archivo de plantilla de diseñador como se muestra en la captura de pantalla siguiente.
 1. Luego defina un rango con nombre, *DataSource**, que haga referencia a este rango de celdas.

      **Crear una plantilla de diseñador y definir un rango con nombre, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)
   
1. Crear una tabla dinámica basada en este rango con nombre.
1. En Microsoft Excel, elija**Datos**, luego **Tabla dinámica** y *Informe de gráfico dinámico**.
 1. Cree una tabla dinámica basada en el rango con nombre creado en el primer paso.

      **Crear una tabla dinámica basada en el rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)

   
 1. Arrastre el campo correspondiente a la fila y columna de la tabla dinámica, luego cree la tabla dinámica resultante como se muestra en la captura de pantalla siguiente.

   **Crear una tabla dinámica basada en un campo correspondiente** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)

   
1. Haga clic derecho en la tabla dinámica y seleccione *Opciones de tabla**.
 1. comprobar**Actualizar al abrir** en**Opciones de datos** ajustes.

      **Configurar las opciones de la tabla dinámica** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Ahora puede guardar este archivo como su archivo de plantilla de diseñador.

1. Completar nuevos datos y cambiar los datos de origen de una tabla dinámica.
 1. Una vez creada la plantilla del diseñador, utilice el siguiente código para cambiar los datos de origen de la tabla dinámica.

La ejecución del código de ejemplo siguiente cambia los datos de origen de la tabla dinámica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

