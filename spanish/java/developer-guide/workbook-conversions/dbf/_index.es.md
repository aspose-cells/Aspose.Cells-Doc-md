---
title: Lectura y escritura de archivos DBF
description: Aspose.Cells es una biblioteca de Java para trabajar con archivos de hojas de cálculo, que admite la lectura y escritura de archivos dBASE III y IV (DBF). Este artículo explica cómo importar datos desde y exportar datos a archivos DBF usando Aspose.Cells, incluyendo detalles del formato de archivo, características compatibles y ejemplos paso a paso.
linktitle: Lectura y escritura de DBF
url: /es/java/reading-and-writing-dbf-files/
keywords: Aspose.Cells, biblioteca de Java, DBF, dBASE, leer DBF, escribir DBF, importar DBF, exportar DBF, formato de archivo, .dbf
type: docs
weight: 200
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells ofrece soporte completo para la lectura y escritura de archivos DBF (dBASE). Puede cargar archivos existentes de dBASE III y dBASE IV en un objeto Workbook, manipular los datos usando la completa API de Aspose.Cells y guardar el libro de trabajo de vuelta en el formato DBF para su uso con aplicaciones de bases de datos heredadas.

## **Introducción**
DBF (DataBase File) es un formato de archivo de base de datos heredado introducido originalmente por dBASE a principios de la década de 1980. A pesar de la antigüedad del formato, los archivos DBF siguen utilizándose ampliamente en muchas industrias para almacenar datos estructurados, particularmente en contabilidad, SIG y otras aplicaciones especializadas. Aspose.Cells le permite integrar estos archivos heredados en los flujos de trabajo modernos de hojas de cálculo de Java sin problemas.
La biblioteca admite tanto la lectura como la escritura de archivos DBF, brindándole la capacidad de:
- Importar datos desde archivos DBF existentes a objetos Workbook de Aspose.Cells para su procesamiento posterior o conversión a otros formatos.
- Crear nuevos archivos DBF desde cero o transformando datos desde otros formatos de hojas de cálculo.
- Mantener las definiciones de los campos, los tipos de datos y las estructuras de los registros al transferir datos dentro y fuera del formato DBF.
Los archivos DBF también pueden abrirse directamente en Microsoft Excel y otras aplicaciones de hojas de cálculo, lo que los convierte en un puente conveniente entre los sistemas heredados y las herramientas modernas de hojas de cálculo.

## **Versiones y características compatibles de DBF**
Aspose.Cells admite las siguientes versiones del formato DBF:
- **dBASE III** — La variante original y más ampliamente compatible del formato DBF.
- **dBASE IV** — Una versión extendida que admite tipos de datos adicionales y tamaños de campo más grandes.

### Características compatibles
La biblioteca ofrece soporte integral para las siguientes operaciones:
- Leer datos DBF en un objeto Workbook, conservando todos los registros y definiciones de campos.
- Escribir los datos del libro de trabajo de vuelta al formato DBF para exportarlos a aplicaciones compatibles con dBASE.
- Manejar los tipos de datos comunes utilizados en archivos DBF, incluyendo campos de carácter, numéricos, de fecha y lógicos.
- Preservar las definiciones de los campos, como el nombre, el tipo y la longitud del campo, en las operaciones de lectura/escritura.

### Limitaciones y consideraciones
Al trabajar con archivos DBF, tenga en cuenta las siguientes restricciones:
- El número máximo de campos por archivo es **128**.
- El tamaño máximo de registro es **4000 bytes**.
- Los nombres de los campos están limitados a **10 caracteres**, deben estar en mayúsculas y no pueden contener espacios.
- Los valores de fecha en los archivos DBF se almacenan en formato `AAAAMMDD`.
- La codificación de caracteres puede variar según la aplicación de origen (comúnmente Windows-1252 o páginas de códigos OEM).

## **Lectura de un archivo DBF**
Aspose.Cells facilita la carga de datos desde un archivo DBF a un objeto Workbook. La biblioteca utiliza la clase `LoadOptions` para especificar el formato de origen, asegurando que los datos se interpreten correctamente durante el proceso de carga.

