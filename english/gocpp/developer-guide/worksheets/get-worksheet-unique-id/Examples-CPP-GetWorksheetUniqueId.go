package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	srcDir := "..\\Data\\01_SourceDirectory\\"

	// Load source Excel file
	workbook, _ := NewWorkbook_String(srcDir + "Book1.xlsx")

	// Access first worksheet
	worksheets, _ := workbook.GetWorksheets()
	worksheet, _ := worksheets.Get_Int(0)

	// Print Unique ID
	uniqueId, _ := worksheet.GetUniqueId()
	fmt.Println("Unique ID:", uniqueId)
}