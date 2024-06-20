---
title: Comportement de copier coller des propriétés EnableClipboardCopyPaste et PasteType de GridDesktop
type: docs
weight: 80
url: /fr/net/aspose-cells-griddesktop/copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties/
keywords: copier, coller, GridPasteType
description: Cet article décrit comment utiliser GridPasteType pour effectuer une opération de copier coller dans GridDesktop.
---

## **Scénarios d'utilisation possibles**
GridDesktop fournit différents types d'options de copier-coller avec la propriété Aspose.Cells.GridDesktop.GridDesktop.PasteType. Ces options sont spécifiées avec l'énumération Aspose.Cells.GridDesktop.Data.GridPasteType. En voici quelques-unes

- GridPasteType.All

Il copie et colle tout, des cellules source aux cellules cibles.

- GridPasteType.Formulas

Il copie et colle des formules des cellules source aux cellules cibles.

- GridPasteType.Comments

Il copie et colle des commentaires des cellules source aux cellules cibles.

- GridPasteType.RowHeights

Il copie et colle les hauteurs de lignes des cellules source aux cellules cibles.

- GridPasteType.ColumnWidths

Il copie et colle les largeurs de colonnes des cellules source aux cellules cibles.

etc.
## **Définissez la propriété EnableClipboardCopyPaste sur True pour activer la propriété PasteType.**
La propriété Aspose.Cells.GridDesktop.PasteType ne fonctionne que si vous définissez la propriété Aspose.Cells.GridDesktop.EnableClipboardCopyPaste sur true, comme indiqué dans cette capture d'écran.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_1.png)
## **Comportement des propriétés EnableClipboardCopyPaste et PasteType**
Étant donné que EnableClipboardCopyPaste est false et PasteType est All, la capture d'écran suivante montre que lorsque la cellule B3 est copiée et collée dans la cellule C5.

![todo:image_alt_text](copy-paste-behavior-of-enableclipboardcopypaste-and-pastetype-griddesktop-properties_3.png)

Étant donné que EnableClipboardCopyPaste est true et PasteType est All, après avoir copié une image depuis Windows. la capture d'écran suivante montre que lorsque la cellule B3 est copiée et collée dans la cellule C5, elle copie également l'image dans la cellule C5.

![à faire: copier l'image](copyimage.png)

![à faire: après copie faire coller](aftercopy.png)


