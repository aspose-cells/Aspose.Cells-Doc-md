---
title: Tableaux croisés dynamiques
description: Créer et formater des tableaux croisés dynamiques de fichiers de feuilles de calcul Excel.
linktitle: Tableaux croisés dynamiques
url: /fr/python-java/create-pivot-table/
type: docs
weight: 160
keywords: Créer un Tableau Croisé Dynamique, Insérer un Tableau Croisé Dynamique, Formater un Tableau Croisé Dynamique.
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Créer un tableau croisé dynamique**
Il est possible d'utiliser Aspose.Cells pour ajouter des tableaux croisés dynamiques aux feuilles de calcul par programmation.

### **Modèle d'objet du tableau croisé dynamique**
Aspose.Cells fournit un ensemble de classes utilisées pour créer et contrôler les tableaux croisés dynamiques. Les éléments constitutifs sont :
- `PivotField` représente un champ dans un `PivotTable`.
- `PivotFieldCollection` représente une collection de tous les objets `PivotField` dans le `PivotTable`.
- `PivotTable` représente un tableau croisé dynamique sur une feuille de calcul.
- `PivotTableCollection` représente une collection de tous les objets `PivotTable` sur une feuille de calcul.

### **Création d'un tableau croisé dynamique simple à l'aide d'Aspose.Cells**
1. Ajoutez des données à une feuille de calcul à l'aide de la méthode `putValue` de la cellule. Ces données serviront de source de données pour le tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode `add` de la collection `PivotTables`, encapsulée dans l'objet feuille de calcul.
3. Accédez au nouvel objet `PivotTable` de la collection `PivotTables` en passant l'index du tableau croisé dynamique.
4. Utilisez n'importe lequel des objets `PivotTable` (expliqués ci-dessus) pour gérer le tableau croisé dynamique.

Après l'exécution du code d'exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

```python
import jpype
import asposecells
jpype.startJVM()
from asposecells.api import Workbook, PivotFieldType

dataDir = "./"
workbook = Workbook()
sheet = workbook.getWorksheets().get(0)
cells = sheet.getCells()

cell = cells.get("A1")
cell.putValue("Sport")
cell = cells.get("B1")
cell.putValue("Quarter")
cell = cells.get("C1")
cell.putValue("Sales")

cell = cells.get("A2")
cell.putValue("Golf")
cell = cells.get("A3")
cell.putValue("Golf")
cell = cells.get("A4")
cell.putValue("Tennis")
cell = cells.get("A5")
cell.putValue("Tennis")
cell = cells.get("A6")
cell.putValue("Tennis")
cell = cells.get("A7")
cell.putValue("Tennis")
cell = cells.get("A8")
cell.putValue("Golf")

cell = cells.get("B2")
cell.putValue("Qtr3")
cell = cells.get("B3")
cell.putValue("Qtr4")
cell = cells.get("B4")
cell.putValue("Qtr3")
cell = cells.get("B5")
cell.putValue("Qtr4")
cell = cells.get("B6")
cell.putValue("Qtr3")
cell = cells.get("B7")
cell.putValue("Qtr4")
cell = cells.get("B8")
cell.putValue("Qtr3")

cell = cells.get("C2")
cell.putValue(1500)
cell = cells.get("C3")
cell.putValue(2000)
cell = cells.get("C4")
cell.putValue(600)
cell = cells.get("C5")
cell.putValue(1500)
cell = cells.get("C6")
cell.putValue(4070)
cell = cells.get("C7")
cell.putValue(5000)
cell = cells.get("C8")
cell.putValue(6430)

pivotTables = sheet.getPivotTables()
index = pivotTables.add("=A1:C8", "E3", "PivotTable2")
pivotTable = pivotTables.get(index)
pivotTable.setRowGrand(False)
pivotTable.addFieldToArea(PivotFieldType.ROW, 0)
pivotTable.addFieldToArea(PivotFieldType.COLUMN, 1)
pivotTable.addFieldToArea(PivotFieldType.DATA, 2)
workbook.save(dataDir + "pivotTable_test_out.xls")
jpype.shutdownJVM()
```

{{% alert color="primary" %}}
Lors de l'affectation d'une plage de cellules comme source de données, la plage doit aller du coin supérieur gauche au coin inférieur droit. Par exemple, "A1:C3" est valide mais "C3:A1" ne l'est pas.
{{% /alert %}}

## Articles connexes
- [Add Filter Fields to a Pivot Table in Aspose.Cells for Python via Java](/cells/fr/python-java/add-page-field-in-pivot-table/)
- [Apply Styles to Pivot Tables in Aspose.Cells for Python via Java](/cells/fr/python-java/apply-style-to-pivot-table/)
- [Modify Page Field Layout in Pivot Table](/cells/fr/python-java/change-page-field-layout/)
- [Filtering Pivot Tables by Label or Value](/cells/fr/python-java/filter-by-label-or-value-of-pivot-table/)
- [Manage Pivot Table Value Fields in Aspose.Cells for Python via Java](/cells/fr/python-java/manage-value-fields/)

{{< app/cells/assistant language="python" >}}