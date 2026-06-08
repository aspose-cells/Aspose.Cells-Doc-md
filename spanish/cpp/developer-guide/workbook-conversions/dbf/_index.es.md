---
title: Leer y Escribir Archivos DBF
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo, que admite la lectura y escritura de archivos dBASE III y IV (DBF). Este artículo explica cómo importar datos desde y exportar datos a archivos DBF usando Aspose.Cells, incluyendo detalles del formato de archivo, características compatibles y ejemplos paso a paso.
keywords: Aspose.Cells, biblioteca C++, DBF, dBASE, leer DBF, escribir DBF, importar DBF, exportar DBF, formato de archivo, .dbf
type: docs
weight: 200
url: /es/cpp/reading-and-writing-dbf-files/
---

{{% alert color="primary" %}}

Aspose.Cells ofrece soporte completo para leer y escribir archivos DBF (dBASE). Puede cargar archivos dBASE III y dBASE IV existentes en un objeto Workbook, manipular los datos usando la rica API de Aspose.Cells, y guardar el libro de trabajo nuevamente en formato DBF para su uso con aplicaciones de bases de datos legacy.

{{% /alert %}}

## **Introducción**

DBF (DataBase File) es un formato de archivo de base de datos legacy introducido originalmente por dBASE a principios de la década de 1980. A pesar de la antigüedad del formato, los archivos DBF todavía se utilizan ampliamente en muchas industrias para almacenar datos estructurados, particularmente en contabilidad, SIG y otras aplicaciones especializadas. Aspose.Cells le permite integrar estos archivos legacy en flujos de trabajo modernos de hojas de cálculo en C++ de forma transparente.

La biblioteca admite tanto la lectura como la escritura de archivos DBF, lo que le permite:

- Importar datos desde archivos DBF existentes a objetos Workbook de Aspose.Cells para su posterior procesamiento o conversión a otros formatos.
- Crear nuevos archivos DBF desde cero o transformando datos desde otros formatos de hojas de cálculo.
- Mantener las definiciones de campos, tipos de datos y estructuras de registros al transferir datos hacia y desde el formato DBF.

Los archivos DBF también se pueden abrir directamente en Microsoft Excel y otras aplicaciones de hojas de cálculo, lo que los convierte en un puente conveniente entre sistemas legacy y herramientas modernas de hojas de cálculo.

## **Versiones de DBF Compatibles y Características**

Aspose.Cells admite las siguientes versiones del formato DBF:

- **dBASE III** — La variante original y más ampliamente compatible del formato DBF.
- **dBASE IV** — Una versión extendida que admite tipos de datos adicionales y tamaños de campo más grandes.

### Características Compatibles

La biblioteca proporciona soporte integral para las siguientes operaciones:

- Lectura de datos DBF en un objeto Workbook, con todos los registros y definiciones de campos preservados.
- Escritura de datos del libro de trabajo de vuelta al formato DBF para exportar a aplicaciones compatibles con dBASE.
- Manejo de tipos de datos comunes utilizados en archivos DBF, incluyendo campos de caracteres, numéricos, de fecha y lógicos.
- Preservación de definiciones de campos como nombre de campo, tipo y longitud durante operaciones de lectura/escritura.

### Limitaciones y Consideraciones

Cuando trabaje con archivos DBF, tenga en cuenta las siguientes restricciones:

- El número máximo de campos por archivo es **128**.
- El tamaño máximo de registro es **4000 bytes**.
- Los nombres de campo están limitados a **10 caracteres**, deben estar en mayúsculas y no pueden contener espacios.
- Los valores de fecha en los archivos DBF se almacenan en formato `YYYYMMDD`.
- La codificación de caracteres puede variar dependiendo de la aplicación de origen (comúnmente Windows-1252 o páginas de código OEM).

## **Leer un Archivo DBF**

Aspose.Cells hace que sea sencillo cargar datos desde un archivo DBF en un objeto Workbook. La biblioteca utiliza la clase `LoadOptions` para especificar el formato de origen, asegurando que los datos se interpreten correctamente durante el proceso de carga.

### Leer un Archivo DBF con Aspose.Cells

Para leer un archivo DBF, necesita crear una instancia de `LoadOptions`, establecer su propiedad `LoadFormat` en `LoadFormat.Dbf`, y pasarla al constructor `Workbook` junto con la ruta del archivo. Una vez cargado, los datos se vuelven accesibles a través de la colección `Worksheets`, donde puede iterar a través de las celdas, extraer valores o manipular los datos según sea necesario.

