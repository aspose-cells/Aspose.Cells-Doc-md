---
title: Tabla dinámica y datos fuente
type: docs
weight: 30
url: /es/python-net/pivot-table-and-source-data/
description: Este artículo muestra cómo cambiar los datos fuente de una tabla dinámica con Aspose.Cells para Python via .NET.
keywords: Aspose.Cells para Python Excel, biblioteca de Python de Excel, Cómo cambiar los datos fuente de la tabla dinámica mediante la biblioteca de Excel Aspose.Cells para Python.
---

## **Datos fuente de la tabla dinámica**

Hay momentos en los que deseas crear informes de Microsoft Excel con tablas dinámicas que toman datos de diferentes fuentes de datos (como una base de datos) que no se conocen en el momento del diseño. Este artículo proporciona un enfoque para cambiar dinámicamente la fuente de datos de una tabla dinámica.

### **Cambio de la fuente de datos de una tabla dinámica**

1. Crear una nueva plantilla de diseño.
   1. Crea un nuevo archivo de plantilla de diseñador como se muestra en la captura de pantalla a continuación.
   1. Luego define un rango nombrado, **DataSource**, que se refiere a este rango de celdas.

      **Creando una plantilla de diseñador y definiendo un rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_1.png)

1. Crear una tabla dinámica basada en este rango nombrado.
   1. En Microsoft Excel, elige **Datos**, luego **Tabla Dinámica** y **Informe de Tabla Dinámica**.
   1. Crear una tabla dinámica basada en el rango nombrado creado en el primer paso.

      **Creando una tabla dinámica basada en el rango nombrado, DataSource** 

![todo:image_alt_text](pivot-table-and-source-data_2.png)


   1. Arrastra el campo correspondiente a la fila y columna de la tabla dinámica, luego crea la tabla dinámica resultante como en la captura de pantalla a continuación.

   **Creando una tabla dinámica basada en un campo correspondiente** 

![todo:image_alt_text](pivot-table-and-source-data_3.png)


1. Haz clic derecho en la tabla dinámica y selecciona **Opciones de Tabla**.
   1. Marca **Actualizar al abrir** en la configuración de **Opciones de Datos**.

      **Configuración de las opciones de la tabla dinámica** 

![todo:image_alt_text](pivot-table-and-source-data_4.png)


Ahora, puedes guardar este archivo como tu archivo de plantilla de diseñador.

1. Poblar nuevos datos y cambiar la fuente de datos de una tabla dinámica.
   1. Una vez que se haya creado la plantilla de diseñador, utiliza el siguiente código para cambiar la fuente de datos de la tabla dinámica.

La ejecución del código de ejemplo a continuación cambia los datos fuente de la tabla dinámica.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PivotTable-ChangeSourceData-1.py" >}}

