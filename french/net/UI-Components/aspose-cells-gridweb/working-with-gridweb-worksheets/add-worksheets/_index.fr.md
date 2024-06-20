---
title: Ajouter des feuilles de calcul
type: docs
weight: 20
url: /fr/net/aspose-cells-gridweb/add-worksheet/
keywords: GridWeb,add,worksheet,add GridWorksheet
description: Cet article présente comment ajouter une feuille de calcul (GridWorksheet) dans GridWeb.
---

{{% alert color="primary" %}} 

Les feuilles de calcul sont une partie intégrante de Aspose.Cells.GridWeb. Toutes les données sont gérées et stockées sous forme de feuilles de calcul. Aspose.Cells.GridWeb permet aux développeurs d'ajouter une ou plusieurs feuilles de calcul au contrôle Aspose.Cells.GridWeb. Ce sujet présente des approches simples pour ajouter des feuilles de calcul à Aspose.Cells.GridWeb.

{{% /alert %}} 
## **Ajout d'une feuille de calcul**
### **Sans spécifier le nom de la feuille**
La manière la plus simple d'ajouter une feuille de calcul à Aspose.Cells.GridWeb est d'appeler la méthode Add de la collection GridWorksheetCollection dans le contrôle GridWeb. Cela crée des feuilles de calcul qui utilisent des noms par défaut (c'est-à-dire Feuille1, Feuille2, Feuille3, et ainsi de suite) et les ajoute au contrôle GridWeb.

**Sortie : une feuille de calcul avec un nom par défaut a été ajoutée à GridWeb** 

![todo:image_alt_text](add-worksheets_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithoutName.cs" >}}

{{% alert color="primary" %}} 

La méthode Add retourne l'index de la nouvelle feuille de calcul qui peut être utilisé pour accéder à l'instance de cette feuille de calcul. Pour plus de détails sur la façon d'accéder aux feuilles de calcul, consultez [Accéder aux feuilles de calcul](/cells/fr/net/aspose-cells-gridweb/access-worksheets/).

{{% /alert %}} 
### **Avec un nom de feuille spécifié**
Pour ajouter une feuille de calcul avec un nom spécifique au contrôle GridWeb au lieu d'utiliser le schéma de nommage par défaut, appelez une version surchargée de la méthode Add qui prend le nom de feuille spécifié. Par exemple, l'exemple ci-dessous ajoute une feuille de calcul nommée Invoice.

**Sortie : une feuille de calcul avec un nom spécifié a été ajoutée à GridWeb** 

![todo:image_alt_text](add-worksheets_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Worksheets-AddWorksheets.aspx-AddWorksheetWithName.cs" >}}

{{% alert color="primary" %}} 

La méthode Add acceptant le nom de la feuille de calcul en tant que chaîne retourne une instance de GridWorksheet.

{{% /alert %}}
