---
title: Lectura y escritura de archivos DBF
description: Aspose.Cells es una biblioteca .NET para trabajar con archivos de hojas de cálculo, que admite la lectura y escritura de archivos dBASE III y IV (DBF). Este artículo explica cómo importar datos desde y exportar datos a archivos DBF usando Aspose.Cells, incluyendo detalles del formato de archivo, características compatibles y ejemplos paso a paso.
keywords: Aspose.Cells, biblioteca .NET, DBF, dBASE, leer DBF, escribir DBF, importar DBF, exportar DBF, formato de archivo, .dbf
type: docs
weight: 200
url: /es/net/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells ofrece soporte completo para la lectura y escritura de archivos DBF (dBASE). Puede cargar archivos dBASE III y dBASE IV existentes en un objeto Workbook, manipular los datos utilizando la rica API de Aspose.Cells y guardar el libro de trabajo de vuelta en formato DBF para su uso con aplicaciones de bases de datos heredadas.

{{% /alert %}}

## **Introducción**

DBF (DataBase File) es un formato de archivo de base de datos heredado introducido originalmente por dBASE a principios de la década de 1980. A pesar de la antigüedad del formato, los archivos DBF todavía se utilizan ampliamente en muchas industrias para almacenar datos estructurados, particularmente en contabilidad, SIG y otras aplicaciones especializadas. Aspose.Cells le permite integrar estos archivos heredados en flujos de trabajo modernos de hojas de cálculo .NET sin problemas.

La biblioteca admite tanto la lectura como la escritura de archivos DBF, brindándole la capacidad de:

- Importar datos desde archivos DBF existentes en objetos Workbook de Aspose.Cells para su procesamiento posterior o conversión a otros formatos.
- Crear nuevos archivos DBF desde cero o transformando datos desde otros formatos de hojas de cálculo.
- Mantener definiciones de campos, tipos de datos y estructuras de registros al transferir datos hacia y desde el formato DBF.

Los archivos DBF también se pueden abrir directamente en Microsoft Excel y otras aplicaciones de hojas de cálculo, lo que los convierte en un puente conveniente entre los sistemas heredados y las herramientas modernas de hojas de cálculo.

## **Versiones y características de DBF compatibles**

Aspose.Cells admite las siguientes versiones del formato DBF:

- **dBASE III** — La variante original y más ampliamente compatible del formato DBF.
- **dBASE IV** — Una versión extendida que admite tipos de datos adicionales y tamaños de campo mayores.

### Características compatibles

La biblioteca ofrece soporte integral para las siguientes operaciones:

- Lectura de datos DBF en un objeto Workbook, con todos los registros y definiciones de campos preservados.
- Escritura de datos del libro de trabajo de vuelta al formato DBF para exportación a aplicaciones compatibles con dBASE.
- Manejo de tipos de datos comunes utilizados en archivos DBF, incluyendo campos de carácter, numéricos, de fecha y lógicos.
- Preservación de las definiciones de campos como nombre, tipo y longitud durante las operaciones de lectura/escritura.

### Limitaciones y consideraciones

Cuando trabaje con archivos DBF, tenga en cuenta las siguientes restricciones:

- El número máximo de campos por archivo es **128**.
- El tamaño máximo de registro es **4000 bytes**.
- Los nombres de campo están limitados a **10 caracteres**, deben estar en mayúsculas y no pueden contener espacios.
- Los valores de fecha en los archivos DBF se almacenan en formato `YYYYMMDD`.
- La codificación de caracteres puede variar según la aplicación de origen (comúnmente Windows-1252 o páginas de código OEM).

## **Leer un archivo DBF**

Aspose.Cells facilita la carga de datos desde un archivo DBF en un objeto Workbook. La biblioteca utiliza la clase `LoadOptions` para especificar el formato de origen, asegurando que los datos se interpreten correctamente durante el proceso de carga.

### Leer un archivo DBF con Aspose.Cells

