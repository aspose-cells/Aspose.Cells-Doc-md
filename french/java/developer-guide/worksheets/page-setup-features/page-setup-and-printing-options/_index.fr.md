---
title: Configuration de la mise en page et des options d impression
type: docs
weight: 10
url: /fr/java/page-setup-and-printing-options/
---

{{% alert color="primary" %}}

Parfois, les développeurs doivent configurer la mise en page et les paramètres d'impression pour contrôler le processus d'impression. Les paramètres de mise en page et d'impression offrent diverses options et sont entièrement pris en charge dans Aspose.Cells.

Cet article montre comment créer une application console et appliquer la mise en page et les options d'impression à une feuille de calcul avec quelques lignes de code simples en utilisant l'API Aspose.Cells.

{{% /alert %}}

## **Travailler avec la mise en page et les paramètres d'impression**

Pour cet exemple, nous avons créé un classeur dans Microsoft Excel et utilisons Aspose.Cells pour définir la mise en page et les options d'impression.

### **Définir les options de mise en page**

Créez d'abord une feuille de calcul simple dans Microsoft Excel. Ensuite, appliquez des options de mise en page. L'exécution du code modifie les options de mise en page comme dans la capture d'écran ci-dessous.

**Fichier de sortie** 

![todo:image_alt_text](page-setup-and-printing-options_1.png)

1. Créez une feuille de calcul avec des données dans Microsoft Excel:
   1. Ouvrir un nouveau classeur dans Microsoft Excel.
   1. Ajoutez des données.
      Ci-dessous se trouve une capture d'écran du fichier.

      **Fichier d'entrée**

![todo:image_alt_text](page-setup-and-printing-options_2.png)

1. Définir les options de mise en page :
   Appliquer les options de mise en page au fichier. Ci-dessous se trouve une capture d'écran des options par défaut, avant l'application des nouvelles options.

   **Options de mise en page par défaut**

![todo:image_alt_text](page-setup-and-printing-options_3.png)

1. Téléchargez et installez Aspose.Cells :
   1. [Téléchargez](https://downloads.aspose.com/cells/java) Aspose.Cells for Java.
   1. Décompressez-le sur votre ordinateur de développement.
      Tous les composants [Aspose](http://www.aspose.com/), une fois installés, fonctionnent en mode d'évaluation. Le mode d'évaluation n'a pas de limite de temps et il ne fait qu'ajouter des filigranes aux documents produits.
1. Créez un projet.
   Créez un projet avec un éditeur Java, par exemple Eclipse, ou créez un programme simple à l'aide d'un éditeur de texte.
1. Ajoutez un chemin de classe.
   1. Extrayez le fichier Aspose.Cells.jar et dom4j_1.6.1.jar du fichier Aspose.Cells.zip.
   1. Définissez le chemin de classe du projet dans Eclipse :
   1. Sélectionnez votre projet dans Eclipse, puis cliquez sur **Projet**, suivi de **Propriétés**.
   1. Sélectionnez **Chemin de construction Java** sur la gauche de la boîte de dialogue.
   1. Sélectionnez l'onglet Bibliothèques, cliquez sur **Ajouter des JAR** ou **Ajouter des JAR externes** pour sélectionner Aspose.Cells.jar et dom4j_1.6.1.jar et ajoutez-les aux chemins de construction.
      Ou vous pouvez le définir à l'exécution dans une invite de commandes DOS sous Windows :

{{< highlight java >}}

 javac \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName .javajava \-classpath %classpath%;e:\Aspose.Cells.jar; ClassName

{{< /highlight >}}

1. Écrivez l'application qui invoque des API :
   Ci-dessous se trouve le code utilisé par le composant dans cet exemple.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPageSetupOptions-SettingPageSetupOptions.java" >}}

### **Paramétrage des options d'impression**

Les paramètres de mise en page fournissent également plusieurs options d'impression (appelées également options de feuille) qui permettent aux utilisateurs de contrôler l'impression des pages de feuille de calcul. Ils permettent aux utilisateurs de :

- Sélectionner une zone d'impression spécifique d'une feuille de calcul.
- Imprimer les titres.
- Imprimer les quadrillages.
- Imprimer les en-têtes de lignes/colonnes.
- Obtenir une qualité brouillon.
- Imprimer des commentaires.
- Imprimer les erreurs de cellules.
- Définir l'ordre des pages.

L'exemple qui suit applique des options d'impression au fichier créé dans l'exemple ci-dessus (PageSetup.xls). La capture d'écran ci-dessous montre les options d'impression par défaut avant l'application de nouvelles options.
**Document d'entrée**

![todo:image_alt_text](page-setup-and-printing-options_4.png)

L'exécution du code modifie les options d'impression.
**Fichier de sortie**

![todo:image_alt_text](page-setup-and-printing-options_5.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingPrintoptions-SettingPrintoptions.java" >}}

## **Résumé**

{{% alert color="primary" %}}

Cet article montre comment définir la mise en page et les options d'impression de feuille à l'aide de Aspose.Cells. Espérons que cela vous donnera un aperçu et que vous pourrez utiliser ces options dans vos propres scénarios.

Aspose.Cells bénéficie de nombreuses années de recherche, de conception et d'optimisation minutieuse. Nous accueillons chaleureusement vos questions, commentaires et suggestions sur le [Forum Aspose.Cells](https://forum.aspose.com/c/cells/9). Nous garantissons une réponse rapide.

{{% /alert %}}
