package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Load source Excel file
	inputFilePath := "sampleSheetId.xlsx"
	wb, _ := NewWorkbook_String(inputFilePath)

	// Access first worksheet
	worksheets, _ := wb.GetWorksheets()
	ws, _ := worksheets.Get_Int(0)

	// Print its Sheet or Tab Id on console
	tabId, _ := ws.GetTabId()
	fmt.Println("Sheet or Tab Id:", tabId)

	// Change Sheet or Tab Id
	_ = ws.SetTabId(358)

	// Save the workbook
	outputFilePath := "outputSheetId.xlsx"
	_ = wb.Save_String(outputFilePath)
}