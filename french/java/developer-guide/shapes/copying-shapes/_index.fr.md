---
title: Copier les formes entre les feuilles de calcul
type: docs
weight: 250
url: /fr/java/copy-shapes-between-worksheets/
---

{{% alert color="primary" %}}

Parfois, vous avez besoin de copier différentes images, graphiques et autres objets de dessin sur différentes feuilles de calcul selon vos besoins. Aspose.Cells prend en charge la copie de formes entre les feuilles de calcul. Les graphiques, images et autres objets sont copiés avec le plus grand degré de précision.

Vous pouvez essayer l'automatisation Office, mais cela comporte ses propres inconvénients. Il existe plusieurs raisons et problèmes : par exemple la sécurité, la stabilité, la scalabilité, la vitesse, le prix et les fonctionnalités. En bref, il y a de nombreuses raisons, la principale étant que Microsoft lui-même recommande fortement de ne pas utiliser l'automatisation Office à partir de solutions logicielles.

Dans cet article, nous créons une application console, effectuons la copie d'images, de graphiques et d'autres objets de dessin entre les feuilles de calcul d'un classeur avec quelques lignes de code simples en utilisant Aspose.Cells.

Ce document est conçu pour fournir aux développeurs une compréhension détaillée sur la façon de copier des formes (images, graphiques, contrôles et autres objets de dessin) entre les feuilles de calcul.

{{% /alert %}}

## **Copier des formes**

Cet article explique comment :

- [Copier une image d'une feuille de calcul à une autre](/cells/fr/java/copy-shapes-between-worksheets/#copier-une-image-dune-feuille-de-calcul-à-une-autre).
- [Copier un graphique d'une feuille de calcul à une autre](/cells/fr/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copier des contrôles et d'autres objets de dessin d'une feuille de calcul à une autre](/cells/fr/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copier une image d'une feuille de calcul à une autre**

#### **Étape 1 : Créer un classeur avec une image et un graphique dans Microsoft Excel**

1. Créer un nouveau classeur dans Microsoft Excel.
1. Ajouter une image sur la première feuille de calcul et un graphique sur la deuxième feuille de calcul.

   Les captures d'écran suivantes montrent les deux feuilles de calcul modèles créées dans Microsoft Excel.

   **Feuille de calcul “Graphique” avec un graphique**

![todo:image_alt_text](copy-shapes-between-worksheets_1.png)

**Feuille de calcul “Image” avec une image**

![todo:image_alt_text](copy-shapes-between-worksheets_2.png)

Maintenant, copiez l'image de la feuille de calcul nommée “Image” vers la dernière feuille de calcul “Résultat”.

#### **Étape 2 : Télécharger Aspose.Cells.Zip**

1. [Télécharger Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Décompressez-le sur votre ordinateur de développement.

   Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.

#### **Étape 3 : Créer un projet**

Vous pouvez soit créer un projet en utilisant un éditeur Java, par exemple, Eclipse, soit créer un programme simple en utilisant un Bloc-notes.

#### **Étape 4 : Ajouter le chemin de classe**

Pour définir un chemin de classe en utilisant Eclipse, veuillez suivre les étapes suivantes :

1. Extrayez le fichier Aspose.Cells.jar et dom4j_1.6.1.jar du fichier Aspose.Cells.zip.
1. Définissez le chemin de classe du projet dans Eclipse :
1. Sélectionnez votre projet dans Eclipse, puis cliquez sur les menus Projet-Propriétés.
1. Sélectionnez "Chemin de construction Java" dans le côté gauche de la fenêtre contextuelle, puis sélectionnez l'onglet "Bibliothèques", cliquez sur "Ajouter JARs" ou "Ajouter des JARs externes" pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et ajoutez-les dans les chemins de construction.
1. Écrivez une application pour appeler les API des composants d'Aspose.

Ou vous pouvez le définir à l'exécution à l'invite DOS dans Windows. Par exemple :

javac -classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava -classpath %classpath%;e:\Aspose.Cells.jar; ClassName

#### **Étape 5 : Copie d'une image d'une feuille de calcul à une autre**

Voici le code pour accomplir la tâche. Il copie une image de la feuille de calcul nommée « Image » à la feuille de calcul « Résultat ».

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Tâche 1 du résultat :**

Après l'exécution du code ci-dessus, l'image de la feuille de calcul « Image » est maintenant copiée sur la dernière feuille de calcul « Résultat »

**Feuille de calcul « Résultat » avec image copiée**

![todo:image_alt_text](copy-shapes-between-worksheets_3.png)

### **Tâche 2 : Copier un graphique d'une feuille de calcul à une autre**

#### **Étape 1 : Copier un graphique d'une feuille de calcul à une autre**

Voici le code réel utilisé par le composant pour accomplir la tâche.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Résultat de la tâche 2**

Après l'exécution du code ci-dessus, le graphique de la feuille de calcul « Graphique » est copié sur la feuille de calcul « Résultat ». Veuillez consulter la capture d'écran suivante de la feuille de calcul résultante.

**Feuille de calcul « Résultat » avec image et graphique copiés**

![todo:image_alt_text](copy-shapes-between-worksheets_4.png)

### **Tâche 3 : Copier les contrôles et autres objets de dessin d'une feuille de calcul à une autre**

**Feuille de calcul « Contrôle » avec zone de texte et ovale**

![todo:image_alt_text](copy-shapes-between-worksheets_5.png)

Veuillez suivre les étapes simples ci-dessous que vous devez effectuer pour obtenir les résultats souhaités.

#### **Étape 1 : Copier une feuille de calcul entre des classeurs**

Voici le code utilisé par le composant pour accomplir la tâche.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Résultat de la tâche 3**

Après l'exécution du code ci-dessus, les contrôles de la feuille de calcul « Contrôle » sont maintenant copiés sur la feuille de calcul « Résultat ». Veuillez consulter la capture d'écran suivante du « Résultat ».

**Feuille de calcul « Résultat » avec zone de texte et ovale copiés**

![todo:image_alt_text](copy-shapes-between-worksheets_6.png)

## **Conclusion**

Cet article a montré comment copier différentes formes telles que des images, des graphiques et d'autres objets de dessin en utilisant Aspose.Cells. Espérons que cela vous donnera un aperçu et que vous pourrez utiliser ces options selon vos différents scénarios.

Aspose.Cells peut offrir plus de flexibilité que d'autres solutions et fournit une rapidité, une efficacité et une fiabilité exceptionnelles pour répondre aux exigences spécifiques des applications commerciales. Les résultats montrent que Aspose.Cells a bénéficié de plusieurs années de recherche, de conception et d'ajustements minutieux.

Nous vous souhaitons chaleureusement la bienvenue pour vos questions, commentaires et suggestions dans le [forum Aspose.Cells](https://forum.aspose.com/c/cells/9).
