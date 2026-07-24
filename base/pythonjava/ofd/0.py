import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook
from asposecells.api import Workbook, Worksheet, Cells, Range, SaveFormat, Style, Cell, TextAlignmentType, BorderType, CellBorderType, Color

dataDir = "/tmp/"

# Create a new Workbook
workbook = Workbook()

# Obtain the first worksheet
worksheet = workbook.getWorksheets().get(0)

# Set column widths
worksheet.getCells().setColumnWidth(0, 5)
worksheet.getCells().setColumnWidth(1, 35)
worksheet.getCells().setColumnWidth(2, 12)
worksheet.getCells().setColumnWidth(3, 15)
worksheet.getCells().setColumnWidth(4, 15)
worksheet.getCells().setColumnWidth(5, 5)

# Insert company logo
worksheet.getPictures().add(1, 1, dataDir + "logo.png")

# Company name and contact details
worksheet.getCells().get("B3").putValue("Acme Corporation")
worksheet.getCells().get("B4").putValue("123 Business Street")
worksheet.getCells().get("B5").putValue("City, State 12345")
worksheet.getCells().get("B6").putValue("Phone: (555) 123-4567")

# INVOICE title - merge cells
worksheet.getCells().merge(7, 1, 2, 4)
titleCell = worksheet.getCells().get("B8")
titleCell.putValue("INVOICE")

titleStyle = workbook.createStyle()
titleStyle.getFont().setBold(True)
titleStyle.getFont().setSize(20)
titleStyle.setHorizontalAlignment(TextAlignmentType.CENTER)
titleCell.setStyle(titleStyle)

# Invoice number and date
worksheet.getCells().get("B11").putValue("Invoice Number:")
worksheet.getCells().get("C11").putValue("INV-2024-001")
worksheet.getCells().get("B12").putValue("Date:")
worksheet.getCells().get("C12").putValue(datetime.datetime.now().strftime("%Y-%m-%d"))

# Bill-to section
worksheet.getCells().get("B14").putValue("Bill To:")
worksheet.getCells().get("B15").putValue("Client Name")
worksheet.getCells().get("B16").putValue("Client Address")
worksheet.getCells().get("B17").putValue("Client City, State")

# Line items header
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

# Currency style with borders
currencyStyle = workbook.createStyle()
currencyStyle.setCustom("\"$\"#,##0.00")
currencyStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
currencyStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Plain border style for description/quantity cells
borderStyle = workbook.createStyle()
borderStyle.getBorders().get(BorderType.TOP_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.BOTTOM_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.LEFT_BORDER).setLineStyle(CellBorderType.THIN)
borderStyle.getBorders().get(BorderType.RIGHT_BORDER).setLineStyle(CellBorderType.THIN)

# Line items rows
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

# Subtotal, tax, grand total
worksheet.getCells().get("B24").putValue("Subtotal:")
subtotalCell = worksheet.getCells().get("E24")
subtotalCell.setFormula("SUM(E20:E22)")

worksheet.getCells().get("B25").putValue("Tax (10%):")
taxCell = worksheet.getCells().get("E25")
taxCell.setFormula("E24*0.1")

worksheet.getCells().get("B26").putValue("Grand Total:")
grandTotalCell = worksheet.getCells().get("E26")
grandTotalCell.setFormula("E24+E25")

# Bold + currency style for total values
totalStyle = workbook.createStyle()
totalStyle.getFont().setBold(True)
totalStyle.setCustom("\"$\"#,##0.00")

subtotalCell.setStyle(totalStyle)
taxCell.setStyle(totalStyle)
grandTotalCell.setStyle(totalStyle)

# Bold style for total labels
boldStyle = workbook.createStyle()
boldStyle.getFont().setBold(True)

worksheet.getCells().get("B24").setStyle(boldStyle)
worksheet.getCells().get("B25").setStyle(boldStyle)
worksheet.getCells().get("B26").setStyle(boldStyle)

# Save the workbook as an OFD file
workbook.save(dataDir + "Invoice.ofd", SaveFormat.Ofd)

jpype.shutdownJVM()