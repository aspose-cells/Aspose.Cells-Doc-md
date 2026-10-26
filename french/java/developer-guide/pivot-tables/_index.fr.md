---
title: Créer un tableau croisé dynamique
linktitle: Créer un tableau croisé dynamique
description: Créez et mettez en forme des tableaux croisés dynamiques avec Aspose.Cells for Java.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Mettre en forme un tableau croisé dynamique.
type: docs
weight: 160
url: /fr/java/create-pivot-table/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un grand ensemble de données brutes présentées ligne par ligne en une matrice compacte, sans la moindre formule. Vous choisissez les colonnes qui deviennent des étiquettes de ligne, celles qui deviennent des étiquettes de colonne et celles dont les valeurs sont agrégées — le tableau croisé dynamique effectue le regroupement et les calculs :
- **Résumer** — le total des ventes par produit, par région ou par trimestre, au lieu de longues chaînes de formules.
- **Comparer** — les catégories placées sur les lignes et les périodes placées sur les colonnes transforment une liste plate en rapport en croisé où les tendances sont visibles d’un coup d’œil.
- **Explorer le détail** — double-cliquez sur n’importe quelle valeur de synthèse pour examiner les lignes de données source sous-jacentes.
- **Actualiser** — lorsque les données sources changent, un seul rafraîchissement recalcule l’ensemble du rapport.
Les scénarios typiques sont les tableaux de bord des ventes, les répartitions de dépenses et les analyses de stock — pour répondre à toute question du type « comment ces chiffres se répartissent-ils par catégorie et par période ? ». Aspose.Cells for Java permet de créer par programme des tableaux croisés dynamiques équivalents, afin que les classeurs générés par votre application puissent contenir des rapports prêts à l’emploi plutôt que uniquement des données brutes.

### **Créer un tableau croisé dynamique avec Aspose.Cells**

{{% alert color="primary" %}}
Avec Aspose.Cells, vous pouvez ajouter des tableaux croisés dynamiques à des feuilles de calcul. Aspose.Cells fournit plusieurs classes dédiées à la création et au contrôle des tableaux croisés dynamiques. Ces classes servent à créer et à définir les propriétés d’un objet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable), qui constitue l’élément de base des tableaux croisés dynamiques.
Les objets de tableau croisé dynamique sont :
- [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) : représente un champ dans un tableau croisé dynamique.
- [**PivotFieldCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotFieldCollection) : représente une collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotField) contenus dans le tableau croisé dynamique.
- [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) : représente un tableau croisé dynamique.
- [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) : représente la collection de tous les objets de tableau croisé dynamique présents sur la feuille de calcul.
{{% /alert %}}

### **Créer un tableau croisé dynamique simple**
La création d’un tableau croisé dynamique comporte trois étapes principales : écrire les données sources dans les cellules de la feuille de calcul, ajouter le tableau croisé dynamique à un emplacement de destination, puis placer les champs du tableau croisé dynamique dans les zones de ligne, de colonne et de données.
1. Ajoutez des données aux cellules de la feuille de calcul à l’aide de la méthode [**setValue**](https://reference.aspose.com/cells/java/com.aspose.cells/cell#setValue-java.lang.Object-) de l’objet [**Cell**](https://reference.aspose.com/cells/java/com.aspose.cells/cell) (`putValue` dans la plupart des exemples). Ces données serviront de source de données au tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/java/com.aspose.cells/pivottablecollection#add-com.aspose.cells.PivotTable-int-int-) de la classe [**PivotTableCollection**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTableCollection) : `add(sourceData, row, column)`. `sourceData` est la plage source (par exemple, « A1:C8 ») ; `row` et `column` sont les indices de ligne et de colonne de la cellule de destination située dans l’angle supérieur gauche du tableau croisé dynamique ; ces indices commencent à 0 (la cellule E3 correspond à la ligne 2 et à la colonne 4). La méthode renvoie directement le nouvel objet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable).
3. Placez les champs à l’aide de la méthode `addFieldToArea` de l’objet [**PivotTable**](https://reference.aspose.com/cells/java/com.aspose.cells/PivotTable) : indiquez le nom du champ à placer dans la zone de ligne (`PivotFieldType.ROW`), dans la zone de colonne (`PivotFieldType.COLUMN`) ou dans la zone de données (`PivotFieldType.DATA`).
4. Enregistrez le classeur — le tableau croisé dynamique est alors écrit dans le fichier.
L’exemple de code ci-dessous crée un tableau croisé dynamique simple en suivant ces étapes. Lors de son exécution, un tableau croisé dynamique basé sur les données sources est ajouté à la feuille de calcul :
![todo:image_alt_text](create-pivot-table_1.png)

```java
import com.aspose.cells.*;

// Créer un nouveau classeur et obtenir la première feuille de calcul
Workbook workbook = new Workbook();
Worksheet sheet = workbook.getWorksheets().get(0);
Cells cells = sheet.getCells();

// Écrire les données source : les ventes par sport et par trimestre
cells.get("A1").putValue("Sport");
cells.get("B1").putValue("Quarter");
cells.get("C1").putValue("Sales");
cells.get("A2").putValue("Golf");
cells.get("B2").putValue("Qtr3");
cells.get("C2").putValue(1500);
cells.get("A3").putValue("Golf");
cells.get("B3").putValue("Qtr4");
cells.get("C3").putValue(2000);
cells.get("A4").putValue("Tennis");
cells.get("B4").putValue("Qtr3");
cells.get("C4").putValue(600);
cells.get("A5").putValue("Tennis");
cells.get("B5").putValue("Qtr4");
cells.get("C5").putValue(1500);
cells.get("A6").putValue("Tennis");
cells.get("B6").putValue("Qtr3");
cells.get("C6").putValue(4070);
cells.get("A7").putValue("Tennis");
cells.get("B7").putValue("Qtr4");
cells.get("C7").putValue(5000);
cells.get("A8").putValue("Golf");
cells.get("B8").putValue("Qtr3");
cells.get("C8").putValue(6430);

// Ajouter un tableau croisé dynamique dans la cellule de destination E3, à partir de A1:C8
PivotTable pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
pivotTable.addFieldToArea(PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(PivotFieldType.DATA, "Sales");

// Enregistrer le classeur
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Lorsqu’une plage de cellules est définie comme source de données, elle doit être spécifiée de la cellule en haut à gauche à la cellule en bas à droite. Par exemple, « A1:C3 » est valide ; « C3:A1 » ne l’est pas.
{{% /alert %}}

{{< app/cells/assistant language="java" >}}