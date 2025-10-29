---
title: Appliquer le formatage conditionnel dans les feuilles de calcul
linktitle: Appliquer le formatage conditionnel dans les feuilles de calcul
description: Comment utiliser la bibliothèque Aspose.Cells dans Node.js via C++ pour appliquer la mise en forme conditionnelle dans les feuilles de calcul pour un meilleur contrôle de l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle, Node.js via C++, Feuille de calcul, Mise en forme
type: docs
weight: 130
url: /fr/nodejs-cpp/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de comment ajouter un formatage conditionnel à une plage de cellules dans une feuille de calcul.

Le formatage conditionnel est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une plage de cellules et d'avoir ce formatage modifié en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte pourrait être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de formatage, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de formatage, le formatage par défaut de la cellule est utilisé.

Il est possible d'appliquer un formatage conditionnel avec l'automatisation Microsoft Office, mais cela présente des inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse. La principale raison de trouver une autre solution est que Microsoft recommande fortement de ne pas utiliser l'automatisation Office pour les solutions logicielles.

Cet article montre comment créer une application console, ajouter un formatage conditionnel sur des cellules avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour Appliquer un Formatage Conditionnel Basé sur la Valeur de la Cellule**

1. **Téléchargez et Installez Aspose.Cells**.
   1. Téléchargez Aspose.Cells for Node.js via C++.
1. Installez-le sur votre ordinateur de développement.
   Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.
1. **Créer un projet**.
    Commencez votre projet Node.js en l'initialisant. Cet exemple crée une application console Node.js.
1. **Ajouter des références**.
    Ajoutez une référence à Aspose.Cells à votre projet, par exemple en requérant le package comme suit :
   ```javascript
   const AsposeCells = require("aspose.cells.node");
   ```
1. ** Appliquer une mise en forme conditionnelle en fonction de la valeur de la cellule **.
   Voici le code utilisé pour réaliser la tâche. Il applique un formatage conditionnel sur une cellule.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToCellValue.js" >}}


Lorsque le code ci-dessus est exécuté, le formatage conditionnel est appliqué à la cellule “A1” de la première feuille du fichier de sortie (output.xls). Le formatage conditionnel appliqué à A1 dépend de la valeur de la cellule. Si la valeur d’A1 est comprise entre 50 et 100, la couleur de fond est rouge en raison du formatage conditionnel appliqué.

## **Utilisation d'Aspose.Cells pour appliquer une mise en forme conditionnelle en fonction de la formule**

1. Appliquer une mise en forme conditionnelle en fonction de la formule (Extrait de code)
   Voici le code pour accomplir la tâche. Il applique une mise en forme conditionnelle sur B3.

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-ConditionalFormatting-ApplyToFormula.js" >}}

Lorsque le code ci-dessus est exécuté, le formatage conditionnel est appliqué à la cellule “B3” de la première feuille du fichier de sortie (output.xls). Le formatage dépend de la formule qui calcule la valeur de “B3” comme la somme de B1 et B2.
{{< app/cells/assistant language="nodejs-cpp" >}}
