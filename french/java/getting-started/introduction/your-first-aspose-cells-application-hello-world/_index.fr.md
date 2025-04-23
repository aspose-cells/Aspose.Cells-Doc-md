---
title: Votre première application Aspose.Cells  Hello World
type: docs
weight: 30
url: /fr/java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

Ce sujet pour débutants montre comment les développeurs peuvent créer une première application simple (Hello World) à l'aide de l'API simple d'Aspose.Cells. L'application crée un fichier Microsoft Excel avec les mots Hello World dans une cellule spécifiée d'une feuille de calcul.

{{% /alert %}}

### **Création de l'application Hello World**

Pour créer l'application Hello World à l'aide de l'API Aspose.Cells :

1. Créez une instance de la classe [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).
1. Appliquer la licence :
   1. Si vous avez acheté une licence, utilisez-la dans votre application pour accéder à toutes les fonctionnalités d'Aspose.Cells.
   1. Si vous utilisez la version d'évaluation du composant (si vous utilisez Aspose.Cells sans licence), ignorez cette étape.
1. Créez un nouveau fichier Microsoft Excel, ou ouvrez un fichier existant dans lequel vous souhaitez ajouter ou mettre à jour du texte.
1. Accédez à n'importe quelle cellule d'une feuille de calcul du fichier Microsoft Excel.
1. Insérez les mots **Bonjour le Monde !** dans une cellule accessible.
1. Générez le fichier Microsoft Excel modifié.

Les exemples ci-dessous démontrent les étapes ci-dessus.

#### **Création d'un classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, écrit les mots "Bonjour le Monde !" dans la cellule A1 sur la première feuille de calcul, et sauvegarde le fichier.

**La feuille de calcul générée** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **Ouverture d'un fichier existant**

L'exemple suivant ouvre un fichier modèle Microsoft Excel existant appelé **book1.xls**, écrit les mots "Bonjour le Monde !" dans la cellule A1 de la première feuille de calcul, et enregistre le classeur sous un nouveau nom de fichier.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
{{< app/cells/assistant language="java" >}}
