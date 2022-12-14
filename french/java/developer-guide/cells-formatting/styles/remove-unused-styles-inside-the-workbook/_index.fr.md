---
title: Supprimer les styles inutilisés dans le classeur
type: docs
weight: 470
url: /fr/java/remove-unused-styles-inside-the-workbook/
---
{{% alert color="primary" %}} 

 Les styles inutilisés dans le fichier Excel prennent non seulement de l'espace, mais entraînent également des problèmes de performances lors de la conversion en différents formats tels que PDF, HTML, etc. Aspose.Cells fournit le[Classeur.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\)) pour supprimer tous les styles inutilisés dans le classeur.

{{% /alert %}} 
## **Supprimer les styles inutilisés dans le classeur**
 Le code suivant explique l'utilisation de[Classeur.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles\(\) ). Le code charge le[modèle de fichier excel](5473451.xlsx) que vous pouvez télécharger à partir du lien fourni. Il contient un style inutilisé nommé**AsposeStyle**ce style et tous les autres styles inutilisés seront supprimés après l'exécution du code. Veuillez consulter la capture d'écran suivante pour plus d'illustrations.

![tâche : image_autre_texte](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
