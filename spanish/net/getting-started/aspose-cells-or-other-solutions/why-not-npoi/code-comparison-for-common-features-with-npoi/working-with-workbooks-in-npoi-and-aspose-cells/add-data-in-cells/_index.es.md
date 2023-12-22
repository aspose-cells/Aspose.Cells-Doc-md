---
title: Agregar datos en Cells
type: docs
weight: 10
url: /es/net/add-data-in-cells/
description: Este artículo explica cómo agregar datos en Cells usando las API Aspose.Cells for .NET.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Cómo agregar datos en Cells usando Aspose.Cells for .NET**
Aspose.Cells proporciona una clase, Libro de trabajo, que representa un archivo Excel Microsoft. La clase Libro de trabajo contiene una Colección de hojas de trabajo que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase Hoja de trabajo. La clase Worksheet proporciona una colección de celdas. Cada elemento de la colección Cells representa un objeto de la clase Cell.

**C#**

{{< highlight "cs" >}}

 //Crear una instancia de un objeto de libro de trabajo

Libro de trabajo libro = nuevo libro de trabajo();

//Accediendo a la hoja de trabajo agregada en el archivo de Excel

Hoja de trabajo hoja de trabajo = libro de trabajo.Hojas de trabajo[0];

entero x = 1;

para (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF - Agregar datos en Cells**
En NPOI, row.createCell(1).setCellValue se puede utilizar para agregar datos en celdas.

**C#**

{{< highlight "cs" >}}

 Libro de trabajo IWorkbook = nuevo XSSFWorkbook();

ISheet hoja1 = libro de trabajo.CreateSheet("Hoja1");

hoja1.CreateRow(0).CreateCell(0).SetCellValue("Esto es una muestra");

entero x = 1;

para (int i = 1; i<= 15; i++)

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
##  **Descargar código de ejecución**
 Descargar**Agregar datos en Cells** desde cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Agregar datos a Cells](/cells/es/net/add-data-in-cells/).

{{% /alert %}}
