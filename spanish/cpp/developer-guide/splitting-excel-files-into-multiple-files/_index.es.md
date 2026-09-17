---
title: División de archivos Excel en varios archivos
description: Aspose.Cells es una biblioteca de C++ para trabajar con archivos de hojas de cálculo, que admite la división de un único archivo Excel en varios archivos. Este artículo presentará cómo dividir archivos Excel copiando cada hoja de cálculo a un libro de trabajo independiente y copiando rangos de celdas específicos a otros libros de trabajo.
linktitle: División de archivos Excel en varios archivos
keywords: Aspose.Cells, biblioteca de C++, hoja de cálculo, dividir archivo Excel, copiar hoja de cálculo, copiar rango, varios libros de trabajo, guardar como archivos separados
type: docs
weight: 195
url: /es/cpp/splitting-excel-files-into-multiple-files/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}
Aspose.Cells admite la división de un único archivo Excel en varios archivos. Existen dos formas principales de hacerlo: (1) copiando cada hoja de cálculo del libro de trabajo de origen a un nuevo libro de trabajo y guardando cada uno como un archivo independiente, y (2) copiando un rango de celdas específico de una hoja de cálculo a un nuevo libro de trabajo. Ambos enfoques son útiles cuando necesita distribuir subconjuntos de datos, crear informes más pequeños para diferentes destinatarios o aislar datos para su procesamiento individual.

## **Introducción**
Existen muchos escenarios del mundo real en los que un desarrollador necesita dividir un único archivo Excel en varios archivos más pequeños. Por ejemplo, un libro de trabajo puede contener una hoja de cálculo por departamento, y cada jefe de departamento necesita recibir únicamente su propia hoja. En otros casos, es posible que desee extraer una tabla o bloque de datos concreto de una hoja de cálculo y enviarlo como archivo independiente por correo electrónico, sin exponer el resto del libro de trabajo. También puede ser necesario dividir libros de trabajo consolidados grandes en fragmentos más pequeños para un manejo más sencillo, una carga más rápida o su procesamiento posterior por otros sistemas.
Aspose.Cells proporciona dos enfoques flexibles para esta tarea. El primer enfoque itera a través de cada hoja de cálculo del libro de trabajo de origen y copia su contenido en una instancia de `Workbook` completamente nueva, guardando cada una como un archivo independiente. El segundo enfoque se centra en un rango de celdas específico dentro de una hoja de cálculo y copia únicamente dicho rango en un nuevo libro de trabajo. En ambos casos, el flujo general es el mismo: cargue el libro de trabajo de origen usando la clase `Workbook`, acceda a los datos relevantes a través de los objetos `Worksheet` y `Cells`, transfiera el contenido a un `Workbook` de destino y, a continuación, guarde el destino en disco.

## **División de un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo**

### **Descripción del enfoque**
En este enfoque, el libro de trabajo de origen se abre una sola vez y, a continuación, para cada `Worksheet` de su colección `Worksheets`, se crea un nuevo `Workbook` de destino. Luego, el contenido de la hoja de cálculo de origen se copia en la primera hoja de cálculo del libro de trabajo de destino, y el libro de trabajo de destino se guarda como un archivo cuyo nombre se deriva del nombre de la hoja de cálculo de origen. El resultado es un archivo de salida por hoja de cálculo, donde cada archivo de salida contiene los datos de una sola hoja de origen.
Este método es la elección adecuada cuando cada hoja de cálculo de su libro de trabajo de origen representa una unidad de información lógicamente independiente (como un departamento, región, mes o línea de producto) y desea entregar o procesar cada unidad por separado.

### **Pasos**
Los siguientes pasos describen cómo dividir un archivo Excel copiando cada hoja de cálculo a un nuevo libro de trabajo:
1. Abra el archivo Excel de origen creando una instancia de un objeto `Workbook` y pasando la ruta del archivo a su constructor.
2. Itere a través de la colección `Workbook.Worksheets` usando un bucle `for` o `foreach` para que cada `Worksheet` del archivo de origen sea procesada.
3. Dentro del bucle, cree una nueva instancia de `Workbook` de destino (un libro de trabajo vacío) para la hoja de cálculo actual.
5. Copie el contenido de la hoja de cálculo de origen en la hoja de cálculo de destino. Esto se puede hacer iterando las celdas de la colección `Cells` de la hoja de cálculo de origen y escribiendo sus valores en las celdas correspondientes de la hoja de cálculo de destino, o usando el método `Cells.Copy` para transferir un rango completo de una sola vez.
6. Construya una ruta de archivo de salida que incorpore el nombre de la hoja de cálculo de origen (por ejemplo, `dataDir + worksheet.Name + ".xls"`) para que cada archivo generado tenga un nombre único.
7. Llame al método `Workbook.Save` del destino para escribir el archivo en disco.
8. Repita los pasos del 3 al 7 para la siguiente hoja de cálculo hasta que se hayan procesado todas las hojas de cálculo.