Para leer un archivo DBF, debe crear una instancia de `LoadOptions`, establecer su propiedad `LoadFormat` en `LoadFormat.Dbf` y pasarla al constructor `Workbook` junto con la ruta del archivo. Una vez cargado, los datos son accesibles a través de la colección `Worksheets`, donde puede iterar a través de las celdas, extraer valores o manipular los datos según sea necesario.

El siguiente ejemplo muestra cómo cargar un archivo DBF existente en Aspose.Cells, acceder a su primera hoja de cálculo y leer los valores de las celdas.

```csharp
using System;
using System.IO;
using System.Text;
using Aspose.Cells;

string dataDir = "Data/";
string filePath = Path.Combine(dataDir, "example.dbf");

LoadOptions loadOptions = new LoadOptions(LoadFormat.Dbf);

Workbook workbook = new Workbook(filePath, loadOptions);

Worksheet worksheet = workbook.Worksheets[0];

Cells cells = worksheet.Cells;

StringBuilder sb = new StringBuilder();

int maxRow = cells.MaxDataRow;
int maxCol = cells.MaxDataColumn;

for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells[i, j];
        string value = cell.StringValue;
        sb.Append("|").Append(value);
    }
    sb.Append("|").AppendLine();
}

Console.WriteLine(sb.ToString());

string outputPath = Path.Combine(dataDir, "output.xlsx");
workbook.Save(outputPath, SaveFormat.Xlsx);

Console.WriteLine("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}

Puede abrir archivos DBF directamente en Microsoft Excel seleccionando el archivo en el cuadro de diálogo Abrir. Excel tratará el archivo DBF como una hoja de cálculo, mostrando sus registros en un diseño tabular. Esto es útil para verificar rápidamente los datos después de leerlos o escribirlos con Aspose.Cells.

{{% /alert %}}

## **Escribir un archivo DBF**

Escribir datos en un archivo DBF sigue un patrón similar al de guardar cualquier otro formato de hoja de cálculo con Aspose.Cells. Cree o cargue un Workbook, rellene la hoja de cálculo con datos y luego llame al método `Save` especificando `SaveFormat.Dbf` como formato de destino.

### Escribir un archivo DBF con Aspose.Cells

Para crear un archivo DBF, siga estos pasos:

1. Cree una nueva instancia de `Workbook`.
2. Acceda a la primera hoja de cálculo de la colección `Worksheets`.
3. Rellene la hoja de cálculo con sus datos, incluyendo los encabezados en la primera fila y los registros en las filas siguientes.
4. Llame al método `Workbook.Save`, pasando la ruta del archivo y `SaveFormat.Dbf` como parámetros.

El siguiente ejemplo muestra cómo crear un nuevo archivo DBF desde cero. Rellena una hoja de cálculo con datos de muestra que contienen diferentes tipos de datos (cadenas, números y fechas) para ilustrar cómo se manejan los tipos de campo al exportar al formato DBF.

```csharp
using System;
using System.IO;
using Aspose.Cells;

string outputDir = @"C:\Output\";
string filePath = Path.Combine(outputDir, "output.dbf");

if (!Directory.Exists(outputDir))
{
    Directory.CreateDirectory(outputDir);
}

Workbook workbook = new Workbook();
Worksheet worksheet = workbook.Worksheets[0];
Cells cells = worksheet.Cells;

// Encabezados de columna
cells[0, 0].PutValue("ID");
cells[0, 1].PutValue("Name");
cells[0, 2].PutValue("Department");
cells[0, 3].PutValue("Salary");
cells[0, 4].PutValue("HireDate");

// Fila de datos 1
cells[1, 0].PutValue(101);
cells[1, 1].PutValue("John Smith");
cells[1, 2].PutValue("Engineering");
cells[1, 3].PutValue(75000.50);
cells[1, 4].PutValue(new DateTime(2020, 3, 15));

// Fila de datos 2
cells[2, 0].PutValue(102);
cells[2, 1].PutValue("Jane Doe");
cells[2, 2].PutValue("Marketing");
cells[2, 3].PutValue(68000.75);
cells[2, 4].PutValue(new DateTime(2019, 7, 22));

