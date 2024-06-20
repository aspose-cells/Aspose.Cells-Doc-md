---
title: Mise en page
type: docs
weight: 80
url: /fr/reportingservices/page-setup/
---

La configuration comprend deux sections et 8 types de propriétés de mise en page. Ces propriétés incluent le nom, l'index, FitToPagesTall, FitToPagesWide, TopMargin, FooterMargin, HeaderMargin, BottomMargin, LeftMargin et RightMargin.

- **nom** représente le nom du rapport, il représente l'ensemble du rapport lorsque le nom est vide.
- **index** représente l'index de la feuille de calcul du fichier Excel exporté.
- **FitToPagesTall** représente le nombre de pages en hauteur que la feuille de calcul sera mise à l'échelle lors de l'impression.
- **FitToPagesWide** représente le nombre de pages en largeur que la feuille de calcul sera mise à l'échelle lors de l'impression.
- **FooterMargin** représente la distance entre le bas de la page et le pied de page, en unité de centimètres.
- **HeaderMargin** représente la distance entre le haut de la page et l'en-tête, en unité de centimètres.
- **LeftMargin** représente la taille de la marge gauche, en unité de centimètres.
- **RightMargin** représente la taille de la marge droite, en unité de centimètres.
- **TopMargin** représente la taille de la marge supérieure, en unité de centimètres.
- **BottomMargin** représente la taille de la marge inférieure, en unité de centimètres.

Exemple de configuration de mise en page :

{{code  lang="xml" }}
<PageSetup>
<Report name=”report name” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”>
<Sheet index=”0” FitToPagesTall=”1” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
<Sheet index=”1” FitToPagesTall=”0” FitToPagesWide =”1” TopMargin =”1.0” FooterMargin =” 1.0” HeaderMargin =” 1.0” BottomMargin =” 1.0” LeftMargin =” 1.0” RightMargin =” 1.0”/>
</Report>
</PageSetup>

{{code}}
