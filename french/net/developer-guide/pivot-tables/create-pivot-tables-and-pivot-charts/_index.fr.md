---
title: Créer des tableaux croisés dynamiques et des graphiques croisés dynamiques
type: docs
weight: 20
url: /fr/net/create-pivot-tables-and-pivot-charts/
---

{{% alert color="primary" %}}

Un tableau croisé dynamique est un résumé interactif des enregistrements. Par exemple, vous pouvez avoir des centaines d'entrées de facture dans une liste dans une feuille de calcul. Un tableau croisé dynamique peut totaliser les factures par client, produit ou date. Avec Microsoft Excel, il est possible de réarranger rapidement les informations dans le tableau croisé dynamique en faisant glisser les boutons vers une nouvelle position.

Un graphique croisé dynamique est une représentation graphique interactive des données dans un tableau croisé dynamique. Les graphiques croisés dynamiques ont été introduits dans Excel 2000. L'utilisation d'un graphique croisé dynamique rend encore plus facile la compréhension des données puisque le tableau croisé dynamique crée automatiquement des sous-totaux et des totaux.

Aspose.Cells prend en charge les [tableaux croisés dynamiques](/cells/fr/net/create-pivot-tables-and-pivot-charts/) et les [graphiques croisés dynamiques](/cells/fr/net/create-pivot-tables-and-pivot-charts/).

{{% /alert %}}

## **Ajout de tables pivot et de graphiques**

Aspose.Cells fournit un ensemble spécial de classes utilisées pour créer des tables pivot. Ces classes sont utilisées pour créer et définir les objets PivotTable, qui agissent comme des blocs de construction de base d'un objet PivotTable :

- PivotField, un champ dans un rapport de tableau croisé dynamique.
- PivotFields, une collection de tous les objets PivotField dans un tableau croisé dynamique.
- PivotTable, un rapport de tableau croisé dynamique sur une feuille de calcul.
- PivotTables, une collection de tous les objets PivotTable sur la feuille de calcul.

### **Préparation à l'utilisation d'Aspose.Cells**

1. Téléchargez et installez Aspose.Cells :
   1. [Téléchargez Aspose.Cells](https://downloads.aspose.com/cells/net).
   1. Installez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits. Pour travailler avec le composant à pleine capacité, vous devez disposer d'une licence valide.
1. Créer un projet :
   1. Démarrer Visual Studio.Net.
   1. Créez une nouvelle application console.
1. Ajouter des références:
   Ajoutez une référence au composant Aspose.Cells dans votre projet, par exemple ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **Ajouter un tableau croisé dynamique**

Pour créer un tableau croisé dynamique en utilisant Aspose.Cells:

1. Ajoutez des données à une feuille de calcul à l'aide de la méthode PutValue/setValue d'un objet Cell. Vous pouvez également utiliser un fichier modèle déjà rempli de données. Ces données seront utilisées comme source de données du tableau croisé dynamique.
1. Ajoutez une table pivotante à la feuille de calcul en appelant la méthode add de la collection PivotTables (encapsulée dans l'objet Feuille de calcul).
1. Accédez au nouvel objet PivotTable depuis la collection PivotTables en passant son index. # Utilisez l'un des objets table pivotante encapsulés dans l'objet PivotTable pour gérer la table.

Des exemples de code sont donnés ci-dessous.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotTable-1.cs" >}}

### **Ajout d'un graphique croisé dynamique**

Pour créer un graphique croisé dynamique en utilisant Aspose.Cells :

1. Ajoutez un graphique.
1. Définissez la PivotSource du graphique pour qu'elle fasse référence à une table pivotante existante dans la feuille de calcul.
1. Définissez d'autres attributs.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-CreatePivotTablesPivotCharts-CreatePivotChart-1.cs" >}}

{{< app/cells/assistant language="csharp" >}}
