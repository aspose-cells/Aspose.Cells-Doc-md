package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Load source Excel file
	wb, _ := NewWorkbook_String("sampleSheetId.xlsx")

	// Access first worksheet
	worksheets, _ := wb.GetWorksheets()
	ws, _ := worksheets.Get_Int(0)

	// Print its Sheet or Tab Id on console
	tabId, _ := ws.GetTabId()
	fmt.Println("Sheet or Tab Id:", tabId)

	// Change Sheet or Tab Id
	_ = ws.SetTabId(358)

	// Save the workbook
	_ = wb.Save_String("outputSheetId.xlsx")
}