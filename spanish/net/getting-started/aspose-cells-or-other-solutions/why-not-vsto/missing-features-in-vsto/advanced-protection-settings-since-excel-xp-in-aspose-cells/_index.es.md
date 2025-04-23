---
title: Configuraciones de protección avanzada desde Excel XP en Aspose.Cells
type: docs
weight: 20
url: /es/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---

{{% alert color="primary" %}}

- Eliminar filas o columnas.
- Editar contenido, objetos o escenarios.
- Formatear celdas, filas o columnas.
- Insertar filas, columnas o hiperenlaces.
- Seleccionar celdas bloqueadas o desbloqueadas.
- Utilizar tablas dinámicas y mucho más.

Aspose.Cells admite todas las configuraciones de protección avanzada ofrecidas por Excel XP o versiones posteriores.

{{% /alert %}}

## **Configuraciones de protección avanzada utilizando Excel XP y versiones posteriores**

Para ver las configuraciones de protección disponibles en Excel XP:

1. Desde el menú **Herramientas**, seleccione **Proteger** seguido de **Proteger hoja**.
   Se muestra un cuadro de diálogo.

   **Cuadro de diálogo para mostrar opciones de protección en Excel XP**

![todo:image_alt_text](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Permitir o restringir funciones de las hojas de cálculo o aplicar una contraseña.

### **Configuraciones de protección avanzada utilizando Aspose.Cells**

Aspose.Cells soporta todas las configuraciones de protección avanzada.

Aspose.Cells proporciona una clase, [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook), que representa un archivo de Microsoft Excel. La clase [**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook) contiene una colección [**Worksheets**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet).

La clase [**Worksheet**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) proporciona la propiedad [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) que se utiliza para aplicar estas configuraciones de protección avanzada. La propiedad [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) es de hecho un objeto de la clase [**Protection**](https://reference.aspose.com/cells/net/aspose.cells/protection) que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra un pequeño ejemplo de aplicación. Abre un archivo de Excel y utiliza la mayoría de los ajustes de protección avanzados admitidos por Excel XP y versiones posteriores.

**C#**

{{< highlight csharp >}}

 //Creating a file stream containing the Excel file to be opened

FileStream fstream = new FileStream("book1.xls", FileMode.Open);

//Instantiating a Workbook object

//Opening the Excel file through the file stream

Workbook excel = new Workbook(fstream);

//Accessing the first worksheet in the Excel file

Worksheet worksheet = excel.Worksheets[0];

//Restricting users to delete columns of the worksheet

worksheet.Protection.AllowDeletingColumn = false;

//Restricting users to delete row of the worksheet

worksheet.Protection.AllowDeletingRow = false;

//Restricting users to edit contents of the worksheet

worksheet.Protection.AllowEditingContent = false;

//Restricting users to edit objects of the worksheet

worksheet.Protection.AllowEditingObject = false;

//Restricting users to edit scenarios of the worksheet

worksheet.Protection.AllowEditingScenario = false;

//Restricting users to filter

worksheet.Protection.AllowFiltering = false;

//Allowing users to format cells of the worksheet

worksheet.Protection.AllowFormattingCell = true;

//Allowing users to format rows of the worksheet

worksheet.Protection.AllowFormattingRow = true;

//Allowing users to insert columns in the worksheet

worksheet.Protection.AllowFormattingColumn = true;

//Allowing users to insert hyperlinks in the worksheet

worksheet.Protection.AllowInsertingHyperlink = true;

//Allowing users to insert rows in the worksheet

worksheet.Protection.AllowInsertingRow = true;

//Allowing users to select locked cells of the worksheet

worksheet.Protection.AllowSelectingLockedCell = true;

//Allowing users to select unlocked cells of the worksheet

worksheet.Protection.AllowSelectingUnlockedCell = true;

//Allowing users to sort

worksheet.Protection.AllowSorting = true;

//Allowing users to use pivot tables in the worksheet

worksheet.Protection.AllowUsingPivotTable = true;

//Saving the modified Excel file

excel.Save("output.xls", SaveFormat.Excel97To2003);

//Closing the file stream to free all resources

fstream.Close();

{{< /highlight >}}

## **Descargar Código en Ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Descargar Código de Ejemplo**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
{{< app/cells/assistant language="csharp" >}}
