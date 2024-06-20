---
title: Appliquer des styles à GridWeb
type: docs
weight: 20
url: /fr/net/aspose-cells-gridweb/apply-styles-to-gridweb/
keywords: GridWeb, style, styles
description: Cet article présente comment appliquer ou définir un style dans GridWeb.
---

{{% alert color="primary" %}} 

Aspose.Cells.GridWeb a son propre aspect par défaut, mais il est possible de changer son apparence. Aspose.Cells.GridWeb propose plusieurs propriétés permettant aux développeurs de contrôler pleinement son apparence. Ce sujet aborde certaines de ces propriétés.

{{% /alert %}} 
## **Appliquer des styles prédéfinis ou personnalisés à Aspose.Cells.GridWeb**
### **Styles prédéfinis**
Pour économiser les efforts des développeurs, Aspose.Cells.GridWeb offre certains styles prédéfinis. Il suffit de sélectionner un style dans la liste pour l'appliquer.

|**Styles**|**Schéma de couleurs**|
| :- | :- |
|Standard|Silver|
|Colorful1|Rose|
|Colorful2|Blue|
|Professional1|Cyan|
|Professional2|Cyan again|
|Traditional1|Dark|
|Traditional2|Gray|
|Custom|Customized|
Quand un style particulier est sélectionné, il change l'apparence globale du contrôle GridWeb. Les développeurs peuvent sélectionner un style prédéfini à appliquer sur le Grid pendant la conception mais cette tâche peut également être accomplie à l'exécution en utilisant l'API flexible d'Aspose.Cells.GridWeb.

{{% alert color="primary" %}} 

Le contrôle Aspose.Cells.GridWeb est représenté par la classe GridWeb.

{{% /alert %}} 

Pour sélectionner un style prédéfini :

1. Ajoutez le contrôle Aspose.Cells.GridWeb à un formulaire Web.
1. Sélectionnez un style prédéfini à appliquer sur le contrôle.

Le contrôle GridWeb fournit la propriété PresetStyle à laquelle les développeurs peuvent affecter n'importe quel style prédéfini souhaité.

Le résultat de l'extrait de code ci-dessous est affiché ci-dessous. 

**Contrôle GridWeb avec le style Colorful1 appliqué** 

