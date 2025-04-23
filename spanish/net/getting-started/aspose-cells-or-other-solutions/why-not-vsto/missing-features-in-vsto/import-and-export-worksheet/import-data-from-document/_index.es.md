---
title: Importar datos desde el documento
type: docs
weight: 20
url: /es/net/import-data-from-document/
---

Los datos son la colección de hechos crudos y creamos documentos de hojas de cálculo o informes para presentar estos hechos crudos de una manera más significativa. Normalmente, agregamos datos a hojas de cálculo por nosotros mismos, pero a veces, necesitamos reutilizar recursos de datos existentes y aquí es donde surge la necesidad de importar datos a hojas de cálculo desde diferentes fuentes de datos. En este tema, discutiremos algunas técnicas para importar datos a hojas de cálculo desde diferentes fuentes de datos.

**Importar datos usando Aspose.Cells** 
Cuando se utiliza **Aspose.Cells** para abrir un archivo de Excel, todos los datos en el archivo se importan automáticamente, pero Aspose.Cells también admite la importación de datos desde diferentes fuentes de datos. Algunas de estas fuentes de datos se enumeran a continuación:

- **Array**
- **ArrayList**
- **DataTable**
- **DataColumn**
- **DataView**
- **DataGrid**
- **DataReader**
- **GridView**

Aspose.Cells proporciona una clase, **Workbook** que representa un archivo de Excel. La clase Workbook contiene una colección de Worksheets que permite acceder a cada hoja de cálculo en el archivo de Excel. Una hoja de cálculo está representada por la clase Worksheet. La clase Worksheet proporciona una colección de Cells.

La colección de Cells proporciona métodos muy útiles para importar datos de diferentes fuentes de datos.

Esta sección tiene los siguientes temas:

- [Importar desde un Arreglo](/cells/es/net/importing-from-array/)
- [Importar desde un ArrayList](/cells/es/net/importing-from-arraylist/)
- [Importar desde Objetos Personalizados](/cells/es/net/importing-from-custom-objects/)
- [Importar desde un DataTable](/cells/es/net/importing-from-datatable/)
{{< app/cells/assistant language="csharp" >}}
