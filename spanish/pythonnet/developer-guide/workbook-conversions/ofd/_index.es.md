---
title: Conversión de Excel al formato OFD
linktitle: Conversión de Excel al formato OFD
description: Aspose.Cells for Python via .NET es una biblioteca de procesamiento de hojas de cálculo que admite la conversión de libros de trabajo de Excel al formato OFD (Open Fixed-layout Document). Este artículo demuestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos Excel existentes a OFD usando Aspose.Cells.
keywords: Aspose.Cells, Python vía biblioteca .NET, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libro de trabajo
type: docs
weight: 195
url: /es/python-net/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells admite la conversión de libros de trabajo de Excel directamente al formato OFD (Open Fixed-layout Document) utilizando el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva el diseño visible del libro de trabajo, el contenido, las celdas combinadas, los anchos de columna, las alturas de fila, las fuentes, los colores, los bordes y los formatos numéricos. Esto hace que Aspose.Cells sea adecuado para flujos de trabajo de archivo, impresión, presentación regulatoria y trámites gubernamentales que requieran una salida de diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Desempeña un papel similar al de PDF para casos de uso en los que la apariencia visual del documento de origen debe conservarse exactamente como fue creada. OFD es ampliamente adoptado para presentaciones gubernamentales, trámites regulatorios, facturas electrónicas y archivado a largo plazo en la República Popular China.

La conversión de libros de trabajo de Excel a OFD es un requisito común en escenarios donde el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura y diseño bloqueado en lugar de como una hoja de cálculo editable. Algunos ejemplos incluyen enviar una factura finalizada a un cliente, archivar un informe financiero trimestral o presentar una hoja de cálculo de presupuesto a una autoridad regulatoria. Aspose.Cells aborda este requisito mediante el valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente en OFD sin requerir un paso de conversión intermedio. La salida OFD conserva los valores de las celdas, los rangos combinados, las fuentes, los colores, los bordes, los formatos numéricos y las opciones de configuración de página configuradas en el libro de trabajo.

{{% alert color="primary" %}}

La salida OFD generada por Aspose.Cells conserva el diseño visible del libro de trabajo de origen, incluyendo el contenido de las celdas, las celdas combinadas, los anchos de columna y las alturas de fila. El formato de las celdas, como fuentes, colores, bordes, alineación y formatos numéricos, también se representa en la salida de diseño fijo. Las opciones de configuración de página configuradas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Creación de un libro de trabajo Excel y guardado como OFD**
Aspose.Cells le permite construir un libro de trabajo mediante programación, rellenarlo con datos y luego guardarlo directamente en formato OFD utilizando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Agrega un logotipo de la empresa, información de encabezado, una sección de facturación, líneas de artículos y totales calculados, y luego exporta el libro de trabajo a un documento OFD.
### **Construcción de una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, rellenando el nombre de la empresa y los datos de contacto, agregando un título "INVOICE" en celdas combinadas, registrando el número y la fecha de la factura, listando el cliente facturado, construyendo una tabla de líneas de artículos con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general usando fórmulas de celdas. Se aplica formato como encabezados en negrita, formato de moneda para los precios, bordes y anchos de columna utilizando objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` utilizando `SaveFormat.Ofd`.

