---
title: Create and Save New Workbooks
type: docs
weight: 70
url: /net/create-and-save-new-workbooks/
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Migration Tips:**
1. Create a Workbook object.  
2. Get the current worksheet.  
3. Insert some text in any cell.  
4. Save the workbook.  

### **VSTO**
Below is a code example for VSTO

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

  Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

  Excel.Range cells = worksheet.Cells;

  cells.set_Item(1, 1, "Some Text");

  newWorkbook.Save();

{{< /highlight >}}

### **Aspose.Cells**
Below is a code example for Aspose.Cells

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

  Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

  Cells cells = worksheet.Cells;

  cells[0, 0].PutValue("Some Text");

  newWorkbook.Save(fileName);

{{< /highlight >}}

## **Download**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
