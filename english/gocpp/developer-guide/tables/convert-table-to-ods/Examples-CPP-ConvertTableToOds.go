package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Source directory path
	sourceDir := "..\\Data\\01_SourceDirectory\\"

	// Output directory path
	outputDir := "..\\Data\\02_OutputDirectory\\"

	// Open an existing file that contains a table/list object in it
	inputFilePath := sourceDir + "SampleTable.xlsx"
	workbook, _ := NewWorkbook_String(inputFilePath)

	// Save the file in ODS format
	_ = workbook.Save_String(outputDir + "ConvertTableToOds_out.ods")

	fmt.Println("Conversion to ODS completed successfully!")
}