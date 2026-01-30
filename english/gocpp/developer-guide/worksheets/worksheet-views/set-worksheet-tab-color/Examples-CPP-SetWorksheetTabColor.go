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

	// Path of input Excel file
	inputFilePath := srcDir + "Book1.xlsx"

	// Path of output Excel file
	outputFilePath := outDir + "worksheettabcolor.out.xls"

	// Create workbook
	workbook, _ := NewWorkbook_String(inputFilePath)

	// Get the first worksheet in the book
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)

	// Set the tab color to red
	redColor, _ := Color_Red()
	worksheet.SetTabColor(redColor)

	// Save the Excel file
	workbook.Save_String(outputFilePath)

	fmt.Println("Worksheet tab color set successfully!")
}