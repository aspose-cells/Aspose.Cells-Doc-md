---
title: Configuraciones de protección avanzada desde Excel XP
type: docs
weight: 30
url: /es/net/advanced-protection-settings-since-excel-xp/
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

Aspose.Cells admite todas las configuraciones de protección avanzada ofrecidas por Excel XP o versiones posteriores.

### **Configuraciones de protección avanzada utilizando Excel XP y versiones posteriores**

Para ver las configuraciones de protección disponibles en Excel XP:

1. Desde el menú **Herramientas**, selecciona **Protección** seguido de **Proteger hoja**. Se mostrará un cuadro de diálogo.

Para ver las configuraciones de protección disponibles en Excel 2016

1. Desde el menú **Archivo**, selecciona **Proteger libro** seguido de **Proteger hoja actual**.
1. Selecciona **Proteger hoja** en el menú **Revisar**.

Siguiendo los pasos mencionados anteriormente se mostrará un cuadro de diálogo donde podrás permitir o restringir funciones de hojas de trabajo o aplicar una contraseña a la hoja de trabajo.

### **Configuraciones de protección avanzada utilizando Aspose.Cells**

Aspose.Cells admite todas las configuraciones de protección avanzada.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección de [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona la propiedad [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) que se utiliza para aplicar estas configuraciones avanzadas de protección. La propiedad [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) es de hecho un objeto de la clase [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra un pequeño ejemplo de aplicación. Abre un archivo de Excel y utiliza la mayoría de los ajustes de protección avanzados admitidos por Excel XP y versiones posteriores.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

Por favor, no llame al método [**Protect**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) de la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) al usar la propiedad [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection). Además, guarde el archivo en formato Excel97To2003 o Xlsx porque las configuraciones de protección avanzada solo son compatibles con Excel XP y versiones posteriores.

{{% /alert %}}

### **Problema de bloqueo de celdas**

Si desea restringir a los usuarios de editar celdas, las celdas deben estar bloqueadas antes de aplicar cualquier configuración de protección. De lo contrario, las celdas se pueden editar incluso si la hoja de cálculo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

|**Cuadro de diálogo para bloquear celdas en Excel XP**|
| :- |
|![todo:image_alt_text](advanced-protection-settings-since-excel-xp_1.png)|

También es posible bloquear celdas mediante la API de Aspose.Cells. Cada celda puede obtener formato que contiene una propiedad booleana, [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked). Establezca la propiedad [**IsLocked**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) en **true** o **false** para bloquear o desbloquear la celda.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
