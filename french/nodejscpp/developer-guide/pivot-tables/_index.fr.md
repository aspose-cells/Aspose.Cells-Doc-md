---
title: Insérer un tableau croisé dynamique
linktitle: Insérer un tableau croisé dynamique
description: Créez et formatez des tableaux croisés dynamiques avec Aspose.Cells for Node.js via C++.
keywords: Créer un tableau croisé dynamique, Insérer un tableau croisé dynamique, Formater un tableau croisé dynamique.
type: docs
weight: 160
url: /fr/nodejs-cpp/create-pivot-table/
ai_search_scope: cells_nodejscpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Qu’est-ce qu’un tableau croisé dynamique ?**
Un tableau croisé dynamique est un rapport de synthèse interactif : il condense un grand volume de données brutes présentées ligne par ligne en une matrice compacte, sans la moindre formule. Vous décidez quelles colonnes deviennent des étiquettes de ligne, lesquelles deviennent des étiquettes de colonne et lesquelles sont agrégées comme valeurs — le tableau croisé dynamique effectue le regroupement et les calculs :
- **Résumer** — totaliser les ventes par produit, par région ou par trimestre, au lieu d’utiliser de longues chaînes de formules.
- **Comparer** — les catégories sur les lignes et les périodes sur les colonnes transforment une liste plate en rapport croisé dans lequel les tendances apparaissent d’un coup d’œil.
- **Analyser en détail** — un double-clic sur une valeur de synthèse permet d’examiner les lignes de données sources sous-jacentes.
- **Actualiser** — lorsque les données source changent, une seule actualisation recalcule l’ensemble du rapport.
Les scénarios typiques comprennent les tableaux de bord des ventes, la ventilation des dépenses et l’analyse des stocks — toute question du type « comment ces chiffres se répartissent-ils par catégorie et par période ? ». Aspose.Cells for Node.js via C++ crée les mêmes tableaux croisés dynamiques par programme, de sorte que les classeurs générés par votre application peuvent contenir des rapports prêts à l’emploi plutôt que seulement des données brutes.

### **Modèle objet du tableau croisé dynamique**
Aspose.Cells for Node.js via C++ fournit un ensemble de classes spécifiques utilisées pour créer et contrôler les tableaux croisés dynamiques. Ces classes permettent de créer et de configurer des objets [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable), qui constituent les éléments de base d’un tableau croisé dynamique. Les objets sont :
- [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) représente un champ dans un [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotFieldCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivotfieldcollection) représente la collection de tous les objets [**PivotField**](https://reference.aspose.com/cells/nodejs-cpp/pivotfield) contenus dans le [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
- [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) représente un objet PivotTable sur une feuille de calcul.
- [**PivotTableCollection**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) représente la collection de tous les objets [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) sur une feuille de calcul.

### **Créer un tableau croisé dynamique simple à l’aide d’Aspose.Cells**
La création d’un tableau croisé dynamique se fait en trois étapes : écrire les données source dans les cellules de la feuille de calcul, ajouter le tableau croisé dynamique à l’emplacement de destination, puis placer les champs du tableau croisé dynamique dans les zones de ligne, de colonne et de données.
1. Ajoutez des données à une feuille de calcul à l’aide de la méthode [**putValue**](https://reference.aspose.com/cells/nodejs-cpp/cell/#putValue-boolean-) de l’objet [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell). Ces données serviront de source de données pour le tableau croisé dynamique.
2. Ajoutez un tableau croisé dynamique à la feuille de calcul en appelant la méthode [**add**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection/#add-string-string-string-) de la collection [**PivotTables**](https://reference.aspose.com/cells/nodejs-cpp/pivottablecollection) : `add(sourceData, row, column)`. `sourceData` correspond à la plage de données source (par exemple, "A1:C8") ; `row` et `column` sont les coordonnées basées sur zéro de la cellule de destination située dans l’angle supérieur gauche du tableau croisé dynamique (la cellule E3 correspond à la ligne 2 et à la colonne 4). La méthode renvoie directement le nouvel objet [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable).
3. Placez les champs du tableau croisé dynamique à l’aide de la méthode `addFieldToArea` de l’objet [**PivotTable**](https://reference.aspose.com/cells/nodejs-cpp/pivottable) : affectez un nom de champ à la zone de ligne (`PivotFieldType.Row`), à la zone de colonne (`PivotFieldType.Column`) ou à la zone de données (`PivotFieldType.Data`).
4. Enregistrez le classeur — le tableau croisé dynamique est écrit dans le fichier enregistré.
Après l’exécution du code d’exemple, un tableau croisé dynamique est ajouté à la feuille de calcul.

```javascript
const AsposeCells = require("aspose.cells.node");

// Créer un nouveau classeur et obtenir la première feuille de calcul
let workbook = new AsposeCells.Workbook();
let sheet = workbook.getWorksheets().get(0);

// Écrire les données source : ventes par sport et trimestre
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

// Ajouter un tableau croisé dynamique à la cellule de destination E3, en utilisant A1:C8 comme source
let pivotTable = sheet.getPivotTables().add("A1:C8", 2, 4);

// Affecter les champs du tableau croisé dynamique : Sport aux lignes, Quarter aux colonnes, Sales aux données
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Row, "Sport");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Column, "Quarter");
pivotTable.addFieldToArea(AsposeCells.PivotFieldType.Data, "Sales");

// Enregistrer le classeur
workbook.save("pivotTable_test_out.xlsx");
```

{{% alert color="primary" %}}
Lors de l’attribution d’une plage de cellules à titre de source de données, la plage doit s’étendre de la cellule supérieure gauche à la cellule inférieure droite. Par exemple, "A1:C3" est valide, mais "C3:A1" ne l’est pas.
{{% /alert %}}

{{< app/cells/assistant language="nodejs-cpp" >}}