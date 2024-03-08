---
title: Comportement de copier-coller des propriétés EnableClipboardCopyPaste et PasteType GridDesktop
type: docs
weight: 80
url: /fr/net/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
---
##  **Scénarios d'utilisation possibles**
GridDesktop propose différents types d’options de type copier-coller avec la propriété Aspose.Cells.GridDesktop.GridDesktop.PasteType. Ces options sont spécifiées avec l’énumération Aspose.Cells.GridDesktop.Data.GridPasteType. Certains d'entre eux sont les suivants

- GridPasteType.Tout

Il copie et colle tout, des cellules sources aux cellules cibles.

- GridPasteType.Formulas

Il copie et colle les formules des cellules source vers les cellules cibles.

- GridPasteType.Comments

Il copie et colle les commentaires des cellules source vers les cellules cibles.

- GridPasteType.RowHeights

Il copie et colle les hauteurs des lignes des cellules source vers les cellules cibles.

- GridPasteType.ColumnWidths

Il copie et colle les largeurs de colonnes des cellules source vers les cellules cibles.

etc.
##  **Définissez la propriété EnableClipboardCopyPaste sur True pour activer la propriété PasteType**
La propriété Aspose.Cells.GridDesktop.GridDesktop.PasteType ne fonctionne que si vous définissez la propriété Aspose.Cells.GridDesktop.GridDesktop.EnableClipboardCopyPaste sur true, comme indiqué dans cette capture d'écran.

![tâche : image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
##  **Comportement des propriétés EnableClipboardCopyPaste et PasteType**
Étant donné que EnableClipboardCopyPaste est false et PasteType est All, la capture d'écran suivante montre que lorsque la cellule B3 est copiée et collée dans la cellule C5.

![tâche : image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Étant donné que EnableClipboardCopyPaste est vrai et que PasteType est All, après avoir copié une image à partir de Windows. la capture d'écran suivante montre que lorsque la cellule B3 est copiée et collée dans la cellule C5, elle copie également l'image dans la cellule C5.

![todo:faire une copie de l'image](copyimage.png)

![todo: après copier, coller](aftercopy.png)


