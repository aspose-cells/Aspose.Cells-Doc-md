---
title: Configuraciones de protección avanzada desde Excel XP
type: docs
weight: 30
url: /es/python-net/advanced-protection-settings-since-excel-xp/
---

{{% alert color="primary" %}}

Desde el lanzamiento de Excel 2002 o XP, Microsoft ha añadido muchas configuraciones avanzadas de protección.

{{% /alert %}}

## **Introducción**

Estas configuraciones de protección restringen o permiten a los usuarios:

- Eliminar filas o columnas.
- Editar contenido, objetos o escenarios.
- Formatear celdas, filas o columnas.
- Insertar filas, columnas o hiperenlaces.
- Seleccionar celdas bloqueadas o desbloqueadas.
- Utilizar tablas dinámicas y mucho más.

Aspose.Cells para Python via .NET soporta todas las configuraciones avanzadas de protección ofrecidas por Excel XP o versiones posteriores.

### **Configuraciones de protección avanzada utilizando Excel XP y versiones posteriores**

Para ver las configuraciones de protección disponibles en Excel XP:

1. Desde el menú **Herramientas**, selecciona **Protección** seguido de **Proteger hoja**. Se mostrará un cuadro de diálogo.

Para ver las configuraciones de protección disponibles en Excel 2016

1. Desde el menú **Archivo**, selecciona **Proteger libro** seguido de **Proteger hoja actual**.
1. Selecciona **Proteger hoja** en el menú **Revisar**.

Siguiendo los pasos mencionados anteriormente se mostrará un cuadro de diálogo donde podrás permitir o restringir funciones de hojas de trabajo o aplicar una contraseña a la hoja de trabajo.

### **Configuraciones avanzadas de protección usando Aspose.Cells para Python via .NET**

Aspose.Cells para Python via .NET soporta todas las configuraciones avanzadas de protección.

Aspose.Cells para Python via .NET proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) contiene una colección [**worksheets**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) proporciona la propiedad [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) que se utiliza para aplicar estas configuraciones avanzadas de protección. La propiedad [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection) es de hecho un objeto de la clase [**Protection**](https://reference.aspose.com/cells/python-net/aspose.cells/protection) que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra un pequeño ejemplo de aplicación. Abre un archivo de Excel y utiliza la mayoría de los ajustes de protección avanzados admitidos por Excel XP y versiones posteriores.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-AdvancedProtectionSettings-1.py" >}}

{{% alert color="primary" %}}

Por favor, no llame al método [**protect**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect) de la clase [**Worksheet**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet) al usar la propiedad [**protection**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protection). Además, guarde el archivo en formato Excel97To2003 o Xlsx porque las configuraciones de protección avanzada solo son compatibles con Excel XP y versiones posteriores.

{{% /alert %}}

### **Problema de bloqueo de celdas**

Si desea restringir a los usuarios de editar celdas, las celdas deben estar bloqueadas antes de aplicar cualquier configuración de protección. De lo contrario, las celdas se pueden editar incluso si la hoja de cálculo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

|**Cuadro de diálogo para bloquear celdas en Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

También es posible bloquear celdas usando la API Aspose.Cells para Python via .NET. Cada celda puede tener un formato [**Style**](https://reference.aspose.com/cells/python-net/aspose.cells/style) que contiene una propiedad booleana, [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked). Establezca la propiedad [**is_locked**](https://reference.aspose.com/cells/python-net/aspose.cells/style/is_locked) en **true** o **false** para bloquear o desbloquear la celda.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-LockCell-1.py" >}}