El siguiente ejemplo demuestra cómo cargar un archivo DBF existente en Aspose.Cells, acceder a su primera hoja de cálculo y leer los valores de las celdas.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <iostream>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "Data/";
    std::string filePath = dataDir + "example.dbf";

    LoadOptions loadOptions(LoadFormat::Dbf);

    Workbook workbook(U16String(filePath.c_str()), loadOptions);

    Worksheet worksheet = workbook.GetWorksheets().Get(0);

    Cells cells = worksheet.GetCells();

    std::string sb = "";

    int maxRow = cells.GetMaxDataRow();
    int maxCol = cells.GetMaxDataColumn();

    for (int i = 0; i <= maxRow; i++) {
        for (int j = 0; j <= maxCol; j++) {
            Cell cell = cells.Get(i, j);
            U16String value = cell.GetStringValue();
            sb += "|";
            sb += value.ToUtf8();
        }
        sb += "|";
        sb += "\n";
    }

    std::cout << sb << std::endl;

    std::string outputPath = dataDir + "output.xlsx";
    workbook.Save(U16String(outputPath.c_str()), SaveFormat::Xlsx);

    std::cout << "DBF file loaded successfully. Converted XLSX saved at: " << outputPath << std::endl;

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Puede abrir archivos DBF directamente en Microsoft Excel seleccionando el archivo en el cuadro de diálogo Abrir. Excel tratará el archivo DBF como una hoja de cálculo, mostrando sus registros en un diseño tabular. Esto es útil para verificar rápidamente los datos después de leerlos o escribirlos con Aspose.Cells.

{{% /alert %}}

## **Escribir un Archivo DBF**

Escribir datos en un archivo DBF sigue un patrón similar al de guardar cualquier otro formato de hoja de cálculo con Aspose.Cells. Crea o carga un Workbook, rellena la hoja de cálculo con datos y luego llama al método `Save` especificando `SaveFormat.Dbf` como formato de destino.

### Escribir un Archivo DBF con Aspose.Cells

Para crear un archivo DBF, siga estos pasos:

1. Cree una nueva instancia de `Workbook`.
2. Acceda a la primera hoja de cálculo desde la colección `Worksheets`.
3. Rellene la hoja de cálculo con sus datos, incluyendo encabezados en la primera fila y registros en las filas subsiguientes.
4. Llame al método `Workbook.Save`, pasando la ruta del archivo y `SaveFormat.Dbf` como parámetros.

El siguiente ejemplo demuestra cómo crear un nuevo archivo DBF desde cero. Rellena una hoja de cálculo con datos de muestra que contienen diferentes tipos de datos (cadenas, números y fechas) para ilustrar cómo se manejan los tipos de campo al exportar al formato DBF.

```cpp
#include "Aspose.Cells.h"
#include <string>
#include <filesystem>

using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string outputDir = "C:/Output/";
    std::string filePath = outputDir + "output.dbf";

    if (!std::filesystem::exists(outputDir)) {
        std::filesystem::create_directories(outputDir);
    }

    Workbook workbook;
    Worksheet worksheet = workbook.GetWorksheets().Get(0);
    Cells cells = worksheet.GetCells();

    // Encabezados de columna
    cells.Get(0, 0).PutValue(u"ID");
    cells.Get(0, 1).PutValue(u"Name");
    cells.Get(0, 2).PutValue(u"Department");
    cells.Get(0, 3).PutValue(u"Salary");
    cells.Get(0, 4).PutValue(u"HireDate");

    // Fila de datos 1
    cells.Get(1, 0).PutValue(101);
    cells.Get(1, 1).PutValue(u"John Smith");
    cells.Get(1, 2).PutValue(u"Engineering");
    cells.Get(1, 3).PutValue(75000.50);
    Date hireDate1{2020, 3, 15, 0, 0, 0, 0};
    cells.Get(1, 4).PutValue(hireDate1);

    // Fila de datos 2
    cells.Get(2, 0).PutValue(102);
    cells.Get(2, 1).PutValue(u"Jane Doe");
    cells.Get(2, 2).PutValue(u"Marketing");
    cells.Get(2, 3).PutValue(68000.75);
    Date hireDate2{2019, 7, 22, 0, 0, 0, 0};
    cells.Get(2, 4).PutValue(hireDate2);

    // Fila de datos 3
    cells.Get(3, 0).PutValue(103);
    cells.Get(3, 1).PutValue(u"Bob Johnson");
    cells.Get(3, 2).PutValue(u"Finance");
    cells.Get(3, 3).PutValue(82000.00);
    Date hireDate3{2021, 1, 10, 0, 0, 0, 0};
    cells.Get(3, 4).PutValue(hireDate3);

    // Fila de datos 4
    cells.Get(4, 0).PutValue(104);
    cells.Get(4, 1).PutValue(u"Alice Brown");
    cells.Get(4, 2).PutValue(u"Human Resources");
    cells.Get(4, 3).PutValue(71000.25);
    Date hireDate4{2018, 11, 5, 0, 0, 0, 0};
    cells.Get(4, 4).PutValue(hireDate4);

    // Fila de datos 5
    cells.Get(5, 0).PutValue(105);
    cells.Get(5, 1).PutValue(u"Charlie Wilson");
    cells.Get(5, 2).PutValue(u"Operations");
    cells.Get(5, 3).PutValue(79500.80);
    Date hireDate5{2022, 5, 30, 0, 0, 0, 0};
    cells.Get(5, 4).PutValue(hireDate5);

    // Establecer anchos de columna para mejor legibilidad
    worksheet.GetCells().SetColumnWidth(0, 8);
    worksheet.GetCells().SetColumnWidth(1, 20);
    worksheet.GetCells().SetColumnWidth(2, 20);
    worksheet.GetCells().SetColumnWidth(3, 12);
    worksheet.GetCells().SetColumnWidth(4, 14);

    workbook.Save(U16String(filePath.c_str()), SaveFormat::Dbf);

    Aspose::Cells::Cleanup();
    return 0;
}
```

