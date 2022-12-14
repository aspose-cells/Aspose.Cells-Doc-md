---
title: Comportement de copier-coller de EnableClipboardCopyPaste et PasteType GridDesktop Properties
type: docs
weight: 80
url: /fr/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
## **Scénarios d'utilisation possibles**
GridDesktop fournit différents types d'options de type copier-coller avec la propriété Aspose.Cells.GridDesktop.GridDesktop.PasteType. Ces options sont spécifiées avec l'énumération Aspose.Cells.GridDesktop.Data.GridPasteType. Certains d'entre eux sont les suivants

- GridPasteType.All

Il copie et colle tout, des cellules source aux cellules cibles.

- GridPasteType.FormulasGridPasteType.Formulas

Il copie et colle les formules des cellules source vers les cellules cible.

- GridPasteType.Comments

Il copie et colle les commentaires des cellules source vers les cellules cible.

- GridPasteType.RowHeights

Il copie et colle les hauteurs des lignes des cellules source vers les cellules cible.

- GridPasteType.ColumnWidths

Il copie et colle les largeurs de colonne des cellules source vers les cellules cible.

etc.
## **Définissez la propriété EnableClipboardCopyPaste sur True pour activer la propriété PasteType**
La propriété Aspose.Cells.GridDesktop.GridDesktop.PasteType ne fonctionne que si vous définissez la propriété Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste sur true comme indiqué dans cette capture d'écran.

![tâche : image_autre_texte](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Comportement des propriétés EnableClipboardCopyPaste et PasteType**
Étant donné que EnableClipboardCopyPaste est false et PasteType est All, la capture d'écran suivante montre que lorsque la cellule B3 est copiée et collée dans la cellule C5, la mise en forme de la cellule n'est pas copiée et seul le contenu de la cellule B3 est copié.

![tâche : image_autre_texte](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_2.png)

Étant donné que EnableClipboardCopyPaste est true et PasteType est All, la capture d'écran suivante montre que lorsque la cellule B3 est copiée et collée dans la cellule C5, elle copie également la mise en forme de la cellule B3 dans la cellule C5.

![tâche : image_autre_texte](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)


