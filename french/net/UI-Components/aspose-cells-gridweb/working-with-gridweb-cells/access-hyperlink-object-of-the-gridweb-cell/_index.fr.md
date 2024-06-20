---
title: Accéder à l objet Hyperlien de la cellule GridWeb
type: docs
weight: 100
url: /fr/net/aspose-cells-gridweb/access-hyperlink-object-of-the-gridweb-cell/
keywords: GridWeb, hyperlien
description: Cet article présente comment travailler avec les hyperliens dans GridWeb.
---

## **Scénarios d'utilisation possibles**
Vous pouvez vérifier si la cellule contient un lien hypertexte ou non en utilisant les deux méthodes suivantes. Ces méthodes renverront null si la cellule ne contient pas de lien hypertexte et si elle en contient un, elle renverra l'objet GridHyperlink.

- GridHyperlinkCollection.GetHyperlink(GridCell cell)
- GridHyperlinkCollection.GetHyperlink(int row,int column)
## **Ouvrir un lien hypertexte dans une fenêtre nouvelle ou existante**
If your excel file contains hyperlink which links to some URL like <http://wwww.aspose.com/> and you load it in GridWeb then the hyperlinks will be rendered with target attribute set to _blank. It means, when you will click the hyperlink in a GridWeb cell, it will open up in a new window instead of existing window. Please check the GridHyperlink.Target property in the following debug window. Besides, if you want to open the hyperlink in the existing window, then please set the GridHyperlink.Target to _self.

![todo:image_alt_text](access-hyperlink-object-of-the-gridweb-cell_1.png)
## **Accéder à l'objet de lien hypertexte de la cellule GridWeb**
Le code d'exemple suivant accède au lien hypertexte de la cellule A1. Si la cellule A1 contient un lien hypertexte, elle renverra l'objet GridHyperlink, sinon elle renverra null.
### **Code d'exemple**
{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-Cells-AccessCellHyperlink.aspx-AccessHyperlink.cs" >}}
