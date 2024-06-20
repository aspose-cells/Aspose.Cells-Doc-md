---
title: Ta bort arbetsblad från arbetsböcker
type: docs
weight: 100
url: /sv/net/delete-worksheets-from-workbooks/
---

Du kan ta bort vilket arbetsblad som helst i en arbetsbok. För att ta bort ett arbetsblad, använd arbetsbladets värdobjekt eller kom åt arbetsbladet genom att använda kalkylbladssamlingen i arbetsboken.
## **VSTO**
{{< highlight csharp >}}

  Excel.Workbook myWorkbook= this.Application.Workbooks.Open(fileName);

 myWorkbook.Sheets[2].Delete();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight csharp >}}

  Workbook myWorkbook = new Workbook(fileName);

 myWorkbook.Worksheets.RemoveAt(1);

 myWorkbook.Save(fileName);

{{< /highlight >}}
## **Nerladdning**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