![todo:image_alt_text](apply-styles-to-gridweb_1.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyPresetStyle.aspx-ApplyPresetStyle.cs" >}}
### **Style de barre d'en-tête**
Si vous regardez le contrôle GridWeb, vous remarquerez deux barres d'en-tête. Une pour les colonnes (c'est-à-dire A, B, C, D, etc.) et une autre pour les lignes (c'est-à-dire 1, 2, 3, 4, etc.). Aspose.Cells.GridWeb permet aux développeurs de contrôler l'apparence de ces barres d'en-tête. Les développeurs peuvent définir le style des barres d'en-tête soit au moment de la conception, soit à l'exécution.

{{% alert color="primary" %}} 

Le contrôle GridWeb fournit la propriété HeaderBarStyle qui applique un style sur les deux barres d'en-tête du contrôle.

{{% /alert %}} 

La sortie du code d'exemple ci-dessous est indiquée ici. 

**Style modifié de la barre d'en-tête** 

![todo:image_alt_text](apply-styles-to-gridweb_2.png)



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyHeaderBarStyle.aspx-ApplyHeaderBarStyle.cs" >}}
### **Style de barre d'onglets**
Il est possible de définir le style de la barre d'onglets. 

**Styles modifiés des barres d'onglets actives et non actives** 

![todo:image_alt_text](apply-styles-to-gridweb_3.png)

Sur la figure ci-dessus, Sheet4 est l'onglet actif, donc son apparence est différente des autres onglets, comme défini par le code d'exemple ci-dessous.





{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyTabBarStyle.aspx-ApplyTabBarStyle.cs" >}}
### **Fichier de style personnalisé réutilisable**
Aspose.Cells.GridWeb prend également en charge la persistance de ses paramètres d'apparence ou de style dans un fichier. Lorsque vous avez défini toutes les propriétés d'apparence du contrôle GridWeb, vous pouvez enregistrer ces propriétés ou paramètres dans un fichier sur disque. Cette approche est très utile pour les développeurs qui peuvent ainsi gagner du temps et des efforts en réutilisant leurs anciennes configurations de style à partir d'un fichier de style au lieu de définir toutes les propriétés de style (ou d'apparence) du contrôle une par une.
### **Enregistrement du fichier de style**
Une fois que vous avez terminé de définir les propriétés de style, vous pouvez enregistrer vos paramètres de configuration de style sous forme de fichier XML (car le fichier de style est stocké sous forme de fichier XML) en appelant la méthode SaveCustomStyleFile du contrôle GridWeb.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-SaveCustomStyle.cs" >}}

{{% alert color="primary" %}} 

Le fichier de style enregistré est au format XML, donc les développeurs peuvent également éditer ce fichier avec n'importe quel éditeur de texte, le cas échéant.

{{% /alert %}} 
### **Chargement du fichier de style**
Pour appliquer les paramètres de style d'un fichier de style existant au contrôle GridWeb, les développeurs peuvent définir le chemin du fichier de style dans la propriété CustomStyleFileName du contrôle. Mais avant cela, il est nécessaire de définir la propriété PresetStyle du contrôle sur Custom. C'est parce que le fichier de style contient des informations de style personnalisé déjà définies par un développeur.

{{% alert color="primary" %}} 

Il est également possible de charger ou d'enregistrer un fichier de style à l'aide de Aspose.Cells.GridWeb Designer.

{{% /alert %}} 

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ApplyCustomPresetStyle.aspx-LoadCustomStyle.cs" >}}

{{% alert color="primary" %}} 

IMPORTANT : Charger un fichier de style dans un contrôle GridWeb n'affecte pas les paramètres de formatage des cellules du contrôle.

{{% /alert %}} 
### **Format standard du modèle de style XML**
{{< highlight java >}}

 <ViewerStyleTemplate SelectCellColor="Black" FrameTableStyle-BorderStyle="Solid" FrameTableStyle-LayoutFixed="Fixed" FrameTableStyle-BorderWidth="1px" FrameTableStyle-BorderColor="Gray" FrameTableStyle-BorderCollapse="Collapse" FrameTableStyle-BackColor="White" SelectCellBgColor="#EEEEFF" HeaderBarWidth="30pt" ScrollBarBaseColor="" HeaderBarStyle-LeftBorderStyle-BorderStyle="Solid" HeaderBarStyle-LeftBorderStyle-BorderWidth="1px" HeaderBarStyle-LeftBorderStyle-BorderColor="White" HeaderBarStyle-VerticalAlign="Middle" HeaderBarStyle-RightBorderStyle-BorderStyle="Solid" HeaderBarStyle-RightBorderStyle-BorderWidth="1px" HeaderBarStyle-RightBorderStyle-BorderColor="Gray" HeaderBarStyle-BorderWidth="1px" HeaderBarStyle-Font-Size="10pt" HeaderBarStyle-Font-Names="Arial" HeaderBarStyle-BorderColor="Gray" HeaderBarStyle-BorderStyle="Solid" HeaderBarStyle-HorizontalAlign="Center" HeaderBarStyle-ForeColor="Black" HeaderBarStyle-TopBorderStyle-BorderStyle="Solid" HeaderBarStyle-TopBorderStyle-BorderWidth="1px" HeaderBarStyle-TopBorderStyle-BorderColor="White" HeaderBarStyle-BackColor="#E0E0E0" HeaderBarStyle-BottomBorderStyle-BorderStyle="Solid" HeaderBarStyle-BottomBorderStyle-BorderWidth="1px" HeaderBarStyle-BottomBorderStyle-BorderColor="Gray" HeaderBarStyle-Wrap="False" ActiveHeaderColor="Black" HeaderBarTableStyle-LayoutFixed="Fixed" HeaderBarTableStyle-BorderWidth="0px" HeaderBarTableStyle-BorderCollapse="Separate" HeaderBarHeight="15pt" ActiveTabStyle-Height="15pt" ActiveTabStyle-BorderWidth="1px" ActiveTabStyle-Font-Size="10pt" ActiveTabStyle-Font-Names="Arial" ActiveTabStyle-BorderColor="Gray" ActiveTabStyle-BorderStyle="Solid" ActiveTabStyle-ForeColor="Black" ActiveTabStyle-BackColor="White" ActiveTabStyle-Wrap="False" ActiveCellColor="Black" DefaultGridLineColor="Silver" ViewTableStyle-LayoutFixed="Fixed" ViewTableStyle-BorderWidth="0px" ViewTableStyle-BorderCollapse="Collapse" ActiveCellBgColor="#DDDDFF" TabStyle-Height="15pt" TabStyle-BorderWidth="1px" TabStyle-Font-Size="10pt" TabStyle-Font-Names="Arial" TabStyle-BorderColor="Gray" TabStyle-BorderStyle="Solid" TabStyle-ForeColor="Black" TabStyle-BackColor="#E0E0E0" TabStyle-Wrap="False" ActiveHeaderBgColor="#F2F2F2" ScrollBarArrowColor="" BottomTableStyle-LayoutFixed="Fixed" BottomTableStyle-Height="20pt" BottomTableStyle-BorderWidth="0px" BottomTableStyle-BorderCollapse="Collapse" BottomTableStyle-TopBorderStyle-BorderStyle="Solid" BottomTableStyle-TopBorderStyle-BorderWidth="1px" BottomTableStyle-TopBorderStyle-BorderColor="Gray" BottomTableStyle-BackColor="#F0F0F0" />


{{< /highlight >}}
