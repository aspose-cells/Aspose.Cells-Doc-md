package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Load Excel file containing Dialog Sheet
	workbook, _ := NewWorkbook_String("sampleFindIfWorksheetIsDialogSheet.xlsx")

	// Access first worksheet
	worksheets, _ := workbook.GetWorksheets()
	ws, _ := worksheets.Get_Int(0)

	// Find if the sheet type is dialog and print the message
	sheetType, _ := ws.GetType()
	if sheetType == SheetType_Dialog {
		fmt.Println("Worksheet is a Dialog Sheet.")
	}
}