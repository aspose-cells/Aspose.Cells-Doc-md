---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 20
url: /fr/nodejs-cpp/create-pivot-tables-and-pivot-charts/
description: Comment ajouter des tableaux croisés dynamiques et des graphiques croisés dynamiques avec Aspose.Cells for Node.js via C++.
keywords: Aspose.Cells for Node.js via C++ Excel, bibliothèque Excel Node.js, ajouter des tableaux croisés dynamiques et des graphiques croisés dynamiques en utilisant la bibliothèque Excel Aspose.Cells for Node.js via C++.
---

{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste dans une feuille de calcul. Un tableau croisé dynamique peut totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réarranger rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un graphique croisé dynamique est une représentation graphique interactive des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique rend encore plus facile la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

Aspose.Cells for Node.js via C++ supporte [tableaux croisés dynamiques](/cells/fr/nodejs-cpp/create-pivot-tables-and-pivot-charts/) et [graphismes croisés dynamiques](/cells/fr/nodejs-cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Ajouter des tableaux croisés dynamiques et des graphiques en utilisant Aspose.Cells for Node.js via C++**

Aspose.Cells for Node.js via C++ fournit un ensemble spécial de classes pour créer des tableaux croisés dynamiques. Ces classes servent à créer et définir des objets PivotTable, qui agissent comme les blocs de construction de base d'un tableau croisé dynamique :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- PivotTable, un rapport de tableau croisé dynamique sur une feuille de calcul.
- PivotTables, une collection de tous les objets PivotTable sur la feuille de calcul.

### **Préparer l'utilisation de Aspose.Cells for Node.js via C++**
1. Installer Aspose.Cells for Node.js via C++ depuis NPM, utiliser la commande : $ npm install aspose.cells.node.
1. Vous pouvez également suivre les instructions étape par étape pour installer “Aspose.Cells for Node.js via C++” dans votre environnement de développement.


### **Comment ajouter un tableau croisé dynamique en utilisant Aspose.Cells for Node.js via C++**

Pour créer un tableau croisé dynamique avec Aspose.Cells for Node.js via C++ :

1. Ajoutez des données à des cellules de feuille de calcul en utilisant la méthode put_value d'un objet Cell. Vous pouvez également utiliser un fichier de modèle déjà rempli de données. Les données seront utilisées comme source de données de la table pivotante.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable depuis la collection PivotTables en passant son index. # Utilisez l'un des objets table pivotante encapsulés dans l'objet PivotTable pour gérer la table.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotTable-1.js" >}}

### **Comment ajouter un graphique croisé dynamique en utilisant la bibliothèque Aspose.Cells for Node.js via C++**

Pour créer un PivotChart avec Aspose.Cells for Node.js via C++ :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "PivotTables-CreatePivotTablesPivotCharts-CreatePivotChart-1.js" >}}

