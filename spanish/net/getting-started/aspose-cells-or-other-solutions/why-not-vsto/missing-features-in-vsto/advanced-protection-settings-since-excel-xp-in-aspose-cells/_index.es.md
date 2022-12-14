---
title: Configuración de protección avanzada desde Excel XP en Aspose.Cells
type: docs
weight: 20
url: /es/net/advanced-protection-settings-since-excel-xp-in-aspose-cells/
---
{{% alert color="primary" %}}

- Eliminar filas o columnas.
- Edita contenidos, objetos o escenarios.
- Formato de celdas, filas o columnas.
- Inserta filas, columnas o hipervínculos.
- Seleccione celdas bloqueadas o desbloqueadas.
- Utilice tablas dinámicas y mucho más.

Aspose.Cells admite todas las configuraciones de protección avanzada que ofrece Excel XP o versiones posteriores.

{{% /alert %}}

## **Configuración de protección avanzada con Excel XP y versiones posteriores**

Para ver la configuración de protección disponible en Excel XP:

1.  Desde el**Instrumentos** menú, seleccione**Proteccion** seguido por**hoja de protección**.
 Se muestra un cuadro de diálogo.

   **Diálogo para mostrar opciones de protección en Excel XP**

![todo:imagen_alternativa_texto](advanced-protection-settings-since-excel-xp-in-aspose-cells_1.png)

1. Permita o restrinja las funciones de las hojas de trabajo o aplique una contraseña.

### **Configuración de protección avanzada usando Aspose.Cells**

Aspose.Cells admite todas las configuraciones de protección avanzada.

 Aspose.Cells proporciona una clase,[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) , que representa un archivo de Excel Microsoft. los[**Libro de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook) la clase contiene un[**Hojas de trabajo**](https://reference.aspose.com/cells/net/aspose.cells/workbook/properties/worksheets) colección que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por el[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) clase.

 los[**Hoja de cálculo**](https://reference.aspose.com/cells/net/aspose.cells/worksheet) la clase proporciona la[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection)propiedad que se utiliza para aplicar esta configuración de protección avanzada. los[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/properties/protection) la propiedad es de hecho un objeto de la[**Proteccion**](https://reference.aspose.com/cells/net/aspose.cells/protection) clase que encapsula varias propiedades booleanas para deshabilitar o habilitar restricciones.

A continuación se muestra una pequeña aplicación de ejemplo. Abre un archivo de Excel y utiliza la mayoría de las configuraciones de protección avanzadas compatibles con Excel XP y versiones posteriores.

**C#**

{{< highlight "csharp" >}}

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

## **Descargar código de ejecución**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/tree/master/Plugins/Aspose.Cells%20Vs%20VSTO%20Spreadsheets/Aspose.Cells%20Features%20missing%20in%20VSTO/Advanced%20Protection%20Settings)

## **Descargar código de muestra**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesAsposeCellsForVSTO1.1)
