package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source and output directory paths
	srcDir := "..\\Data\\01_SourceDirectory\\"
	outDir := "..\\Data\\02_OutputDirectory\\"

	// Instantiate a new Workbook
	workbook, _ := NewWorkbook()

	// Get first Worksheet
	worksheets, _ := workbook.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)

	// Get Cells collection
	cells, _ := sheet.GetCells()

	// Set formula with external links in A1
	formulaA1 := "=SUM('[" + srcDir + "book1.xlsx]Sheet1'!A2, '['" + srcDir + "book1.xlsx]Sheet1'!A4)"
	cellA1, _ := cells.Get_String("A1")
	cellA1.SetFormula_String(formulaA1)

	// Set formula with external links in A2
	formulaA2 := "='[" + srcDir + "book1.xlsx]Sheet1'!A8"
	cellA2, _ := cells.Get_String("A2")
	cellA2.SetFormula_String(formulaA2)

	// Save the workbook
	_ = workbook.Save_String(outDir + "output_out.xlsx")

	fmt.Println("Workbook saved successfully with external links!")
}