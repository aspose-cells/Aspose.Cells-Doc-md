---
title: Accéder à l'objet Lien hypertexte du GridWeb Cell
type: docs
weight: 100
url: /fr/net/access-hyperlink-object-of-the-gridweb-cell/
---
## **Scénarios d'utilisation possibles**
Vous pouvez vérifier si la cellule contient un lien hypertexte ou non en utilisant les deux méthodes suivantes. Ces méthodes renverront null si la cellule ne contient pas de lien hypertexte et si elle contient un lien hypertexte, elle renverra l'objet GridHyperlink.

- GridHyperlinkCollection.GetHyperlink (cellule GridCell)
- GridHyperlinkCollection.GetHyperlink (ligne int, colonne int)
## **Ouvrir un lien hypertexte dans une fenêtre nouvelle ou existante**
 Si votre fichier Excel contient un lien hypertexte qui renvoie à une URL telle que<http://wwww.aspose.com/> et que vous le chargez dans GridWeb, les hyperliens seront rendus avec l'attribut cible défini sur_ Vide. Cela signifie que lorsque vous cliquerez sur le lien hypertexte dans une cellule GridWeb, il s'ouvrira dans une nouvelle fenêtre au lieu de la fenêtre existante. Veuillez vérifier la propriété GridHyperlink.Target dans la fenêtre de débogage suivante. En outre, si vous souhaitez ouvrir le lien hypertexte dans la fenêtre existante, veuillez définir GridHyperlink.Target sur_soi.

![tâche : image_autre_texte](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Accéder à l'objet Lien hypertexte du GridWeb Cell**
L'exemple de code suivant accède au lien hypertexte de la cellule A1. Si la cellule A1 contient un lien hypertexte, elle renverra l'objet GridHyperlink, sinon, elle renverra null.
### **Exemple de code**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
