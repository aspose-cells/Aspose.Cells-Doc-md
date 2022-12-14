---
title: Copier des formes entre des feuilles de calcul
type: docs
weight: 250
url: /fr/java/copy-shapes-between-worksheets/
---
{{% alert color="primary" %}}

Parfois, vous devez copier différentes images, graphiques et autres objets de dessin dans différentes feuilles de calcul selon vos besoins. Aspose.Cells prend en charge la copie de formes entre les feuilles de calcul. Les graphiques, images et autres objets sont copiés avec le plus haut degré de précision.

Vous pouvez essayer Office Automation, mais cela a ses propres inconvénients. Il y a plusieurs raisons et problèmes impliqués : par exemple la sécurité, la stabilité, l'évolutivité, la vitesse, le prix et les fonctionnalités. En bref, il existe de nombreuses raisons, la principale étant que Microsoft lui-même déconseille fortement la bureautique à partir de solutions logicielles.

Dans cet article, nous créons une application console, effectuons la copie d'images, de graphiques et d'autres objets de dessin entre les feuilles de calcul d'un classeur avec quelques lignes de code simples à l'aide de Aspose.Cells.

Ce document est conçu pour fournir aux développeurs une compréhension détaillée sur la façon de copier des formes (images, graphiques, contrôles et autres objets de dessin) entre les feuilles de calcul.

{{% /alert %}}

## **Copier des formes**

Cet article explique comment :

- [Copier une image d'une feuille de calcul à une autre](/cells/fr/java/copy-shapes-between-worksheets/#copying-a-picture-from-one-worksheet-to-another).
- [Copier un graphique d'une feuille de calcul à une autre](/cells/fr/java/copy-shapes-between-worksheets/#task-2-copying-a-chart-from-one-worksheet-to-another).
- [Copier des contrôles et d'autres objets de dessin d'une feuille de calcul à une autre](/cells/fr/java/copy-shapes-between-worksheets/#task-3-copying-controls-and-other-drawing-objects-from-one-worksheet-to-another).

### **Copier une image d'une feuille de travail à une autre**

#### **Étape 1 : Création d'un classeur avec image et graphique dans Microsoft Excel**

1. Création d'un nouveau classeur dans Microsoft Excel.
1. Ajoutez une image sur la première feuille de calcul et un graphique sur la deuxième feuille de calcul.

 Les captures d'écran suivantes montrent les deux modèles de feuilles de calcul créés dans Microsoft Excel.

   **Feuille de calcul "Graphique" avec graphique**

![tâche : image_autre_texte](copy-shapes-between-worksheets_1.png)

**Feuille de travail "Image" avec image**

![tâche : image_autre_texte](copy-shapes-between-worksheets_2.png)

Maintenant, copiez l'image dans la feuille de calcul nommée "Image" dans la dernière feuille de calcul "Résultat".

#### **Étape 2 : Téléchargez Aspose.Cells.Zip**

1. [Télécharger Aspose.Cells for Java](https://downloads.aspose.com/cells/java).
1. Décompressez-le sur votre ordinateur de développement.

 Tout[Aspose](http://www.aspose.com/) les composants, une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il injecte uniquement des filigranes dans les documents produits.

#### **Étape 3 : créer un projet**

Vous pouvez soit créer un projet à l'aide d'un éditeur Java, par exemple Eclipse, soit créer un programme simple à l'aide d'un bloc-notes.

#### **Étape 4 : Ajouter un chemin de classe**

Pour définir un chemin de classe à l'aide d'Eclipse, veuillez suivre les étapes suivantes :

1. Extrayez les fichiers Aspose.Cells.jar et dom4j_1.6.1.jar de Aspose.Cells.zip.
1. Définissez le classpath du projet dans Eclipse :
1. Sélectionnez votre projet dans Eclipse puis cliquez sur les menus Projet-Propriétés.
1. Sélectionnez "Java Build Path" dans la partie gauche de la fenêtre contextuelle, puis sélectionnez l'onglet "Bibliothèques", cliquez sur "Ajouter des fichiers JAR" ou "Ajouter des fichiers JAR externes" pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et ajoutez-les dans la construction chemins.
1. Écrivez une application pour invoquer les API des composants de Aspose.

Ou vous pouvez le définir lors de l'exécution à l'invite DOS dans Windows. Par exemple :

javac -classpath %classpath%;e:\Aspose.Cells.jar; NomClasse .javajava -classpath %classpath%;e:\Aspose.Cells.jar; Nom du cours

#### **Étape 5 : copier une image d'une feuille de calcul à une autre**

Voici le code pour accomplir la tâche. Il copie une image de la feuille de calcul nommée "Image" dans la feuille de calcul "Résultat".

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyPicturefromOneWorksheetToAnother-CopyPicturefromOneWorksheetToAnother.java" >}}

#### **Résultat Tâche 1 :**

Après avoir exécuté le code ci-dessus, l'image de la feuille de calcul "Image" est maintenant copiée dans la dernière feuille de calcul "Résultat"

**Feuille de calcul "Résultat" avec image copiée**

![tâche : image_autre_texte](copy-shapes-between-worksheets_3.png)

### **Tâche 2 : copier un graphique d'une feuille de calcul à une autre**

#### **Étape 1 : copier un graphique d'une feuille de calcul à une autre**

Voici le code réel utilisé par le composant pour accomplir la tâche.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyChartFromOneWorksheetToAnother-CopyChartFromOneWorksheetToAnother.java" >}}

#### **Résultat Tâche 2**

Après avoir exécuté le code ci-dessus, le graphique de la feuille de calcul "Graphique" est copié dans la feuille de calcul "Résultat". Veuillez consulter l'instantané suivant de la feuille de calcul résultante.

**Feuille de calcul "Résultat" avec image et graphique copiés**

![tâche : image_autre_texte](copy-shapes-between-worksheets_4.png)

### **Tâche 3 : copier des contrôles et d'autres objets de dessin d'une feuille de calcul à une autre**

**Feuille de calcul "Contrôle" avec zone de texte et ovale**

![tâche : image_autre_texte](copy-shapes-between-worksheets_5.png)

Veuillez consulter les étapes simples suivantes que vous devez effectuer pour obtenir les résultats souhaités.

#### **Étape 1 : copier une feuille de calcul entre des classeurs**

Voici le code utilisé par le composant pour accomplir la tâche.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopyWorksheetBetweenWorkbooks-CopyWorksheetBetweenWorkbooks.java" >}}

#### **Résultat Tâche 3**

Après avoir exécuté le code ci-dessus, les contrôles de la feuille de calcul "Contrôle" sont maintenant copiés dans la feuille de calcul "Résultat". Veuillez consulter l'instantané suivant du "Résultat".

**Feuille de calcul "Résultat" avec zone de texte copiée et ovale**

![tâche : image_autre_texte](copy-shapes-between-worksheets_6.png)

## **Conclusion**

Cet article a montré comment copier différentes formes telles que des images, des graphiques et d'autres objets de dessin entre l'utilisation de Aspose.Cells. J'espère que cela vous donnera un aperçu et que vous pourrez utiliser ces options en fonction de vos différents scénarios.

Aspose.Cells peut offrir plus de flexibilité que les autres pour les solutions et offre une vitesse, une efficacité et une fiabilité exceptionnelles pour répondre aux exigences spécifiques des applications commerciales. Les résultats montrent que Aspose.Cells a bénéficié d'années de recherche, de conception et de réglage minutieux.

 Nous accueillons chaleureusement vos questions, commentaires et suggestions dans le[Aspose.CellsForum](https://forum.aspose.com/c/cells/9).