{{% alert color="primary" %}}

Al escribir datos en un archivo DBF, asegúrese de que sus datos cumplan con las limitaciones del formato. Los nombres de campo no deben tener más de 10 caracteres y no deben contener espacios. Los registros que excedan los 4000 bytes en total no se guardarán correctamente. Las fechas deben ser valores de fecha válidos que puedan representarse en el formato YYYYMMDD.

{{% /alert %}}

## **Consideraciones sobre Tipos de Datos y Formato**

Al transferir datos entre Aspose.Cells y el formato DBF, es importante comprender cómo se mapean los tipos de datos entre los dos sistemas para garantizar la integridad de los datos.

### Tipos de Celdas a Tipos de Campos DBF

Los valores de celda de Aspose.Cells se convierten automáticamente a los tipos de campo DBF apropiados al guardar:

- **Cadenas** se asignan a campos de caracteres (C).
- **Valores numéricos** (enteros y decimales) se asignan a campos numéricos (N).
- **Valores de fecha** se asignan a campos de fecha (D) en formato `YYYYMMDD`.
- **Valores booleanos** se asignan a campos lógicos (L).

### Codificación

Los archivos DBF pueden usar diferentes codificaciones de caracteres dependiendo de la aplicación que los creó. Aspose.Cells maneja la codificación de forma transparente en la mayoría de los casos, pero si encuentra problemas de visualización de caracteres, puede que necesite verificar la codificación del archivo de origen.

### Reglas de Nombres de Campo

Los nombres de campo DBF deben cumplir con las siguientes reglas:

- Longitud máxima de 10 caracteres.
- Debe comenzar con una letra.
- No puede contener espacios ni caracteres especiales.
- Almacenado en mayúsculas independientemente del caso utilizado en la entrada.

### Verificando el Resultado

Después de escribir un archivo DBF, puede verificar el resultado abriéndolo en Microsoft Excel o cualquier aplicación compatible con dBASE. Los datos deben aparecer en un diseño tabular con los nombres de campo como encabezados de columna, y los registros completados según los datos proporcionados.

## **Conversión entre DBF y Otros Formatos**

Uno de los casos de uso más prácticos para leer y escribir archivos DBF con Aspose.Cells es la conversión de datos entre el formato DBF y formatos modernos de hojas de cálculo como XLSX, XLS o CSV. Dado que Aspose.Cells admite una amplia gama de formatos, puede cargar fácilmente un archivo DBF y volverlo a guardar en cualquier otro formato compatible, o viceversa.

Por ejemplo, puede leer un archivo DBF, aplicar formato o cálculos usando la API de Aspose.Cells y luego guardar el resultado como un archivo XLSX para distribuir a usuarios que trabajan con aplicaciones modernas de hojas de cálculo. Por el contrario, puede tomar datos de un archivo XLSX o CSV y exportarlos al formato DBF para su integración con sistemas legacy.



{{< app/cells/assistant language="cpp" >}}