# Biblioteca Go para formatos de archivos de Excel

![Versión 24.11.0](https://img.shields.io/badge/go-v24.11.0-blue)

[Página del Producto](https://products.aspose.com/cells/go-cpp/) | [Documentación](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [Referencia de la API](https://reference.aspose.com/cells/go-cpp) | [Ejemplos](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Lanzamientos](https://releases.aspose.com/cells/go-cpp/) | [Soporte gratuito](https://forum.aspose.com/c/cells) | [Licencia temporal](https://purchase.aspose.com/temporary-license/)

[Aspose.Cells for Go via C++](https://products.aspose.com/cells/go-cpp/) es una biblioteca nativa en Go para crear, manipular, procesar y convertir archivos de Microsoft Excel sin necesidad de Microsoft Office o Automatización. La API de Excel en Go soporta Excel 97-2003 (XLS), Excel 2007-2013/2016 (XLSX, XLSM, XLSB), OpenOffice XML y otros formatos como CSV, TSV y más.

Permite a los desarrolladores trabajar con filas, columnas, datos, fórmulas, tablas dinámicas, hojas de cálculo, tablas, gráficos y objetos de dibujo desde sus propias aplicaciones en Go.

## ¿Qué es Aspose.Cells for Go via C++?

Aspose.Cells for Go via C++ es una API nativa en Go para integrar funciones de creación, manipulación y conversión de hojas de cálculo en tus aplicaciones en Go. Soporta trabajar con muchos formatos de archivos de hojas de cálculo populares de Microsoft Excel (XLS, XLSX, XLSB, CSV, etc.) y OpenOffice/LibreOffice (ODS).

Puedes usar Aspose.Cells for Go via C++ para desarrollar aplicaciones de 64 bits en cualquier entorno de desarrollo que soporte Go, como Microsoft Visual Studio. Aspose.Cells for Go via C++ es un ensamblaje nativo que se puede desplegar simplemente copiándolo. No tienes que preocuparte por otros servicios o módulos.

Aspose.Cells for Go via C++ te permite trabajar con las propiedades incorporadas y personalizadas del documento en Microsoft Excel. Compatible con conversiones de alta calidad de libros de trabajo de Excel a archivos conformes con PDF/A. Trabaja con fórmulas, tablas dinámicas, hojas, tablas, rangos, gráficos, objetos OLE y mucho más.

## Características de Procesamiento de Archivos de Excel

- Abra un archivo de hoja de cálculo sin Microsoft Excel.
- [Abrir un archivo de Excel](https://docs.aspose.com/cells/go/different-ways-to-open-files/) mediante una ruta en la computadora local o usando un stream.
- [Convertir hoja de cálculo](https://docs.aspose.com/cells/go/converting-worksheet-to-different-image-formats/) a diferentes formatos de imagen.
- [Aplicar formato condicional](https://docs.aspose.com/cells/go/apply-conditional-formatting-in-worksheet/) según tu preferencia.
- [Manipular tablas dinámicas](https://docs.aspose.com/cells/go/manipulate-pivot-table/) en tus hojas de cálculo.
- [Convertir tabla a rango](https://docs.aspose.com/cells/go/tables-and-ranges/) sin perder el formato.
- Obtener el nombre de una celda proporcionando el índice de fila y columna, de manera similar, [obtener el índice de fila y columna de la celda](https://docs.aspose.com/cells/go/names-and-indices/) a partir de su nombre.
- Crear [Gráfico de pirámide, gráfico de líneas, gráfico de burbujas](https://docs.aspose.com/cells/go/creating-and-customizing-charts/), u otro gráfico personalizado.
- [Representar](https://docs.aspose.com/cells/go/chart-rendering/) tipos de gráficos soportados en imágenes o PDF.
- [Insertar un objeto OLE en la hoja](https://docs.aspose.com/cells/go/inserting-ole-objects-into-the-worksheet/).
- Acceder a todos los objetos OLE contenidos en la hoja para [extracción](https://docs.aspose.com/cells/go/extracting-ole-objects-from-worksheet/).

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

¿Estás listo para probar Aspose.Cells for Go via C++? Simplemente ejecuta `go get -u github.com/aspose-cells/aspose-cells-go-cpp` e importa `github.com/aspose-cells/aspose-cells-go-cpp` desde tu archivo Go. Si ya tienes Aspose.Cells for Go via C++ y deseas actualizar la versión, ejecuta `go get github.com/aspose-cells/aspose-cells-go-cpp@v24.12.0` para obtener la versión más reciente.

### Convertir XLS a XLSX, XLSB y CSV usando Go

Intenta ejecutar el siguiente fragmento para ver cómo funciona la API en tu entorno o consulta el [Repositorio de GitHub](https://github.com/aspose-cells/aspose-cells-go-cpp) para otros escenarios de uso comunes.

```Go
lic, _ := NewLicense()
lic.SetLicense_String(os.Getenv("LicensePath"))
workbook, err1 := NewWorkbook_String("Book1.xlsx")
if err1 != nil {
    println(err1)
}
workbook.Save_String("Book1.pdf")
workbook.Save_String("Book1.png")
workbook.Save_String("Book1.txt")
workbook.Save_String("Book1.ods")
workbook.Save_String("Book1.md")
workbook.Save_String("Book1.json")
workbook.Save_String("Book1.html")
```

### Crear un gráfico de Excel personalizado con Go

```Go
package main

import (
 . "asposecells"
 "os"
)

func main() {
 lic, _ := NewLicense()
 lic.SetLicense_String(os.Getenv("LicensePath"))

 workbook, _ := NewWorkbook()
 worksheets, _ := workbook.GetWorksheets()
 worksheet, _ := worksheets.Get_Int(0)
 cells, _ := worksheet.GetCells()
 cell, _ := cells.Get_String("A1")
 cell.PutValue_Int(50)
 cell, _ = cells.Get_String("A2")
 cell.PutValue_Int(100)
 cell, _ = cells.Get_String("A3")
 cell.PutValue_Int(150)
 cell, _ = cells.Get_String("B1")
 cell.PutValue_Int(4)
 cell, _ = cells.Get_String("B2")
 cell.PutValue_Int(20)
 cell, _ = cells.Get_String("B3")
 cell.PutValue_Int(50)
 charts, _ := worksheet.GetCharts()
 chartIndex, _ := charts.Add_ChartType_Int_Int_Int_Int(ChartType_Pyramid, 5, 0, 20, 8)
 chart, _ := charts.Get_Int(chartIndex)
 series, _ := chart.GetNSeries()
 series.Add_String_Bool("A1:B3", true)
 workbook.Save_String("CreateChart.xlsx")
}

```

[Página del Producto](https://products.aspose.com/cells/go-cpp/) | [Documentación](https://docs.aspose.com/cells/go-cpp/) | [Demos](https://products.aspose.app/cells/family) | [Referencia de la API](https://reference.aspose.com/cells/go-cpp) | [Ejemplos](https://github.com/aspose-cells/aspose-cells-go-cpp) | [Blog](https://blog.aspose.com/category/cells/) | [Lanzamientos](https://releases.aspose.com/cells/go-cpp/) | [Soporte gratuito](https://forum.aspose.com/c/cells) | [Licencia temporal](https://purchase.aspose.com/temporary-license/)
