package main

import (
	"fmt"

	. "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
	// Directories
	srcDir := "..\\Data\\01_SourceDirectory\\"
	outDir := "..\\Data\\02_OutputDirectory\\"

	// Load workbook
	workbook, err := NewWorkbook_String(srcDir + "SampleBook.xlsx")
	if err != nil {
		fmt.Println(err)
		return
	}

	// Access first worksheet
	worksheets, err := workbook.GetWorksheets()
	if err != nil {
		fmt.Println(err)
		return
	}
	worksheet, err := worksheets.Get_Int(0)
	if err != nil {
		fmt.Println(err)
		return
	}

	// Set image options
	opts, err := NewImageOrPrintOptions()
	if err != nil {
		fmt.Println(err)
		return
	}
	if err = opts.SetOnePagePerSheet(true); err != nil {
		fmt.Println(err)
		return
	}
	if err = opts.SetImageType(ImageType_Png); err != nil {
		fmt.Println(err)
		return
	}

	// Render sheet to image
	sr, err := NewSheetRender(worksheet, opts)
	if err != nil {
		fmt.Println(err)
		return
	}
	if err = sr.ToImage_Int_String(0, outDir+"OutputImage_out.png"); err != nil {
		fmt.Println(err)
		return
	}
}