```python
from datetime import datetime

data_dir = "C:\\Temp\\"

# Crear un nuevo Workbook
workbook = ac.Workbook()

# Obtener la primera hoja de trabajo
worksheet = workbook.worksheets[0]

# Establecer anchos de columna
worksheet.cells.set_column_width(0, 5)
worksheet.cells.set_column_width(1, 35)
worksheet.cells.set_column_width(2, 12)
worksheet.cells.set_column_width(3, 15)
worksheet.cells.set_column_width(4, 15)
worksheet.cells.set_column_width(5, 5)

# Insertar logo de la empresa
worksheet.pictures.add(1, 1, data_dir + "logo.png")

# Nombre de la empresa y datos de contacto
worksheet.cells["B3"].put_value("Acme Corporation")
worksheet.cells["B4"].put_value("123 Business Street")
worksheet.cells["B5"].put_value("City, State 12345")
worksheet.cells["B6"].put_value("Phone: (555) 123-4567")

# Título de FACTURA - combinar celdas
worksheet.cells.merge(7, 1, 2, 4)
title_cell = worksheet.cells["B8"]
title_cell.put_value("INVOICE")

title_style = workbook.create_style()
title_style.font.is_bold = True
title_style.font.size = 20
title_style.horizontal_alignment = ac.TextAlignmentType.CENTER
title_cell.set_style(title_style)

# Número de factura y fecha
worksheet.cells["B11"].put_value("Invoice Number:")
worksheet.cells["C11"].put_value("INV-2024-001")
worksheet.cells["B12"].put_value("Date:")
worksheet.cells["C12"].put_value(datetime.now().strftime("%Y-%m-%d"))

# Sección de facturación
worksheet.cells["B14"].put_value("Bill To:")
worksheet.cells["B15"].put_value("Client Name")
worksheet.cells["B16"].put_value("Client Address")
worksheet.cells["B17"].put_value("Client City, State")

# Encabezado de líneas de detalle
header_desc = worksheet.cells["B19"]
header_qty = worksheet.cells["C19"]
header_price = worksheet.cells["D19"]
header_total = worksheet.cells["E19"]

header_desc.put_value("Description")
header_qty.put_value("Quantity")
header_price.put_value("Unit Price")
header_total.put_value("Total")

header_style = workbook.create_style()
header_style.font.is_bold = True
header_style.font.color = drawing.Color.white
header_style.background_color = drawing.Color.navy
header_style.horizontal_alignment = ac.TextAlignmentType.CENTER
header_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
header_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

header_desc.set_style(header_style)
header_qty.set_style(header_style)
header_price.set_style(header_style)
header_total.set_style(header_style)

# Estilo de moneda con bordes
currency_style = workbook.create_style()
currency_style.custom = "\"$\"#,##0.00"
currency_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
currency_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Estilo de borde simple para celdas de descripción/cantidad
border_style = workbook.create_style()
border_style.borders[ac.BorderType.TOP_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.BOTTOM_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.LEFT_BORDER].line_style = ac.CellBorderType.THIN
border_style.borders[ac.BorderType.RIGHT_BORDER].line_style = ac.CellBorderType.THIN

# Filas de líneas de detalle
line_items = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(line_items)):
    row = 20 + i
    desc_cell = worksheet.cells[row, 1]
    qty_cell = worksheet.cells[row, 2]
    price_cell = worksheet.cells[row, 3]
    total_cell = worksheet.cells[row, 4]

    desc_cell.put_value(line_items[i][0])
    qty_cell.put_value(line_items[i][1])
    price_cell.put_value(line_items[i][2])
    total_cell.formula = "C" + str(row) + "*D" + str(row)

    desc_cell.set_style(border_style)
    qty_cell.set_style(border_style)
    price_cell.set_style(currency_style)
    total_cell.set_style(currency_style)

# Subtotal, impuestos, total general
worksheet.cells["B24"].put_value("Subtotal:")
subtotal_cell = worksheet.cells["E24"]
subtotal_cell.formula = "SUM(E20:E22)"

worksheet.cells["B25"].put_value("Tax (10%):")
tax_cell = worksheet.cells["E25"]
tax_cell.formula = "E24*0.1"

worksheet.cells["B26"].put_value("Grand Total:")
grand_total_cell = worksheet.cells["E26"]
grand_total_cell.formula = "E24+E25"

# Estilo de negrita + moneda para valores totales
total_style = workbook.create_style()
total_style.font.is_bold = True
total_style.custom = "\"$\"#,##0.00"

subtotal_cell.set_style(total_style)
tax_cell.set_style(total_style)
grand_total_cell.set_style(total_style)

# Estilo de negrita para etiquetas de totales
bold_style = workbook.create_style()
bold_style.font.is_bold = True

worksheet.cells["B24"].set_style(bold_style)
worksheet.cells["B25"].set_style(bold_style)
worksheet.cells["B26"].set_style(bold_style)

# Guardar el libro como archivo OFD
workbook.save(data_dir + "Invoice.ofd", ac.SaveFormat.Ofd)
```
## **Conversión de un archivo Excel existente a OFD**
Aspose.Cells también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente al formato OFD. Esto es útil para pipelines de conversión por lotes, flujos de trabajo de archivo y escenarios donde el libro de trabajo de origen fue producido por otra herramienta y solo necesita ser reemitido como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```python
from datetime import datetime

dataDir = "C:\\Examples\\"

# Abrir un libro de Excel existente desde el disco
workbook = ac.Workbook(dataDir + "SampleBook.xlsx")

# (1) Leer y mostrar valores de las celdas seleccionadas para confirmar que el archivo se cargó
firstSheet = workbook.worksheets[0]
print("First sheet name: " + firstSheet.name)
print("Cell A1: " + firstSheet.cells["A1"].string_value)
print("Cell B1: " + firstSheet.cells["B1"].string_value)
print("Cell C1: " + firstSheet.cells["C1"].string_value)

# (2) Iterar sobre la colección Worksheets para enumerar las hojas disponibles
print("\nAvailable worksheets:")
for i in range(workbook.worksheets.count):
    ws = workbook.worksheets[i]
    print("  [" + str(i) + "] " + ws.name)

# (3) Opcionalmente actualizar una celda de marca de tiempo para reflejar la conversión
firstSheet.cells["A1"].put_value("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
firstSheet.cells.insert_row(0)
firstSheet.cells["A1"].put_value("Conversion Summary")
firstSheet.cells["A2"].put_value("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Configurar las propiedades de PageSetup en la hoja de cálculo
pageSetup = firstSheet.page_setup
pageSetup.orientation = ac.PageOrientationType.LANDSCAPE
pageSetup.paper_size = ac.PaperSizeType.PAPER_A4
pageSetup.fit_to_pages_tall = 1
pageSetup.fit_to_pages_wide = 1

# (5) Opcionalmente establecer el área de impresión para la salida OFD
lastRow = firstSheet.cells.max_data_row
lastCol = firstSheet.cells.max_data_column
lastColLetter = ac.CellsHelper.column_index_to_name(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.page_setup.print_area = printArea
print("\nPrint area set to: " + printArea)

# (6) Guardar el libro como un archivo OFD
workbook.save(dataDir + "SampleBook.ofd", ac.SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")
```

## **Artículos relacionados**
- [División de archivos Excel en varios archivos](/cells/es/python-net/splitting-excel-files-into-multiple-files/)
- [Insertar una imagen en una celda](/cells/es/python-net/inserting-an-image-into-a-cell/)
- [Lectura y escritura de archivos DBF](/cells/es/python-net/dbf/)
- [Convertir minigráfico a imagen y HTML en Aspose.Cells para Aspose.Cells para Python a través de .NET](/cells/es/python-net/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}