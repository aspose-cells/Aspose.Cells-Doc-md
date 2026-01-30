package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	dirPath := "..\\Data\\PivotTables\\"
	// Output directory path
	outPath := "..\\Data\\Output\\"

	// Path of input excel file
	sampleManipulatePivotTable := dirPath + "sampleManipulatePivotTable.xlsx"
	// Path of output excel file
	outputManipulatePivotTable := outPath + "outputManipulatePivotTable.xlsx"

	// Load the sample excel file
	wb, _ := NewWorkbook_String(sampleManipulatePivotTable)

	// Access first worksheet
	wss, _ := wb.GetWorksheets()
	ws, _ := wss.Get_Int(0)

	// Change value of cell B3 which is inside the source data of pivot table
	cells, _ := ws.GetCells()
	cellB3, _ := cells.Get_String("B3")
	cellB3.PutValue_String("Cup")

	// Get the value of cell H8 before refreshing pivot table
	cellH8, _ := cells.Get_String("H8")
	val, _ := cellH8.GetStringValue()
	fmt.Println("Before refreshing Pivot Table value of cell H8:", val)

	// Access pivot table, refresh and calculate it
	pivotTables, _ := ws.GetPivotTables()
	pt, _ := pivotTables.Get_Int(0)
	pt.RefreshData()
	pt.CalculateData()

	// Get the value of cell H8 after refreshing pivot table
	cellH8After, _ := cells.Get_String("H8")
	valAfter, _ := cellH8After.GetStringValue()
	fmt.Println("After refreshing Pivot Table value of cell H8:", valAfter)

	// Save the output excel file
	wb.Save_String(outputManipulatePivotTable)
}