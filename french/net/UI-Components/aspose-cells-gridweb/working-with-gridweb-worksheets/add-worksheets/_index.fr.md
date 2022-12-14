---
title: Ajouter des feuilles de calcul
type: docs
weight: 20
url: /fr/net/add-worksheets/
---
{{% alert color="primary" %}} 

Les feuilles de travail font partie intégrante de Aspose.Cells.GridWeb. Toutes les données sont gérées et stockées sous forme de feuilles de calcul. Aspose.Cells.GridWeb permet aux développeurs d'ajouter une ou plusieurs feuilles de calcul au contrôle Aspose.Cells.GridWeb. Cette rubrique présente des approches simples pour ajouter des feuilles de calcul à Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Ajout d'une feuille de calcul**
### **Sans spécifier le nom de la feuille**
Le moyen le plus simple d'ajouter une feuille de calcul à Aspose.Cells.GridWeb consiste à appeler la méthode Add de la collection GridWorksheetCollection dans le contrôle GridWeb. Cela crée des feuilles de calcul qui utilisent des noms par défaut (c'est-à-dire Feuil1, Feuil2, Feuil3, etc.) et les ajoute au contrôle GridWeb.

**Sortie : une feuille de calcul avec un nom par défaut a été ajoutée à GridWeb** 

![tâche : image_autre_texte](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

 La méthode Add renvoie l'index de la nouvelle feuille de calcul qui peut être utilisé pour accéder à l'instance de cette feuille de calcul. Pour plus de détails sur la façon d'accéder aux feuilles de calcul, lisez[Accéder aux feuilles de travail](/cells/fr/net/access-worksheets/).

{{% /alert %}} 
### **Avec le nom de feuille spécifié**
Pour ajouter une feuille de calcul avec un nom spécifique au contrôle GridWeb au lieu d'utiliser le schéma de dénomination par défaut, appelez une version surchargée de la méthode Add qui prend le SheetName spécifié. Pour une instance, l'exemple ci-dessous ajoute une feuille de calcul nommée Facture.

**Sortie : une feuille de calcul avec un nom spécifié a été ajoutée à GridWeb** 

![tâche : image_autre_texte](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

La méthode Add qui accepte le nom de la feuille de calcul en tant que chaîne renvoie une instance de GridWorksheet.

{{% /alert %}}
