---
title: Dividir Archivos Excel en Varios Archivos
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo, que admite dividir un único archivo Excel en varios archivos. Este artículo presentará cómo dividir archivos Excel copiando cada hoja de cálculo a un libro de trabajo separado y copiando rangos de celdas específicos a otros libros de trabajo.
keywords: Aspose.Cells, biblioteca C++, hoja de cálculo, dividir archivo Excel, copiar hoja de cálculo, copiar rango, varios libros de trabajo, guardar como archivos separados
type: docs
weight: 195
url: /es/cpp/splitting-excel-files-into-multiple-files/
---

{{% alert color="primary" %}}

Aspose.Cells admite dividir un único archivo Excel en varios archivos. Existen dos formas principales de hacerlo: (1) copiando cada hoja de cálculo del libro de trabajo de origen a un nuevo libro de trabajo y guardando cada uno como un archivo separado, y (2) copiando un rango de celdas específico de una hoja de cálculo a un nuevo libro de trabajo. Ambos enfoques son útiles cuando necesita distribuir subconjuntos de datos, crear informes más pequeños para diferentes destinatarios o aislar datos para su procesamiento individual.

{{% /alert %}}

## **Introducción**

Existen muchos escenarios del mundo real en los que un desarrollador necesita dividir un único archivo Excel en varios archivos más pequeños. Por ejemplo, un libro de trabajo puede contener una hoja de cálculo por departamento, y cada jefe de departamento necesita recibir solo su propia hoja. En otros casos, es posible que desee extraer una tabla o bloque de datos particular de una hoja de cálculo y enviarlo como un archivo independiente por correo electrónico, sin exponer el resto del libro de trabajo. Los libros de trabajo consolidados grandes también pueden necesitar dividirse en piezas más pequeñas para un manejo más sencillo, una carga más rápida o un procesamiento posterior por parte de otros sistemas.

Aspose.Cells proporciona dos enfoques flexibles para esta tarea. El primer enfoque recorre cada hoja de cálculo en el libro de trabajo de origen y copia su contenido en una nueva instancia de `Workbook`, guardando cada una como un archivo separado. El segundo enfoque se centra en un rango de celdas específico dentro de una hoja de cálculo y copia solo ese rango en un nuevo libro de trabajo. En ambos casos, el flujo general es el mismo: cargue el libro de trabajo de origen utilizando la clase `Workbook`, acceda a los datos relevantes a través de los objetos `Worksheet` y `Cells`, transfiera el contenido a un `Workbook` de destino y luego guarde el destino en disco.

## **Dividir un Archivo Excel Copiando Cada Hoja de Cálculo a un Nuevo Libro de Trabajo**

### **Descripción General del Enfoque**

En este enfoque, el libro de trabajo de origen se abre una vez, y luego, para cada `Worksheet` en su colección `Worksheets`, se crea un nuevo `Workbook` de destino. El contenido de la hoja de cálculo de origen se copia entonces en la primera hoja de cálculo del libro de trabajo de destino, y el libro de trabajo de destino se guarda como un archivo cuyo nombre se deriva del nombre de la hoja de cálculo de origen. El resultado es un archivo de salida por hoja de cálculo, donde cada archivo de salida contiene los datos de una sola hoja de origen.

Este método es la opción correcta cuando cada hoja de cálculo en su libro de trabajo de origen representa una unidad de información lógicamente independiente (como un departamento, región, mes o línea de productos) y desea entregar o procesar cada unidad por separado.

### **Pasos**

Los siguientes pasos describen cómo dividir un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo:

1. Abra el archivo Excel de origen instanciando un objeto `Workbook` y pasando la ruta del archivo a su constructor.
2. Recorra la colección `Workbook.Worksheets` usando un bucle `for` o `foreach` para que se procese cada `Worksheet` en el archivo de origen.
3. Dentro del bucle, cree una nueva instancia de `Workbook` de destino (un libro de trabajo vacío) para la hoja de cálculo actual.
4. Agregue una nueva `Worksheet` al libro de trabajo de destino (o use la primera hoja de cálculo predeterminada) y asígnele un nombre significativo, idealmente el mismo que la propiedad `Name` de la hoja de cálculo de origen.
5. Copie el contenido de la hoja de cálculo de origen en la hoja de cálculo de destino. Esto se puede hacer recorriendo las celdas de la colección `Cells` de la hoja de cálculo de origen y escribiendo sus valores en las celdas correspondientes de la hoja de cálculo de destino, o utilizando el método `Cells.Copy` para transferir un rango completo de una vez.
6. Construya una ruta de archivo de salida que incorpore el nombre de la hoja de cálculo de origen (por ejemplo, `dataDir + worksheet.Name + ".xls"`) para que cada archivo generado tenga un nombre único.
7. Llame al método `Workbook.Save` del destino para escribir el archivo en disco.
8. Repita los pasos 3 a 7 para la siguiente hoja de cálculo hasta que se hayan procesado todas las hojas de cálculo.