### Lectura de un archivo DBF con Aspose.Cells
Para leer un archivo DBF, necesita crear una instancia de `LoadOptions`, establecer su propiedad `LoadFormat` en `LoadFormat.Dbf` y pasarla al constructor de `Workbook` junto con la ruta del archivo. Una vez cargados, los datos quedan accesibles a través de la colección `getWorksheets()`, donde puede iterar por las celdas, extraer valores o manipular los datos según sea necesario.
El siguiente ejemplo demuestra cómo cargar un archivo DBF existente en Aspose.Cells, acceder a su primera hoja de cálculo y leer los valores de las celdas.

```java
import com.aspose.cells.*;
import java.io.File;
String dataDir = "Data/";
String filePath = new File(new File(dataDir), "example.dbf").getPath();
LoadOptions loadOptions = new LoadOptions(LoadFormat.DBF);
Workbook workbook = new Workbook(filePath, loadOptions);
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
StringBuilder sb = new StringBuilder();
int maxRow = cells.getMaxDataRow();
int maxCol = cells.getMaxDataColumn();
for (int i = 0; i <= maxRow; i++)
{
    for (int j = 0; j <= maxCol; j++)
    {
        Cell cell = cells.get(i, j);
        String value = cell.getStringValue();
        sb.append("|").append(value);
    }
    sb.append("|").append(System.lineSeparator());
}
System.out.println(sb.toString());
String outputPath = new File(new File(dataDir), "output.xlsx").getPath();
workbook.save(outputPath, SaveFormat.XLSX);
System.out.println("DBF file loaded successfully. Converted XLSX saved at: " + outputPath);
```

{{% alert color="primary" %}}
Puede abrir archivos DBF directamente en Microsoft Excel seleccionando el archivo en el cuadro de diálogo Abrir. Excel tratará el archivo DBF como una hoja de cálculo y mostrará sus registros en un diseño tabular. Esto resulta útil para verificar rápidamente los datos después de leerlos o escribirlos con Aspose.Cells.

## **Escritura de un archivo DBF**
Escribir datos en un archivo DBF sigue un patrón similar al de guardar cualquier otro formato de hoja de cálculo con Aspose.Cells. Cree o cargue un Workbook, rellene la hoja de cálculo con datos y, a continuación, llame al método `save` especificando `SaveFormat.Dbf` como formato de destino.

### Escritura de un archivo DBF con Aspose.Cells
Para crear un archivo DBF, siga estos pasos:
1. Cree una nueva instancia de `Workbook`.
2. Acceda a la primera hoja de cálculo desde la colección `getWorksheets()`.
3. Rellene la hoja de cálculo con sus datos, incluyendo los encabezados en la primera fila y los registros en las filas siguientes.
4. Llame al método `Workbook.save`, pasando la ruta del archivo y `SaveFormat.Dbf` como parámetros.
El siguiente ejemplo demuestra cómo crear un nuevo archivo DBF desde cero. Rellena una hoja de cálculo con datos de muestra que contienen diferentes tipos de datos (cadenas, números y fechas) para ilustrar cómo se gestionan los tipos de campo al exportar al formato DBF.

