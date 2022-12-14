---
title: Copier et coller des lignes dans GridDesktop dans le contrôle et entre le contrôle et Excel
type: docs
weight: 70
url: /fr/net/copy-and-paste-rows-in-griddesktop-within-the-control-and-between-the-control-and-excel/
---
{{% alert color="primary" %}} 

Si vous souhaitez activer le copier-coller des lignes dans GridDesktop dans le contrôle ou entre le contrôle et Excel, veuillez définir la propriété GridDesktop.ClipboardCopyPaste sur true. Vous pouvez définir cette propriété au moment du design ou dans le code. La valeur par défaut de cette propriété est false. Actuellement, il ne peut copier et coller que des valeurs de cellule et ne copiera aucun autre paramètre de la cellule comme le format, le style de bordure, etc.

{{% /alert %}} 
## **Définition de la propriété GridDesktop.ClipboardCopyPaste en mode conception et au moment de l'exécution**
 L'exemple de code suivant définit la propriété GridDesktop.ClipboardCopyPaste dans**Durée**.



{{< gist "aspose-cells-gists" "e204d6243cc67d7d255d51c9b85b2c64" "Examples.GridDesktop-CSharp-GridDesktop.Examples-Articles-CopyAndPasteRows-1.cs" >}}