### **Ejemplo de Código**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    std::string dataDir = "data/";
    Workbook wb(U16String((dataDir + "book1.xls").c_str()));

    int sheetCount = wb.GetWorksheets().GetCount();
    for (int i = 0; i < sheetCount; ++i) {
        Worksheet sourceSheet = wb.GetWorksheets().Get(i);
        U16String sheetName = sourceSheet.GetName();

        Workbook destWorkbook;
        int destIndex = destWorkbook.GetWorksheets().Add();
        Worksheet destSheet = destWorkbook.GetWorksheets().Get(destIndex);
        destSheet.SetName(sheetName);

        destSheet.Copy(sourceSheet);

        std::string destFile = dataDir + sheetName.ToUtf8() + ".xls";
        destWorkbook.Save(U16String(destFile.c_str()), SaveFormat::Excel97To2003);
    }

    Aspose::Cells::Cleanup();
    return 0;
}
```

El resultado esperado es un conjunto de nuevos archivos en el directorio de datos, un archivo por hoja de cálculo del libro de trabajo de origen. Cada archivo lleva el nombre de su hoja de origen correspondiente, y el archivo contiene los datos (y opcionalmente el formato) de esa única hoja.

## **Dividir un Archivo Excel Copiando un Rango a un Nuevo Libro de Trabajo**

### **Descripción General del Enfoque**

A veces, los datos que necesita dividir no corresponden a una hoja de cálculo completa, sino a una región rectangular específica de una hoja de cálculo, como `A1:D10` o un rango con nombre que representa una tabla particular. En estos casos, copiar hojas de cálculo completas es un desperdicio, y se requiere un enfoque más preciso: identifique el rango de origen, copie solo ese rango en un nuevo libro de trabajo y guarde el nuevo archivo.

Este enfoque es ideal cuando desea extraer una sola tabla, bloque de informe o área de datos de una hoja de cálculo más grande descartando todo el contenido no relacionado. También es útil para exportar regiones seleccionadas por el usuario de una hoja como archivos independientes.

### **Pasos**

Los siguientes pasos describen cómo dividir un archivo Excel copiando un rango específico a un nuevo libro de trabajo:

1. Abra el archivo Excel de origen instanciando un objeto `Workbook` con la ruta del archivo.
2. Recupere la `Worksheet` de destino que contiene el rango que desea copiar, ya sea por índice (por ejemplo, la primera hoja) o por nombre de la colección `Worksheets`.
3. Identifique el rango a copiar. Puede ser un rango de celdas codificado como `A1:C10`, o un rango con nombre obtenido a través de la colección `Worksheet.Cells`, o un rango creado mediante `Worksheet.Cells.CreateRange`.
4. Cree una nueva instancia de `Workbook` de destino.
5. Acceda a la primera `Worksheet` del libro de trabajo de destino (la hoja predeterminada).
6. Copie el rango de origen en la hoja de cálculo de destino, normalmente comenzando desde la celda `A1`. El método `Cells.Copy` en la colección `Cells` de destino se puede usar para copiar un rango completo, o puede recorrer las celdas del rango de origen y escribir sus valores en las celdas de destino con `PutValue`. Se pueden proporcionar `CopyOptions` opcionales para controlar lo que se transfiere (solo valores, valores y estilos, fórmulas, etc.).
7. Guarde el libro de trabajo de destino en una nueva ruta de archivo en disco usando el método `Workbook.Save`.

### **Ejemplo de Código**

```cpp
using namespace Aspose::Cells;

int main() {
    Aspose::Cells::Startup();

    // Define el directorio de datos y las rutas de archivo
    std::string dataDir = "data/";
    std::string sourcePath = dataDir + "book1.xls";
    std::string outputPath = dataDir + "outputrange.xls";

    // Abre el archivo Excel de origen
    Workbook sourceWorkbook(U16String(sourcePath.c_str()));

    // Obtiene la primera hoja de cálculo del libro de origen
    Worksheet sourceWorksheet = sourceWorkbook.GetWorksheets().Get(0);

    // Define el rango de celdas de origen A1:C10 (10 filas, 3 columnas comenzando en la fila 0, columna 0)
    Range sourceRange = sourceWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Crea un nuevo libro de destino
    Workbook destWorkbook;

    // Accede a la primera hoja de cálculo en el libro de destino
    Worksheet destWorksheet = destWorkbook.GetWorksheets().Get(0);

    // Crea el rango de destino en A1 con las mismas dimensiones que el rango de origen
    Range destRange = destWorksheet.GetCells().CreateRange(0, 0, 10, 3);

    // Copia el rango de origen al rango de destino
    destRange.Copy(sourceRange);

    // Guarda el libro de destino en un nuevo archivo .xls
    destWorkbook.Save(U16String(outputPath.c_str()), SaveFormat::Excel97To2003);

    Aspose::Cells::Cleanup();
    return 0;
}
```

El resultado esperado es un único archivo nuevo en el directorio de datos que contiene solo los valores (y opcionalmente el formato) del rango especificado extraído del libro de trabajo de origen. El archivo de destino no tiene relación con ningún otro dato en el archivo de origen; contiene solo el rango extraído, comenzando en la celda `A1` de su primera hoja de cálculo.

## **Artículos Relacionados**

- [Copiar Filas y Columnas](/es/cells/cpp/copying-rows-and-columns/)
- [Combinar y Descombinar Celdas](/es/cells/cpp/merging-and-unmerging-cells/)

{{< app/cells/assistant language="cpp" >}}