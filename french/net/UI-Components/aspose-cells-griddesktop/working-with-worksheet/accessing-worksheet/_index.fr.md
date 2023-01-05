---
title: Accéder à la feuille de calcul
type: docs
weight: 10
url: /fr/net/accessing-worksheet/
---
{{% alert color="primary" %}} 

Une feuille de calcul fait partie intégrante d'un fichier Excel. En fait, un fichier Excel est composé d'une ou plusieurs feuilles de calcul. Chaque feuille de calcul peut être composée de jusqu'à 65 536 lignes et 256 colonnes uniquement. C'est la feuille de calcul qui contient les données dans un fichier Excel.

Aspose.Cells.GridDesktop peut créer et manipuler des fichiers Excel existants et nouveaux. Il existe donc bien sûr un moyen d'accéder aux feuilles de calcul à l'aide de Aspose.Cells.GridDesktop. Cette rubrique explique comment.

{{% /alert %}} 
## **Utilisation de l'index de feuille de calcul**
Les développeurs peuvent accéder à une instance de n'importe quelle feuille de calcul en utilisant l'index de feuille de calcul de n'importe quelle feuille de calcul souhaitée, comme indiqué ci-dessous dans l'exemple. Cette approche est idéale pour parcourir un certain nombre de feuilles de calcul dans un fichier Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Utilisation du nom de la feuille de calcul**
Si le nom de la feuille de travail est connu, il est possible d'accéder à une feuille de travail en utilisant son nom comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accéder à une feuille de calcul active**
Il est possible qu'un fichier Excel contienne plus d'une feuille de calcul. Celui sur lequel un utilisateur travaille s'appelle la feuille de calcul active. Il est possible d'accéder à la feuille active.

Pour accéder à une feuille de calcul active, Aspose.Cells.GridDesktop propose deux approches :
### **Utilisation de la propriété AcriveSheetIndex**
Une façon d'accéder à une feuille de calcul active à l'aide du contrôle Aspose.Cells.GridDesktop consiste à utiliser la propriété ActiveSheetIndex du contrôle GridDesktop. Grâce à cette propriété, il est possible d'obtenir l'index de la feuille de calcul active dans le contrôle Aspose.Cells.GridDesktop. Ensuite, cet index peut être utilisé pour accéder à la feuille de calcul de manière traditionnelle, comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Utilisation de la méthode GetActiveWorksheet**
L'autre approche consiste à appeler la méthode GetActiveWorksheet du contrôle GridDesktop. Cette méthode fournit une référence de la feuille de calcul actuellement active dans le contrôle Aspose.Cells.GridDesktop, comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
