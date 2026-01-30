package main

import (
    "fmt"
    . "github.com/aspose-cells/aspose-cells-go-cpp/v25"
)

func main() {
    srcDir := "..\\Data\\01_SourceDirectory\\"
    outDir := "..\\Data\\02_OutputDirectory\\"
    filePath := srcDir + "source.xlsx"

    workbook, _ := NewWorkbook_String(filePath)

    worksheets, _ := workbook.GetWorksheets()
    worksheet, _ := worksheets.Get_Int(0)

    _ = worksheet.SetShowFormulas(true)

    _ = workbook.Save_String(outDir + "out.xlsx")

    fmt.Println("Formulas shown successfully!")
}