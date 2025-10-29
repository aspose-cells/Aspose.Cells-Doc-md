---
title: Appliquer le formatage conditionnel dans les feuilles de calcul
description: Comment utiliser la bibliothèque Aspose.Cells pour Python via .NET pour appliquer une mise en forme conditionnelle dans les feuilles de calcul. En ajustant ces critères, vous avez plus de contrôle sur l apparence des cellules.
keywords: Aspose.Cells, Mise en forme conditionnelle, Python, Feuille de calcul, Mise en forme
type: docs
weight: 130
url: /fr/python-net/apply-conditional-formatting-in-worksheets/
---

{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de comment ajouter un formatage conditionnel à une plage de cellules dans une feuille de calcul.

Le formatage conditionnel est une fonctionnalité avancée de Microsoft Excel qui vous permet d'appliquer des formats à une plage de cellules et d'avoir ce formatage modifié en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte pourrait être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de formatage, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de formatage, le formatage par défaut de la cellule est utilisé.

Il est possible d'appliquer un formatage conditionnel avec l'automatisation Microsoft Office, mais cela présente des inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, la scalabilité et la vitesse. La principale raison de trouver une autre solution est que Microsoft recommande fortement de ne pas utiliser l'automatisation Office pour les solutions logicielles.

Cet article montre comment créer une application console, ajouter un formatage conditionnel sur des cellules avec quelques lignes de code les plus simples à l'aide de l'API Aspose.Cells.

{{% /alert %}}

## **Utilisation d'Aspose.Cells pour Appliquer un Formatage Conditionnel Basé sur la Valeur de la Cellule**

1. **Téléchargez et Installez Aspose.Cells**.
   1. Télécharger Aspose.Cells pour Python via .NET.
1. Installez-le sur votre ordinateur de développement.
   Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et n'injecte que des filigranes dans les documents produits.
1. **Créer un projet**.
   Démarrez Visual Studio.NET et créez une nouvelle application console. Cet exemple crée une application console Python, mais vous pouvez également utiliser VB.NET.
1. **Ajouter des références**.
   Ajouter une référence à Aspose.Cells dans votre projet.
1. *Appliquer une mise en forme conditionnelle en fonction de la valeur de la cellule.
   Voici le code utilisé pour accomplir la tâche. J'applique une mise en forme conditionnelle sur une cellule.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingCellValue-1.py" >}}

Lorsque le code ci-dessus est exécuté, une mise en forme conditionnelle est appliquée à la cellule "A1" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée à A1 dépend de la valeur de la cellule. Si la valeur de la cellule A1 est comprise entre 50 et 100, la couleur d'arrière-plan est rouge en raison de la mise en forme conditionnelle appliquée.

## **Utilisation d'Aspose.Cells pour appliquer une mise en forme conditionnelle en fonction de la formule**

1. Appliquer une mise en forme conditionnelle en fonction de la formule (Extrait de code)
   Voici le code pour accomplir la tâche. Il applique une mise en forme conditionnelle sur B3.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Cells-Formatting-ApplyConditionalFormattingFormula-1.py" >}}

Lorsque le code ci-dessus est exécuté, une mise en forme conditionnelle est appliquée à la cellule "B3" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée dépend de la formule qui calcule la valeur de "B3" comme la somme de B1 & B2.

{{< app/cells/assistant language="python-net" >}}
