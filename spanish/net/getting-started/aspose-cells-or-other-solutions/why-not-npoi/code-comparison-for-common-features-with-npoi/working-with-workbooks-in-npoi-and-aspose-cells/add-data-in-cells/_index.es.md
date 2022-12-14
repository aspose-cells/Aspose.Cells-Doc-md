---
title: Agregar Datos en Cells
type: docs
weight: 10
url: /es/net/add-data-in-cells/
---
## **Aspose.Cells - Agregar datos en Cells**
Aspose.Cells proporciona una clase, Workbook, que representa un archivo de Excel Microsoft. La clase Workbook contiene una WorksheetCollection que permite el acceso a cada hoja de trabajo en el archivo de Excel. Una hoja de trabajo está representada por la clase Worksheet. La clase Worksheet proporciona una colección Cells. Cada elemento de la colección Cells representa un objeto de la clase Cell.

**C#**

{{< highlight "cs" >}}

 // Instanciando un objeto Workbook

Libro de trabajo libro de trabajo = nuevo libro de trabajo ();

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
## **NPOI HSSF XSSF - Agregar datos en Cells**
En NPOI, se puede usar row.createCell(1).setCellValue para agregar datos en las celdas.

**C#**

{{< highlight "cs" >}}

 Libro de trabajo IWorkbook = new XSSFWorkbook();

ISheet hoja1 = libro de trabajo.CreateSheet("Hoja1");

hoja1.CreateRow(0).CreateCell(0).SetCellValue("Esta es una muestra");

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
## **Descargar código de ejecución**
 Descargar**Agregar Datos en Cells** formar cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Para más detalles, visite[Agregando datos al Cells](/cells/es/net/add-data-in-cells/).

{{% /alert %}}
