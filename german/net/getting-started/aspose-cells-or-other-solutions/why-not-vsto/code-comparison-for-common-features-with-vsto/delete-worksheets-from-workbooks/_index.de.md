---
title: Arbeitsblätter aus Arbeitsmappen löschen
type: docs
weight: 100
url: /de/net/delete-worksheets-from-workbooks/
---

Sie können jedes Arbeitsblatt in einer Arbeitsmappe löschen. Verwenden Sie zum Löschen eines Arbeitsblatts das Arbeitsblatthostelement oder greifen Sie auf das Arbeitsblatt über die Blattsammlung der Arbeitsmappe zu.
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
## **Herunterladen**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
{{< app/cells/assistant language="csharp" >}}
