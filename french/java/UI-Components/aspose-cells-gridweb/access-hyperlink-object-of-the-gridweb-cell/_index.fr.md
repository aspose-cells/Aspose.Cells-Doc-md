---
title: Accéder à l'objet Hyperlien du GridWeb Cell
type: docs
weight: 60
url: /fr/java/access-hyperlink-object-of-the-gridweb-cell/
---
##  **Scénarios d'utilisation possibles**
Vous pouvez vérifier si la cellule contient ou non un lien hypertexte en utilisant les deux méthodes suivantes. Ces méthodes renverront null si la cellule ne contient pas de lien hypertexte et si elle contient un lien hypertexte, elle renverra l'objet GridHyperlink.

- GridHyperlinkCollection.getHyperlink (cellule GridCell)
- GridHyperlinkCollection.getHyperlink (int ligne, int colonne)
##  **Ouvrir le lien hypertexte dans une fenêtre nouvelle ou existante**
 Si votre fichier Excel contient un lien hypertexte vers une URL telle que<http://wwww.aspose.com/> et vous le chargez dans GridWeb, les hyperliens seront rendus avec l'attribut cible défini sur _blank. Cela signifie que lorsque vous cliquez sur le lien hypertexte dans une cellule GridWeb, il s'ouvrira dans une nouvelle fenêtre au lieu de la fenêtre existante. De plus, si vous souhaitez ouvrir le lien hypertexte dans la fenêtre existante, veuillez définir GridHyperlink.Target sur _self.
##  **Accéder à l'objet Hyperlien du GridWeb Cell**
L’exemple de code suivant accède au lien hypertexte de la cellule A1. Si la cellule A1 contient un lien hypertexte, elle renverra l'objet GridHyperlink, sinon elle renverra null.
##  **Exemple de code**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "examples-cells-AccessHyperlinkobjectofGridWebCell-AccessHyperlinkobjectofGridWebCell.jsp" >}}
