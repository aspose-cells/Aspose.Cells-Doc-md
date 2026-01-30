package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	sourceDir := "..\\Data\\01_SourceDirectory\\"

	// Load the first workbook with automatic paper size set to false
	wb1, _ := NewWorkbook_String(sourceDir + "samplePageSetupIsAutomaticPaperSize-False.xlsx")

	// Load the second workbook with automatic paper size set to true
	wb2, _ := NewWorkbook_String(sourceDir + "samplePageSetupIsAutomaticPaperSize-True.xlsx")

	// Access the first worksheet of both workbooks
	wss1, _ := wb1.GetWorksheets()
	ws11, _ := wss1.Get_Int(0)

	wss2, _ := wb2.GetWorksheets()
	ws12, _ := wss2.Get_Int(0)

	// Get PageSetup objects
	ps1, _ := ws11.GetPageSetup()
	ps2, _ := ws12.GetPageSetup()

	// Retrieve IsAutomaticPaperSize properties
	isAuto1, _ := ps1.IsAutomaticPaperSize()
	isAuto2, _ := ps2.IsAutomaticPaperSize()

	// Print the results
	fmt.Printf("First Worksheet of First Workbook - IsAutomaticPaperSize: %v\n", isAuto1)
	fmt.Printf("First Worksheet of Second Workbook - IsAutomaticPaperSize: %v\n", isAuto2)
}