---
title: Accès à la feuille de calcul
type: docs
weight: 10
url: /fr/net/aspose-cells-griddesktop/access-worksheet/
keywords: GridDesktop,feuille de calcul
description: Cet article présente comment travailler avec une feuille de calcul dans GridDesktop.
---

{{% alert color="primary" %}} 

Une feuille de calcul est une partie intégrante d'un fichier Excel. En fait, un fichier Excel est composé d'une ou plusieurs feuilles de calcul. Chaque feuille de calcul peut être composée de jusqu'à 65 536 lignes et 256 colonnes uniquement. C'est la feuille de calcul qui contient les données dans un fichier Excel.

Aspose.Cells.GridDesktop peut créer et manipuler des fichiers Excel existants et nouveaux, il existe bien sûr un moyen d'accéder aux feuilles de calcul en utilisant Aspose.Cells.GridDesktop. Ce sujet en discute.

{{% /alert %}} 
## **Utilisation de l'index de la feuille de calcul**
Les développeurs peuvent accéder à une instance de n'importe quelle feuille de calcul en utilisant l'index de feuille de calcul de la feuille de calcul souhaitée comme le montre l'exemple ci-dessous. Cette approche est bonne pour parcourir un certain nombre de feuilles de calcul dans un fichier Excel.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithIndex.cs" >}}
## **Utilisation du nom de la feuille de calcul**
Si le nom de la feuille de calcul est connu, il est possible d'accéder à une feuille de calcul en utilisant son nom comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithName.cs" >}}
## **Accès à une feuille de calcul active**
Il est possible qu'un fichier Excel contienne plus d'une feuille de calcul. Celle sur laquelle un utilisateur travaille est appelée feuille de calcul active. Il est possible d'y accéder.

Pour accéder à une feuille de calcul active, Aspose.Cells.GridDesktop propose deux approches :
### **Utilisation de la propriété AcriveSheetIndex**
Une façon d'accéder à une feuille de calcul active en utilisant le contrôle Aspose.Cells.GridDesktop est d'utiliser la propriété ActiveSheetIndex du contrôle GridDesktop. En utilisant cette propriété, il est possible d'obtenir l'index de la feuille de calcul active dans le contrôle Aspose.Cells.GridDesktop. Cet index peut ensuite être utilisé pour accéder à la feuille de calcul de manière traditionnelle comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithActiveWorksheet.cs" >}}
### **Utilisation de la méthode GetActiveWorksheet**
L'autre approche consiste à appeler la méthode GetActiveWorksheet du contrôle GridDesktop. Cette méthode fournit une référence à la feuille de calcul qui est actuellement active dans le contrôle Aspose.Cells.GridDesktop comme indiqué ci-dessous.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-WorkingWithWorksheet-AccessingWorksheets-AccessingWithGetActiveWorksheet.cs" >}}
