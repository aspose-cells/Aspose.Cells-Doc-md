---
title: Configuración de protección avanzada desde Excel XP
type: docs
weight: 30
url: /es/net/advanced-protection-settings-since-excel-xp/
---
{{% alert color="primary" %}}

Desde el lanzamiento de Excel 2002 o XP, Microsoft ha agregado muchas configuraciones de protección avanzadas.

{{% /alert %}}

## **Introducción**

Estas configuraciones de protección restringen o permiten a los usuarios:

- Eliminar filas o columnas.
- Edita contenidos, objetos o escenarios.
- Formato de celdas, filas o columnas.
- Inserta filas, columnas o hipervínculos.
- Seleccione celdas bloqueadas o desbloqueadas.
- Utilice tablas dinámicas y mucho más.

Aspose.Cells admite todas las configuraciones de protección avanzada que ofrece Excel XP o versiones posteriores.

### **Configuración de protección avanzada con Excel XP y versiones posteriores**

Para ver la configuración de protección disponible en Excel XP:

1.  Desde el**Instrumentos** menú, seleccione**Proteccion** seguido por**hoja de protección**. Se mostrará un cuadro de diálogo.

Para ver la configuración de protección disponible en Excel 2016

1.  Desde el**Expediente** menú, seleccione**Proteger libro de trabajo** seguido por**Proteger hoja actual**.
1.  Selecciona el**hoja de protección** en el**Revisar** menú.

Siguiendo los pasos mencionados anteriormente, se mostrará un cuadro de diálogo donde puede permitir o restringir las funciones de las hojas de trabajo o aplicar una contraseña a la hoja de trabajo.

### **Configuración de protección avanzada usando Aspose.Cells**

Aspose.Cells admite todas las configuraciones de protección avanzada.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/worksheetcollection) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)clase.

 los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet)la clase proporciona la[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) propiedad que se utiliza para aplicar esta configuración de protección avanzada. los[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) la propiedad es de hecho un objeto de la[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/protection)clase que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra una pequeña aplicación de ejemplo. Abre un archivo de Excel y utiliza la mayoría de las configuraciones de protección avanzadas compatibles con Excel XP y versiones posteriores.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-AdvancedProtectionSettings-1.cs" >}}

{{% alert color="primary" %}}

 Por favor, no llame al[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase'[**Proteger**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/protect/index) método cuando se utiliza el[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)propiedad. Además, guarde el archivo en formato Excel97To2003 o Xlsx porque la configuración de protección avanzada solo es compatible con Excel XP y versiones posteriores.

{{% /alert %}}

### **Cell Problema de bloqueo**

Si desea restringir que los usuarios editen celdas, las celdas deben bloquearse antes de que se aplique cualquier configuración de protección. De lo contrario, las celdas se pueden editar incluso si la hoja de trabajo está protegida. En Microsoft Excel XP, las celdas se pueden bloquear a través del siguiente cuadro de diálogo:

|**Diálogo para bloquear celdas en Excel XP**|
|:- |
|![todo:imagen_alternativa_texto](advanced-protection-settings-since-excel-xp_1.png)|

También es posible bloquear celdas usando el Aspose.Cells API. Cada celda puede obtener[**Estilo**](https://reference.aspose.com/cells/net/aspose.cells/style) formato que contiene una propiedad booleana,[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) . Selecciona el[**Está bloqueado**](https://reference.aspose.com/cells/net/aspose.cells/style/properties/islocked) propiedad a**verdadero** o**falso** para bloquear o desbloquear la celda.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-Security-LockCell-1.cs" >}}
