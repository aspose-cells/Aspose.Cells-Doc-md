package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	sourceDir := "..\\Data\\01_SourceDirectory\\"

	// Load source Excel file
	workbook, _ := NewWorkbook_String(sourceDir + "BookWithSomeData.xlsx")

	// Access first worksheet
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)

	// Print number of cells in the worksheet
	cells, _ := worksheet.GetCells()
	count, _ := cells.GetCount()
	fmt.Println("Number of Cells:", count)

	// In case the number of cells is greater than 2147483647, use CountLarge
	countLarge, _ := cells.GetCountLarge()
	fmt.Println("Number of Cells (CountLarge):", countLarge)
}