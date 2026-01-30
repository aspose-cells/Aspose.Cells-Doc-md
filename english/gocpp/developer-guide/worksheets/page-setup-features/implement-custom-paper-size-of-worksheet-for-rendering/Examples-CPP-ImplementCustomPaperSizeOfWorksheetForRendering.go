package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Create workbook object
	wb, _ := NewWorkbook()

	// Access first worksheet
	worksheets, _ := wb.GetWorksheets()
	ws, _ := worksheets.Get_Int(0)

	// Set custom paper size in unit of inches
	pageSetup, _ := ws.GetPageSetup()
	pageSetup.CustomPaperSize(6, 4)

	// Access cell B4
	cells, _ := ws.GetCells()
	cell, _ := cells.Get_String("B4")

	// Add the message to cell B4
	cell.PutValue_String("Pdf Page Dimensions: 6.00 x 4.00 in")

	// Save the workbook in PDF format
	outputDir := "..\\Data\\02_OutputDirectory\\"
	wb.Save_String(outputDir + "outputCustomPaperSize.pdf")

	fmt.Println("Workbook saved successfully!")
}