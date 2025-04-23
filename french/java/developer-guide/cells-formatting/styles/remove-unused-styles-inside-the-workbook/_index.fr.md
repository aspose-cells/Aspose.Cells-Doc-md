---
title: Supprimer les styles inutilisés dans le classeur
type: docs
weight: 470
url: /fr/java/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}} 

Les styles inutilisés dans le fichier Excel prennent non seulement de l'espace mais aussi causent des problèmes de performance lors de la conversion vers différents formats comme PDF, HTML, etc. Aspose.Cells fournit la méthode [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--) pour supprimer tous les styles inutilisés dans le classeur.

{{% /alert %}} 
## **Supprimer les styles inutilisés dans le classeur**
Le code suivant explique l'utilisation de [Workbook.removeUnusedStyles()](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#removeUnusedStyles--). Le code charge le [fichier Excel modèle](5473451.xlsx) que vous pouvez télécharger via le lien fourni. Il contient un style inutilisé nommé **AsposeStyle**. Ce style et tous les autres styles inutilisés seront supprimés après l'exécution du code. Veuillez voir la capture d'écran suivante pour plus d'illustrations.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-RemoveUnusedStyles-RemoveUnusedStyles.java" >}}
{{< app/cells/assistant language="java" >}}