```java
import com.aspose.cells.*;
import java.io.File;
import java.util.GregorianCalendar;
String outputDir = "C:\\Output\\";
String filePath = new File(new File(outputDir), "output.dbf").getPath();
if (!new File(outputDir).exists())
{
    new File(outputDir).mkdirs();
}
Workbook workbook = new Workbook();
Worksheet worksheet = workbook.getWorksheets().get(0);
Cells cells = worksheet.getCells();
// Encabezados de columna
cells.get(0, 0).putValue("ID");
cells.get(0, 1).putValue("Name");
cells.get(0, 2).putValue("Department");
cells.get(0, 3).putValue("Salary");
cells.get(0, 4).putValue("HireDate");
// Fila de datos 1
cells.get(1, 0).putValue(101);
cells.get(1, 1).putValue("John Smith");
cells.get(1, 2).putValue("Engineering");
cells.get(1, 3).putValue(75000.50);
cells.get(1, 4).putValue(new GregorianCalendar(2020, 2, 15).getTime());
// Fila de datos 2
cells.get(2, 0).putValue(102);
cells.get(2, 1).putValue("Jane Doe");
cells.get(2, 2).putValue("Marketing");
cells.get(2, 3).putValue(68000.75);
cells.get(2, 4).putValue(new GregorianCalendar(2019, 6, 22).getTime());
// Fila de datos 3
cells.get(3, 0).putValue(103);
cells.get(3, 1).putValue("Bob Johnson");
cells.get(3, 2).putValue("Finance");
cells.get(3, 3).putValue(82000.00);
cells.get(3, 4).putValue(new GregorianCalendar(2021, 0, 10).getTime());
// Fila de datos 4
cells.get(4, 0).putValue(104);
cells.get(4, 1).putValue("Alice Brown");
cells.get(4, 2).putValue("Human Resources");
cells.get(4, 3).putValue(71000.25);
cells.get(4, 4).putValue(new GregorianCalendar(2018, 10, 5).getTime());
// Fila de datos 5
cells.get(5, 0).putValue(105);
cells.get(5, 1).putValue("Charlie Wilson");
cells.get(5, 2).putValue("Operations");
cells.get(5, 3).putValue(79500.80);
cells.get(5, 4).putValue(new GregorianCalendar(2022, 4, 30).getTime());
// Establecer anchos de columna para mejor legibilidad
worksheet.getCells().setColumnWidth(0, 8);
worksheet.getCells().setColumnWidth(1, 20);
worksheet.getCells().setColumnWidth(2, 20);
worksheet.getCells().setColumnWidth(3, 12);
worksheet.getCells().setColumnWidth(4, 14);
workbook.save(filePath, SaveFormat.DBF);
```

{{% alert color="primary" %}}
Al escribir datos en un archivo DBF, asegúrese de que sus datos se ajusten a las limitaciones del formato. Los nombres de los campos no deben superar los 10 caracteres y no deben contener espacios. Los registros que excedan los 4000 bytes en total no se guardarán correctamente. Las fechas deben ser valores de fecha válidos que puedan representarse en el formato AAAAMMDD.

## **Consideraciones sobre tipos de datos y formato**
Al transferir datos entre Aspose.Cells y el formato DBF, es importante comprender cómo se asignan los tipos de datos entre los dos sistemas para garantizar la integridad de los datos.

### Tipos de celda a tipos de campo DBF
Los valores de celda de Aspose.Cells se convierten automáticamente a los tipos de campo DBF apropiados al guardar:
- **Cadenas** se asignan a campos de carácter (C).
- **Valores numéricos** (enteros y decimales) se asignan a campos numéricos (N).
- **Valores de fecha** se asignan a campos de fecha (D) en formato `AAAAMMDD`.
- **Valores booleanos** se asignan a campos lógicos (L).

### Codificación
Los archivos DBF pueden utilizar diferentes codificaciones de caracteres según la aplicación que los creó. Aspose.Cells gestiona la codificación de forma transparente en la mayoría de los casos, pero si encuentra problemas de visualización de caracteres, puede que necesite comprobar la codificación del archivo de origen.

### Reglas para los nombres de campo
Los nombres de campo DBF deben cumplir las siguientes reglas:
- Longitud máxima de 10 caracteres.
- Deben comenzar con una letra.
- No pueden contener espacios ni caracteres especiales.
- Se almacenan en mayúsculas independientemente del caso utilizado en la entrada.

### Verificación del resultado
Después de escribir un archivo DBF, puede verificar el resultado abriéndolo en Microsoft Excel o en cualquier aplicación compatible con dBASE. Los datos deben aparecer en un diseño tabular con los nombres de campo como encabezados de columna y los registros cumplimentados según los datos proporcionados.

## **Conversión entre DBF y otros formatos**
Uno de los casos de uso más prácticos para leer y escribir archivos DBF con Aspose.Cells es la conversión de datos entre el formato DBF y formatos modernos de hojas de cálculo como XLSX, XLS o CSV. Dado que Aspose.Cells admite una amplia gama de formatos, puede cargar fácilmente un archivo DBF y volver a guardarlo en cualquier otro formato compatible, o viceversa.
{{% /alert %}}

{{% /alert %}}

{{% /alert %}}

{{< app/cells/assistant language="java" >}}