### **Ejemplo de código**

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

El resultado esperado es un conjunto de archivos nuevos en el directorio de datos, un archivo por hoja de cálculo del libro de trabajo de origen. Cada archivo lleva el nombre de su hoja de origen correspondiente y contiene los datos (y, opcionalmente, el formato) de esa única hoja.

## **División de un archivo Excel copiando un rango a un nuevo libro de trabajo**

### **Descripción del enfoque**
A veces, los datos que necesita dividir no corresponden a una hoja de cálculo completa, sino a una región rectangular específica de una hoja de cálculo, como `A1:D10` o un rango con nombre que representa una tabla concreta. En estos casos, copiar hojas de cálculo enteras es un desperdicio, y se requiere un enfoque más preciso: identifique el rango de origen, copie únicamente dicho rango en un nuevo libro de trabajo y guarde el nuevo archivo.
Este enfoque es ideal cuando desea extraer una sola tabla, bloque de informe o área de datos de una hoja de cálculo más grande, descartando todo el contenido no relacionado. También es útil para exportar regiones seleccionadas por el usuario de una hoja como archivos independientes.

### **Pasos**
Los siguientes pasos describen cómo dividir un archivo Excel copiando un rango específico a un nuevo libro de trabajo:
1. Abra el archivo Excel de origen creando una instancia de un objeto `Workbook` con la ruta del archivo.
2. Obtenga la `Worksheet` de destino que contiene el rango que desea copiar, ya sea por índice (por ejemplo, la primera hoja) o por nombre de la colección `Worksheets`.
3. Identifique el rango que se va a copiar. Puede ser un rango de celdas codificado de forma rígida como `A1:C10`, o un rango con nombre obtenido a través de la colección `Worksheet.Cells`, o un rango creado mediante `Worksheet.Cells.CreateRange`.
4. Cree una nueva instancia de `Workbook` de destino.
5. Acceda a la primera `Worksheet` del libro de trabajo de destino (la hoja predeterminada).
6. Copie el rango de origen en la hoja de cálculo de destino, generalmente comenzando desde la celda `A1`. El método `Cells.Copy` en la colección `Cells` de destino se puede usar para copiar un rango completo, o puede iterar a través de las celdas del rango de origen y escribir sus valores en las celdas de destino con `PutValue`. Se pueden proporcionar `CopyOptions` opcionales para controlar lo que se transfiere (solo valores, valores y estilos, fórmulas, etc.).
7. Guarde el libro de trabajo de destino en una nueva ruta de archivo en disco usando el método `Workbook.Save`.

### **Ejemplo de código**
El resultado esperado es un único archivo nuevo en el directorio de datos que contiene solo los valores (y, opcionalmente, el formato) del rango especificado extraído del libro de trabajo de origen. El archivo de destino no tiene relación con ningún otro dato del archivo de origen; contiene únicamente el rango extraído, comenzando en la celda `A1` de su primera hoja de cálculo.
{{% /alert %}}

## Artículos relacionados
- [Agregar campos de filtro a una Tabla Dinámica en Aspose.Cells for C++](/cells/es/cpp/add-page-field-in-pivot-table/)
- [Aplicar estilos a las Tablas Dinámicas en Aspose.Cells for C++](/cells/es/cpp/apply-style-to-pivot-table/)
- [Modificar el diseño del campo de página en una Tabla Dinámica](/cells/es/cpp/change-page-field-layout/)
- [Convertir minigráficos a imagen y HTML en Aspose.Cells for C++](/cells/es/cpp/convert-sparkline-to-image-and-html/)
- [Conversión de Excel al formato OFD](/cells/es/cpp/converting-excel-to-ofd-format/)

{{< app/cells/assistant language="cpp" >}}