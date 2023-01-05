---
title: Supprimer les styles inutilisés dans le classeur
type: docs
weight: 340
url: /fr/net/remove-unused-styles-inside-the-workbook/
---
{{% alert color="primary" %}}

Les styles inutilisés dans le fichier Excel prennent non seulement de l'espace, mais entraînent également des problèmes de performances lors de la conversion en différents formats tels que PDF, HTML, etc. Aspose.Cells fournit le[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) pour supprimer tous les styles inutilisés dans le classeur.

{{% /alert %}}

 Le code suivant explique l'utilisation de[**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/removeunusedstyles) . Le code charge le[modèle de fichier excel](5115520.xlsx) que vous pouvez télécharger à partir du lien fourni. Il contient un style inutilisé nommé**AsposeStyle**, ce style et tous les autres styles inutilisés seront supprimés après l'exécution du code.

![tâche : image_autre_texte](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RemoveUnusedStyles-1.cs" >}}
