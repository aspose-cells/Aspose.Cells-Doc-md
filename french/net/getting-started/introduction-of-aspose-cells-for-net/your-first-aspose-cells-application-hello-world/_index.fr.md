---
title: Votre première application Aspose.Cells  Hello World
type: docs
weight: 30
url: /fr/net/your-first-aspose-cells-application-hello-world/
description: Créez, modifiez et enregistrez votre premier fichier Excel dans n importe quel format pris en charge en utilisant Aspose.Cells for .NET pour découvrir sa simplicité et sa puissance en C#.
keywords: C# Bonjour le monde, Aspose.Cells for .NET Bonjour le monde, La première application utilisant Aspose.Cells for .NET, Le premier programme via Aspose.Cells for .NET.
---

{{% alert color="primary" %}}

Ce tutoriel montre comment créer une toute première application (Bonjour le monde) en utilisant l'API simple d'Aspose.Cells. Cette application simple crée un fichier Microsoft Excel avec le texte 'Bonjour le monde' dans une cellule de feuille de calcul spécifiée.

{{% /alert %}}

## **Comment créer l'application Bonjour le monde**

Les étapes ci-dessous créent l'application Bonjour le monde en utilisant l'API Aspose.Cells :

1. Créez une instance de la classe [Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook).
1. Si vous avez une licence, alors [appliquez-la](/cells/fr/net/licensing/).
   Si vous utilisez la version d'évaluation, ignorez les lignes de code relatives à la licence.
1. Créez un nouveau fichier Excel, ouvrez un fichier Excel existant.
1. Accédez à n'importe quelle cellule souhaitée d'une feuille de calcul dans le fichier Excel.
1. Insérez les mots **Bonjour le Monde !** dans une cellule accessible.
1. Générez le fichier Microsoft Excel modifié.

La mise en œuvre des étapes ci-dessus est démontrée dans les exemples ci-dessous.

### **Comment créer un nouveau classeur**

L'exemple suivant crée un nouveau classeur à partir de zéro, écrit Bonjour le monde! dans la cellule A1 de la première feuille de calcul et enregistre le fichier Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **Comment ouvrir un fichier existant**

L'exemple suivant ouvre un fichier modèle Microsoft Excel existant nommé "Sample.xlsx", saisit le texte "Bonjour le monde!" dans la cellule A1 de la première feuille de calcul et enregistre le classeur.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
