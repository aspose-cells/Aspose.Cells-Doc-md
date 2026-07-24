using System;
using Aspose.Cells;
using System.Drawing;

string dataDir = "C:\\Temp\\";

// Create a new Workbook
Workbook workbook = new Workbook();

// Obtain the first worksheet
Worksheet worksheet = workbook.Worksheets[0];

// Set column widths
worksheet.Cells.SetColumnWidth(0, 5);
worksheet.Cells.SetColumnWidth(1, 35);
worksheet.Cells.SetColumnWidth(2, 12);
worksheet.Cells.SetColumnWidth(3, 15);
worksheet.Cells.SetColumnWidth(4, 15);
worksheet.Cells.SetColumnWidth(5, 5);

// Insert company logo
worksheet.Pictures.Add(1, 1, dataDir + "logo.png");

// Company name and contact details
worksheet.Cells["B3"].PutValue("Acme Corporation");
worksheet.Cells["B4"].PutValue("123 Business Street");
worksheet.Cells["B5"].PutValue("City, State 12345");
worksheet.Cells["B6"].PutValue("Phone: (555) 123-4567");

// INVOICE title - merge cells
worksheet.Cells.Merge(7, 1, 2, 4);
Cell titleCell = worksheet.Cells["B8"];
titleCell.PutValue("INVOICE");

Style titleStyle = workbook.CreateStyle();
titleStyle.Font.IsBold = true;
titleStyle.Font.Size = 20;
titleStyle.HorizontalAlignment = TextAlignmentType.Center;
titleCell.SetStyle(titleStyle);

// Invoice number and date
worksheet.Cells["B11"].PutValue("Invoice Number:");
worksheet.Cells["C11"].PutValue("INV-2024-001");
worksheet.Cells["B12"].PutValue("Date:");
worksheet.Cells["C12"].PutValue(DateTime.Now.ToString("yyyy-MM-dd"));

// Bill-to section
worksheet.Cells["B14"].PutValue("Bill To:");
worksheet.Cells["B15"].PutValue("Client Name");
worksheet.Cells["B16"].PutValue("Client Address");
worksheet.Cells["B17"].PutValue("Client City, State");

// Line items header
Cell headerDesc = worksheet.Cells["B19"];
Cell headerQty = worksheet.Cells["C19"];
Cell headerPrice = worksheet.Cells["D19"];
Cell headerTotal = worksheet.Cells["E19"];

headerDesc.PutValue("Description");
headerQty.PutValue("Quantity");
headerPrice.PutValue("Unit Price");
headerTotal.PutValue("Total");

Style headerStyle = workbook.CreateStyle();
headerStyle.Font.IsBold = true;
headerStyle.Font.Color = Color.White;
headerStyle.BackgroundColor = Color.Navy;
headerStyle.HorizontalAlignment = TextAlignmentType.Center;
headerStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
headerStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

headerDesc.SetStyle(headerStyle);
headerQty.SetStyle(headerStyle);
headerPrice.SetStyle(headerStyle);
headerTotal.SetStyle(headerStyle);

// Currency style with borders
Style currencyStyle = workbook.CreateStyle();
currencyStyle.Custom = "\"$\"#,##0.00";
currencyStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
currencyStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Plain border style for description/quantity cells
Style borderStyle = workbook.CreateStyle();
borderStyle.Borders[BorderType.TopBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.BottomBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.LeftBorder].LineStyle = CellBorderType.Thin;
borderStyle.Borders[BorderType.RightBorder].LineStyle = CellBorderType.Thin;

// Line items rows
object[,] lineItems = new object[,] {
    {"Product A - Widget", 2, 50.00},
    {"Product B - Gadget", 3, 75.00},
    {"Product C - Service", 1, 100.00}
};

for (int i = 0; i < lineItems.GetLength(0); i++)
{
    int row = 20 + i;
    Cell descCell = worksheet.Cells[row, 1];
    Cell qtyCell = worksheet.Cells[row, 2];
    Cell priceCell = worksheet.Cells[row, 3];
    Cell totalCell = worksheet.Cells[row, 4];

    descCell.PutValue(lineItems[i, 0]);
    qtyCell.PutValue(lineItems[i, 1]);
    priceCell.PutValue(lineItems[i, 2]);
    totalCell.Formula = "C" + row + "*D" + row;

    descCell.SetStyle(borderStyle);
    qtyCell.SetStyle(borderStyle);
    priceCell.SetStyle(currencyStyle);
    totalCell.SetStyle(currencyStyle);
}

// Subtotal, tax, grand total
worksheet.Cells["B24"].PutValue("Subtotal:");
Cell subtotalCell = worksheet.Cells["E24"];
subtotalCell.Formula = "SUM(E20:E22)";

worksheet.Cells["B25"].PutValue("Tax (10%):");
Cell taxCell = worksheet.Cells["E25"];
taxCell.Formula = "E24*0.1";

worksheet.Cells["B26"].PutValue("Grand Total:");
Cell grandTotalCell = worksheet.Cells["E26"];
grandTotalCell.Formula = "E24+E25";

// Bold + currency style for total values
Style totalStyle = workbook.CreateStyle();
totalStyle.Font.IsBold = true;
totalStyle.Custom = "\"$\"#,##0.00";

subtotalCell.SetStyle(totalStyle);
taxCell.SetStyle(totalStyle);
grandTotalCell.SetStyle(totalStyle);

// Bold style for total labels
Style boldStyle = workbook.CreateStyle();
boldStyle.Font.IsBold = true;

worksheet.Cells["B24"].SetStyle(boldStyle);
worksheet.Cells["B25"].SetStyle(boldStyle);
worksheet.Cells["B26"].SetStyle(boldStyle);

// Save the workbook as an OFD file
workbook.Save(dataDir + "Invoice.ofd", SaveFormat.Ofd);
