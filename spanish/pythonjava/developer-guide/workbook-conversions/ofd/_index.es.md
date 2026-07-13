---
title: Conversión de Excel a formato OFD
linktitle: Conversión de Excel a formato OFD
description: Aspose.Cells for Python via Java es una biblioteca para trabajar con archivos de hojas de cálculo que admite la conversión de libros de trabajo de Excel al formato OFD (Open Fixed-layout Document). Este artículo demuestra cómo crear contenido de Excel y exportarlo como OFD, así como cómo convertir archivos de Excel existentes a OFD usando Aspose.Cells for Python via Java.
keywords: Aspose.Cells, biblioteca Python via Java, hoja de cálculo, Excel a OFD, conversión OFD, SaveFormat.Ofd, documento de diseño fijo, exportación de libros de trabajo
type: docs
weight: 195
url: /es/python-java/converting-excel-to-ofd-format/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells for Python via Java admite la conversión de libros de trabajo de Excel directamente al formato OFD (Open Fixed-layout Document) usando el valor de enumeración `SaveFormat.Ofd`. El documento OFD resultante conserva el diseño visible, el contenido, las celdas combinadas, los anchos de columna, los altos de fila, las fuentes, los colores, los bordes y los formatos de número del libro de trabajo. Esto hace que Aspose.Cells for Python via Java sea adecuado para flujos de trabajo de archivo, impresión, presentación regulatoria y envío a entidades gubernamentales que requieran una salida con diseño fijo.

{{% /alert %}}
## **Introducción**
OFD (Open Fixed-layout Document) es un estándar nacional chino (GB/T 33190-2016) para representar documentos digitales en un diseño fijo basado en páginas. Desempeña un papel similar al de PDF para casos de uso en los que la apariencia visual del documento de origen debe conservarse exactamente como fue creada. OFD es ampliamente adoptado para presentaciones ante entidades gubernamentales, trámites regulatorios, facturas electrónicas y archivo a largo plazo en la República Popular China.

Convertir libros de trabajo de Excel a OFD es un requisito común en escenarios en los que el contenido de la hoja de cálculo debe distribuirse como un artefacto de solo lectura y con diseño bloqueado en lugar de como una hoja de cálculo editable. Los ejemplos incluyen enviar una factura finalizada a un cliente, archivar un informe financiero trimestral o enviar una hoja de cálculo de presupuesto a una autoridad regulatoria. Aspose.Cells for Python via Java aborda este requisito a través del valor de enumeración `SaveFormat.Ofd`, que escribe el libro de trabajo directamente a OFD sin requerir un paso de conversión intermedio. La salida OFD conserva los valores de celda, los rangos combinados, las fuentes, los colores, los bordes, los formatos de número y las opciones de configuración de página configuradas en el libro de trabajo.

{{% alert color="primary" %}}

La salida OFD generada por Aspose.Cells for Python via Java conserva el diseño visible del libro de trabajo de origen, incluyendo el contenido de las celdas, las celdas combinadas, los anchos de columna y los altos de fila. El formato de celda, como fuentes, colores, bordes, alineación y formatos de número, también se representa en la salida de diseño fijo. Las opciones de configuración de página configuradas en la hoja de cálculo, como el tamaño del papel, la orientación y el área de impresión, influyen en el diseño del documento OFD resultante.

{{% /alert %}}
## **Crear un libro de trabajo de Excel y guardarlo como OFD**
Aspose.Cells for Python via Java le permite crear un libro de trabajo mediante programación, rellenarlo con datos y luego guardarlo directamente en formato OFD usando la enumeración `SaveFormat.Ofd`. El siguiente ejemplo crea una factura desde cero. Agrega un logotipo de la empresa, información del encabezado, una sección de facturación, líneas de artículos y totales calculados, luego exporta el libro de trabajo a un documento OFD.
### **Construir una factura con un logotipo**
El ejemplo construye una hoja de cálculo de factura insertando una imagen de logotipo en el área superior izquierda, completando el nombre de la empresa y los datos de contacto, agregando un título "INVOICE" a lo largo de celdas combinadas, registrando el número y la fecha de la factura, listando el cliente facturado, construyendo una tabla de líneas de artículos con columnas de descripción, cantidad, precio unitario y total, y calculando el subtotal, el impuesto y el total general usando fórmulas de celda. Se aplica formato como encabezados en negrita, formato de moneda para los precios, bordes y anchos de columna usando objetos `Style` y `Font`. Finalmente, el libro de trabajo se guarda con la extensión `.ofd` usando `SaveFormat.Ofd`.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Crear un nuevo Workbook
workbook = Workbook()

# Obtener la primera hoja de trabajo
worksheet = workbook.getWorksheets().get(0)

# Establecer anchos de columna
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Insertar el logo de la empresa
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Nombre de la empresa y datos de contacto
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# Título INVOICE - combinar celdas
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# Número de factura y fecha
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# Sección Facturar a
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# Encabezado de líneas de detalle
headerDesc = worksheet.getCells().get("B19")
headerQty = worksheet.getCells().get("C19")
headerPrice = worksheet.getCells().get("D19")
headerTotal = worksheet.getCells().get("E19")

headerDesc.putValue("Description")
headerQty.putValue("Quantity")
headerPrice.putValue("Unit Price")
headerTotal.putValue("Total")

