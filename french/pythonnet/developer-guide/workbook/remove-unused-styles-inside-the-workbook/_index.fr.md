---
title: Supprimer les styles inutilisés dans le classeur
type: docs
weight: 340
url: /fr/python-net/remove-unused-styles-inside-the-workbook/
---

{{% alert color="primary" %}}

Les styles inutilisés dans le fichier Excel non seulement occupent de l'espace mais causent également des problèmes de performance lors de la conversion dans différents formats comme PDF, HTML, etc. Aspose.Cells pour Python via .NET offre la méthode [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles) pour supprimer tous les styles inutilisés dans le classeur.

{{% /alert %}}

Le code suivant explique l'utilisation de [**Workbook.remove_unused_styles()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/remove_unused_styles). Le code charge le [fichier Excel modèle](5115520.xlsx) que vous pouvez télécharger à partir du lien fourni. Il contient un style inutilisé nommé **AsposeStyle**, ce style et tous les autres styles inutilisés seront supprimés après l'exécution du code.

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-RemoveUnusedStyles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
