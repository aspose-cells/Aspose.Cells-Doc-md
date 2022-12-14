---
title: Ta bort kalkylblad från arbetsböcker
type: docs
weight: 100
url: /sv/net/delete-worksheets-from-workbooks/
---
Du kan ta bort alla kalkylblad i en arbetsbok. Om du vill ta bort ett kalkylblad använder du kalkylbladets värdobjekt eller kommer åt kalkylbladet genom att använda arbetsbokens arksamling.
## **VSTO**
{{< highlight "csharp" >}}

  Excel.Workbook myWorkbook= this.Application.Workbooks.Open(fileName);

 myWorkbook.Sheets[2].Delete();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

  Workbook myWorkbook = new Workbook(fileName);

 myWorkbook.Worksheets.RemoveAt(1);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **Ladda ner**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
