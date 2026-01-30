package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	srcDir := "..\\Data\\01_SourceDirectory\\"

	// Create an instance of Workbook and load a spreadsheet
	book, _ := NewWorkbook_String(srcDir + "sample.xlsx")

	// Access the protected Worksheet
	worksheets, _ := book.GetWorksheets()
	sheet, _ := worksheets.Get_Int(0)

	// Check if Worksheet is password protected
	protection, _ := sheet.GetProtection()
	isProtected, _ := protection.IsProtectedWithPassword()
	if isProtected {
		fmt.Println("Worksheet is password protected")
	} else {
		fmt.Println("Worksheet is not password protected")
	}
}