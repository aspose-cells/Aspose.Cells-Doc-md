package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	srcDir := "..\\Data\\01_SourceDirectory\\"

	// Output directory path
	outDir := "..\\Data\\02_OutputDirectory\\"

	// Open an existing Excel file
	inputFilePath := srcDir + "SampleInput.xlsx"
	workbook, _ := NewWorkbook_String(inputFilePath)

	// Create a Worksheets object with reference to the sheets of the Workbook
	sheets, _ := workbook.GetWorksheets()

	// Get the first Worksheet from WorksheetCollection
	sheet, _ := sheets.Get_Int(0)

	// Delete the Blank Rows from the worksheet
	cells, _ := sheet.GetCells()
	cells.DeleteBlankRows()

	// Save the Excel file
	outputFilePath := outDir + "mybook.out.xlsx"
	workbook.Save_String(outputFilePath)

	fmt.Println("Blank rows deleted and workbook saved successfully!")
}