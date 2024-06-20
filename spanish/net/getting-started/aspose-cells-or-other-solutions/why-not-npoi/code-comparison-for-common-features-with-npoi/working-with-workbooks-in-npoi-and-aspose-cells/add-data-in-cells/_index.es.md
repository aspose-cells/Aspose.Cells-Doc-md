---
title: Agregar Datos en Celdas
type: docs
weight: 10
url: /es/net/add-data-in-cells/
description: Este artículo explica cómo agregar datos en celdas usando las APIs Aspose.Cells for .NET.
keywords: C# Agregar Datos en Celdas, C# Insertar Datos en Hoja de Trabajo, C# Establecer Datos de Celda.
---


## **Cómo Agregar Datos en Celdas Usando Aspose.Cells for .NET**
Aspose.Cells proporciona una clase, Workbook, que representa un archivo de Microsoft Excel. La clase Workbook contiene una WorksheetCollection que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una colección de celdas. Cada elemento en la colección de celdas representa un objeto de la clase Cell.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i <= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - Agregar Datos en Celdas**
En NPOI se puede utilizar row.createCell(1).setCellValue para agregar datos en celdas.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");

int x = 1;

for (int i = 1; i <= 15; i++)

{

	IRow row = sheet1.CreateRow(i);

	for (int j = 0; j < 15; j++)

	{

		row.CreateCell(j).SetCellValue(x++);

	}

}

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Agregar Datos en Celdas** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Para más detalles, visita [Agregar Datos en Celdas](/cells/es/net/add-data-in-cells/).

{{% /alert %}}