// Fila de datos 3
cells[3, 0].PutValue(103);
cells[3, 1].PutValue("Bob Johnson");
cells[3, 2].PutValue("Finance");
cells[3, 3].PutValue(82000.00);
cells[3, 4].PutValue(new DateTime(2021, 1, 10));

// Fila de datos 4
cells[4, 0].PutValue(104);
cells[4, 1].PutValue("Alice Brown");
cells[4, 2].PutValue("Human Resources");
cells[4, 3].PutValue(71000.25);
cells[4, 4].PutValue(new DateTime(2018, 11, 5));

// Fila de datos 5
cells[5, 0].PutValue(105);
cells[5, 1].PutValue("Charlie Wilson");
cells[5, 2].PutValue("Operations");
cells[5, 3].PutValue(79500.80);
cells[5, 4].PutValue(new DateTime(2022, 5, 30));

// Establecer anchos de columna para mejor legibilidad
worksheet.Cells.SetColumnWidth(0, 8);
worksheet.Cells.SetColumnWidth(1, 20);
worksheet.Cells.SetColumnWidth(2, 20);
worksheet.Cells.SetColumnWidth(3, 12);
worksheet.Cells.SetColumnWidth(4, 14);

workbook.Save(filePath, SaveFormat.Dbf);
```

{{% alert color="primary" %}}

Al escribir datos en un archivo DBF, asegúrese de que sus datos se ajusten a las limitaciones del formato. Los nombres de campo no deben tener más de 10 caracteres y no deben contener espacios. Los registros que excedan los 4000 bytes en total no se guardarán correctamente. Las fechas deben ser valores de fecha válidos que puedan representarse en formato YYYYMMDD.

{{% /alert %}}

## **Consideraciones sobre tipos de datos y formato**

Al transferir datos entre Aspose.Cells y el formato DBF, es importante comprender cómo se asignan los tipos de datos entre los dos sistemas para garantizar la integridad de los datos.

### Tipos de celda a tipos de campo DBF

Los valores de las celdas de Aspose.Cells se convierten automáticamente a los tipos de campo DBF apropiados al guardar:

- Las **cadenas** se asignan a campos de carácter (C).
- Los **valores numéricos** (enteros y decimales) se asignan a campos numéricos (N).
- Los **valores de fecha** se asignan a campos de fecha (D) en formato `YYYYMMDD`.
- Los **valores booleanos** se asignan a campos lógicos (L).

### Codificación

Los archivos DBF pueden usar diferentes codificaciones de caracteres según la aplicación que los haya creado. Aspose.Cells maneja la codificación de forma transparente en la mayoría de los casos, pero si encuentra problemas de visualización de caracteres, es posible que necesite verificar la codificación del archivo de origen.

### Reglas para nombres de campo

Los nombres de campo DBF deben cumplir las siguientes reglas:

- Longitud máxima de 10 caracteres.
- Deben comenzar con una letra.
- No pueden contener espacios ni caracteres especiales.
- Se almacenan en mayúsculas independientemente del caso utilizado en la entrada.

### Verificación del resultado

Después de escribir un archivo DBF, puede verificar el resultado abriéndolo en Microsoft Excel o cualquier aplicación compatible con dBASE. Los datos deben aparecer en un diseño tabular con los nombres de campo como encabezados de columna, y los registros rellenados según los datos proporcionados.

## **Conversión entre DBF y otros formatos**

Uno de los casos de uso más prácticos para leer y escribir archivos DBF con Aspose.Cells es la conversión de datos entre el formato DBF y formatos modernos de hojas de cálculo como XLSX, XLS o CSV. Dado que Aspose.Cells admite una amplia gama de formatos, puede cargar fácilmente un archivo DBF y guardarlo en cualquier otro formato compatible, o viceversa.

Por ejemplo, puede leer un archivo DBF, aplicar formato o cálculos utilizando la API de Aspose.Cells y luego guardar el resultado como un archivo XLSX para distribuirlo a usuarios que trabajan con aplicaciones modernas de hojas de cálculo. Por el contrario, puede tomar datos de un archivo XLSX o CSV y exportarlos a formato DBF para integrarlos con sistemas heredados.



{{< app/cells/assistant language="csharp" >}}