---
title: Keep Separators for Blank Rows while exporting spreadsheets to CSV format
type: docs
weight: 160
url: /net/keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format/
---

## **Keep Separators for Blank Rows while exporting spreadsheets to CSV format**

Aspose.Cells provides the ability to keep line separators while converting spreadsheets to CSV format. For this, You may use the **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** property of **[TxtSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions)** class. **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** is a boolean property. To keep the separators for blank lines while converting the Excel File to CSV, set the **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** property to **true**.

The following sample code loads the [source Excel file](84378743.xlsx). It sets **[TxtSaveOptions.KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** property to **true** and saves it as [output.csv](84378744.csv). The screenshot shows the comparison between the source Excel file, the default output generated while converting the spreadsheet to CSV and the output generated by setting **[KeepSeparatorsForBlankRow](https://reference.aspose.com/cells/net/aspose.cells/txtsaveoptions/properties/keepseparatorsforblankrow)** to **true**.

![todo:image_alt_text](keep-separators-for-blank-rows-while-exporting-spreadsheets-to-csv-format_1.jpg)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Handling-KeepSeparatorsForBlankRow-1.cs" >}}