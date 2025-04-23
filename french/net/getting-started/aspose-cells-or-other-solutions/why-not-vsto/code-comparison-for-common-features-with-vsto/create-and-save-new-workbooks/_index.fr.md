---
title: Créer et enregistrer de nouveaux classeurs
type: docs
weight: 70
url: /fr/net/create-and-save-new-workbooks/
---

## **Conseils de migration :**
\1. Créer un objet Classeur
\2. Obtenir la feuille de travail actuelle.
\3. Insérer un texte dans n'importe quelle cellule.
\4. Enregistrer le classeur.
### **VSTO**
Voici un exemple de code pour VSTO

{{< highlight csharp >}}

  Excel.Workbook newWorkbook = this.Application.Workbooks.Add();

 Excel.Worksheet worksheet = newWorkbook.ActiveSheet;

 Excel.Range cells = worksheet.Cells;

 cells.set_Item(1,1,"Some Text");

 newWorkbook.Save();

{{< /highlight >}}
### **Aspose.Cells**
Voici un exemple de code pour Aspose.Cells

{{< highlight csharp >}}

  Workbook newWorkbook = new Workbook();

 Worksheet worksheet = newWorkbook.Worksheets.Add("New Sheet");

 Cells cells = worksheet.Cells;

 cells[0,0].PutValue("Some Text");

 newWorkbook.Save(fileName);

{{< /highlight >}}
## **Télécharger**
- [GitHub](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Create_SaveNewWorkbooks.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
