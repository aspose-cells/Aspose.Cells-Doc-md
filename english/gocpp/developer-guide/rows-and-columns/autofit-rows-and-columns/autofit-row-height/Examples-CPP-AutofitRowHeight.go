package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Define the file path
	filePath := "..\\Data\\01_SourceDirectory\\"

	// Open an existing Excel file and save it as PDF
	wb, _ := NewWorkbook_String(filePath + "sample.xlsx")
	_ = wb.Save_String(filePath + "out.pdf")

	// Set load options for the second workbook
	loadOptions, _ := NewLoadOptions()
	autoFitterOptions, _ := NewAutoFitterOptions()
	_ = autoFitterOptions.SetOnlyAuto(true)
	_ = loadOptions.SetAutoFitterOptions(autoFitterOptions)

	// Open the existing Excel file with load options and save it as PDF
	book, _ := NewWorkbook_String_LoadOptions(filePath+"sample.xlsx", loadOptions)
	_ = book.Save_String(filePath + "out2.pdf")

	fmt.Println("PDF files created successfully!")
}