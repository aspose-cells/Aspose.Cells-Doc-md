---
title: Insérer un tableau croisé dynamique
linktitle: Insérer un tableau croisé dynamique
description: Créez et formatez des tableaux croisés dynamiques dans des fichiers de tableur Excel à l’aide d’Aspose.Cells for Node.js via Java.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Formater un tableau croisé dynamique, Aspose.Cells for Node.js via Java.
type: docs
weight: 160
url: /fr/nodejs-java/create-pivot-table/
ai_search_scope: cells_nodejsjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un grand bloc de données brutes organisées ligne par ligne dans une matrice compacte, sans aucune formule. Vous choisissez les colonnes qui deviennent des étiquettes de ligne, celles qui deviennent des étiquettes de colonne et celles qui sont agrégées comme valeurs ; le tableau croisé dynamique assure le regroupement et les calculs :
- **Résumer** — totaliser les ventes par produit, par région ou par trimestre, au lieu d’utiliser de longues chaînes de formules.
- **Comparer** — les catégories placées sur les lignes et les périodes placées sur les colonnes transforment une liste plate en rapport croisé où les tendances sont visibles en un coup d’œil.
- **Explorer les détails** — un double-clic sur n’importe quelle valeur de synthèse permet d’examiner les lignes de données source à l’origine de cette valeur.
- **Actualiser** — lorsque les données source changent, une seule actualisation recalcule l’ensemble du rapport.
Les scénarios typiques sont les tableaux de bord des ventes, les répartitions des dépenses et l’analyse des stocks — toute question du type « comment ces chiffres se répartissent-ils par catégorie et par période ? » Aspose.Cells for Node.js via Java construit les mêmes tableaux croisés dynamiques par programme, afin que les classeurs générés par votre application puissent contenir des rapports prêts à l’emploi plutôt que uniquement des données brutes.

### **Modèle d’objet du tableau croisé dynamique**
Aspose.Cells fournit un ensemble de classes permettant de créer et de contrôler les tableaux croisés dynamiques. Les éléments de base sont :
- `PivotField` représente un champ dans un `PivotTable`.
- `PivotFieldCollection` représente une collection de tous les objets `PivotField` du `PivotTable`.
- `PivotTable` représente un tableau croisé dynamique sur une feuille de calcul.
- `PivotTableCollection` représente une collection de tous les objets `PivotTable` d’une feuille de calcul.

### **Création d’un tableau croisé dynamique simple avec Aspose.Cells**
La création d’un tableau croisé dynamique comprend les étapes suivantes : écrire les données source dans les cellules de la feuille de calcul, ajouter le tableau croisé dynamique à une position de destination, puis placer les champs du tableau croisé dynamique dans les zones de ligne, de colonne et de données.
1. Ajoutez des données à une feuille de calcul à l’aide de la méthode `putValue` de la cellule. Ces données fourniront la source de données du tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode `add` de la collection `PivotTables` : `add(sourceData, row, column)`. `sourceData` est la plage source (par exemple, "A1:C8") ; `row` et `column` sont les coordonnées indexées à partir de 0 de la cellule de destination, dans l’angle supérieur gauche du tableau croisé dynamique (la cellule E3 correspond à la ligne 2 et à la colonne 4). La méthode renvoie directement le nouvel objet `PivotTable`.
3. Placez les champs du tableau croisé dynamique à l’aide de la méthode `addFieldToArea` de l’objet `PivotTable` : le nom d’un champ est placé dans la zone de ligne (`PivotFieldType.ROW`), dans la zone de colonne (`PivotFieldType.COLUMN`) ou dans la zone de données (`PivotFieldType.DATA`).
4. Enregistrez le classeur : le tableau croisé dynamique est alors écrit dans le fichier.
Après l’exécution du code de l’exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

```javascript
const AsposeCells = require("aspose.cells");

// Créer un nouveau classeur et obtenir la première feuille de calcul
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Écrire les données source : ventes par sport et par trimestre
sheet.getCells().get("A1").putValue("Sport");
sheet.getCells().get("B1").putValue("Quarter");
sheet.getCells().get("C1").putValue("Sales");
sheet.getCells().get("A2").putValue("Golf");
sheet.getCells().get("B2").putValue("Qtr3");
sheet.getCells().get("C2").putValue(1500);
sheet.getCells().get("A3").putValue("Golf");
sheet.getCells().get("B3").putValue("Qtr4");
sheet.getCells().get("C3").putValue(2000);
sheet.getCells().get("A4").putValue("Tennis");
sheet.getCells().get("B4").putValue("Qtr3");
sheet.getCells().get("C4").putValue(600);
sheet.getCells().get("A5").putValue("Tennis");
sheet.getCells().get("B5").putValue("Qtr4");
sheet.getCells().get("C5").putValue(1500);
sheet.getCells().get("A6").putValue("Tennis");
sheet.getCells().get("B6").putValue("Qtr3");
sheet.getCells().get("C6").putValue(4070);
sheet.getCells().get("A7").putValue("Tennis");
sheet.getCells().get("B7").putValue("Qtr4");
sheet.getCells().get("C7").putValue(5000);
sheet.getCells().get("A8").putValue("Golf");
sheet.getCells().get("B8").putValue("Qtr3");
sheet.getCells().get("C8").putValue(6430);

// Ajouter un tableau croisé dynamique à la cellule de destination E3, à partir de A1:C8
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.ROW, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.COLUMN, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.DATA, "Sales");

// Enregistrer le classeur
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Lorsqu’une plage de cellules est utilisée comme source de données, elle doit s’étendre de la cellule supérieure gauche à la cellule inférieure droite. Par exemple, "A1:C3" est valide, mais "C3:A1" ne l’est pas.
{{% /alert %}}

## Articles connexes
- [Ajouter des champs de filtre à un tableau croisé dynamique avec Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/add-page-field-in-pivot-table/)
- [Appliquer des styles aux tableaux croisés dynamiques avec Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/apply-style-to-pivot-table/)
- [Modifier la disposition des champs de page dans un tableau croisé dynamique](/cells/fr/nodejs-java/change-page-field-layout/)
- [Filtrer les tableaux croisés dynamiques par libellé ou par valeur](/cells/fr/nodejs-java/filter-by-label-or-value-of-pivot-table/)
- [Gérer les champs de valeur des tableaux croisés dynamiques avec Aspose.Cells for Node.js via Java](/cells/fr/nodejs-java/manage-value-fields/)

{{< app/cells/assistant language="nodejs-java" >}}