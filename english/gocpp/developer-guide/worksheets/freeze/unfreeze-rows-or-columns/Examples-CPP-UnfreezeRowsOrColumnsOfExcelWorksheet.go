package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Instantiate a new Workbook
	inputFilePath := "Frozen.xlsx"
	workbook, _ := NewWorkbook_String(inputFilePath)

	// Unfreeze panes in the first worksheet
	worksheets, _ := workbook.GetWorksheets()
	sheet0, _ := worksheets.Get_Int(0)
	sheet0.UnFreezePanes()

	// Save the modified workbook
	outputFilePath := "Unfrozen.xlsx"
	workbook.Save_String(outputFilePath)

	fmt.Println("Panes unfrozen successfully!")
}