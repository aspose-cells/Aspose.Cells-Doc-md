# Biblioteca C++ para Formatos de Archivos de Excel

![Versión 23.11.0](https://img.shields.io/badge/nuget-v23.11.0-azul) ![NuGet](https://img.shields.io/nuget/dt/Aspose.Cells.Cpp)

[![banner](https://raw.githubusercontent.com/Aspose/aspose.github.io/master/img/banners/aspose_cells-for-cpp-banner.png)](https://releases.aspose.com/cells/cpp/)

[Página del Producto](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [Referencia de la API](https://reference.aspose.com/cells/cpp) | [Ejemplos](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Versiones](https://releases.aspose.com/cells/cpp/) | [Soporte Gratuito](https://forum.aspose.com/c/cells) | [Licencia Temporal](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for C++](https://products.aspose.com/cells/cpp/) es una biblioteca nativa de C++ para crear, manipular, procesar y convertir archivos de Microsoft Excel sin necesidad de Microsoft Office o Automation. La API de Excel C++ admite Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML y otros formatos como CSV, TSV y más.

Permite a los desarrolladores trabajar con filas de hojas de cálculo, columnas, datos, fórmulas, tablas dinámicas, hojas de trabajo, tablas, gráficos y objetos de dibujo desde sus propias aplicaciones en C++.

## ¿Qué es Aspose.Cells for C++?

Aspose.Cells for C++ es una API nativa de C++ local para integrar funciones de creación, manipulación y conversión de hojas de cálculo en sus aplicaciones de C++. Admite trabajar con muchos formatos de archivo de hojas de cálculo populares de Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) y OpenOffice/LibreOffice (ODS).

Puede usar Aspose.Cells for C++ para desarrollar aplicaciones de 64 bits en cualquier entorno de desarrollo que admita C++, como Microsoft Visual Studio. Aspose.Cells for C++ es un ensamblado nativo que se puede implementar simplemente copiándolo. No tiene que preocuparse por otros servicios o módulos.

Aspose.Cells for C++ le permite trabajar con las propiedades incorporadas y personalizadas de documentos en Microsoft Excel. Admite la conversión de alta calidad de libros de Excel a archivos compatibles con PDF/A. Trabaje con fórmulas, tablas dinámicas, hojas de cálculo, tablas, rangos, gráficos, objetos OLE y mucho más.

## Características de Procesamiento de Archivos de Excel

- Abra un archivo de hoja de cálculo sin Microsoft Excel.
- [Abra un archivo de Excel](https://docs.aspose.com/cells/cpp/different-ways-to-open-files/) a través de una ruta en la computadora local o usando un flujo.
- [Convertir hoja de cálculo](https://docs.aspose.com/cells/cpp/converting-worksheet-to-different-image-formats/) a diferentes formatos de imagen.
- [Aplicar formato condicional](https://docs.aspose.com/cells/cpp/apply-conditional-formatting-in-worksheet/) según su elección.
- [Manipular tablas dinámicas](https://docs.aspose.com/cells/cpp/manipulate-pivot-table/) en sus hojas de cálculo.
- [Convertir tabla en rango](https://docs.aspose.com/cells/cpp/tables-and-ranges/) sin perder formato.
- Obtenga el nombre de una celda proporcionando el índice de fila y columna, de manera similar, [obtenga el índice de fila y columna de la celda](https://docs.aspose.com/cells/cpp/names-and-indices/) a partir de su nombre.
- Cree [Gráfico de pirámide, Gráfico de líneas, Gráfico de burbujas](https://docs.aspose.com/cells/cpp/creating-and-customizing-charts/), o un gráfico personalizado.
- [Renderizar](https://docs.aspose.com/cells/cpp/chart-rendering/) tipos de gráficos admitidos a imágenes o PDF.
- [Inserte un objeto OLE en la hoja de cálculo](https://docs.aspose.com/cells/cpp/inserting-ole-objects-into-the-worksheet/).
- Acceda a todos los objetos OLE contenidos en la hoja de cálculo para [extracción](https://docs.aspose.com/cells/cpp/extracting-ole-objects-from-worksheet/).

## Formatos de Lectura y Escritura Soportados

**Microsoft Excel:** XLS, XLSX, XLSB, SpreadsheetML\
**Text:** CSV, TSV, TabDelimited\
**OpenDocument:** ODS\
**Otros:** HTML, MHTML

## Guardar Documentos de Hojas de Cálculo como

**Microsoft Excel:** XLSM, XLTX, XLTM, XLAM\
**Formato de Documento Portátil:** PDF, XPS\
**Text:** CSV, TSV, TabDelimited\
**Imágenes:** SVG, JPEG, PNG, BMP, GIF\
**Web:** HTML, MHTML\
**Metarchivo:** EMF\
**Otros** DIF

## Empezar

¿Estás listo para probar Aspose.Cells for C++? Simplemente ejecuta `Install-Package Aspose.Cells.Cpp` desde la Consola del Administrador de Paquetes en Visual Studio para obtener el paquete NuGet. Si ya tienes Aspose.Cells for C++ y deseas actualizar la versión, por favor ejecuta `Update-Package Aspose.Cells.Cpp` para obtener la última versión.

### Convertir XLS a XLSX, XLSB y CSV usando C++

Intenta ejecutar el fragmento a continuación para ver cómo funciona la API en tu entorno o revisa el [Repositorio de GitHub](https://github.com/aspose-cells/Aspose.Cells-for-C) para otros escenarios de uso común.

```c++
U16String dir(u"your path");
// load the file to be converted
Workbook book(dir + u"template.xls");
// save in different formats
book.Save(dir + u"output.xlsx", SaveFormat::Xlsx);
book.Save(dir + u"output.xlsb", SaveFormat::Xlsb);
book.Save(dir + u"output.csv", SaveFormat::CSV);
book.Save(dir + u"output.json", SaveFormat::Json);
```

### Crear un Gráfico de Excel Personalizado con C++

```c++
// create a new workbook
Workbook workbook;

// get first worksheet which is created by default
Worksheet worksheet = workbook.GetWorksheets().Get(0);

// add sample data
worksheet.GetCells().Get(u"A1").PutValue(50);
worksheet.GetCells().Get(u"A2").PutValue(100);
worksheet.GetCells().Get(u"A3").PutValue(150);
worksheet.GetCells().Get(u"A4").PutValue(110);
worksheet.GetCells().Get(u"B1").PutValue(260);
worksheet.GetCells().Get(u"B2").PutValue(12);
worksheet.GetCells().Get(u"B3").PutValue(50);
worksheet.GetCells().Get(u"B4").PutValue(100);

// add a chart to the worksheet
int chartIndex = worksheet.GetCharts().Add(Aspose::Cells::Charts::ChartType::Column, 5, 0, 20, 8);

// access the instance of the newly added chart
Chart chart = worksheet.GetCharts().Get(chartIndex);

// add SeriesCollection (chart data source) to the chart ranging from A1 to B4
chart.GetNSeries().Add(u"A1:B4", true);

// set the chart type of 2nd NSeries to display as line chart
chart.GetNSeries().Get(1).SetType(
	Aspose::Cells::Charts::ChartType::Line);

// save the Excel file
workbook.Save(u"output.xlsx");
```

[Página del Producto](https://products.aspose.com/cells/cpp/) | [Docs](https://docs.aspose.com/cells/cpp/) | [Demos](https://products.aspose.app/cells/family) | [Referencia de la API](https://reference.aspose.com/cells/cpp) | [Ejemplos](https://github.com/aspose-cells/Aspose.Cells-for-C) | [Blog](https://blog.aspose.com/category/cells/) | [Versiones](https://releases.aspose.com/cells/cpp/) | [Soporte Gratuito](https://forum.aspose.com/c/cells) | [Licencia Temporal](https://purchase.aspose.com/temporary-license/)