headerStyle = workbook.createStyle()
headerStyle.getFont().setBold(True)
headerStyle.getFont().setColor(Color.getWhite())
headerStyle.setBackgroundColor(Color.getNavy())
headerStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
headerStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
headerStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

headerDesc.setStyle(headerStyle)
headerQty.setStyle(headerStyle)
headerPrice.setStyle(headerStyle)
headerTotal.setStyle(headerStyle)

# Estilo de moneda con bordes
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Estilo de borde simple para celdas de descripción/cantidad
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Filas de líneas de detalle
lineItems = [
    ["Product A - Widget", 2, 50.00],
    ["Product B - Gadget", 3, 75.00],
    ["Product C - Service", 1, 100.00]
]

for i in range(len(lineItems)):
    row = 20 + i
    descCell = worksheet.getCells().get(row, 1)
    qtyCell = worksheet.getCells().get(row, 2)
    priceCell = worksheet.getCells().get(row, 3)
    totalCell = worksheet.getCells().get(row, 4)

    descCell.putValue(lineItems[i][0])
    qtyCell.putValue(lineItems[i][1])
    priceCell.putValue(lineItems[i][2])
    totalCell.setFormula("C" + str(row) + "*D" + str(row))

    descCell.setStyle(borderStyle)
    qtyCell.setStyle(borderStyle)
    priceCell.setStyle(currencyStyle)
    totalCell.setStyle(currencyStyle)

# Subtotal, impuesto, total general
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Estilo negrita + moneda para los valores totales
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Estilo negrita para las etiquetas de totales
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Guardar el libro como un archivo OFD
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()
```
## **Convertir un archivo de Excel existente a OFD**
Aspose.Cells for Python via Java también puede cargar un libro de trabajo de Excel existente desde el disco y exportarlo directamente al formato OFD. Esto es útil para canalizaciones de conversión por lotes, flujos de trabajo de archivo y escenarios en los que el libro de trabajo de origen fue producido por otra herramienta y solo necesita ser reemitido como un artefacto de diseño fijo. El siguiente ejemplo carga un libro de trabajo `.xlsx` existente, lee los datos de sus celdas, aplica ajustes opcionales de configuración de página y guarda el resultado como un documento OFD.

```python
from datetime import datetime
jpype.startJVM()
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, PageOrientationType, PaperSizeType, CellsHelper

dataDir = "C:\\Examples\\"

# Abrir un libro de Excel existente desde el disco
workbook = Workbook(dataDir + "SampleBook.xlsx")

# (1) Leer y mostrar valores de celdas seleccionadas para confirmar que el archivo fue cargado
firstSheet = workbook.getWorksheets().get(0)
print("First sheet name: " + firstSheet.getName())
print("Cell A1: " + firstSheet.getCells().get("A1").getStringValue())
print("Cell B1: " + firstSheet.getCells().get("B1").getStringValue())
print("Cell C1: " + firstSheet.getCells().get("C1").getStringValue())

# (2) Iterar sobre la colección Worksheets para enumerar las hojas disponibles
print("\nAvailable worksheets:")
for i in range(workbook.getWorksheets().getCount()):
    ws = workbook.getWorksheets().get(i)
    print("  [" + str(i) + "] " + ws.getName())

# (3) Opcionalmente actualizar una celda de marca de tiempo para reflejar la conversión
firstSheet.getCells().get("A1").putValue("Converted on: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Agregar una fila de encabezado de resumen en la parte superior del bloque de datos
firstSheet.getCells().insertRow(0)
firstSheet.getCells().get("A1").putValue("Conversion Summary")
firstSheet.getCells().get("A2").putValue("Generated: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# (4) Configurar las propiedades de PageSetup en la hoja de cálculo
pageSetup = firstSheet.getPageSetup()
pageSetup.setOrientation(PageOrientationType.LANDSCAPE)
pageSetup.setPaperSize(PaperSizeType.PAPER_A_4)
pageSetup.setFitToPagesTall(1)
pageSetup.setFitToPagesWide(1)

# (5) Opcionalmente establecer el área de impresión para la salida OFD
lastRow = firstSheet.getCells().getMaxDataRow()
lastCol = firstSheet.getCells().getMaxDataColumn()
lastColLetter = CellsHelper.columnIndexToName(lastCol)
printArea = "A1:" + lastColLetter + str(lastRow + 1)
firstSheet.getPageSetup().setPrintArea(printArea)
print("\nPrint area set to: " + printArea)

# (6) Guardar el libro como un archivo OFD
workbook.save(dataDir + "SampleBook.ofd", SaveFormat.Ofd)
print("\nFile successfully converted to OFD format: " + dataDir + "SampleBook.ofd")

jpype.shutdownJVM()
```

## **Artículos relacionados**
- [Dividir archivos de Excel en varios archivos](/cells/es/python-java/splitting-excel-files-into-multiple-files/)
- [Insertar una imagen en una celda](/cells/es/python-java/inserting-an-image-into-a-cell/)
- [Leer y escribir archivos DBF](/cells/es/python-java/dbf/)
- [Convertir minigráficos a imagen y HTML en Aspose.Cells for Python via Java](/cells/es/python-java/convert-sparkline-to-image-and-html/)
{{< app/cells/assistant language="python" >}}