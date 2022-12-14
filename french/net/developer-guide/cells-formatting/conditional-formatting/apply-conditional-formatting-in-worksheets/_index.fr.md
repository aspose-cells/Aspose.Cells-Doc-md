---
title: Appliquer la mise en forme conditionnelle dans les feuilles de calcul
type: docs
weight: 130
url: /fr/net/apply-conditional-formatting-in-worksheets/
---
{{% alert color="primary" %}}

Cet article est conçu pour fournir une compréhension détaillée de la façon d'ajouter une mise en forme conditionnelle à une plage de cellules dans une feuille de calcul.

La mise en forme conditionnelle est une fonctionnalité avancée d'Excel Microsoft qui vous permet d'appliquer des formats à une plage de cellules et de modifier cette mise en forme en fonction de la valeur de la cellule ou de la valeur d'une formule. Par exemple, l'arrière-plan d'une cellule peut être rouge pour mettre en évidence une valeur négative, ou la couleur du texte peut être verte pour une valeur positive. Lorsque la valeur de la cellule répond à la condition de format, le format est appliqué. Si la valeur de la cellule ne répond pas à la condition de format, la mise en forme par défaut de la cellule est utilisée.

Il est possible d'appliquer une mise en forme conditionnelle avec Microsoft Office Automation mais cela a ses inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple, la sécurité, la stabilité, l'évolutivité et la vitesse. La raison principale pour trouver une autre solution est que Microsoft eux-mêmes déconseillent fortement la bureautique pour les solutions logicielles.

Cet article montre comment créer une application console, ajouter une mise en forme conditionnelle sur les cellules avec quelques lignes de code les plus simples en utilisant le Aspose.Cells API.

{{% /alert %}}

## **Utilisation de Aspose.Cells pour appliquer une mise en forme conditionnelle basée sur la valeur Cell**

1. **Téléchargez et installez Aspose.Cells**.
 1. Téléchargez Aspose.Cells for .NET.
1. Installez-le sur votre poste de développement.
Tous les composants Aspose, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.
1. **Créer un projet**.
 Démarrez Visual Studio.NET et créez une nouvelle application console. Cet exemple crée une application console C#, mais vous pouvez également utiliser VB.NET.
1. **Ajouter des références**.
 Ajoutez une référence à Aspose.Cells à votre projet, par exemple ajoutez une référence à ….\Program Files\Aspose.Cells\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll
1. *Appliquez une mise en forme conditionnelle en fonction de la valeur de la cellule.
 Vous trouverez ci-dessous le code utilisé pour accomplir la tâche. J'applique une mise en forme conditionnelle sur une cellule.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingCellValue-1.cs" >}}

Lorsque le code ci-dessus est exécuté, la mise en forme conditionnelle est appliquée à la cellule "A1" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée à A1 dépend de la valeur de la cellule. Si la valeur de cellule de A1 est comprise entre 50 et 100, la couleur d'arrière-plan est rouge en raison de la mise en forme conditionnelle appliquée.

## **Utilisation de Aspose.Cells pour appliquer une mise en forme conditionnelle basée sur une formule**

1. Application de la mise en forme conditionnelle en fonction de la formule (extrait de code)
 Vous trouverez ci-dessous le code pour accomplir la tâche. Il applique une mise en forme conditionnelle sur B3.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ApplyConditionalFormatting-ApplyConditionalFormattingFormula-1.cs" >}}

Lorsque le code ci-dessus est exécuté, la mise en forme conditionnelle est appliquée à la cellule "B3" dans la première feuille de calcul du fichier de sortie (output.xls). La mise en forme conditionnelle appliquée dépend de la formule qui calcule la valeur de "B3" comme somme de B1 et B2.
