---
title: Créez des tableaux croisés dynamiques et des graphiques croisés dynamiques avec Golang via C++
linktitle: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 20
url: /fr/go-cpp/create-pivot-tables-and-pivot-charts/
description: Apprenez comment créer des tableaux croisés dynamiques et des graphiques croisés dynamiques dans des fichiers Excel à l aide d Aspose.Cells avec Golang via C++.
---

{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de factures dans une liste dans une feuille de calcul. Un tableau croisé dynamique peut totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réorganiser rapidement les informations dans le tableau croisé dynamique en faisant glisser des boutons vers une nouvelle position.

Un graphique croisé dynamique est une représentation graphique interactive des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique rend encore plus facile la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

Aspose.Cells prend en charge [les tableaux croisés dynamiques](/cells/fr/cpp/create-pivot-tables-and-pivot-charts/) et [les graphiques croisés dynamiques](/cells/fr/cpp/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Ajout de tables pivot et de graphiques**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer des tables pivot. Ces classes sont utilisées pour créer et définir les objets PivotTable, qui agissent comme des blocs de construction de base d'un objet PivotTable :

- **ChampDePivot**, un champ dans un rapport de tableau croisé dynamique.
- **ChampsDePivot**, une collection de tous les objets ChampDePivot dans un tableau croisé dynamique.
- **TableauCroiseDynamique**, un rapport de tableau croisé dynamique sur une feuille de calcul.
- **TableauxCroisesDynamiques**, une collection de tous les objets TableauCroiseDynamique sur la feuille de calcul.

### **Préparation à l'utilisation d'Aspose.Cells**

1. Téléchargez et installez Aspose.Cells :
   1. [Télécharger Aspose.Cells](https://downloads.aspose.com/cells/go-cpp/).
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et ne fait que injecter des filigranes dans les documents produits. Pour utiliser pleinement le composant, vous devez disposer d'une licence valide.
1. Créer un projet :
   1. Démarrez votre environnement de développement C++ (par exemple, Visual Studio).
   1. Créez une nouvelle application console.
1. Ajouter des références:
   Ajoutez une référence au composant Aspose.Cells dans votre projet, par exemple, `...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll`.

### **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données dans les cellules d'une feuille de calcul en utilisant la méthode `PutValue` de l'objet `Cell`. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Les données seront utilisées comme source des données pour le tableau croisé dynamique.
1. Ajoutez un tableau croisé dynamique à la feuille en appelant la méthode `Add` de la collection `PivotTables` (encapsulée dans l'objet `Worksheet`).
1. Accédez au nouvel objet `PivotTable` dans la collection `PivotTables` en passant son index. Utilisez l'un des objets de tableau croisé dynamique encapsulés dans l'objet `PivotTable` pour gérer le tableau.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts.go" >}}
### **Ajout d'un graphique croisé dynamique**

Pour créer un graphique croisé dynamique en utilisant Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez le `PivotSource` du graphique pour référencer un tableau croisé dynamique existant dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatePivotTablesAndPivotCharts-1.go" >}}
