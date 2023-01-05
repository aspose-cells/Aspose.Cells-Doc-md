---
title: Problème de tableau croisé dynamique
type: docs
weight: 50
url: /fr/net/pivot-table-issue/
---
## **Symptôme**
"J'ai essayé d'ouvrir le fichier Excel généré à partir du bouton" Ouvrir "de l'IE. L'excel a été généré en lisant un modèle Excel. Pendant que je clique sur le bouton Ouvrir, il s'ouvre et en même temps, il apparaît un message d'erreur indiquant "Impossible d'ouvrir le fichier source du tableau croisé dynamique .....".

Mais lorsque j'enregistre le fichier Excel généré à l'aide du bouton "Enregistrer" et que je l'ouvre à partir du fichier à partir du chemin enregistré, il s'ouvre correctement sans aucune erreur. "
### **La solution**
Aspose.Cells définit le format de données pivot et force MS Excel à créer un rapport de tableau croisé dynamique et d'autres tâches de calcul en fonction de la source de données lorsque le classeur s'ouvre dans MS Excel. Il faut donc utiliser**SaveType.OpenInBrowser** plutôt que d'utiliser**SaveType.OpenInExcel**L'une des nombreuses raisons est que lorsque vous utilisez l'option OpenInExcel lors de l'enregistrement du fichier de sortie généré dans MS Excel lors de l'exécution à l'aide du bouton "Ouvrir" de la boîte de dialogue de téléchargement, MS Excel n'a pas pu analyser les données du classeur pour générer un rapport de tableau croisé dynamique. Ceci est causé par le problème de nom de fichier, c'est la routine d'IE car il ajoute quelque chose comme "[1]" pour en faire "fileName" + "[1]" + ".xls" au nom d'origine et donc rien à faire avec Aspose.Cells. (c'est-à-dire... il ajoute toujours "[1]" pour faire "fileName"+ "[1]"+ ".xls" et non comme fileName.xls). En bref, si un fichier contient un tableau croisé dynamique, il ne peut pas être ouvert à l'aide de l'option OpenInExcel SaveType et cela s'appliquera aux deux, c'est-à-dire si vous créez le fichier à partir de rien ou si vous utilisez un fichier modèle pour les données source afin de créer un rapport de tableau croisé dynamique. Ainsi, vous devez utiliser l'option OpenInBrowser SaveType si le fichier contient des données de tableau croisé dynamique pour créer un rapport de tableau croisé dynamique.

Vous devez modifier votre code et mettre à jour vers SaveType.OpenInBrowser si vous utilisez la méthode Workbook.Save()

Ou modifiez votre code pour utiliser "en ligne" si vous utilisez l'option "pièce jointe" dans votre code. c'est à dire



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
