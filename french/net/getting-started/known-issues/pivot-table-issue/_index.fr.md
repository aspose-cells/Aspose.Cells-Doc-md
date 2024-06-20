---
title: Problème de tableau croisé dynamique
type: docs
weight: 50
url: /fr/net/pivot-table-issue/
---

## **Symptôme**
"J'ai essayé d'ouvrir le fichier Excel généré à partir du bouton "Ouvrir" d'IE. L'Excel a été généré en lisant un modèle Excel. Lorsque je clique sur le bouton Ouvrir, il s'ouvre et en même temps, il affiche un message d'erreur disant "Impossible d'accéder au fichier source du tableau croisé dynamique.....".

Mais lorsque j'enregistre le fichier Excel généré en utilisant le bouton "Enregistrer" et que je l'ouvre à partir du chemin enregistré, il s'ouvre correctement sans aucune erreur."
### **Solution**
Aspose.Cells défini le format des données du tableau croisé dynamique et force MS Excel à créer un rapport de tableau croisé dynamique et d'autres tâches de calcul basées sur la source de données lorsque le classeur s'ouvre dans MS Excel. Ainsi, il convient d'utiliser **SaveType.OpenInBrowser** plutôt que d'utiliser **SaveType.OpenInExcel**. Une des nombreuses raisons est lorsque vous utilisez l'option OpenInExcel lors de l'enregistrement du fichier généré en sortie dans MS Excel en cours d'exécution en utilisant le bouton "Ouvrir" de la boîte de dialogue de téléchargement, MS Excel ne peut pas analyser les données du classeur pour générer un rapport de tableau croisé dynamique. Cela est causé par le problème du nom de fichier, c'est la routine d'IE car elle ajoute quelque chose comme "[1]" pour le transformer en "nomFichier" + "[1]"+ ".xls" pour le nom d'origine et donc rien à voir avec Aspose.Cells. (c'est-à-dire.... il ajoute toujours "[1]" pour faire "nomFichier"+ "[1]"+ ".xls" et non comme nomFichier.xls). En bref, si un fichier contient un tableau croisé dynamique, il ne peut pas être ouvert en utilisant l'option SaveType.OpenInExcel et cela s'appliquera aussi bien si vous créez le fichier à partir de zéro ou en utilisant un fichier de modèle pour les données source pour créer un rapport de tableau croisé dynamique. Par conséquent, vous devriez utiliser l'option SaveType.OpenInBrowser si le fichier contient des données de tableau croisé dynamique pour créer un rapport de tableau croisé dynamique.

Vous devriez modifier votre code et mettre à jour en utilisant SaveType.OpenInBrowser si vous utilisez la méthode Enregistrer() du classeur

Ou modifiez votre code pour utiliser "inline" si vous utilisez l'option "attachment" dans votre code. c'est-à-dire



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-PivotTableIssue.aspx-PivotTableIssue.cs" >}}
