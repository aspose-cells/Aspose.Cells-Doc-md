---
title: Copier des feuilles de calcul
type: docs
weight: 60
url: /fr/net/copy-worksheets/
---

## **Astuce de migration :**
\1. Créer un objet Workbook et obtenir une feuille de calcul.
\2. Insérer du texte dans la feuille de calcul.
\3. Créer une nouvelle feuille de calcul et la copier dans la feuille de calcul précédente.
### **VSTO**
Erreur de rendu de la macro 'code' : Valeur non valide spécifiée pour le paramètre lang
### **Aspose.Cells**
{{< highlight csharp >}}

  private static string fileName ="CopyWorksheets.xlsx";

 Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0, 0].PutValue("Some Text");

 Worksheet worksheet2 = newWorkbook.Worksheets.Add("MySheet");

 worksheet2.Copy(worksheet);

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Télécharger**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/CopyWorksheets.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
