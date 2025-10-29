---  
title: Supprimer les styles inutilisés dans le classeur avec Golang via C++  
linktitle: Supprimer les styles inutilisés dans le classeur  
type: docs  
weight: 340  
url: /fr/go-cpp/remove-unused-styles-inside-the-workbook/  
description: Supprimer les styles inutilisés dans le classeur Excel en utilisant Aspose.Cells avec Golang via C++.  
---  

{{% alert color="primary" %}}  

Les styles inutilisés dans les fichiers Excel prennent non seulement de la place mais causent également des problèmes de performance lors de la conversion en différents formats comme PDF, HTML, etc. Aspose.Cells fournit la [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/) pour supprimer tous les styles inutilisés à l'intérieur du classeur.  

{{% /alert %}}  

Le code suivant explique l'utilisation de [**Workbook.RemoveUnusedStyles()**](https://reference.aspose.com/cells/go-cpp/workbook/removeunusedstyles/). Le code charge le [fichier Excel modèle](5115520.xlsx) que vous pouvez télécharger via le lien fourni. Il contient un style inutilisé nommé **AsposeStyle** ; ce style et tous les autres styles inutilisés seront supprimés après exécution du code.  

![todo:image_alt_text](remove-unused-styles-inside-the-workbook_1.png)  

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RemoveUnusedStylesInsideTheWorkbook.go" >}}
