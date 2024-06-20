---
title: Supprimer des feuilles de calcul à partir des classeurs
type: docs
weight: 100
url: /fr/net/delete-worksheets-from-workbooks/
---

Vous pouvez supprimer n'importe quelle feuille de calcul dans un classeur. Pour supprimer une feuille de calcul, utilisez l'élément hôte de feuille de calcul ou accédez à la feuille de calcul en utilisant la collection de feuilles du classeur.
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
## **Télécharger**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/DeleteWorksheetsFromWorkbooks.zip)
