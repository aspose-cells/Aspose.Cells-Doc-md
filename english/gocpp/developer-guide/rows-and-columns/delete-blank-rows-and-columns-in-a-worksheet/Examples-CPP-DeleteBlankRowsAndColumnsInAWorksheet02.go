package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	srcDir := "..\\Data\\01_SourceDirectory\\"

	// Path of input Excel file
	inputFilePath := srcDir + "SampleInput.xlsx"

	// Create a new Workbook instance
	workbook, _ := NewWorkbook_String(inputFilePath)

	// Create a Worksheets object with reference to the sheets of the Workbook
	worksheets, _ := workbook.GetWorksheets()

	// Get the first Worksheet from WorksheetCollection
	sheet, _ := worksheets.Get_Int(0)

	// Delete the blank columns from the worksheet
	cells, _ := sheet.GetCells()
	cells.DeleteBlankColumns()

	// Save the Excel file
	outputFilePath := srcDir + "mybook.out.xlsx"
	workbook.Save_String(outputFilePath)

	fmt.Println("Blank columns deleted successfully!")
}