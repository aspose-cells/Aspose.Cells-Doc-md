---
title: Crear Nuevo Libro de Trabajo
type: docs
weight: 20
url: /es/net/create-new-workbook/
---

## **Aspose.Cells - Crear Nuevo Libro de Trabajo**
La clase Workbook está disponible para un uso sencillo

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Crear Nuevo Libro de Trabajo**
Crear un nuevo libro de trabajo usando la clase Workbook y guardarlo usando FileOutputStream.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Descargar Código en Ejecución**
Descargar **Crear Nuevo Libro de Trabajo** de cualquiera de los sitios de codificación social mencionados a continuación:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
