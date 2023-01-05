---
title: Mise en page
type: docs
weight: 80
url: /fr/reportingservices/page-setup/
---
La configuration comprend deux sections et 8 types de propriétés de mise en page. Ces propriétés incluent le nom, l'index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin et RightMargin.

- **Nom** représente le nom du rapport, il représente le rapport entier lorsque le nom est vide.
- **indice** représente l'index de feuille de calcul du fichier Excel exporté.
- **FitToPagesTall** représente le nombre de pages de hauteur sur lesquelles la feuille de calcul sera mise à l'échelle lors de son impression.
- **FitToPagesWide** représente le nombre de pages de largeur sur lesquelles la feuille de calcul sera mise à l'échelle lors de son impression.
- **Marge de pied de page** représente la distance entre le bas de la page et le pied de page, en centimètres.
- **Marge d'en-tête** représente la distance entre le haut de la page et l'en-tête, en centimètres.
- **Marge de gauche** représente la taille de la marge de gauche, en centimètres.
- **Marge droite** représente la taille de la marge droite, en centimètres.
- **Marge supérieure** représente la taille de la marge supérieure, en centimètres.
- **Marge inférieure**représente la taille de la marge inférieure, en centimètres.

Exemple de configuration PageSetup :

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
